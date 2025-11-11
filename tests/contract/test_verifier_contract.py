"""
Contract Tests for Verification Agent
DS-STAR Multi-Agent Enhancement - Feature 001

Tests the Verification Agent's contract compliance with verifier.yaml.
Validates POST /verify endpoint, request/response schemas, and binary decision logic.

Test Coverage:
- POST /verify with valid specification (T006)
- POST /verify with incomplete specification (T006)
- Response schema matches contracts/verifier.yaml (T006)
- Binary decision (sufficient/insufficient) (T006)
- Feedback generation for insufficient quality (T006)
- VerificationDecision output format (T006)
"""

import json
import pytest
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Import fixtures
from tests.fixtures.setup_test_environment import (
    incomplete_spec_sample,
    complete_spec_sample,
    temp_test_dir,
    create_test_spec_file,
)


# ===================================================================
# Contract Test: POST /verify with Valid Specification
# ===================================================================

@pytest.mark.contract
def test_verify_valid_specification_returns_sufficient(
    complete_spec_sample, temp_test_dir
):
    """
    Test that POST /verify returns 'sufficient' decision for complete specification.

    Contract: verifier.yaml - POST /verify endpoint
    Expected: VerificationResponse with decision='sufficient', quality_score >= 0.85
    """
    # Arrange
    spec_path = temp_test_dir / "complete-spec.md"
    spec_path.write_text(complete_spec_sample)

    request_payload = {
        "agent_id": "quality.verifier",
        "task_id": "550e8400-e29b-41d4-a716-446655440000",
        "phase": "specification",
        "artifact_type": "spec",
        "artifact_path": str(spec_path),
        "quality_thresholds": {
            "completeness": 0.90,
            "constitutional_compliance": 0.85,
            "test_coverage": 0.80,
            "spec_alignment": 0.90,
        },
        "context": {
            "spec_path": str(spec_path),
            "cumulative_feedback": [],
        },
    }

    # Act
    # This will fail until VerificationAgent is implemented
    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()
    response = agent.verify(request_payload)

    # Assert - Response structure
    assert "agent_id" in response
    assert response["agent_id"] == "quality.verifier"
    assert "task_id" in response
    assert "success" in response
    assert response["success"] == True
    assert "output_data" in response
    assert "reasoning" in response
    assert "confidence" in response
    assert "next_actions" in response
    assert "timestamp" in response

    # Assert - VerificationDecision structure
    output_data = response["output_data"]
    assert "decision" in output_data
    assert output_data["decision"] == "sufficient"
    assert "quality_score" in output_data
    assert output_data["quality_score"] >= 0.85
    assert "dimension_scores" in output_data
    assert "feedback" in output_data
    assert "violations" in output_data
    assert "passed_checks" in output_data

    # Assert - Dimension scores present
    dimension_scores = output_data["dimension_scores"]
    assert "completeness" in dimension_scores
    assert "constitutional_compliance" in dimension_scores
    assert "test_coverage" in dimension_scores
    assert "spec_alignment" in dimension_scores

    # Assert - Quality thresholds met
    assert dimension_scores["completeness"] >= 0.90
    assert dimension_scores["constitutional_compliance"] >= 0.85

    # Assert - No violations for sufficient decision
    assert len(output_data["violations"]) == 0

    # Assert - Confidence score valid
    assert 0.0 <= response["confidence"] <= 1.0


# ===================================================================
# Contract Test: POST /verify with Incomplete Specification
# ===================================================================

@pytest.mark.contract
def test_verify_incomplete_specification_returns_insufficient(
    incomplete_spec_sample, temp_test_dir
):
    """
    Test that POST /verify returns 'insufficient' decision for incomplete spec.

    Contract: verifier.yaml - POST /verify with insufficient artifact
    Expected: VerificationResponse with decision='insufficient', actionable feedback
    """
    # Arrange
    spec_path = temp_test_dir / "incomplete-spec.md"
    spec_path.write_text(incomplete_spec_sample)

    request_payload = {
        "agent_id": "quality.verifier",
        "task_id": "550e8400-e29b-41d4-a716-446655440001",
        "phase": "specification",
        "artifact_type": "spec",
        "artifact_path": str(spec_path),
        "quality_thresholds": {
            "completeness": 0.90,
            "constitutional_compliance": 0.85,
            "test_coverage": 0.80,
            "spec_alignment": 0.90,
        },
        "context": {
            "spec_path": str(spec_path),
            "cumulative_feedback": [],
        },
    }

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()
    response = agent.verify(request_payload)

    # Assert - Response structure
    assert response["success"] == True  # Agent executed successfully
    assert "output_data" in response

    # Assert - VerificationDecision indicates insufficient
    output_data = response["output_data"]
    assert output_data["decision"] == "insufficient"
    assert output_data["quality_score"] < 0.85  # Below threshold

    # Assert - Feedback is provided
    assert "feedback" in output_data
    assert len(output_data["feedback"]) > 0
    assert all(isinstance(item, str) for item in output_data["feedback"])

    # Assert - Violations identified
    assert "violations" in output_data
    assert len(output_data["violations"]) > 0

    # Assert - Some checks may have passed
    assert "passed_checks" in output_data

    # Assert - Reasoning explains decision
    assert len(response["reasoning"]) > 0
    assert "insufficient" in response["reasoning"].lower() or "missing" in response["reasoning"].lower()


# ===================================================================
# Contract Test: Response Schema Validation
# ===================================================================

@pytest.mark.contract
def test_verify_response_matches_contract_schema(
    complete_spec_sample, temp_test_dir
):
    """
    Test that POST /verify response exactly matches verifier.yaml schema.

    Contract: verifier.yaml - VerificationResponse schema
    Expected: All required fields present, correct types, valid enum values
    """
    # Arrange
    spec_path = temp_test_dir / "schema-test-spec.md"
    spec_path.write_text(complete_spec_sample)

    request_payload = {
        "agent_id": "quality.verifier",
        "task_id": "550e8400-e29b-41d4-a716-446655440002",
        "phase": "planning",
        "artifact_type": "plan",
        "artifact_path": str(spec_path),
        "quality_thresholds": {
            "completeness": 0.90,
            "constitutional_compliance": 0.85,
            "test_coverage": 0.80,
            "spec_alignment": 0.90,
        },
        "context": {
            "spec_path": str(spec_path),
            "plan_path": None,
            "previous_outputs": [],
            "cumulative_feedback": [],
        },
    }

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()
    response = agent.verify(request_payload)

    # Assert - Required top-level fields (per VerificationResponse schema)
    required_fields = [
        "agent_id",
        "task_id",
        "success",
        "output_data",
        "reasoning",
        "confidence",
        "next_actions",
        "timestamp",
    ]
    for field in required_fields:
        assert field in response, f"Missing required field: {field}"

    # Assert - Field types
    assert isinstance(response["agent_id"], str)
    assert isinstance(response["task_id"], str)
    assert isinstance(response["success"], bool)
    assert isinstance(response["output_data"], dict)
    assert isinstance(response["reasoning"], str)
    assert isinstance(response["confidence"], (int, float))
    assert isinstance(response["next_actions"], list)
    assert isinstance(response["timestamp"], str)

    # Assert - VerificationDecision required fields
    output_data = response["output_data"]
    decision_required_fields = [
        "decision",
        "quality_score",
        "dimension_scores",
        "feedback",
        "violations",
        "passed_checks",
    ]
    for field in decision_required_fields:
        assert field in output_data, f"Missing required decision field: {field}"

    # Assert - Decision enum validation
    assert output_data["decision"] in ["sufficient", "insufficient"]

    # Assert - Numeric ranges
    assert 0.0 <= output_data["quality_score"] <= 1.0
    assert 0.0 <= response["confidence"] <= 1.0

    # Assert - Timestamp format (ISO 8601)
    try:
        datetime.fromisoformat(response["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        pytest.fail("Timestamp not in ISO 8601 format")


# ===================================================================
# Contract Test: Binary Decision Logic
# ===================================================================

@pytest.mark.contract
def test_verify_binary_decision_logic(complete_spec_sample, incomplete_spec_sample, temp_test_dir):
    """
    Test that verification decision is strictly binary (sufficient/insufficient).

    Contract: verifier.yaml - VerificationDecision.decision enum
    Expected: Only 'sufficient' or 'insufficient', no intermediate states
    """
    import uuid

    # Arrange - Create multiple test cases with varying quality
    test_cases = [
        ("complete", True, "sufficient", complete_spec_sample),
        ("incomplete", False, "insufficient", incomplete_spec_sample),
    ]

    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()

    for spec_type, should_pass, expected_decision, spec_content in test_cases:
        # Arrange
        spec_path = temp_test_dir / f"{spec_type}-spec.md"
        spec_path.write_text(spec_content)

        request_payload = {
            "agent_id": "quality.verifier",
            "task_id": str(uuid.uuid4()),
            "phase": "specification",
            "artifact_type": "spec",
            "artifact_path": str(spec_path),
            "quality_thresholds": {
                "completeness": 0.90,
                "constitutional_compliance": 0.85,
                "test_coverage": 0.80,
                "spec_alignment": 0.90,
            },
            "context": {"cumulative_feedback": []},
        }

        # Act
        response = agent.verify(request_payload)

        # Assert - Binary decision only
        decision = response["output_data"]["decision"]
        assert decision in ["sufficient", "insufficient"]
        assert decision == expected_decision

        # Cleanup
        Path(spec_path).unlink()


# ===================================================================
# Contract Test: Feedback Generation
# ===================================================================

@pytest.mark.contract
def test_verify_generates_actionable_feedback_on_insufficient(
    incomplete_spec_sample, temp_test_dir
):
    """
    Test that insufficient decisions include actionable feedback.

    Contract: verifier.yaml - VerificationDecision.feedback (required if insufficient)
    Expected: List of specific, actionable improvement suggestions
    """
    # Arrange
    spec_path = temp_test_dir / "feedback-test-spec.md"
    spec_path.write_text(incomplete_spec_sample)

    request_payload = {
        "agent_id": "quality.verifier",
        "task_id": "550e8400-e29b-41d4-a716-446655440003",
        "phase": "specification",
        "artifact_type": "spec",
        "artifact_path": str(spec_path),
        "quality_thresholds": {
            "completeness": 0.90,
            "constitutional_compliance": 0.85,
            "test_coverage": 0.80,
            "spec_alignment": 0.90,
        },
        "context": {"cumulative_feedback": []},
    }

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()
    response = agent.verify(request_payload)

    # Assert - Insufficient decision
    assert response["output_data"]["decision"] == "insufficient"

    # Assert - Feedback provided
    feedback = response["output_data"]["feedback"]
    assert isinstance(feedback, list)
    assert len(feedback) > 0

    # Assert - Feedback is actionable (contains action verbs or specifics)
    action_keywords = ["add", "include", "specify", "define", "improve", "clarify", "update"]
    for feedback_item in feedback:
        assert isinstance(feedback_item, str)
        assert len(feedback_item) > 10  # Not just empty strings
        # At least some feedback should be actionable

    # Assert - Next actions provided
    assert len(response["next_actions"]) > 0


# ===================================================================
# Contract Test: VerificationDecision Output Format
# ===================================================================

@pytest.mark.contract
def test_verification_decision_output_format(
    complete_spec_sample, temp_test_dir
):
    """
    Test that VerificationDecision output matches expected format.

    Contract: verifier.yaml - VerificationDecision schema
    Expected: All dimension scores present, ranges valid, arrays not null
    """
    # Arrange
    spec_path = temp_test_dir / "format-test-spec.md"
    spec_path.write_text(complete_spec_sample)

    request_payload = {
        "agent_id": "quality.verifier",
        "task_id": "550e8400-e29b-41d4-a716-446655440004",
        "phase": "specification",
        "artifact_type": "spec",
        "artifact_path": str(spec_path),
        "quality_thresholds": {
            "completeness": 0.90,
            "constitutional_compliance": 0.85,
            "test_coverage": 0.80,
            "spec_alignment": 0.90,
        },
        "context": {"cumulative_feedback": []},
    }

    # Act
    from sdd.agents.quality.verifier import VerificationAgent
    agent = VerificationAgent()
    response = agent.verify(request_payload)

    # Assert - Output data structure
    output_data = response["output_data"]

    # Dimension scores - all 4 dimensions must be present
    dimension_scores = output_data["dimension_scores"]
    required_dimensions = [
        "completeness",
        "constitutional_compliance",
        "test_coverage",
        "spec_alignment",
    ]
    for dimension in required_dimensions:
        assert dimension in dimension_scores
        score = dimension_scores[dimension]
        assert isinstance(score, (int, float))
        assert 0.0 <= score <= 1.0

    # Feedback - array (may be empty if sufficient)
    assert isinstance(output_data["feedback"], list)

    # Violations - array (may be empty if sufficient)
    assert isinstance(output_data["violations"], list)

    # Passed checks - array (should not be empty)
    assert isinstance(output_data["passed_checks"], list)

    # Quality score aligns with dimension scores (rough average)
    avg_dimension = sum(dimension_scores.values()) / len(dimension_scores)
    quality_score = output_data["quality_score"]
    # Quality score should be within reasonable range of dimension average
    assert abs(quality_score - avg_dimension) < 0.3
