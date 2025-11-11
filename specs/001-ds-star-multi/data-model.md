# Data Model: DS-STAR Multi-Agent Enhancement

**Feature**: DS-STAR Multi-Agent Enhancement
**Date**: 2025-11-10
**Phase**: Phase 1 - Design & Contracts

---

## Overview

This data model defines the entities and structures for the DS-STAR multi-agent enhancement system. All entities use Pydantic for validation and JSON for persistence, aligned with the framework's filesystem-based approach.

---

## Agent Input/Output Entities

### AgentInput
**Purpose**: Standardized input contract for all agents
**Fields**:
- `agent_id: str` - Unique identifier for the agent (e.g., "quality.verifier")
- `task_id: str` - Unique identifier for the current task (UUID format)
- `phase: str` - Workflow phase ("specification", "planning", "implementation", "validation")
- `input_data: Dict[str, Any]` - Agent-specific input payload
- `context: AgentContext` - Shared context from previous agents

**Relationships**:
- Contains one AgentContext
- References RefinementState via context

**Validation**:
- agent_id must match pattern: `{department}.{agent_name}`
- task_id must be valid UUID
- phase must be one of valid workflow phases

**State Transitions**: Immutable once created

**Example**:
```python
AgentInput(
    agent_id="quality.verifier",
    task_id="550e8400-e29b-41d4-a716-446655440000",
    phase="planning",
    input_data={"plan_path": "/workspaces/sdd-agentic-framework/specs/001-ds-star-multi/plan.md"},
    context=AgentContext(...)
)
```

---

### AgentOutput
**Purpose**: Standardized output contract for all agents
**Fields**:
- `agent_id: str` - Agent that produced this output
- `task_id: str` - Task identifier (matches input)
- `success: bool` - Whether agent completed successfully
- `output_data: Dict[str, Any]` - Agent-specific output payload
- `reasoning: str` - Human-readable explanation of decision/action
- `confidence: float` - Confidence score (0.0 to 1.0)
- `next_actions: List[str]` - Suggested next steps
- `metadata: Dict[str, Any]` - Additional structured data
- `timestamp: datetime` - When output was generated

**Relationships**:
- Referenced by AgentContext in subsequent agent invocations
- Stored in audit trail

**Validation**:
- confidence must be between 0.0 and 1.0
- reasoning must be non-empty string
- timestamp must not be in future

**State Transitions**: Immutable once created (audit trail integrity)

**Example**:
```python
AgentOutput(
    agent_id="quality.verifier",
    task_id="550e8400-e29b-41d4-a716-446655440000",
    success=False,
    output_data={"decision": "insufficient", "quality_score": 0.72},
    reasoning="Plan lacks contract definitions for 3 endpoints",
    confidence=0.91,
    next_actions=["Generate OpenAPI schemas", "Add validation rules"],
    metadata={"violations": ["missing_contracts"]},
    timestamp=datetime.now()
)
```

---

### AgentContext
**Purpose**: Shared context passed between agents
**Fields**:
- `spec_path: Optional[str]` - Path to feature specification
- `plan_path: Optional[str]` - Path to implementation plan
- `previous_outputs: List[AgentOutput]` - History of agent outputs
- `cumulative_feedback: List[str]` - Accumulated feedback from verification failures
- `refinement_state: Optional[RefinementState]` - Current refinement iteration state

**Relationships**:
- Contains multiple AgentOutput references
- Contains one RefinementState (if refinement active)

**Validation**:
- File paths must exist if provided
- previous_outputs must be chronologically ordered

**State Transitions**: Grows with each agent invocation (append-only)

---

## Agent-Specific Entities

### VerificationDecision
**Purpose**: Output from Verification Agent
**Fields**:
- `decision: str` - Binary decision ("sufficient" or "insufficient")
- `quality_score: float` - Numerical quality assessment (0.0 to 1.0)
- `dimension_scores: Dict[str, float]` - Scores per evaluation dimension
- `feedback: List[str]` - Actionable improvement suggestions
- `violations: List[str]` - Specific issues identified
- `passed_checks: List[str]` - Checks that passed

**Relationships**:
- Stored in `.docs/agents/quality/verifier/decisions/{task_id}.json`
- Referenced by RefinementState

**Validation**:
- decision must be "sufficient" or "insufficient"
- quality_score must match decision (sufficient >= threshold)
- feedback required if decision is insufficient

**Evaluation Dimensions**:
- `completeness`: All required sections present
- `constitutional_compliance`: Follows all 14 principles
- `test_coverage`: >80% code coverage
- `spec_alignment`: Matches specification requirements

**Example**:
```python
VerificationDecision(
    decision="insufficient",
    quality_score=0.72,
    dimension_scores={
        "completeness": 0.85,
        "constitutional_compliance": 0.65,
        "test_coverage": 0.70,
        "spec_alignment": 0.90
    },
    feedback=[
        "Add contract tests for POST /api/users endpoint",
        "Library-first principle not followed: extract auth logic to library"
    ],
    violations=["missing_contract_test", "library_first_violation"],
    passed_checks=["completeness", "spec_alignment"]
)
```

---

### RoutingDecision
**Purpose**: Output from Router Agent
**Fields**:
- `selected_agents: List[str]` - Agent IDs to invoke
- `execution_strategy: str` - How to execute ("sequential", "parallel", "dag")
- `dependency_graph: Optional[Dict[str, List[str]]]` - Agent dependencies (if DAG)
- `refinement_strategy: Optional[str]` - On failure ("ADD_STEP", "TRUNCATE_FROM", "ROUTE_TO_DEBUG", "RETRY")
- `reasoning: str` - Why these agents were selected
- `confidence: float` - Confidence in routing decision

**Relationships**:
- Stored in `.docs/agents/architecture/router/decisions/{task_id}.json`
- Referenced by orchestration layer

**Validation**:
- selected_agents must be non-empty
- execution_strategy must be valid option
- dependency_graph required if strategy is "dag"
- All agents in dependency_graph must exist in selected_agents

**Execution Strategies**:
- `sequential`: Execute agents one after another
- `parallel`: Execute all agents simultaneously (independent tasks)
- `dag`: Execute based on dependency graph (topological order)

**Refinement Strategies**:
- `ADD_STEP`: Add additional verification/validation step
- `TRUNCATE_FROM(index)`: Restart from specific agent in sequence
- `ROUTE_TO_DEBUG`: Send to auto-debug agent for error repair
- `RETRY_WITH_FEEDBACK`: Re-run same agent with accumulated feedback

**Example**:
```python
RoutingDecision(
    selected_agents=["engineering.backend", "engineering.frontend"],
    execution_strategy="dag",
    dependency_graph={
        "engineering.backend": [],  # No dependencies, can run first
        "engineering.frontend": ["engineering.backend"]  # Depends on backend
    },
    refinement_strategy="ROUTE_TO_DEBUG",
    reasoning="Feature requires both backend API and frontend UI. Backend must complete first to define API contract.",
    confidence=0.88
)
```

---

### DebugAttempt
**Purpose**: Single auto-debug iteration record
**Fields**:
- `iteration: int` - Iteration number (1-5)
- `error_pattern: str` - Classified error type ("syntax", "type", "name", "null", "import")
- `error_message: str` - Original error message
- `stack_trace: str` - Full stack trace
- `repair_action: str` - Description of attempted repair
- `repaired_code: str` - Code after repair attempt
- `test_result: str` - Outcome ("passed", "failed", "error")
- `reasoning: str` - Why this repair was attempted

**Relationships**:
- Part of DebugSession
- Chronologically ordered within session

**Validation**:
- iteration must be 1-5 (max debug iterations)
- error_pattern must be recognized type
- test_result must be valid outcome

**Example**:
```python
DebugAttempt(
    iteration=1,
    error_pattern="type",
    error_message="TypeError: unsupported operand type(s) for +: 'int' and 'str'",
    stack_trace="Traceback (most recent call last):\n  File 'app.py', line 42...",
    repair_action="Convert string to int before addition: int(user_input) + count",
    repaired_code="result = int(user_input) + count",
    test_result="passed",
    reasoning="Error indicates string + int operation. Spec requires numerical calculation, so convert input to int."
)
```

---

### DebugSession
**Purpose**: Complete auto-debug session for an error
**Fields**:
- `task_id: str` - Task identifier
- `original_code: str` - Code before debugging
- `final_code: Optional[str]` - Code after successful debugging (if resolved)
- `attempts: List[DebugAttempt]` - All debug attempts
- `success: bool` - Whether error was auto-resolved
- `escalated: bool` - Whether escalated to human
- `total_iterations: int` - Number of attempts made
- `resolution_time_seconds: float` - Time to resolve (if successful)

**Relationships**:
- Contains multiple DebugAttempt records
- Stored in `.docs/agents/engineering/autodebug/sessions/{task_id}.json`

**Validation**:
- attempts must be non-empty
- total_iterations must match len(attempts)
- If success=True, final_code must be provided
- If escalated=True, success must be False

**State Transitions**:
1. Initialize with original_code
2. Add attempts (1-5 iterations)
3. Either: Mark success=True with final_code, OR escalated=True

---

### ContextSummary
**Purpose**: Codebase analysis result from Context Analyzer
**Fields**:
- `task_id: str` - Task identifier
- `relevant_files: List[str]` - File paths relevant to task
- `file_summaries: Dict[str, str]` - Brief description per file
- `existing_patterns: List[str]` - Architectural patterns found
- `dependencies: Dict[str, List[str]]` - File dependency graph
- `related_specs: List[str]` - Similar past feature specifications
- `constitutional_status: Dict[str, bool]` - Principle compliance per area
- `embedding_vector: Optional[List[float]]` - Semantic embedding (384-dim)
- `generated_at: datetime` - When analysis was performed

**Relationships**:
- Stored in `.docs/agents/shared/context-summaries/{task_id}.json`
- Referenced by other agents via AgentContext

**Validation**:
- relevant_files must all exist
- constitutional_status must include all 14 principles
- embedding_vector must be 384 dimensions if provided

**Example**:
```python
ContextSummary(
    task_id="550e8400-e29b-41d4-a716-446655440000",
    relevant_files=[
        "/workspaces/sdd-agentic-framework/.claude/agents/product/planning-agent.md",
        "/workspaces/sdd-agentic-framework/.specify/memory/constitution.md"
    ],
    file_summaries={
        "planning-agent.md": "Implementation planning specialist, executes /plan command",
        "constitution.md": "14 enforceable principles, 3 immutable"
    },
    existing_patterns=["Library-First Architecture", "Agent Delegation Protocol"],
    dependencies={
        "planning-agent.md": ["constitution.md", "agent-governance.md"]
    },
    related_specs=["specs/000-agent-framework/spec.md"],
    constitutional_status={"Principle I": True, "Principle II": True, ...},
    embedding_vector=[0.123, -0.456, ...],  # 384 dimensions
    generated_at=datetime.now()
)
```

---

## Workflow State Entities

### RefinementState
**Purpose**: Tracks iterative refinement progress
**Fields**:
- `task_id: str` - Task identifier (UUID)
- `phase: str` - Workflow phase being refined
- `current_round: int` - Current iteration number
- `max_rounds: int` - Maximum iterations allowed (default 20)
- `iterations: List[IterationRecord]` - History of all iterations
- `cumulative_feedback: List[str]` - Accumulated feedback
- `ema_quality: float` - Exponential moving average of quality scores
- `quality_threshold: float` - Minimum quality to proceed (default 0.85)
- `early_stopping_threshold: float` - Quality for early stopping (default 0.95)
- `started_at: datetime` - When refinement began
- `updated_at: datetime` - Last update timestamp

**Relationships**:
- Stored in `.docs/agents/shared/refinement-state/{task_id}.json`
- Contains multiple IterationRecord entries
- Referenced by AgentContext

**Validation**:
- current_round must be <= max_rounds
- ema_quality must be between 0.0 and 1.0
- quality_threshold < early_stopping_threshold
- iterations must be chronologically ordered

**State Transitions**:
1. Initialize at round 0
2. Each iteration: increment current_round, append IterationRecord
3. Terminal states: quality achieved OR max_rounds reached

**Example**:
```python
RefinementState(
    task_id="550e8400-e29b-41d4-a716-446655440000",
    phase="planning",
    current_round=3,
    max_rounds=20,
    iterations=[...],  # 3 IterationRecord objects
    cumulative_feedback=[
        "Add contract for POST /api/users",
        "Increase test coverage to 80%",
        "Extract auth logic to library"
    ],
    ema_quality=0.78,
    quality_threshold=0.85,
    early_stopping_threshold=0.95,
    started_at=datetime(2025, 11, 10, 10, 0, 0),
    updated_at=datetime(2025, 11, 10, 10, 5, 30)
)
```

---

### IterationRecord
**Purpose**: Single refinement iteration result
**Fields**:
- `round: int` - Iteration number
- `timestamp: datetime` - When iteration executed
- `input_state: Dict[str, Any]` - Input snapshot
- `output_state: Dict[str, Any]` - Output snapshot
- `verification_result: VerificationDecision` - Quality gate result
- `quality_score: float` - Quality score for this iteration
- `duration_seconds: float` - Time taken for iteration
- `agent_invocations: List[str]` - Agents invoked this iteration

**Relationships**:
- Part of RefinementState
- Contains one VerificationDecision

**Validation**:
- round must match position in iterations list
- quality_score must match verification_result.quality_score

**Example**:
```python
IterationRecord(
    round=3,
    timestamp=datetime(2025, 11, 10, 10, 5, 30),
    input_state={"plan_version": 2, "feedback_count": 2},
    output_state={"plan_version": 3, "feedback_count": 3},
    verification_result=VerificationDecision(...),
    quality_score=0.78,
    duration_seconds=45.2,
    agent_invocations=["quality.verifier", "architecture.router"]
)
```

---

## Metrics Entities

### TaskMetrics
**Purpose**: Comprehensive metrics for a task
**Fields**:
- `task_id: str` - Task identifier
- `phase: str` - Workflow phase
- `started_at: datetime` - Task start time
- `completed_at: Optional[datetime]` - Task completion time (if finished)
- `duration_seconds: Optional[float]` - Total duration (if finished)
- `refinement_rounds: int` - Number of refinement iterations
- `refinement_quality_scores: List[float]` - Quality score per iteration
- `early_stopped: bool` - Whether early stopping triggered
- `errors_encountered: int` - Total errors during task
- `errors_auto_resolved: int` - Errors fixed by auto-debug
- `debug_iterations: List[int]` - Debug iterations per error
- `context_queries: int` - Number of context retrieval queries
- `avg_context_latency_ms: float` - Average context query latency
- `context_relevance_scores: List[float]` - Relevance per query
- `verification_checks: int` - Total verification checks
- `verification_passes_first_time: int` - Checks passed without refinement
- `completed_without_intervention: bool` - No manual intervention needed
- `escalated_to_human: bool` - Required human intervention

**Relationships**:
- Stored in `.docs/agents/shared/metrics/{phase}/{task_id}.json`
- Aggregated for KPI calculation

**Validation**:
- If completed_at is set, duration_seconds must be set
- errors_auto_resolved <= errors_encountered
- verification_passes_first_time <= verification_checks

**KPI Calculations**:
```python
# Task Completion Accuracy
accuracy = (completed_without_intervention / total_tasks) * 100

# Debug Success Rate
debug_rate = (errors_auto_resolved / errors_encountered) * 100

# Constitutional Compliance Rate
compliance_rate = (verification_passes_first_time / verification_checks) * 100
```

---

## Configuration Entities

### AgentConfig
**Purpose**: Configuration for agent behavior
**Fields**:
- `agent_id: str` - Agent identifier
- `enabled: bool` - Feature flag for gradual rollout
- `quality_thresholds: Dict[str, float]` - Quality thresholds per dimension
- `max_iterations: int` - Maximum iterations before escalation
- `timeout_seconds: int` - Maximum execution time
- `circuit_breaker_threshold: float` - Failure rate to disable agent
- `model_selection: str` - AI model to use ("sonnet-4.5", "opus-4.1")

**Relationships**:
- Stored in `.docs/agents/{department}/{agent_name}/config.yaml`

**Validation**:
- thresholds must be between 0.0 and 1.0
- max_iterations > 0
- circuit_breaker_threshold between 0.0 and 1.0

**Example**:
```yaml
agent_id: quality.verifier
enabled: true
quality_thresholds:
  completeness: 0.90
  constitutional_compliance: 0.85
  test_coverage: 0.80
  spec_alignment: 0.90
max_iterations: 3
timeout_seconds: 120
circuit_breaker_threshold: 0.30  # Disable if 30% failures
model_selection: sonnet-4.5
```

---

## Entity Relationships Diagram

```
AgentInput
├── contains: AgentContext
│   ├── contains: List[AgentOutput]
│   └── references: RefinementState
│       └── contains: List[IterationRecord]
│           └── contains: VerificationDecision
└── produces: AgentOutput

RoutingDecision
└── selects: List[AgentInput]

DebugSession
└── contains: List[DebugAttempt]

ContextSummary
└── references: List[file_paths]

TaskMetrics
├── aggregates: RefinementState
├── aggregates: DebugSession
└── aggregates: ContextSummary
```

---

## Storage Strategy

All entities persisted as JSON files in filesystem hierarchy:

```
.docs/agents/
├── quality/verifier/decisions/{task_id}.json         # VerificationDecision
├── architecture/router/decisions/{task_id}.json      # RoutingDecision
├── engineering/autodebug/sessions/{task_id}.json     # DebugSession
├── architecture/context_analyzer/summaries/{task_id}.json  # ContextSummary
└── shared/
    ├── refinement-state/{task_id}.json               # RefinementState
    └── metrics/{phase}/{task_id}.json                # TaskMetrics
```

**Rationale**: Filesystem-based storage aligns with framework's current approach, no database dependency, easy to inspect/debug, git-trackable for audit trail.

---

**Data Model Complete**: 2025-11-10
**Next Step**: Generate API contracts in `/contracts/` directory
