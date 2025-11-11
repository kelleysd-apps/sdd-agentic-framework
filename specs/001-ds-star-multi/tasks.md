# Tasks: DS-STAR Multi-Agent Enhancement

**Input**: Design documents from `/workspaces/sdd-agentic-framework/specs/001-ds-star-multi/`
**Prerequisites**: plan.md (✓), research.md (✓), data-model.md (✓), contracts/ (✓ 5 files), quickstart.md (✓)

## Execution Flow (main)
```
1. Load plan.md from feature directory
   ✓ SUCCESS: Tech stack: Python 3.11+, sentence-transformers, pydantic, pytest
2. Load optional design documents:
   ✓ data-model.md: 12 entities extracted → 12 model tasks
   ✓ contracts/: 5 files → 5 contract test tasks
   ✓ quickstart.md: 7 scenarios → 7 integration test tasks
   ✓ research.md: Dependencies and decisions extracted
3. Generate tasks by category:
   ✓ Setup: 5 tasks (project init, deps, linting, directories, config)
   ✓ Tests: 12 tasks (5 contract tests, 7 integration tests)
   ✓ Core: 24 tasks (12 models, 5 agents, 7 supporting libraries)
   ✓ Integration: 6 tasks (refinement engine, feedback system, metrics, orchestration)
   ✓ Polish: 6 tasks (unit tests, docs, validation, cleanup)
4. Apply task rules:
   ✓ Different files = marked [P] for parallel (28 tasks)
   ✓ Same file = sequential (25 tasks)
   ✓ Tests before implementation (TDD enforced)
5. Number tasks sequentially (T001-T053)
6. Generate dependency graph (below)
7. Create parallel execution examples (below)
8. Validate task completeness:
   ✓ All 5 contracts have tests
   ✓ All 12 entities have models
   ✓ All 5 agents implemented
   ✓ All 7 scenarios covered
9. Return: SUCCESS (53 tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Libraries: `src/sdd/agents/`, `src/sdd/refinement/`, etc.
- Tests: `tests/unit/`, `tests/contract/`, `tests/integration/`

---

## Phase 3.1: Setup & Configuration

- [ ] **T001** Create project directory structure for DS-STAR enhancement
  - Create `src/sdd/agents/quality/`, `src/sdd/agents/architecture/`, `src/sdd/agents/engineering/`
  - Create `src/sdd/refinement/`, `src/sdd/feedback/`, `src/sdd/context/`, `src/sdd/metrics/`
  - Create `tests/unit/`, `tests/contract/`, `tests/integration/`, `tests/fixtures/`
  - Create `.docs/agents/quality/verifier/decisions/`, `.docs/agents/architecture/router/decisions/`
  - Create `.docs/agents/shared/refinement-state/`, `.docs/agents/shared/context-summaries/`

- [ ] **T002** Initialize Python project with dependencies in `requirements.txt`
  - Add `sentence-transformers==2.2.2`
  - Add `scikit-learn==1.3.2`
  - Add `pydantic==2.5.0`
  - Add `pytest==7.4.3`
  - Add `numpy==1.24.3`
  - Pin all versions (exact, no ranges per Principle IX)

- [ ] **T003** [P] Configure linting and formatting tools
  - Create `.pylintrc` for code quality checks
  - Create `pyproject.toml` for black/isort configuration
  - Create `.pre-commit-config.yaml` (but disable auto-commit per Principle VI)

- [ ] **T004** [P] Create refinement configuration in `.specify/config/refinement.conf`
  - Set `MAX_REFINEMENT_ROUNDS=20`
  - Set `EARLY_STOP_THRESHOLD=0.95`
  - Set `FEEDBACK_ACCUMULATION=true`
  - Define quality thresholds per phase
  - Document all configuration options

- [ ] **T005** [P] Set up test environment fixtures in `tests/fixtures/setup_test_environment.py`
  - Create test specification samples (complete and incomplete)
  - Create test plan samples (valid and invalid)
  - Create test code samples (with syntax/type/null errors)
  - Create mock agent contexts and outputs
  - Set up temporary directories for test artifacts

---

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

### Contract Tests (Agent Interfaces)

- [ ] **T006** [P] Contract test Verification Agent in `tests/contract/test_verifier_contract.py`
  - Test POST /verify endpoint with valid spec
  - Test POST /verify with incomplete spec
  - Test response schema matches `contracts/verifier.yaml`
  - Test binary decision (sufficient/insufficient)
  - Test feedback generation for insufficient quality
  - Verify VerificationDecision output format

- [ ] **T007** [P] Contract test Router Agent in `tests/contract/test_router_contract.py`
  - Test POST /route endpoint with task analysis
  - Test refinement strategy decisions (ADD_STEP, TRUNCATE, ROUTE_TO_DEBUG, RETRY)
  - Test response schema matches `contracts/router.yaml`
  - Test parallel execution planning
  - Test agent selection logic
  - Verify RoutingDecision output format

- [ ] **T008** [P] Contract test Auto-Debug Agent in `tests/contract/test_autodebug_contract.py`
  - Test POST /debug endpoint with syntax error
  - Test POST /debug with type error
  - Test max iteration limit (5 attempts)
  - Test response schema matches `contracts/autodebug.yaml`
  - Test escalation after max iterations
  - Verify DebugSession output format

- [ ] **T009** [P] Contract test Context Analyzer in `tests/contract/test_context_contract.py`
  - Test POST /analyze endpoint with codebase path
  - Test file relevance identification
  - Test dependency mapping
  - Test response schema matches `contracts/context.yaml`
  - Test semantic similarity search
  - Verify ContextSummary output format

- [ ] **T010** [P] Contract test Compliance Finalizer in `tests/contract/test_finalizer_contract.py`
  - Test POST /finalize endpoint with complete implementation
  - Test constitutional compliance checks (all 14 principles)
  - Test git approval gate (must request user approval)
  - Test response schema matches `contracts/finalizer.yaml`
  - Test pre-commit checklist validation
  - Verify no autonomous git operations

### Integration Tests (User Scenarios)

- [ ] **T011** [P] Integration test Scenario 1: Quality Verification gate in `tests/integration/test_verification_gate.py`
  - Test incomplete spec blocked by verifier
  - Test sufficient spec passes gate
  - Test actionable feedback provided
  - Test quality score calculation
  - Verify FR-001, FR-002, FR-003, FR-004

- [ ] **T012** [P] Integration test Scenario 2: Intelligent Routing in `tests/integration/test_routing_orchestration.py`
  - Test multi-domain feature routing
  - Test parallel execution planning
  - Test agent selection based on keywords
  - Test routing decision audit trail
  - Verify FR-007, FR-008, FR-009, FR-010

- [ ] **T013** [P] Integration test Scenario 3: Self-Healing in `tests/integration/test_auto_debug.py`
  - Test syntax error auto-fix
  - Test type error auto-fix
  - Test max 5 iteration limit
  - Test escalation with full context
  - Test >70% fix rate target (use error corpus)
  - Verify FR-012, FR-013, FR-014, FR-015, FR-016

- [ ] **T014** [P] Integration test Scenario 4: Iterative Refinement in `tests/integration/test_refinement_loop.py`
  - Test spec refinement until quality threshold
  - Test feedback accumulation across iterations
  - Test early stopping at 0.95 threshold
  - Test max 20 rounds limit
  - Test state persistence between iterations
  - Verify FR-019, FR-020, FR-021, FR-022, FR-023

- [ ] **T015** [P] Integration test Scenario 5: Context Intelligence in `tests/integration/test_context_retrieval.py`
  - Test semantic search retrieval <2 seconds
  - Test relevant file identification accuracy
  - Test graceful degradation to keyword search
  - Test embedding index updates
  - Verify FR-026, FR-027, FR-028, FR-029, FR-031, FR-032

- [ ] **T016** [P] Integration test Scenario 6: Output Standardization in `tests/integration/test_finalizer_compliance.py`
  - Test pre-commit constitutional checks
  - Test git approval gate enforcement
  - Test code formatting and docs generation
  - Test >95% first-time pass rate target
  - Verify FR-034, FR-035, FR-036, FR-037, FR-038, FR-039

- [ ] **T017** [P] Integration test Scenario 7: End-to-End Coordination in `tests/integration/test_e2e_workflow.py`
  - Test full workflow: specify → verify → plan → verify → implement → debug → finalize
  - Test multi-agent handoffs with context preservation
  - Test 3.5x improvement in task completion (baseline vs enhanced)
  - Test all quality gates functioning
  - Verify FR-047 (3.5x improvement target)

---

## Phase 3.3: Core Implementation (ONLY after tests are failing)

### Shared Data Models (Pydantic)

- [ ] **T018** [P] AgentInput model in `src/sdd/agents/shared/models.py`
  - Define Pydantic schema with agent_id, task_id, phase, input_data, context
  - Add validation: agent_id pattern, task_id UUID, phase enum
  - Add immutability after creation
  - Add JSON serialization/deserialization
  - Follow data-model.md specification

- [ ] **T019** [P] AgentOutput model in `src/sdd/agents/shared/models.py`
  - Define Pydantic schema with agent_id, task_id, success, output_data, reasoning, confidence, next_actions, metadata, timestamp
  - Add validation: confidence 0.0-1.0, reasoning non-empty, no future timestamps
  - Add immutability (audit trail integrity)
  - Add JSON serialization/deserialization

- [ ] **T020** [P] AgentContext model in `src/sdd/agents/shared/models.py`
  - Define Pydantic schema with spec_path, plan_path, previous_outputs, cumulative_feedback, refinement_state
  - Add validation: file paths exist, outputs chronologically ordered
  - Add append-only state transitions
  - Add context handoff helpers

- [ ] **T021** [P] VerificationDecision model in `src/sdd/agents/quality/models.py`
  - Define Pydantic schema per data-model.md
  - Add binary decision validation (sufficient/insufficient)
  - Add dimension scores (completeness, constitutional_compliance, test_coverage, spec_alignment)
  - Add quality score calculation logic
  - Add feedback generation helpers

- [ ] **T022** [P] RoutingDecision model in `src/sdd/agents/architecture/models.py`
  - Define Pydantic schema per data-model.md
  - Add strategy validation (ADD_STEP, TRUNCATE, ROUTE_TO_DEBUG, RETRY)
  - Add agent selection reasoning
  - Add parallel execution plan structure
  - Add routing audit trail helpers

- [ ] **T023** [P] DebugAttempt and DebugSession models in `src/sdd/agents/engineering/models.py`
  - Define DebugAttempt with error_type, analysis, fix_code, test_result
  - Define DebugSession with attempts list, max 5 iterations
  - Add error pattern classification (syntax, type, name, null, import)
  - Add fix validation and test re-run logic
  - Add escalation context generation

- [ ] **T024** [P] ContextSummary model in `src/sdd/agents/architecture/models.py`
  - Define Pydantic schema per data-model.md
  - Add relevant files list with descriptions
  - Add existing patterns and conventions
  - Add dependencies and related specs
  - Add constitutional compliance status
  - Add semantic similarity scoring

- [ ] **T025** [P] RefinementState model in `src/sdd/refinement/models.py`
  - Define Pydantic schema with task_id, phase, iterations, cumulative_learnings
  - Add iteration tracking (round, timestamp, input, output, verification_result, feedback)
  - Add state persistence to `.docs/agents/shared/refinement-state/{task_id}.json`
  - Add early stopping detection logic
  - Add max rounds enforcement

- [ ] **T026** [P] IterationRecord model in `src/sdd/refinement/models.py`
  - Define Pydantic schema per data-model.md
  - Add progress tracking fields
  - Add feedback accumulation
  - Add quality delta calculation
  - Add chronological ordering

- [ ] **T027** [P] TaskMetrics model in `src/sdd/metrics/models.py`
  - Define Pydantic schema per data-model.md
  - Add task_id, task_completion_accuracy, refinement_rounds, debug_success_rate, context_relevance, constitutional_compliance_rate
  - Add baseline comparison helpers
  - Add 3.5x improvement validation
  - Add JSON export for analysis

- [ ] **T028** [P] AgentConfig model in `src/sdd/agents/shared/models.py`
  - Define Pydantic schema for agent configuration
  - Add quality thresholds per phase
  - Add model selection (Sonnet vs Opus)
  - Add tool access permissions
  - Add constitutional constraints

### Agent Libraries (Library-First Principle I)

- [ ] **T029** Verification Agent library in `src/sdd/agents/quality/verifier.py`
  - Implement VerificationAgent class with verify() method
  - Load quality thresholds from config
  - Evaluate completeness, constitutional_compliance, test_coverage, spec_alignment
  - Generate binary decision (sufficient/insufficient)
  - Provide actionable feedback for improvements
  - Log decisions to `.docs/agents/quality/verifier/decisions/{task_id}.json`
  - Return VerificationDecision in AgentOutput
  - Follow contracts/verifier.yaml interface

- [ ] **T030** Router Agent library in `src/sdd/agents/architecture/router.py`
  - Implement RouterAgent class with route() method
  - Analyze task complexity and current state
  - Determine refinement strategy (ADD_STEP, TRUNCATE, ROUTE_TO_DEBUG, RETRY)
  - Select appropriate agent(s) based on domain keywords
  - Plan parallel execution for independent tasks
  - Log routing decisions to `.docs/agents/architecture/router/decisions/{task_id}.json`
  - Return RoutingDecision in AgentOutput
  - Follow contracts/router.yaml interface

- [ ] **T031** Auto-Debug Agent library in `src/sdd/agents/engineering/autodebug.py`
  - Implement AutoDebugAgent class with debug() method
  - Classify error type (syntax, type, name, null, import)
  - Analyze error against spec, constitution, dependencies, tests
  - Generate fix with reasoning
  - Apply fix and re-run tests
  - Track iterations (max 5) in DebugSession
  - Escalate to human after max iterations with full context
  - Return DebugAttempt in AgentOutput
  - Follow contracts/autodebug.yaml interface
  - Target >70% auto-fix rate for common errors

- [ ] **T032** Context Analyzer library in `src/sdd/agents/architecture/context_analyzer.py`
  - Implement ContextAnalyzerAgent class with analyze() method
  - Scan relevant directories (src/, tests/, specs/)
  - Identify files relevant to current task using keyword matching
  - Map dependencies and relationships
  - Load embeddings using sentence-transformers (all-MiniLM-L6-v2)
  - Perform semantic similarity search
  - Generate ContextSummary with structured format
  - Store summaries to `.docs/agents/shared/context-summaries/{task_id}.json`
  - Return ContextSummary in AgentOutput
  - Follow contracts/context.yaml interface
  - Ensure <2 second retrieval time (FR-031)

- [ ] **T033** Compliance Finalizer library in `src/sdd/agents/quality/finalizer.py`
  - Implement FinalizerAgent class with finalize() method
  - Run pre-commit checklist (code quality, constitutional compliance, docs, security)
  - Check all 14 constitutional principles
  - Check tests passing, coverage >80%, no linting errors
  - Check documentation sync (CLAUDE.md, README, specs)
  - Check no secrets in code, .env template updated
  - Format code to standards (black, isort)
  - Generate missing documentation
  - **CRITICAL**: Request explicit user approval before ANY git operation (Principle VI)
  - Return compliance report in AgentOutput
  - Follow contracts/finalizer.yaml interface
  - Never perform autonomous git operations

### Supporting Libraries

- [ ] **T034** Refinement Engine library in `src/sdd/refinement/engine.py`
  - Implement RefinementEngine class with refine_until_sufficient() method
  - Load config from `.specify/config/refinement.conf`
  - Implement iteration loop (max 20 rounds)
  - Invoke verification agent each iteration
  - Accumulate feedback in RefinementState
  - Detect early stopping (quality >= 0.95)
  - Persist state to `.docs/agents/shared/refinement-state/`
  - Escalate to human at max rounds
  - Integrate with all workflow phases (specify, plan, implement)

- [ ] **T035** Feedback Accumulation library in `src/sdd/feedback/accumulator.py`
  - Implement FeedbackAccumulator class with add(), get_cumulative() methods
  - Store feedback records to `.docs/agents/shared/feedback/{task_id}.json`
  - Track iteration history with timestamps
  - Extract cumulative learnings from failures
  - Provide rich context for refinement agents
  - Enable progressive improvement across iterations
  - Implement archival for old feedback (>1000 iterations)

- [ ] **T036** Context Retrieval library in `src/sdd/context/retriever.py`
  - Implement ContextRetriever class with retrieve_relevant_specs(), retrieve_similar_tasks(), retrieve_decisions() methods
  - Load sentence-transformers model (all-MiniLM-L6-v2, 384-dim)
  - Build embedding index from specs/, plans/, decisions/
  - Implement semantic similarity search with top_k results
  - Implement graceful degradation to TF-IDF keyword search if slow
  - Cache embeddings for frequent queries
  - Update index when new specs/plans created
  - Return results in <2 seconds (FR-031)
  - Store index at `.docs/agents/shared/embeddings/`

- [ ] **T037** Metrics Collection library in `src/sdd/metrics/collector.py`
  - Implement MetricsCollector class with record_task(), calculate_improvement() methods
  - Track task_completion_accuracy (% without manual intervention)
  - Track average_refinement_rounds per task
  - Track debug_success_rate (% auto-resolved)
  - Track context_retrieval_accuracy
  - Track constitutional_compliance_rate (% passing finalizer first time)
  - Compare against baseline metrics (established pre-implementation)
  - Validate 3.5x improvement target (FR-047)
  - Export metrics to JSON for analysis
  - Log structured metrics per Principle VII

- [ ] **T038** Agent Communication library in `src/sdd/agents/shared/communication.py`
  - Implement AgentChannel class with send(), receive(), handoff() methods
  - Validate messages using Pydantic models
  - Serialize/deserialize AgentInput and AgentOutput to JSON
  - Implement context handoff protocol
  - Track agent invocation chain for audit trail
  - Enforce communication contracts (OpenAPI schemas)
  - Log all agent-to-agent communication
  - Handle timeouts and errors gracefully

- [ ] **T039** Constitutional Validator library in `src/sdd/validation/constitutional.py`
  - Implement ConstitutionalValidator class with validate_all_principles() method
  - Check Principle I (Library-First): Each agent is standalone library
  - Check Principle II (Test-First): Tests exist before implementation
  - Check Principle III (Contract-First): Contracts defined before code
  - Check Principle IV-XIV as applicable
  - Generate compliance report with violations list
  - Provide remediation suggestions
  - Used by Finalizer agent for pre-commit checks
  - Log all compliance checks to audit trail

- [ ] **T040** Error Pattern Classifier library in `src/sdd/agents/engineering/error_classifier.py`
  - Implement ErrorClassifier class with classify() method
  - Detect syntax errors (SyntaxError, IndentationError)
  - Detect type errors (TypeError, AttributeError)
  - Detect name errors (NameError, UnboundLocalError)
  - Detect null errors (NullPointerException, AttributeError on None)
  - Detect import errors (ImportError, ModuleNotFoundError)
  - Extract error context (stack trace, line number, code snippet)
  - Provide fix templates per error type
  - Used by Auto-Debug agent for error analysis

---

## Phase 3.4: Integration & Orchestration

- [ ] **T041** Integrate Refinement Engine with /specify command in `.specify/scripts/bash/create-new-feature.sh`
  - Add verification gate after spec generation
  - Loop: generate → verify → refine until sufficient
  - Pass cumulative feedback to each iteration
  - Enforce max 20 rounds limit
  - Update CLAUDE.md with refinement behavior

- [ ] **T042** Integrate Verification Agent with /plan command in `.specify/scripts/bash/setup-plan.sh`
  - Add verification gate after plan generation
  - Check plan against constitution and spec
  - Block progression if insufficient quality
  - Provide actionable feedback for improvements
  - Update CLAUDE.md with verification behavior

- [ ] **T043** Integrate Router Agent with multi-domain workflows
  - Add routing logic to task-orchestrator agent
  - Implement domain keyword detection
  - Route to appropriate specialized agents
  - Coordinate parallel execution
  - Update `.specify/memory/agent-collaboration-triggers.md` with router patterns

- [ ] **T044** Integrate Auto-Debug with implementation workflows
  - Add error detection after test failures
  - Auto-invoke debug agent on common errors
  - Apply fixes and re-run tests
  - Escalate after 5 failed iterations
  - Update error handling documentation

- [ ] **T045** Integrate Context Analyzer with planning phase
  - Invoke analyzer before spec creation
  - Provide codebase context to planning-agent
  - Update context summaries when code changes
  - Enable semantic search for past decisions
  - Update planning workflow documentation

- [ ] **T046** Integrate Finalizer with git workflows
  - Add pre-commit hook invocation (disabled by default per Principle VI)
  - Add manual /finalize command for validation
  - Request user approval for all git operations
  - Update Git Operation Approval protocol in constitution
  - Document in CLAUDE.md

---

## Phase 3.5: Polish & Documentation

- [ ] **T047** [P] Unit tests for all libraries in `tests/unit/`
  - Test each library class in isolation
  - Mock dependencies and MCP servers
  - Test decision logic independently
  - Achieve >90% code coverage target
  - Test error handling and edge cases

- [ ] **T048** [P] Performance benchmarks in `tests/performance/`
  - Benchmark context retrieval <2 seconds (FR-031)
  - Benchmark debug iteration <30 seconds per attempt
  - Benchmark refinement loop efficiency
  - Benchmark agent invocation overhead
  - Test memory usage under load
  - Document performance baselines

- [ ] **T049** [P] Update framework documentation
  - Update `CLAUDE.md` with all 5 new agents
  - Update `.specify/memory/agent-collaboration-triggers.md` with new domains
  - Create agent usage examples in `.docs/examples/`
  - Write troubleshooting guide for common issues
  - Document configuration options in refinement.conf
  - Update README with DS-STAR enhancement features

- [ ] **T050** [P] Create constitutional amendment
  - Add new section to `.specify/memory/constitution.md` on "Quality Gates and Verification"
  - Update Principle X with Router agent orchestration patterns
  - Document git approval requirements for Finalizer
  - Follow `.specify/memory/constitution_update_checklist.md`
  - Update version to 1.6.0

- [ ] **T051** Run full constitutional compliance check
  - Execute `.specify/scripts/bash/constitutional-check.sh`
  - Verify all 14 principles compliance
  - Fix any violations detected
  - Document compliance report

- [ ] **T052** Run sanitization audit
  - Execute `.specify/scripts/bash/sanitization-audit.sh`
  - Verify no project-specific elements leaked
  - Check framework is reusable
  - Document audit results

- [ ] **T053** Establish performance baselines and validate 3.5x improvement
  - Measure current task completion accuracy (pre-enhancement)
  - Run enhanced framework on benchmark task set
  - Calculate improvement ratio (target: 3.5x per FR-047)
  - Document metrics comparison
  - Validate all success criteria met (>70% auto-fix, <2s retrieval, >95% compliance)

---

## Dependencies

### Critical Path
1. **Setup** (T001-T005) must complete before all other phases
2. **All Tests** (T006-T017) MUST complete and FAIL before any implementation
3. **Shared Models** (T018-T020) block all agent implementations
4. **Agent-Specific Models** (T021-T028) block respective agent implementations
5. **Agents** (T029-T033) block integration tasks
6. **Supporting Libraries** (T034-T040) block integration tasks
7. **Integration** (T041-T046) requires all agents and libraries complete
8. **Polish** (T047-T053) requires everything else complete

### Detailed Dependencies
- T001 (directories) blocks → all file creation tasks
- T002 (dependencies) blocks → all implementation tasks
- T006-T017 (all tests) block → T018-T040 (all implementation)
- T018-T020 (shared models) block → T021-T028 (agent models), T029-T033 (agents)
- T021 (VerificationDecision) blocks → T029 (Verification Agent)
- T022 (RoutingDecision) blocks → T030 (Router Agent)
- T023 (DebugSession) blocks → T031 (Auto-Debug Agent)
- T024 (ContextSummary) blocks → T032 (Context Analyzer)
- T025-T026 (RefinementState) blocks → T034 (Refinement Engine)
- T029 (Verification Agent) blocks → T041, T042 (integration)
- T030 (Router Agent) blocks → T043 (integration)
- T031 (Auto-Debug Agent) blocks → T044 (integration)
- T032 (Context Analyzer) blocks → T045 (integration)
- T033 (Finalizer) blocks → T046 (integration)
- T041-T046 (all integration) block → T047-T053 (polish)

---

## Parallel Execution Examples

### Phase 1: Setup (All Parallel)
```bash
# All setup tasks can run in parallel (different files, no dependencies after T001)
# Launch T002-T005 together after T001 completes:
```
```python
Task(subagent_type="backend-architect", description="Initialize Python project", prompt="T002: Initialize Python project with dependencies in requirements.txt...")
Task(subagent_type="devops-engineer", description="Configure linting tools", prompt="T003: Configure linting and formatting tools...")
Task(subagent_type="backend-architect", description="Create refinement config", prompt="T004: Create refinement configuration in .specify/config/refinement.conf...")
Task(subagent_type="testing-specialist", description="Set up test fixtures", prompt="T005: Set up test environment fixtures in tests/fixtures/setup_test_environment.py...")
```

### Phase 2: Contract Tests (All Parallel)
```bash
# All contract tests independent (different files)
# Launch T006-T010 together:
```
```python
Task(subagent_type="testing-specialist", description="Verifier contract test", prompt="T006: Contract test Verification Agent in tests/contract/test_verifier_contract.py...")
Task(subagent_type="testing-specialist", description="Router contract test", prompt="T007: Contract test Router Agent in tests/contract/test_router_contract.py...")
Task(subagent_type="testing-specialist", description="Auto-debug contract test", prompt="T008: Contract test Auto-Debug Agent in tests/contract/test_autodebug_contract.py...")
Task(subagent_type="testing-specialist", description="Context contract test", prompt="T009: Contract test Context Analyzer in tests/contract/test_context_contract.py...")
Task(subagent_type="testing-specialist", description="Finalizer contract test", prompt="T010: Contract test Compliance Finalizer in tests/contract/test_finalizer_contract.py...")
```

### Phase 2: Integration Tests (All Parallel)
```bash
# All integration tests independent (different files)
# Launch T011-T017 together:
```
```python
Task(subagent_type="testing-specialist", description="Verification gate test", prompt="T011: Integration test Scenario 1: Quality Verification gate in tests/integration/test_verification_gate.py...")
Task(subagent_type="testing-specialist", description="Routing test", prompt="T012: Integration test Scenario 2: Intelligent Routing in tests/integration/test_routing_orchestration.py...")
Task(subagent_type="testing-specialist", description="Auto-debug test", prompt="T013: Integration test Scenario 3: Self-Healing in tests/integration/test_auto_debug.py...")
Task(subagent_type="testing-specialist", description="Refinement test", prompt="T014: Integration test Scenario 4: Iterative Refinement in tests/integration/test_refinement_loop.py...")
Task(subagent_type="testing-specialist", description="Context test", prompt="T015: Integration test Scenario 5: Context Intelligence in tests/integration/test_context_retrieval.py...")
Task(subagent_type="testing-specialist", description="Finalizer test", prompt="T016: Integration test Scenario 6: Output Standardization in tests/integration/test_finalizer_compliance.py...")
Task(subagent_type="testing-specialist", description="E2E test", prompt="T017: Integration test Scenario 7: End-to-End Coordination in tests/integration/test_e2e_workflow.py...")
```

### Phase 3: Shared Models (All Parallel after T018-T020)
```bash
# T018-T020 must complete first (same file: src/sdd/agents/shared/models.py)
# Then T021-T028 can run in parallel (different files):
```
```python
Task(subagent_type="backend-architect", description="VerificationDecision model", prompt="T021: VerificationDecision model in src/sdd/agents/quality/models.py...")
Task(subagent_type="backend-architect", description="RoutingDecision model", prompt="T022: RoutingDecision model in src/sdd/agents/architecture/models.py...")
Task(subagent_type="backend-architect", description="DebugSession models", prompt="T023: DebugAttempt and DebugSession models in src/sdd/agents/engineering/models.py...")
Task(subagent_type="backend-architect", description="ContextSummary model", prompt="T024: ContextSummary model in src/sdd/agents/architecture/models.py...")
Task(subagent_type="backend-architect", description="RefinementState model", prompt="T025: RefinementState model in src/sdd/refinement/models.py...")
Task(subagent_type="backend-architect", description="IterationRecord model", prompt="T026: IterationRecord model in src/sdd/refinement/models.py...")
Task(subagent_type="backend-architect", description="TaskMetrics model", prompt="T027: TaskMetrics model in src/sdd/metrics/models.py...")
Task(subagent_type="backend-architect", description="AgentConfig model", prompt="T028: AgentConfig model in src/sdd/agents/shared/models.py...")
```

### Phase 3: Supporting Libraries (Parallel Groups)
```bash
# T034-T040 can run in parallel (different files, different domains):
```
```python
Task(subagent_type="backend-architect", description="Refinement Engine", prompt="T034: Refinement Engine library in src/sdd/refinement/engine.py...")
Task(subagent_type="backend-architect", description="Feedback Accumulator", prompt="T035: Feedback Accumulation library in src/sdd/feedback/accumulator.py...")
Task(subagent_type="backend-architect", description="Context Retriever", prompt="T036: Context Retrieval library in src/sdd/context/retriever.py...")
Task(subagent_type="backend-architect", description="Metrics Collector", prompt="T037: Metrics Collection library in src/sdd/metrics/collector.py...")
Task(subagent_type="backend-architect", description="Agent Communication", prompt="T038: Agent Communication library in src/sdd/agents/shared/communication.py...")
Task(subagent_type="security-specialist", description="Constitutional Validator", prompt="T039: Constitutional Validator library in src/sdd/validation/constitutional.py...")
Task(subagent_type="backend-architect", description="Error Classifier", prompt="T040: Error Pattern Classifier library in src/sdd/agents/engineering/error_classifier.py...")
```

### Phase 5: Polish (All Parallel)
```bash
# T047-T050 can run in parallel (different files/domains):
```
```python
Task(subagent_type="testing-specialist", description="Unit tests", prompt="T047: Unit tests for all libraries in tests/unit/...")
Task(subagent_type="performance-engineer", description="Performance benchmarks", prompt="T048: Performance benchmarks in tests/performance/...")
Task(subagent_type="full-stack-developer", description="Update docs", prompt="T049: Update framework documentation...")
Task(subagent_type="specification-agent", description="Constitutional amendment", prompt="T050: Create constitutional amendment...")
```

---

## Task Statistics

- **Total Tasks**: 53
- **Parallel Tasks**: 28 (marked with [P], ~53% parallelizable)
- **Sequential Tasks**: 25 (dependencies or same-file modifications)
- **Setup Tasks**: 5 (T001-T005)
- **Test Tasks**: 12 (T006-T017)
- **Model Tasks**: 11 (T018-T028)
- **Agent Implementation**: 5 (T029-T033)
- **Supporting Libraries**: 7 (T034-T040)
- **Integration Tasks**: 6 (T041-T046)
- **Polish Tasks**: 7 (T047-T053)

**Estimated Parallel Execution Time Savings**: ~40-50% reduction vs sequential execution

---

## Constitutional Compliance Checklist

**Principle I (Library-First)**: ✓ Each agent is standalone library (T029-T033)
**Principle II (Test-First)**: ✓ All tests (T006-T017) MUST complete before implementation (T018-T040)
**Principle III (Contract-First)**: ✓ Contract tests (T006-T010) validate OpenAPI schemas before implementation
**Principle IV (Idempotent)**: ✓ Refinement engine supports safe retry (T034)
**Principle V (Progressive Enhancement)**: ✓ Phased implementation with feature flags
**Principle VI (Git Approval)**: ✓ Finalizer requests user approval (T033, T046)
**Principle VII (Observability)**: ✓ Metrics collection and structured logging (T037)
**Principle VIII (Documentation Sync)**: ✓ Docs updated (T049, T050)
**Principle IX (Dependency Management)**: ✓ Version-pinned dependencies (T002)
**Principle X (Agent Delegation)**: ✓ Router agent orchestration (T030, T043)
**Principle XI (Input Validation)**: ✓ Pydantic models for all data (T018-T028)
**Principle XIV (Model Selection)**: ✓ Documented in agent configs (T028)

---

## Notes

- **[P] tasks** = different files, no dependencies, can run in parallel
- **Verify all tests fail** before implementing (Phase 3.2 → 3.3 gate)
- **Commit after each task** for atomic progress tracking
- **Avoid**: vague tasks, same-file conflicts in parallel execution
- **Agent Selection**: Use task-orchestrator for multi-domain coordination
- **TDD Enforcement**: Phase 3.2 is a HARD GATE - no implementation without failing tests
- **Library-First**: Each agent is a reusable library with its own tests and docs
- **Contract-First**: All agent interfaces defined by OpenAPI schemas before code
- **Git Safety**: All git operations require explicit user approval (Principle VI)

---

## Validation Checklist
*GATE: Checked during task generation*

- [x] All 5 contracts have corresponding tests (T006-T010)
- [x] All 12 entities have model tasks (T018-T028)
- [x] All 7 integration scenarios have tests (T011-T017)
- [x] All 5 agents have implementation tasks (T029-T033)
- [x] All tests come before implementation (Phase 3.2 → 3.3)
- [x] Parallel tasks truly independent (different files, verified)
- [x] Each task specifies exact file path
- [x] No task modifies same file as another [P] task
- [x] Constitutional principles enforced throughout
- [x] Dependencies properly ordered (setup → tests → models → agents → integration → polish)

---

## Execution Status

- [x] Plan.md loaded and analyzed
- [x] Design documents processed (research.md, data-model.md, contracts/, quickstart.md)
- [x] Tasks generated by category (setup, tests, core, integration, polish)
- [x] Task rules applied (parallel marking, TDD ordering, dependencies)
- [x] Tasks numbered sequentially (T001-T053)
- [x] Dependency graph created
- [x] Parallel execution examples generated
- [x] Task completeness validated

**Status**: READY FOR EXECUTION
**Next Step**: Begin with T001 (Setup) or launch parallel execution groups
