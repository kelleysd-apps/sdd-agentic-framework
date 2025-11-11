# Quickstart Testing Guide: DS-STAR Multi-Agent Enhancement

**Feature**: DS-STAR Multi-Agent Enhancement
**Date**: 2025-11-10
**Phase**: Phase 1 - Integration Testing

---

## Overview

This quickstart guide provides step-by-step integration test scenarios extracted from the user stories in spec.md. Each scenario validates end-to-end agent behavior and multi-agent coordination.

---

## Prerequisites

1. **Install dependencies**:
```bash
pip install -r requirements.txt
# Ensure: sentence-transformers==2.2.2, scikit-learn==1.3.2, pydantic==2.5.0, pytest==7.4.3
```

2. **Set up test environment**:
```bash
export SDD_TEST_MODE=true
export SDD_METRICS_DIR=.docs/agents/shared/metrics/test
```

3. **Initialize test data**:
```bash
pytest tests/fixtures/setup_test_environment.py
```

---

## Scenario 1: Quality Verification - Specification Gate

**User Story**: Quality Verification Acceptance Scenario 1
**Requirement**: FR-001, FR-002, FR-003, FR-004

### Test Steps

1. **Create test specification** (incomplete):
```bash
cat > /tmp/test-spec-incomplete.md << 'EOF'
# Feature Specification: Test Feature

## Overview
This is a test feature.

## Requirements
- FR-001: Do something
EOF
```

2. **Invoke verification agent**:
```python
# tests/integration/test_verification_gate.py
from sdd.agents.quality.verifier import VerificationAgent
from sdd.agents.shared.models import AgentInput, AgentContext

def test_specification_quality_gate_blocks_insufficient():
    # Arrange
    agent = VerificationAgent()
    request = AgentInput(
        agent_id="quality.verifier",
        task_id="test-001",
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": "/tmp/test-spec-incomplete.md",
        },
        context=AgentContext(cumulative_feedback=[])
    )

    # Act
    response = agent.verify(request)

    # Assert
    assert response.success == True  # Agent executed successfully
    assert response.output_data["decision"] == "insufficient"  # Quality gate blocks
    assert response.output_data["quality_score"] < 0.85  # Below threshold
    assert len(response.output_data["feedback"]) > 0  # Actionable feedback provided
    assert "completeness" in str(response.output_data["violations"])
```

3. **Run test**:
```bash
pytest tests/integration/test_verification_gate.py::test_specification_quality_gate_blocks_insufficient -v
```

4. **Expected Output**:
```
PASSED: Quality gate correctly blocks incomplete specification
Decision: insufficient
Quality Score: 0.42
Feedback: ["Add User Scenarios section", "Add Functional Requirements", "Add Key Entities"]
```

### Validation
- [ ] Verification agent returns "insufficient" decision
- [ ] Quality score below 0.85 threshold
- [ ] Actionable feedback provided
- [ ] Workflow progression blocked (verified in orchestration test)

---

## Scenario 2: Intelligent Routing - Multi-Domain Feature

**User Story**: Intelligent Routing Acceptance Scenario 3
**Requirement**: FR-007, FR-008, FR-011

### Test Steps

1. **Create multi-domain feature spec**:
```bash
cat > /tmp/test-spec-multi-domain.md << 'EOF'
# Feature Specification: User Authentication

## Overview
Implement user authentication with frontend login form and backend API.

## Requirements
- Frontend: Login form with email/password
- Backend: POST /api/auth/login endpoint
- Security: Password hashing, JWT tokens
EOF
```

2. **Invoke router agent**:
```python
# tests/integration/test_intelligent_routing.py
from sdd.agents.architecture.router import RouterAgent

def test_router_identifies_multi_domain_feature():
    # Arrange
    agent = RouterAgent()
    request = AgentInput(
        agent_id="architecture.router",
        task_id="test-002",
        phase="planning",
        input_data={
            "task_description": "Implement user authentication with frontend and backend",
            "domains_detected": ["frontend", "backend", "security"],
            "current_state": {"completed_agents": [], "failed_agents": []}
        },
        context=AgentContext(spec_path="/tmp/test-spec-multi-domain.md")
    )

    # Act
    response = agent.route(request)

    # Assert
    assert response.success == True
    decision = response.output_data
    assert "engineering.backend" in decision["selected_agents"]
    assert "engineering.frontend" in decision["selected_agents"]
    assert "security.specialist" in decision["selected_agents"]
    assert decision["execution_strategy"] == "dag"  # Sequential with dependencies
    assert "engineering.backend" in decision["dependency_graph"]
```

3. **Run test**:
```bash
pytest tests/integration/test_intelligent_routing.py::test_router_identifies_multi_domain_feature -v
```

4. **Expected Output**:
```
PASSED: Router correctly identifies multi-domain feature
Selected Agents: [engineering.backend, security.specialist, engineering.frontend]
Execution Strategy: dag
Dependency Graph:
  engineering.backend: []
  security.specialist: [engineering.backend]
  engineering.frontend: [engineering.backend, security.specialist]
```

### Validation
- [ ] Router selects all required domain agents
- [ ] Execution strategy is DAG (not parallel)
- [ ] Dependency graph correctly orders agents
- [ ] Backend → Security → Frontend sequence enforced

---

## Scenario 3: Self-Healing - Syntax Error Auto-Fix

**User Story**: Self-Healing Acceptance Scenario 5
**Requirement**: FR-012, FR-013, FR-014, FR-016

### Test Steps

1. **Create code with syntax error**:
```python
# /tmp/test-code-syntax-error.py
def calculate_total(items):
    total = 0
    for item in items  # Missing colon
        total += item.price
    return total
```

2. **Invoke auto-debug agent**:
```python
# tests/integration/test_auto_debug.py
from sdd.agents.engineering.autodebug import AutoDebugAgent

def test_autodebug_fixes_syntax_error():
    # Arrange
    agent = AutoDebugAgent()
    with open("/tmp/test-code-syntax-error.py") as f:
        failed_code = f.read()

    request = AgentInput(
        agent_id="engineering.autodebug",
        task_id="test-003",
        phase="implementation",
        input_data={
            "failed_code": failed_code,
            "stack_trace": "SyntaxError: invalid syntax (line 3)",
            "test_expectations": ["Returns sum of item prices"],
            "max_iterations": 5
        },
        context=AgentContext()
    )

    # Act
    response = agent.debug(request)

    # Assert
    assert response.success == True
    session = response.output_data
    assert session["resolved"] == True  # Error fixed
    assert session["total_iterations"] == 1  # Fixed on first attempt
    assert session["error_pattern"] == "syntax"
    assert ":" in session["final_code"]  # Colon added
    assert session.get("escalated") != True  # Not escalated
```

3. **Run test**:
```bash
pytest tests/integration/test_auto_debug.py::test_autodebug_fixes_syntax_error -v
```

4. **Expected Output**:
```
PASSED: Auto-debug successfully fixes syntax error
Error Pattern: syntax
Iterations: 1
Repair: Added colon after for statement (line 3)
Test Result: passed
```

### Validation
- [ ] Error detected and classified as "syntax"
- [ ] Repair applied in single iteration
- [ ] Final code has colon added
- [ ] Tests pass after repair
- [ ] Not escalated to human

---

## Scenario 4: Iterative Refinement - Specification Improvement

**User Story**: Iterative Refinement Acceptance Scenario 7
**Requirement**: FR-019, FR-020, FR-021, FR-022, FR-023

### Test Steps

1. **Create low-quality specification**:
```bash
cat > /tmp/test-spec-low-quality.md << 'EOF'
# Feature Specification: Simple Feature

## Overview
A feature.

## Requirements
- Do stuff
EOF
```

2. **Run refinement loop**:
```python
# tests/integration/test_refinement_loop.py
from sdd.refinement.loop import RefinementLoop
from sdd.agents.quality.verifier import VerificationAgent

def test_refinement_loop_improves_specification():
    # Arrange
    loop = RefinementLoop(
        max_rounds=20,
        quality_threshold=0.85,
        early_stopping_threshold=0.95
    )
    verifier = VerificationAgent()

    # Act
    result = loop.refine(
        task_id="test-004",
        phase="specification",
        artifact_path="/tmp/test-spec-low-quality.md",
        verifier=verifier
    )

    # Assert
    assert result.completed == True
    assert result.quality_achieved == True
    assert result.final_quality_score >= 0.85
    assert result.total_rounds < 20  # Should not hit max
    assert result.total_rounds >= 2  # At least some refinement
    assert len(result.feedback_accumulated) > 0

    # Check refinement state persisted
    state_path = f".docs/agents/shared/refinement-state/test-004.json"
    assert os.path.exists(state_path)
```

3. **Run test**:
```bash
pytest tests/integration/test_refinement_loop.py::test_refinement_loop_improves_specification -v
```

4. **Expected Output**:
```
PASSED: Refinement loop improves specification to quality threshold
Initial Quality: 0.25
Round 1 Quality: 0.52 (feedback: Add user scenarios, requirements, entities)
Round 2 Quality: 0.78 (feedback: Improve requirement clarity)
Round 3 Quality: 0.87 (feedback: None - threshold met)
Final Quality: 0.87
Total Rounds: 3
```

### Validation
- [ ] Quality score improves with each iteration
- [ ] Refinement stops when threshold (0.85) met
- [ ] Feedback accumulates across iterations
- [ ] Refinement state persisted to filesystem
- [ ] Doesn't hit maximum 20 rounds

---

## Scenario 5: Context Intelligence - Semantic Retrieval

**User Story**: Context Intelligence Acceptance Scenario 10
**Requirement**: FR-026, FR-027, FR-028, FR-030, FR-031

### Test Steps

1. **Initialize context index** (one-time setup):
```bash
python scripts/index_codebase.py --paths .claude/agents .specify/memory specs
```

2. **Invoke context analyzer**:
```python
# tests/integration/test_context_intelligence.py
from sdd.agents.architecture.context_analyzer import ContextAnalyzer
import time

def test_context_retrieval_performance():
    # Arrange
    analyzer = ContextAnalyzer()
    request = AgentInput(
        agent_id="architecture.context_analyzer",
        task_id="test-005",
        phase="specification",
        input_data={
            "task_description": "Implement quality verification gates",
            "search_keywords": ["quality", "verification", "gate", "validation"],
            "scan_paths": [".claude/agents", ".specify/memory"],
            "max_results": 10,
            "performance_target_ms": 2000
        },
        context=AgentContext()
    )

    # Act
    start = time.time()
    response = analyzer.analyze(request)
    latency_ms = (time.time() - start) * 1000

    # Assert
    assert response.success == True
    summary = response.output_data
    assert len(summary["relevant_files"]) > 0
    assert summary["retrieval_latency_ms"] < 2000  # Performance requirement
    assert summary["retrieval_method"] in ["semantic_embedding", "keyword_fallback"]
    assert latency_ms < 2000  # End-to-end under 2 seconds

    # Check relevance
    file_paths = summary["relevant_files"]
    assert any("verifier" in path.lower() or "quality" in path.lower() for path in file_paths)
```

3. **Run test**:
```bash
pytest tests/integration/test_context_intelligence.py::test_context_retrieval_performance -v
```

4. **Expected Output**:
```
PASSED: Context retrieval meets performance requirements
Relevant Files Found: 7
  - .specify/memory/constitution.md
  - .claude/agents/quality/verifier.md (hypothetical)
  - specs/000-agent-framework/spec.md
Retrieval Latency: 487ms
Retrieval Method: semantic_embedding
End-to-End Latency: 521ms
```

### Validation
- [ ] Context retrieval completes in <2 seconds
- [ ] Relevant files identified (contains "quality" or "verification")
- [ ] Semantic embedding method used (not fallback)
- [ ] File summaries provided
- [ ] Existing patterns identified

---

## Scenario 6: Output Standardization - Pre-Commit Validation

**User Story**: Output Standardization Acceptance Scenario (implied from FR-034 to FR-040)
**Requirement**: FR-034, FR-035, FR-036, FR-037, FR-039

### Test Steps

1. **Prepare code for finalization**:
```bash
# Create test files
mkdir -p /tmp/test-finalization/src /tmp/test-finalization/tests
cat > /tmp/test-finalization/src/calculator.py << 'EOF'
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
EOF

cat > /tmp/test-finalization/tests/test_calculator.py << 'EOF'
from src.calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
EOF
```

2. **Invoke compliance finalizer**:
```python
# tests/integration/test_compliance_finalizer.py
from sdd.agents.quality.finalizer import ComplianceFinalizerAgent

def test_finalizer_blocks_commit_without_approval():
    # Arrange
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id="test-006",
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": ["/tmp/test-finalization/src/calculator.py"],
                "test_files": ["/tmp/test-finalization/tests/test_calculator.py"]
            },
            "validation_checks": [
                "tests_passing",
                "code_coverage",
                "constitutional_compliance"
            ],
            "git_operation": {
                "type": "commit",
                "message": "feat: Add calculator",
                "files_to_stage": ["src/calculator.py", "tests/test_calculator.py"]
            }
        },
        context=AgentContext()
    )

    # Act
    response = agent.finalize(request)

    # Assert
    assert response.success == True
    result = response.output_data
    assert result["git_approval_required"] == True  # MUST require approval
    assert result.get("user_approved") != True  # Not auto-approved
    assert "git_operation_summary" in result  # User sees what will be committed
```

3. **Simulate user approval** (in real system, user would approve):
```python
def test_finalizer_executes_commit_after_approval():
    # Arrange (same as above)
    # ...

    # Act - Simulate user approval
    approval_response = agent.request_user_approval(
        operation_summary=result["git_operation_summary"]
    )
    # In real system: user_approved = get_user_input("Approve commit? (y/n)")

    # Assert
    assert approval_response.requires_approval == True
    # If user approves, then git operation proceeds
```

4. **Run test**:
```bash
pytest tests/integration/test_compliance_finalizer.py::test_finalizer_blocks_commit_without_approval -v
```

5. **Expected Output**:
```
PASSED: Finalizer requires user approval for git operations
All Checks Passed: True
Git Approval Required: True
User Approved: None (awaiting input)
Git Operation Summary:
  Commit 2 files with message:
  feat: Add calculator
```

### Validation
- [ ] All validation checks pass (tests, coverage, compliance)
- [ ] Git approval explicitly required (CRITICAL)
- [ ] User sees clear summary of git operation
- [ ] Commit does NOT execute without approval
- [ ] Principle VI (Git Operation Approval) enforced

---

## Scenario 7: End-to-End Multi-Agent Coordination

**User Story**: Combined scenarios - full workflow
**Requirement**: All FRs integrated

### Test Steps

1. **Run full workflow simulation**:
```python
# tests/integration/test_end_to_end_workflow.py
from sdd.orchestration.coordinator import MultiAgentCoordinator

def test_full_workflow_specification_to_commit():
    # Arrange
    coordinator = MultiAgentCoordinator()

    # Act - Run full workflow
    result = coordinator.execute_workflow(
        feature_name="test-feature",
        spec_path="/tmp/test-feature-spec.md",
        workflow_phases=["specification", "planning", "implementation", "validation"]
    )

    # Assert
    assert result.completed == True
    assert result.all_phases_passed == True

    # Verify each phase
    assert result.phases["specification"]["verification_passed"] == True
    assert result.phases["planning"]["routing_decision"] is not None
    assert result.phases["implementation"]["debug_sessions"] >= 0
    assert result.phases["validation"]["finalizer_approved"] == True  # User approved

    # Check metrics collected
    metrics = result.metrics
    assert metrics.task_id is not None
    assert metrics.completed_without_intervention in [True, False]
    assert metrics.refinement_rounds >= 0
    assert metrics.errors_auto_resolved >= 0
```

2. **Run test**:
```bash
pytest tests/integration/test_end_to_end_workflow.py::test_full_workflow_specification_to_commit -v
```

3. **Expected Output**:
```
PASSED: Full workflow completes successfully
Phase: specification
  - Verification: PASS (quality: 0.91)
  - Refinement rounds: 2
Phase: planning
  - Router: 1 agent selected
  - Contracts generated: 3
Phase: implementation
  - Code generated: 5 files
  - Auto-debug sessions: 1 (resolved: 1)
Phase: validation
  - Finalizer: PASS
  - User approval: REQUIRED (approved: True)
Metrics:
  - Task completion: WITH intervention (user approval)
  - Refinement rounds: 2
  - Debug success: 100%
```

### Validation
- [ ] All workflow phases complete successfully
- [ ] Quality gates enforce standards at each phase
- [ ] Router coordinates agent invocations
- [ ] Auto-debug resolves errors automatically
- [ ] Finalizer requires user approval
- [ ] Metrics collected throughout workflow

---

## Performance Validation

Run performance benchmarks to validate targets:

```bash
# Verify context retrieval <2s
pytest tests/integration/test_context_intelligence.py::test_context_retrieval_performance --benchmark

# Verify debug iteration cycle <30s
pytest tests/integration/test_auto_debug.py --benchmark

# Verify refinement efficiency
pytest tests/integration/test_refinement_loop.py --benchmark
```

**Expected Results**:
- Context retrieval: <2000ms (FR-031)
- Debug iteration: <30000ms
- Refinement round: <60000ms

---

## Metrics Collection Verification

Validate metrics are being collected correctly:

```bash
# Run full workflow and check metrics
pytest tests/integration/test_end_to_end_workflow.py -v
cat .docs/agents/shared/metrics/test/test-*.json | jq '.task_completion_accuracy'
```

**Expected Metrics**:
- `task_id`: UUID
- `refinement_rounds`: int
- `errors_auto_resolved`: int >= 0
- `context_queries`: int >= 0
- `completed_without_intervention`: bool

---

## Summary

This quickstart guide covers 7 integration test scenarios:
1. Quality Verification - Specification gate blocks progression
2. Intelligent Routing - Multi-domain feature orchestration
3. Self-Healing - Syntax error auto-fix
4. Iterative Refinement - Specification improvement loop
5. Context Intelligence - Semantic retrieval performance
6. Output Standardization - Pre-commit validation with user approval
7. End-to-End - Full workflow coordination

All scenarios validate functional requirements and user acceptance criteria from spec.md.

**Next Steps**:
1. Implement agent libraries to make contract tests pass
2. Add additional edge case tests
3. Benchmark performance at scale
4. Validate 3.5x improvement after implementation

---

**Quickstart Guide Complete**: 2025-11-10
**Ready for**: Phase 2 - Task Generation (/tasks command)
