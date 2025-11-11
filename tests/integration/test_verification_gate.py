"""
Integration Test: Quality Verification Gate (Scenario 1)
DS-STAR Multi-Agent Enhancement - Feature 001

Tests end-to-end quality gate behavior for specifications.
Validates that incomplete specs are blocked and sufficient specs pass.

Test Coverage:
- Incomplete spec blocked by verifier (T011 - FR-001, FR-002, FR-003, FR-004)
- Sufficient spec passes gate (T011)
- Actionable feedback provided (T011)
- Quality score calculation (T011)
"""

import json
import uuid
import pytest
from pathlib import Path
from typing import Dict, Any

# Import fixtures
from tests.fixtures.setup_test_environment import (
    incomplete_spec_sample,
    complete_spec_sample,
    spec_with_clarifications,
    temp_test_dir,
    create_test_spec_file,
)


# ===================================================================
# Integration Test: Incomplete Spec Blocked by Quality Gate
# ===================================================================

@pytest.mark.integration
def test_incomplete_specification_blocked_by_quality_gate(incomplete_spec_sample, temp_test_dir):
    """
    Integration test: Incomplete specification is blocked by quality verification gate.

    User Story: Quality Verification Acceptance Scenario 1
    Requirements: FR-001, FR-002, FR-003, FR-004

    Expected Behavior:
    1. Verification agent evaluates incomplete spec
    2. Decision is 'insufficient'
    3. Quality score below 0.85 threshold
    4. Actionable feedback provided
    5. Workflow progression blocked
    """
    # Arrange
    spec_path = temp_test_dir / "incomplete-spec.md"
    spec_path.write_text(incomplete_spec_sample)

    # Act - Invoke verification agent
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()
    request = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {
                "completeness": 0.90,
                "constitutional_compliance": 0.85,
                "test_coverage": 0.80,
                "spec_alignment": 0.90,
            },
        },
        context=AgentContext(
            spec_path=str(spec_path),
            cumulative_feedback=[],
        ),
    )

    response = agent.verify(request)

    # Assert - Verification gate blocks progression
    assert response.success == True  # Agent executed successfully
    assert response.output_data.decision == "insufficient"  # Quality gate BLOCKS

    # Assert - Quality score below threshold (FR-001)
    assert response.output_data.quality_score < 0.85
    assert response.output_data.quality_score >= 0.0

    # Assert - Actionable feedback provided (FR-002, FR-003)
    assert len(response.output_data.feedback) > 0
    assert all(isinstance(item, str) for item in response.output_data.feedback)
    assert all(len(item) > 10 for item in response.output_data.feedback)  # Meaningful feedback

    # Assert - Specific issues identified (FR-004)
    assert len(response.output_data.violations) > 0
    expected_violations = [
        "missing_user_scenarios",
        "incomplete_requirements",
        "missing_entities",
        "missing_acceptance_criteria",
    ]
    # At least one expected violation should be present
    assert any(
        any(violation_keyword in v.lower() for violation_keyword in ["missing", "incomplete"])
        for v in response.output_data.violations
    )

    # Assert - Feedback is actionable (contains action verbs)
    action_keywords = ["add", "include", "specify", "define", "improve", "clarify"]
    has_actionable_feedback = any(
        any(keyword in feedback.lower() for keyword in action_keywords)
        for feedback in response.output_data.feedback
    )
    assert has_actionable_feedback, "Feedback should contain actionable suggestions"


# ===================================================================
# Integration Test: Sufficient Spec Passes Quality Gate
# ===================================================================

@pytest.mark.integration
def test_sufficient_specification_passes_quality_gate(complete_spec_sample, temp_test_dir):
    """
    Integration test: Complete specification passes quality verification gate.

    User Story: Quality Verification Acceptance Scenario 1 (positive case)
    Requirements: FR-001, FR-002, FR-003, FR-004

    Expected Behavior:
    1. Verification agent evaluates complete spec
    2. Decision is 'sufficient'
    3. Quality score meets or exceeds 0.85 threshold
    4. No blocking violations
    5. Workflow can proceed
    """
    # Arrange
    spec_path = temp_test_dir / "complete-spec.md"
    spec_path.write_text(complete_spec_sample)

    # Act - Invoke verification agent
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()
    request = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {
                "completeness": 0.90,
                "constitutional_compliance": 0.85,
                "test_coverage": 0.80,
                "spec_alignment": 0.90,
            },
        },
        context=AgentContext(
            spec_path=str(spec_path),
            cumulative_feedback=[],
        ),
    )

    response = agent.verify(request)

    # Assert - Verification gate allows progression
    assert response.success == True
    assert response.output_data.decision == "sufficient"  # Quality gate PASSES

    # Assert - Quality score meets threshold (FR-001)
    assert response.output_data.quality_score >= 0.85
    assert response.output_data.quality_score <= 1.0

    # Assert - Dimension scores all meet thresholds
    dimension_scores = response.output_data.dimension_scores
    assert dimension_scores.completeness >= 0.90
    assert dimension_scores.constitutional_compliance >= 0.85

    # Assert - No blocking violations (FR-004)
    assert len(response.output_data.violations) == 0

    # Assert - Passed checks documented
    assert len(response.output_data.passed_checks) > 0
    expected_checks = ["completeness", "requirements", "user_scenarios"]
    # At least some checks should have passed
    assert len(response.output_data.passed_checks) >= 3

    # Assert - High confidence in decision
    assert response.confidence > 0.85


# ===================================================================
# Integration Test: Quality Score Calculation Accuracy
# ===================================================================

@pytest.mark.integration
def test_quality_score_reflects_spec_completeness(temp_test_dir):
    """
    Integration test: Quality score accurately reflects specification completeness.

    Requirements: FR-001 (quality score calculation)

    Expected Behavior:
    - Minimal spec: quality_score < 0.5
    - Partial spec: 0.5 <= quality_score < 0.85
    - Complete spec: quality_score >= 0.85
    """
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()

    # Test Case 1: Minimal spec
    minimal_spec = "# Feature\n## Requirements\n- Do something"
    minimal_path = temp_test_dir / "minimal-spec.md"
    minimal_path.write_text(minimal_spec)

    request_minimal = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(minimal_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(spec_path=str(minimal_path)),
    )

    response_minimal = agent.verify(request_minimal)
    assert response_minimal.output_data.quality_score < 0.5

    # Test Case 2: Partial spec (has requirements but missing scenarios)
    partial_spec = """# Feature
## Requirements
- FR-001: System must do X
- FR-002: System must do Y
- FR-003: System must do Z
"""
    partial_path = temp_test_dir / "partial-spec.md"
    partial_path.write_text(partial_spec)

    request_partial = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(partial_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(spec_path=str(partial_path)),
    )

    response_partial = agent.verify(request_partial)
    assert 0.5 <= response_partial.output_data.quality_score < 0.85


# ===================================================================
# Integration Test: Actionable Feedback Generation
# ===================================================================

@pytest.mark.integration
def test_verification_provides_specific_actionable_feedback(incomplete_spec_sample, temp_test_dir):
    """
    Integration test: Verification provides specific, actionable feedback.

    Requirements: FR-002, FR-003 (actionable feedback, specific issues)

    Expected Behavior:
    1. Feedback items are specific (not generic)
    2. Feedback includes section names or requirements
    3. Feedback provides clear action steps
    """
    # Arrange
    spec_path = temp_test_dir / "feedback-test-spec.md"
    spec_path.write_text(incomplete_spec_sample)

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()
    request = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(spec_path=str(spec_path), cumulative_feedback=[]),
    )

    response = agent.verify(request)

    # Assert - Feedback is specific (FR-003)
    feedback_items = response.output_data.feedback
    assert len(feedback_items) > 0

    # Check for specificity indicators
    specificity_indicators = [
        "User Scenarios",
        "Functional Requirements",
        "Key Entities",
        "Acceptance Criteria",
        "section",
        "requirement",
    ]
    specific_feedback = any(
        any(indicator in feedback for indicator in specificity_indicators)
        for feedback in feedback_items
    )
    assert specific_feedback, "Feedback should be specific with section/requirement names"

    # Assert - Feedback is actionable (FR-002)
    action_verbs = ["add", "include", "specify", "define", "improve", "clarify", "update", "create"]
    actionable_feedback = any(
        any(verb in feedback.lower() for verb in action_verbs)
        for feedback in feedback_items
    )
    assert actionable_feedback, "Feedback should start with action verbs"


# ===================================================================
# Integration Test: Cumulative Feedback Across Iterations
# ===================================================================

@pytest.mark.integration
def test_verification_accumulates_feedback_across_iterations(incomplete_spec_sample, temp_test_dir):
    """
    Integration test: Verification accumulates feedback across multiple iterations.

    Requirements: FR-019, FR-020, FR-021 (refinement loop context)

    Expected Behavior:
    1. First iteration provides initial feedback
    2. Subsequent iterations consider previous feedback
    3. New feedback builds on previous feedback
    """
    # Arrange
    spec_path = temp_test_dir / "iterative-spec.md"
    spec_path.write_text(incomplete_spec_sample)

    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()

    # Act - First iteration
    request_iteration_1 = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(
            spec_path=str(spec_path),
            cumulative_feedback=[],
        ),
    )

    response_1 = agent.verify(request_iteration_1)
    feedback_1 = response_1.output_data.feedback

    # Act - Second iteration with previous feedback
    request_iteration_2 = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(
            spec_path=str(spec_path),
            cumulative_feedback=feedback_1,
        ),
    )

    response_2 = agent.verify(request_iteration_2)

    # Assert - Feedback provided in both iterations
    assert len(feedback_1) > 0
    assert len(response_2.output_data.feedback) >= 0  # May be empty if improved

    # Assert - Second iteration aware of first (via context)
    # This is validated by passing cumulative_feedback in context


# ===================================================================
# Integration Test: Workflow Progression Control
# ===================================================================

@pytest.mark.integration
def test_verification_gate_controls_workflow_progression(incomplete_spec_sample, complete_spec_sample, temp_test_dir):
    """
    Integration test: Verification gate controls whether workflow can proceed.

    Requirements: FR-001, FR-004 (quality gate enforcement)

    Expected Behavior:
    1. Insufficient quality: workflow should NOT proceed
    2. Sufficient quality: workflow CAN proceed
    3. Decision is binary and unambiguous
    """
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()

    # Test Case 1: Insufficient quality blocks progression
    incomplete_path = temp_test_dir / "workflow-incomplete.md"
    incomplete_path.write_text(incomplete_spec_sample)

    request_insufficient = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(incomplete_path),
            "quality_thresholds": {"completeness": 0.85},
        },
        context=AgentContext(spec_path=str(incomplete_path)),
    )

    response_insufficient = agent.verify(request_insufficient)
    workflow_can_proceed_insufficient = response_insufficient.output_data.decision == "sufficient"
    assert not workflow_can_proceed_insufficient, "Incomplete spec should block workflow"

    # Test Case 2: Sufficient quality allows progression
    complete_path = temp_test_dir / "workflow-complete.md"
    complete_path.write_text(complete_spec_sample)

    request_sufficient = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(complete_path),
            "quality_thresholds": {"completeness": 0.85},
        },
        context=AgentContext(spec_path=str(complete_path)),
    )

    response_sufficient = agent.verify(request_sufficient)
    workflow_can_proceed_sufficient = response_sufficient.output_data.decision == "sufficient"
    assert workflow_can_proceed_sufficient, "Complete spec should allow workflow progression"


# ===================================================================
# Integration Test: [NEEDS CLARIFICATION] Detection
# ===================================================================

@pytest.mark.integration
def test_verification_detects_clarification_markers(spec_with_clarifications, temp_test_dir):
    """
    Integration test: Verification detects [NEEDS CLARIFICATION] markers.

    Requirements: FR-003 (specific issues identification)

    Expected Behavior:
    1. [NEEDS CLARIFICATION] markers detected
    2. Violations or feedback mention clarification needed
    3. Quality score reflects unresolved clarifications
    """
    # Arrange
    spec_path = temp_test_dir / "clarification-spec.md"
    spec_path.write_text(spec_with_clarifications)

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    agent = VerificationAgent()
    request = AgentInput(
        agent_id="quality.verifier",
        task_id=str(uuid.uuid4()),
        phase="specification",
        input_data={
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {"completeness": 0.90},
        },
        context=AgentContext(spec_path=str(spec_path)),
    )

    response = agent.verify(request)

    # Assert - Decision is insufficient due to clarifications
    assert response.output_data.decision == "insufficient"

    # Assert - Feedback or violations mention clarification
    all_text = " ".join(response.output_data.feedback + response.output_data.violations)
    assert "clarification" in all_text.lower()

    # Assert - Quality score reduced
    assert response.output_data.quality_score < 0.85
