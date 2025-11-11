
# Implementation Plan: DS-STAR Multi-Agent Enhancement

**Branch**: `001-ds-star-multi` | **Date**: 2025-11-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/workspaces/sdd-agentic-framework/specs/001-ds-star-multi/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   ✓ SUCCESS: Spec loaded from /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/spec.md
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   ✓ SUCCESS: Technical Context filled, all NEEDS CLARIFICATION resolved in research phase
3. Fill the Constitution Check section based on the content of the constitution document.
   ✓ SUCCESS: Constitution Check completed - ALL PRINCIPLES PASS
4. Evaluate Constitution Check section below
   ✓ SUCCESS: No violations, all applicable principles satisfied
5. Execute Phase 0 → research.md
   ✓ SUCCESS: research.md generated with 6 research areas resolved
6. Execute Phase 1 → contracts, data-model.md, quickstart.md
   ✓ SUCCESS: All Phase 1 artifacts generated
7. Re-evaluate Constitution Check section
   ✓ SUCCESS: Post-design check confirms continued compliance
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
   ✓ SUCCESS: Task generation strategy described below
9. STOP - Ready for /tasks command
   ✓ COMPLETE: Plan ready for task generation phase
```

**IMPORTANT**: The /plan command STOPS at step 9. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary

This feature enhances the SDD Agentic Framework with proven multi-agent patterns from Google's DS-STAR system. It introduces five new specialized agents (Verification, Router, Auto-Debug, Context Analyzer, Compliance Finalizer) and supporting systems (refinement state management, feedback accumulation, context intelligence, quality metrics) to achieve 3.5x improvement in task completion accuracy through automated quality gates, intelligent orchestration, self-healing capabilities, iterative refinement, and context-aware decision making. The implementation is purely additive to the existing framework with phased rollout capability and full constitutional compliance.

## Technical Context

**Language/Version**: Python 3.11+ (existing framework language, matches current codebase)
**Primary Dependencies**:
  - sentence-transformers==2.2.2 (semantic embeddings)
  - scikit-learn==1.3.2 (similarity computations)
  - pydantic==2.5.0 (data validation and agent interfaces)
  - pytest==7.4.3 (testing framework)
  - numpy==1.24.3 (array operations for embeddings)

**Storage**: Filesystem-based JSON/YAML (aligned with current framework approach)
  - `.docs/agents/quality/verifier/decisions/` (verification decisions)
  - `.docs/agents/shared/refinement-state/` (iteration state)
  - `.docs/agents/shared/context-summaries/` (codebase context)
  - `.docs/agents/architecture/router/decisions/` (routing audit trail)

**Testing**: pytest with contract tests (aligned with Principle II: Test-First)
**Target Platform**: Linux/macOS development environments (existing framework target)
**Project Type**: single (framework enhancement, not web/mobile app)
**Performance Goals**:
  - Context retrieval: <2 seconds (FR-031)
  - Debug iteration cycle: <30 seconds per attempt
  - 3.5x improvement in task completion accuracy (FR-047)
  - >70% automatic fix rate for common errors (FR-016)

**Constraints**:
  - Must maintain backward compatibility with existing workflows (FR-052)
  - No autonomous git operations (Principle VI, FR-039)
  - Maximum 20 refinement rounds to prevent infinite loops (FR-019)
  - Maximum 5 debug iterations before escalation (FR-015)
  - All agent decisions must be auditable (FR-050)

**Scale/Scope**:
  - 5 new specialized agents across 3 departments
  - 5 new data structures for agent coordination
  - 53 functional requirements across 8 categories
  - Phased implementation over 12 weeks (per SOW)
  - Integration with 13 existing agents

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Library-First Architecture
**Status**: PASS
**Rationale**: Each agent implemented as standalone library with clear interfaces:
  - `sdd.agents.quality.verifier` library
  - `sdd.agents.architecture.router` library
  - `sdd.agents.engineering.autodebug` library
  - `sdd.agents.architecture.context_analyzer` library
  - `sdd.agents.quality.finalizer` library
  - Supporting libraries: `sdd.refinement`, `sdd.feedback`, `sdd.context`, `sdd.metrics`

### Principle II: Test-First Development
**Status**: PASS
**Rationale**: Contract tests generated for all agent interfaces before implementation. Each agent library will have unit tests with >80% coverage. Integration tests validate multi-agent coordination. quickstart.md provides 7 integration test scenarios.

### Principle III: Contract-First Design
**Status**: PASS
**Rationale**: Agent interfaces defined as explicit contracts (OpenAPI schemas) before implementation:
  - `contracts/verifier.yaml` - Verification agent contract
  - `contracts/router.yaml` - Router agent contract
  - `contracts/autodebug.yaml` - Auto-debug agent contract
  - `contracts/context.yaml` - Context analyzer contract
  - `contracts/finalizer.yaml` - Compliance finalizer contract

### Principle IV: Idempotent Operations
**Status**: PASS
**Rationale**: All agent operations designed to be safely repeatable:
  - Verification decisions can be re-run without side effects
  - Router decisions are deterministic based on state
  - Debug attempts track iterations to prevent infinite loops
  - Context analysis can be re-executed safely
  - Refinement state persistence enables resume from any point

### Principle V: Progressive Enhancement
**Status**: PASS
**Rationale**: Feature flags enable phased rollout (FR-051). Start with simplest implementations:
  - Phase 1: Core agent foundations (verification, basic routing)
  - Phase 2: Refinement loops and feedback accumulation
  - Phase 3: Context intelligence and debugging
  - Phase 4: Full integration and optimization

### Principle VI: Git Operation Approval (CRITICAL)
**Status**: PASS
**Rationale**: Finalizer agent explicitly requires user approval before ANY git operations (FR-039). All git operations use request_git_approval() function from common.sh. No autonomous commits, pushes, or branch operations. Validated in quickstart.md Scenario 6.

### Principle VII: Observability and Structured Logging
**Status**: PASS
**Rationale**: All agent decisions logged in structured JSON format (FR-046). Audit trails maintained for:
  - Verification decisions with reasoning (FR-005)
  - Routing decisions with strategy selection (FR-010)
  - Debug attempts with error analysis (FR-018)
  - Context retrieval performance metrics (FR-044)
  - Constitutional compliance rate tracking (FR-045)

### Principle VIII: Documentation Synchronization
**Status**: PASS
**Rationale**: Documentation updates are part of definition of done:
  - CLAUDE.md update with agent capabilities
  - constitution.md amendment for quality gates
  - agent-collaboration-triggers.md update with new agents
  - Individual agent README files with usage examples
  - Cross-references validated via update checklist

### Principle IX: Dependency Management
**Status**: PASS
**Rationale**: All new dependencies explicitly declared with version pinning:
  - sentence-transformers==2.2.2 (semantic embeddings)
  - scikit-learn==1.3.2 (similarity computations)
  - pydantic==2.5.0 (data validation)
  - numpy==1.24.3 (array operations)
  - No external services required (local embeddings)
  - Graceful degradation if dependencies unavailable (FR-032)

### Principle X: Agent Delegation Protocol
**Status**: PASS
**Rationale**: This feature explicitly implements specialized agents per delegation protocol. Each new agent has clear domain boundaries:
  - quality/verifier: Quality gate decisions
  - architecture/router: Orchestration and routing
  - engineering/autodebug: Error detection and repair
  - architecture/context_analyzer: Codebase analysis
  - quality/finalizer: Pre-commit validation

### Principle XI: Input Validation and Output Sanitization
**Status**: PASS
**Rationale**: All agent inputs validated via Pydantic schemas (see data-model.md). File paths validated before filesystem operations. No user input directly executed in shell commands. Secrets never logged or committed (FR-038).

### Principle XII: Design System Compliance
**Status**: N/A (No UI components)
**Rationale**: This is a backend framework enhancement without user-facing UI components. Agent outputs are structured data and CLI feedback only.

### Principle XIII: Feature Access Control
**Status**: N/A (Framework capability, not user-facing feature)
**Rationale**: Agent capabilities are framework-level, not end-user features requiring tiered access control.

### Principle XIV: AI Model Selection Protocol
**Status**: PASS
**Rationale**:
  - Default to Claude Sonnet 4.5 for agent operations (90% of tasks)
  - Escalate to Opus 4.1 for safety-critical decisions (verification gates, security validations, complex routing decisions)
  - Document escalation reasoning in agent decision logs
  - Model selection tracked in metrics (future enhancement)

**GATE RESULT**: PASS - All applicable principles satisfied. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)
```
specs/001-ds-star-multi/
├── spec.md              # Feature specification (completed)
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (completed)
├── data-model.md        # Phase 1 output (completed)
├── quickstart.md        # Phase 1 output (completed)
├── contracts/           # Phase 1 output (completed)
│   ├── verifier.yaml    # Verification agent contract
│   ├── router.yaml      # Router agent contract
│   ├── autodebug.yaml   # Auto-debug agent contract
│   ├── context.yaml     # Context analyzer contract
│   └── finalizer.yaml   # Compliance finalizer contract
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Option 1: Single project (DEFAULT) - Framework Enhancement
.docs/agents/
├── quality/
│   ├── verifier/
│   │   ├── __init__.py         # Verification agent library
│   │   ├── verifier.py         # Core verification logic
│   │   ├── decisions/          # Decision audit trail
│   │   └── README.md           # Agent documentation
│   └── finalizer/
│       ├── __init__.py         # Finalizer agent library
│       ├── finalizer.py        # Pre-commit validation
│       └── README.md           # Agent documentation
├── architecture/
│   ├── router/
│   │   ├── __init__.py         # Router agent library
│   │   ├── router.py           # Orchestration logic
│   │   ├── decisions/          # Routing audit trail
│   │   └── README.md           # Agent documentation
│   └── context_analyzer/
│       ├── __init__.py         # Context analyzer library
│       ├── analyzer.py         # Codebase analysis
│       └── README.md           # Agent documentation
├── engineering/
│   └── autodebug/
│       ├── __init__.py         # Auto-debug agent library
│       ├── debugger.py         # Error repair logic
│       └── README.md           # Agent documentation
└── shared/
    ├── refinement-state/       # Iteration state storage
    ├── context-summaries/      # Codebase context cache
    └── metrics/                # Performance tracking

src/sdd/
├── agents/
│   ├── quality/                # Quality agent libraries
│   ├── architecture/           # Architecture agent libraries
│   ├── engineering/            # Engineering agent libraries
│   └── shared/                 # Shared utilities
├── refinement/                 # Refinement loop library
├── feedback/                   # Feedback accumulation library
├── context/                    # Context intelligence library
└── metrics/                    # Metrics collection library

tests/
├── contract/                   # Contract tests for agent interfaces
│   ├── test_verifier_contract.py
│   ├── test_router_contract.py
│   ├── test_autodebug_contract.py
│   ├── test_context_contract.py
│   └── test_finalizer_contract.py
├── integration/                # Multi-agent integration tests
│   ├── test_verification_gate.py
│   ├── test_intelligent_routing.py
│   ├── test_auto_debug.py
│   ├── test_refinement_loop.py
│   ├── test_context_intelligence.py
│   ├── test_compliance_finalizer.py
│   └── test_end_to_end_workflow.py
└── unit/                       # Unit tests for libraries
    ├── test_verifier.py
    ├── test_router.py
    ├── test_autodebug.py
    ├── test_context.py
    └── test_finalizer.py
```

**Structure Decision**: Option 1 (single project) - This is a framework enhancement, not a separate application.

## Phase 0: Outline & Research

**Status**: COMPLETE ✓

### Research Areas Resolved

All technical unknowns from the specification have been researched and resolved in `research.md`:

1. **DS-STAR Pattern Implementation** ✓
   - Decision: Adopt DS-STAR multi-agent architecture with local adaptations
   - Key patterns: Binary quality gates, intelligent routing, iterative refinement, auto-debugging, context intelligence
   - All patterns validated against constitutional principles

2. **Embedding Model Selection** ✓
   - Decision: Use sentence-transformers with `all-MiniLM-L6-v2` model
   - Performance: <2s retrieval (avg 0.5s for 10k documents)
   - Graceful degradation to TF-IDF keyword search if needed
   - Resolves NEEDS CLARIFICATION #2 from spec.md

3. **Refinement Algorithm Design** ✓
   - Decision: Feedback accumulation with exponential moving average and early stopping
   - Max rounds: 20 (prevents infinite loops)
   - Early stopping threshold: 0.95
   - State persistence enables idempotent resume

4. **Auto-Debug Pattern Library** ✓
   - Decision: Pattern-based error detection with constitutional-aware repair
   - Covers 5 error types: syntax, type, name/attribute, null reference, import
   - Target: >70% auto-fix rate (achievable based on research)
   - Max 5 iterations before escalation

5. **Quality Metrics Framework** ✓
   - Decision: JSON-based metrics collection with baseline comparison
   - 5 core metrics: task completion accuracy, refinement rounds, debug success, context performance, constitutional compliance
   - Baseline measurement plan addresses NEEDS CLARIFICATION #1
   - Validates 3.5x improvement target

6. **Agent Communication Patterns** ✓
   - Decision: Structured JSON-based context handoff with Pydantic validation
   - Input/output contracts defined (AgentInput, AgentOutput, AgentContext)
   - Multi-agent coordination via DAG execution
   - Conflict resolution with router authority

**Output**: research.md with all decisions documented, rationale provided, alternatives considered.

## Phase 1: Design & Contracts

**Status**: COMPLETE ✓

### Artifacts Generated

1. **data-model.md** ✓
   - 10 core entities defined with fields, relationships, validation rules
   - Agent Input/Output contracts (AgentInput, AgentOutput, AgentContext)
   - Agent-specific entities (VerificationDecision, RoutingDecision, DebugSession, ContextSummary)
   - Workflow state entities (RefinementState, IterationRecord)
   - Metrics entities (TaskMetrics)
   - Configuration entities (AgentConfig)
   - All entities use Pydantic for validation
   - Filesystem-based JSON storage strategy defined

2. **contracts/** ✓
   - `verifier.yaml`: OpenAPI 3.0 contract for Verification Agent (POST /verify)
   - `router.yaml`: OpenAPI 3.0 contract for Router Agent (POST /route)
   - `autodebug.yaml`: OpenAPI 3.0 contract for Auto-Debug Agent (POST /debug)
   - `context.yaml`: OpenAPI 3.0 contract for Context Analyzer (POST /analyze, POST /search)
   - `finalizer.yaml`: OpenAPI 3.0 contract for Compliance Finalizer (POST /finalize)
   - All contracts include request/response schemas, examples, error handling

3. **quickstart.md** ✓
   - 7 integration test scenarios extracted from user stories
   - Scenario 1: Quality Verification - Specification gate blocks progression
   - Scenario 2: Intelligent Routing - Multi-domain feature orchestration
   - Scenario 3: Self-Healing - Syntax error auto-fix
   - Scenario 4: Iterative Refinement - Specification improvement loop
   - Scenario 5: Context Intelligence - Semantic retrieval performance
   - Scenario 6: Output Standardization - Pre-commit validation with user approval
   - Scenario 7: End-to-End - Full workflow coordination
   - Each scenario includes test steps, expected output, validation criteria
   - Performance validation commands included

### Contract Test Generation (TDD)

Contract tests must be generated before implementation. Each contract requires:

```python
# tests/contract/test_verifier_contract.py
def test_verifier_contract_specification_gate():
    """Contract: POST /verify returns binary decision with feedback"""
    # This test will FAIL initially (no implementation)
    response = verifier.verify(request)
    assert response.output_data["decision"] in ["sufficient", "insufficient"]
    assert "quality_score" in response.output_data
    assert isinstance(response.output_data["feedback"], list)
```

**Contract Test Coverage**:
- Verifier: 2 contract tests (sufficient/insufficient paths)
- Router: 3 contract tests (sequential/parallel/dag strategies)
- Auto-Debug: 2 contract tests (resolved/escalated paths)
- Context: 2 contract tests (semantic/fallback paths)
- Finalizer: 2 contract tests (passed/failed validation paths)
- **Total**: 11 contract tests (all must fail initially per TDD)

## Phase 2: Task Planning Approach

**Status**: READY FOR /tasks COMMAND

*This section describes what the /tasks command will do - DO NOT execute during /plan*

### Task Generation Strategy

The /tasks command will:

1. **Load Design Artifacts**:
   - Read data-model.md for entities
   - Parse contracts/*.yaml for agent interfaces
   - Extract test scenarios from quickstart.md
   - Review research.md for implementation guidance

2. **Generate Contract Test Tasks** (TDD-first):
   - Task 1-11: Generate failing contract tests [P] (parallel, independent)
   - One task per contract endpoint
   - Tests assert request/response schemas
   - All tests must fail initially

3. **Generate Library Creation Tasks**:
   - Task 12: Create `sdd.agents.shared` package with base classes [P]
   - Task 13: Create `sdd.refinement` library stub [P]
   - Task 14: Create `sdd.feedback` library stub [P]
   - Task 15: Create `sdd.context` library stub [P]
   - Task 16: Create `sdd.metrics` library stub [P]

4. **Generate Agent Implementation Tasks** (Library-First):
   - Task 17: Implement Verification Agent library (make contract tests pass)
   - Task 18: Implement Router Agent library (make contract tests pass)
   - Task 19: Implement Auto-Debug Agent library (make contract tests pass)
   - Task 20: Implement Context Analyzer library (make contract tests pass)
   - Task 21: Implement Compliance Finalizer library (make contract tests pass)

5. **Generate Integration Test Tasks**:
   - Task 22: Implement Scenario 1 test (Quality Verification)
   - Task 23: Implement Scenario 2 test (Intelligent Routing)
   - Task 24: Implement Scenario 3 test (Self-Healing)
   - Task 25: Implement Scenario 4 test (Iterative Refinement)
   - Task 26: Implement Scenario 5 test (Context Intelligence)
   - Task 27: Implement Scenario 6 test (Output Standardization)
   - Task 28: Implement Scenario 7 test (End-to-End)

6. **Generate Supporting System Tasks**:
   - Task 29: Implement refinement loop algorithm
   - Task 30: Implement feedback accumulation system
   - Task 31: Implement context indexing and retrieval
   - Task 32: Implement metrics collection framework
   - Task 33: Implement multi-agent coordinator

7. **Generate Documentation Tasks**:
   - Task 34: Update CLAUDE.md with agent capabilities
   - Task 35: Update agent-collaboration-triggers.md with new agents
   - Task 36: Create agent README files
   - Task 37: Update constitution.md with quality gate formalization

8. **Generate Validation Tasks**:
   - Task 38: Run all tests and verify >80% coverage
   - Task 39: Run performance benchmarks
   - Task 40: Validate constitutional compliance
   - Task 41: Measure baseline and validate 3.5x improvement

### Ordering Strategy

**Dependency Order** (TDD, Library-First, Contract-First):
1. Contract tests first (Tasks 1-11) - Define interfaces [PARALLEL]
2. Library stubs next (Tasks 12-16) - Foundation [PARALLEL]
3. Agent implementations (Tasks 17-21) - Make tests pass [SEQUENTIAL by agent]
4. Integration tests (Tasks 22-28) - Validate coordination [SEQUENTIAL]
5. Supporting systems (Tasks 29-33) - Complete infrastructure [SEQUENTIAL]
6. Documentation (Tasks 34-37) - Sync docs [PARALLEL]
7. Validation (Tasks 38-41) - Final checks [SEQUENTIAL]

**Parallelization Markers**:
- [P] for tasks that can execute simultaneously (independent files)
- Contract tests all marked [P] (11 parallel tasks)
- Library stubs all marked [P] (5 parallel tasks)
- Documentation tasks marked [P] (4 parallel tasks)

### Estimated Output

**Total Tasks**: ~41 numbered, dependency-ordered tasks in tasks.md
**Parallel Opportunities**: ~20 tasks marked [P] (50% parallelizable)
**Estimated Implementation Time**: 12 weeks per SOW (phased rollout)

**Task Complexity Distribution**:
- Simple (1-2 hours): Contract tests, library stubs, docs (20 tasks)
- Medium (1-2 days): Agent implementations, integration tests (15 tasks)
- Complex (3-5 days): Supporting systems, end-to-end validation (6 tasks)

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

**No constitutional violations identified.** All 14 principles satisfied without requiring complexity justifications.

The feature design inherently aligns with constitutional principles:
- Library-First enforced by agent architecture
- Test-First enforced by contract tests before implementation
- Contract-First enforced by OpenAPI schemas
- Git Approval enforced by Finalizer agent design
- All other principles naturally satisfied by design choices

## Progress Tracking

**Phase Status**:
- [x] Phase 0: Research complete (/plan command) - research.md generated
- [x] Phase 1: Design complete (/plan command) - data-model.md, contracts/, quickstart.md generated
- [x] Phase 2: Task planning complete (/plan command - described approach, NOT executed)
- [ ] Phase 3: Tasks generated (/tasks command - NEXT STEP)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS (all applicable principles satisfied)
- [x] Post-Design Constitution Check: PASS (continued compliance)
- [x] All NEEDS CLARIFICATION resolved (baseline measurement plan, embedding model selection)
- [x] Complexity deviations documented (NONE - no violations)

**Artifacts Generated**:
- [x] plan.md (this file)
- [x] research.md (6 research areas, all unknowns resolved)
- [x] data-model.md (10 entities with Pydantic schemas)
- [x] contracts/verifier.yaml (OpenAPI 3.0 contract)
- [x] contracts/router.yaml (OpenAPI 3.0 contract)
- [x] contracts/autodebug.yaml (OpenAPI 3.0 contract)
- [x] contracts/context.yaml (OpenAPI 3.0 contract)
- [x] contracts/finalizer.yaml (OpenAPI 3.0 contract)
- [x] quickstart.md (7 integration test scenarios)

**Ready for Next Phase**: YES - All /plan command requirements satisfied.

---

## Next Steps

**Immediate Action**: Run `/tasks` command to generate dependency-ordered task list.

**Command**: `/tasks`

**Expected Output**: tasks.md with ~41 tasks organized by:
1. Contract tests (11 tasks, all [P])
2. Library foundations (5 tasks, all [P])
3. Agent implementations (5 tasks)
4. Integration tests (7 tasks)
5. Supporting systems (5 tasks)
6. Documentation updates (4 tasks)
7. Validation and metrics (4 tasks)

**Validation Before /tasks**:
```bash
# Verify all Phase 1 artifacts exist
ls /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/research.md
ls /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/data-model.md
ls /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/quickstart.md
ls /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/contracts/*.yaml

# Run validation script
./.specify/scripts/bash/validate-plan.sh --file /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/plan.md

# Detect domains
./.specify/scripts/bash/detect-phase-domain.sh --file /workspaces/sdd-agentic-framework/specs/001-ds-star-multi/plan.md
```

---

*Based on Constitution v1.5.0 - See `.specify/memory/constitution.md`*
*Plan generated by planning-agent on 2025-11-10*
