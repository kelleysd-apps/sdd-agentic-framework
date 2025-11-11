# DS-STAR Supporting Libraries - Quick Reference

**Feature**: 001-ds-star-multi
**Phase**: 3.3 - Supporting Libraries
**Status**: Complete ✅

---

## Overview

7 supporting libraries provide infrastructure for DS-STAR Multi-Agent Enhancement:

| Library | Purpose | File | Key Function |
|---------|---------|------|--------------|
| **RefinementEngine** | Iterative refinement loops | `sdd/refinement/engine.py` | `refine_until_sufficient()` |
| **FeedbackAccumulator** | Feedback storage & retrieval | `sdd/feedback/accumulator.py` | `add()`, `get_cumulative()` |
| **ContextRetriever** | Semantic codebase search | `sdd/context/retriever.py` | `retrieve_relevant_specs()` |
| **MetricsCollector** | Performance tracking | `sdd/metrics/collector.py` | `record_task()`, `calculate_improvement()` |
| **AgentChannel** | Agent communication | `sdd/agents/shared/communication.py` | `send()`, `handoff()` |
| **ConstitutionalValidator** | 14-principle compliance | `sdd/validation/constitutional.py` | `validate_all_principles()` |
| **ErrorClassifier** | Error pattern detection | `sdd/agents/engineering/error_classifier.py` | `classify()` |

---

## Quick Start Examples

### 1. Refinement Engine

**Purpose**: Orchestrate iterative refinement with quality gates.

```python
from sdd.refinement.engine import RefinementEngine
from sdd.agents.quality.verifier import VerificationAgent

# Initialize
engine = RefinementEngine()
verifier = VerificationAgent()

# Define refinement function
def refine_plan(state):
    """Apply accumulated feedback to plan."""
    feedback = state.cumulative_feedback
    # ... apply feedback to artifact ...

# Run refinement loop
final_state = engine.refine_until_sufficient(
    task_id="550e8400-e29b-41d4-a716-446655440000",
    phase="planning",
    artifact_path="/workspaces/sdd-agentic-framework/specs/001-ds-star-multi/plan.md",
    verifier=verifier,
    refinement_fn=refine_plan
)

# Check result
if final_state.ema_quality >= final_state.quality_threshold:
    print(f"✓ Quality achieved in {final_state.current_round} rounds")
else:
    print(f"✗ Max rounds reached - escalate to human")
```

**Configuration** (`.specify/config/refinement.conf`):
- `MAX_REFINEMENT_ROUNDS=20`
- `EARLY_STOP_THRESHOLD=0.95`
- `PLAN_QUALITY_THRESHOLD=0.85`

---

### 2. Feedback Accumulator

**Purpose**: Store and retrieve feedback for progressive learning.

```python
from sdd.feedback.accumulator import FeedbackAccumulator

# Initialize
accumulator = FeedbackAccumulator()

# Add feedback
accumulator.add(
    task_id="550e8400-e29b-41d4-a716-446655440000",
    feedback="Add contract for POST /api/users endpoint",
    iteration=1,
    quality_score=0.72,
    agent_id="quality.verifier",
    metadata={"dimension": "completeness"}
)

# Retrieve cumulative learnings
learnings = accumulator.get_cumulative(
    task_id="550e8400-e29b-41d4-a716-446655440000"
)

for feedback in learnings:
    print(f"- {feedback}")

# Get quality progression
scores = accumulator.get_quality_progression(task_id)
print(f"Quality trend: {scores}")

# Archive old feedback (>1000 iterations)
accumulator.archive(task_id)
```

**Storage**: `.docs/agents/shared/feedback/{task_id}.json`

---

### 3. Context Retriever

**Purpose**: Semantic search over specs, plans, and decisions.

```python
from sdd.context.retriever import ContextRetriever

# Initialize
retriever = ContextRetriever()

# Build index (first time or after new specs added)
retriever.build_index(
    specs_dir="/workspaces/sdd-agentic-framework/specs",
    docs_dir="/workspaces/sdd-agentic-framework/.docs"
)

# Retrieve relevant specs
results = retriever.retrieve_relevant_specs(
    query="user authentication with JWT tokens",
    top_k=5
)

for result in results:
    print(f"{result['path']}: {result['similarity']:.3f}")
    print(f"  {result['content'][:100]}...")

# Retrieve similar tasks
tasks = retriever.retrieve_similar_tasks(
    query="implement REST API endpoints"
)

# Retrieve architecture decisions
decisions = retriever.retrieve_decisions(
    query="database schema design patterns"
)
```

**Configuration**:
- `EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
- `TOP_K_RESULTS=5`
- `CONTEXT_RETRIEVAL_TIMEOUT=2000` (ms)
- `ENABLE_GRACEFUL_DEGRADATION=true`

**Performance**: <2 seconds (FR-031)
**Fallback**: TF-IDF keyword search if embeddings slow

---

### 4. Metrics Collector

**Purpose**: Track performance and validate 3.5x improvement.

```python
from sdd.metrics.collector import MetricsCollector
from sdd.metrics.models import TaskMetrics
from datetime import datetime

# Initialize
collector = MetricsCollector()

# Set baseline (pre-enhancement)
collector.set_baseline(
    task_completion_accuracy=20.0,  # 20% baseline
    avg_refinement_rounds=5.0,
    debug_success_rate=30.0,        # 30% auto-resolved
    constitutional_compliance_rate=60.0,  # 60% pass first time
    task_count=50
)

# Record task metrics
metrics = TaskMetrics(
    task_id="550e8400-e29b-41d4-a716-446655440000",
    phase="planning",
    started_at=datetime.now(),
    completed_at=datetime.now(),
    duration_seconds=120.5,
    refinement_rounds=3,
    refinement_quality_scores=[0.72, 0.78, 0.88],
    early_stopped=False,
    errors_encountered=2,
    errors_auto_resolved=2,
    completed_without_intervention=True,
    escalated_to_human=False
)
collector.record_task(metrics)

# Calculate improvement
improvement = collector.calculate_improvement()
print(f"Improvement: {improvement:.2f}x (target: 3.5x)")

# Get aggregate metrics
agg = collector.get_aggregate_metrics(phase="planning")
print(f"Task completion accuracy: {agg['task_completion_accuracy']:.1f}%")
print(f"Avg refinement rounds: {agg['avg_refinement_rounds']:.1f}")

# Export report
report_path = collector.export_metrics_report()
print(f"Report saved: {report_path}")
```

**Storage**: `.docs/agents/shared/metrics/{phase}/{task_id}.json`
**Target**: 3.5x improvement (FR-047)

---

### 5. Agent Channel

**Purpose**: Structured agent-to-agent communication.

```python
from sdd.agents.shared.communication import AgentChannel
from sdd.agents.shared.models import AgentInput, AgentContext, AgentOutput

# Initialize
channel = AgentChannel()

# Send message to agent
agent_input = AgentInput(
    agent_id="quality.verifier",
    task_id="550e8400-e29b-41d4-a716-446655440000",
    phase="planning",
    input_data={"artifact_path": "/path/to/plan.md"},
    context=AgentContext(spec_path="/path/to/spec.md")
)
message_id = channel.send(agent_input, sender="orchestrator")

# Receive message
received = channel.receive(agent_id="quality.verifier")

# Respond from agent
agent_output = AgentOutput(
    agent_id="quality.verifier",
    task_id="550e8400-e29b-41d4-a716-446655440000",
    success=False,
    output_data={"decision": "insufficient", "quality_score": 0.72},
    reasoning="Plan lacks contract definitions",
    confidence=0.91,
    next_actions=["Generate OpenAPI schemas"]
)
channel.respond(agent_output)

# Hand off context to next agent
updated_context = context.add_output(agent_output)
handoff_id = channel.handoff(
    from_agent="quality.verifier",
    to_agent="architecture.router",
    context=updated_context,
    reason="Quality insufficient, need routing decision"
)

# Export audit trail
audit_path = channel.export_audit_trail(task_id)
print(f"Audit saved: {audit_path}")
```

**Audit Trail**:
- Messages: `.docs/agents/shared/communication/messages.jsonl`
- Handoffs: `.docs/agents/shared/communication/handoffs.jsonl`

---

### 6. Constitutional Validator

**Purpose**: Validate artifacts against all 14 principles.

```python
from sdd.validation.constitutional import ConstitutionalValidator

# Initialize
validator = ConstitutionalValidator()

# Validate artifact
report = validator.validate_all_principles(
    artifact_path="/workspaces/sdd-agentic-framework/specs/001-ds-star-multi/plan.md",
    artifact_type="plan"
)

if report['compliant']:
    print("✓ All principles satisfied!")
    print(f"Passed checks: {len(report['passed_checks'])}")
else:
    print(f"✗ Violations found: {len(report['violations'])}")

    for violation in report['violations']:
        print(f"\n{violation['principle']} [{violation['severity']}]")
        print(f"  Issue: {violation['description']}")
        print(f"  Fix: {violation['remediation']}")
        if violation['location']:
            print(f"  Location: {violation['location']}")

# Save report
report_path = validator.save_report(report)
print(f"Report saved: {report_path}")
```

**Principles Validated**: All 14 (I-XIV)
**Storage**: `.docs/agents/shared/compliance-reports/`

---

### 7. Error Classifier

**Purpose**: Classify errors and provide fix templates.

```python
from sdd.agents.engineering.error_classifier import ErrorClassifier

# Initialize
classifier = ErrorClassifier()

# Classify error
pattern = classifier.classify(
    error_message="NameError: name 'foo' is not defined",
    stack_trace="Traceback (most recent call last):\n  File test.py, line 10, in bar\n    return foo + 1",
    code_context="def bar():\n    return foo + 1"
)

print(f"Error type: {pattern.error_type}")
print(f"Error class: {pattern.error_class}")
print(f"Confidence: {pattern.confidence:.2f}")
print(f"Line: {pattern.line_number}")
print(f"\nExplanation:\n{pattern.explanation}")
print(f"\nFix template:\n{pattern.fix_template}")

# Get fix template for specific error type
template = classifier.get_pattern('name')

# Analyze error trends
trends = classifier.analyze_error_trend(error_history)
print(f"Most common error: {trends['most_common_type']}")

# Get preventive measures
measures = classifier.suggest_preventive_measures('name')
for measure in measures:
    print(f"- {measure}")
```

**Error Types**: syntax, type, name, attribute, import, value, assertion, logic

---

## Configuration

### Global Config File
**Location**: `.specify/config/refinement.conf`

**Key Settings**:
```bash
# Refinement
MAX_REFINEMENT_ROUNDS=20
EARLY_STOP_THRESHOLD=0.95

# Quality Thresholds
SPEC_COMPLETENESS_THRESHOLD=0.90
PLAN_QUALITY_THRESHOLD=0.85
CODE_QUALITY_THRESHOLD=0.80
TEST_COVERAGE_THRESHOLD=0.80

# Context Retrieval
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
TOP_K_RESULTS=5
CONTEXT_RETRIEVAL_TIMEOUT=2000
ENABLE_GRACEFUL_DEGRADATION=true

# Auto-Debug
MAX_DEBUG_ITERATIONS=5
AUTO_DEBUG_ENABLED=true
AUTO_FIX_TARGET_RATE=0.70

# Metrics
TASK_COMPLETION_IMPROVEMENT_TARGET=3.5
```

---

## Storage Locations

```
.docs/agents/shared/
├── refinement-state/          # RefinementEngine state
│   └── {task_id}.json
├── feedback/                  # FeedbackAccumulator records
│   ├── {task_id}.json
│   └── archive/
├── embeddings/                # ContextRetriever index
│   ├── index.pkl
│   └── cache/
├── metrics/                   # MetricsCollector data
│   ├── baseline.json
│   ├── planning/{task_id}.json
│   ├── implementation/{task_id}.json
│   └── report_{timestamp}.json
├── communication/             # AgentChannel audit
│   ├── messages.jsonl
│   ├── handoffs.jsonl
│   └── {task_id}_audit.json
└── compliance-reports/        # ConstitutionalValidator reports
    └── {artifact}_{timestamp}_report.json
```

---

## Import Statements

```python
# Refinement
from sdd.refinement.engine import RefinementEngine
from sdd.refinement.models import RefinementState, IterationRecord

# Feedback
from sdd.feedback.accumulator import FeedbackAccumulator

# Context
from sdd.context.retriever import ContextRetriever

# Metrics
from sdd.metrics.collector import MetricsCollector
from sdd.metrics.models import TaskMetrics

# Communication
from sdd.agents.shared.communication import AgentChannel
from sdd.agents.shared.models import AgentInput, AgentOutput, AgentContext

# Validation
from sdd.validation.constitutional import ConstitutionalValidator

# Error Classification
from sdd.agents.engineering.error_classifier import ErrorClassifier
```

---

## Integration Examples

### Refinement Loop with All Libraries

```python
from sdd.refinement.engine import RefinementEngine
from sdd.feedback.accumulator import FeedbackAccumulator
from sdd.context.retriever import ContextRetriever
from sdd.metrics.collector import MetricsCollector
from sdd.agents.quality.verifier import VerificationAgent
from datetime import datetime

# Initialize all components
engine = RefinementEngine()
accumulator = FeedbackAccumulator()
retriever = ContextRetriever()
collector = MetricsCollector()
verifier = VerificationAgent()

# Build context index
retriever.build_index()

# Retrieve relevant context
context_results = retriever.retrieve_relevant_specs(
    query="similar to current task"
)

# Start metrics tracking
task_id = "550e8400-e29b-41d4-a716-446655440000"
start_time = datetime.now()

# Run refinement
def refine_with_feedback(state):
    """Apply feedback using accumulator."""
    learnings = accumulator.get_cumulative(task_id)
    # Apply learnings to artifact

final_state = engine.refine_until_sufficient(
    task_id=task_id,
    phase="planning",
    artifact_path="/path/to/plan.md",
    verifier=verifier,
    refinement_fn=refine_with_feedback
)

# Record metrics
metrics = TaskMetrics(
    task_id=task_id,
    phase="planning",
    started_at=start_time,
    completed_at=datetime.now(),
    duration_seconds=(datetime.now() - start_time).total_seconds(),
    refinement_rounds=final_state.current_round,
    refinement_quality_scores=[i.quality_score for i in final_state.iterations],
    completed_without_intervention=final_state.ema_quality >= final_state.quality_threshold
)
collector.record_task(metrics)

# Check improvement
improvement = collector.calculate_improvement()
print(f"Improvement: {improvement:.2f}x / 3.5x target")
```

---

## Testing

**Test Files** (Next Phase: T041-T046):
- `tests/test_refinement_engine.py`
- `tests/test_feedback_accumulator.py`
- `tests/test_context_retriever.py`
- `tests/test_metrics_collector.py`
- `tests/test_agent_channel.py`
- `tests/test_constitutional_validator.py`
- `tests/test_error_classifier.py`

**Run Tests**:
```bash
pytest tests/ -v --cov=src/sdd --cov-report=term-missing
```

---

## Troubleshooting

### Context Retrieval Slow
**Issue**: Retrieval takes >2 seconds
**Solution**:
1. Check if sentence-transformers installed
2. Enable graceful degradation (uses TF-IDF fallback)
3. Clear embedding cache: `rm -rf .docs/agents/shared/embeddings/cache/*`

### Refinement Not Converging
**Issue**: Max rounds reached without quality threshold
**Solution**:
1. Check quality threshold in refinement.conf
2. Review feedback in `.docs/agents/shared/feedback/{task_id}.json`
3. Manually review artifact and apply accumulated learnings

### Metrics Show No Improvement
**Issue**: Improvement ratio < 3.5x
**Solution**:
1. Check baseline is set correctly
2. Ensure all agents wired properly
3. Review escalation reports for patterns
4. Consider adjusting quality thresholds

---

## Performance Targets

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Context retrieval | <2s | TBD | ⏳ |
| Refinement convergence | <10 rounds | TBD | ⏳ |
| Task completion accuracy | 3.5x baseline | TBD | ⏳ |
| Debug success rate | >70% | TBD | ⏳ |
| Constitutional compliance | >95% first-time | TBD | ⏳ |

---

## Next Steps

1. **Write Tests** (T041-T046): Unit and integration tests
2. **Measure Baseline** (T047): Pre-enhancement metrics
3. **Wire Agents** (T048): Connect libraries to agents
4. **Validate Performance** (T049): Meet FR targets
5. **Deploy** (T050): Production rollout

---

**Reference Version**: 1.0
**Last Updated**: 2025-11-10
**Feature**: 001-ds-star-multi
**Constitution**: v1.5.0 (14 Principles)
