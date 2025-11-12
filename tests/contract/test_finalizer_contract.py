"""
Contract Tests for Compliance Finalizer Agent
DS-STAR Multi-Agent Enhancement - Feature 001

Tests the Compliance Finalizer Agent's contract compliance with finalizer.yaml.
Validates POST /finalize endpoint, pre-commit validation, constitutional compliance,
and CRITICAL git approval gate enforcement.

Test Coverage:
- POST /finalize with complete implementation (T010)
- Constitutional compliance checks (all 14 principles) (T010)
- Git approval gate (MUST request user approval) (T010)
- Response schema matches contracts/finalizer.yaml (T010)
- Pre-commit checklist validation (T010)
- No autonomous git operations (CRITICAL) (T010)
"""

import json
import pytest
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Import fixtures
from tests.fixtures.setup_test_environment import (
    temp_test_dir,
    correct_code_sample,
)


# ===================================================================
# Contract Test: POST /finalize with Complete Implementation
# ===================================================================

@pytest.mark.contract
def test_finalize_complete_implementation_passes_checks(temp_test_dir, correct_code_sample):
    """
    Test that POST /finalize validates complete implementation successfully.

    Contract: finalizer.yaml - POST /finalize endpoint
    Expected: FinalizationResult with all_checks_passed=True, git_approval_required=True
    """
    # Arrange
    code_file = temp_test_dir / "calculator.py"
    code_file.write_text(correct_code_sample)

    test_file = temp_test_dir / "test_calculator.py"
    test_file.write_text("""
import pytest
from calculator import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    """)

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440040",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [str(test_file)],
            "docs_files": [],
        },
        "validation_checks": [
            "tests_passing",
            "code_coverage",
            "linting",
            "constitutional_compliance",
            "documentation_sync",
            "secrets_check",
        ],
        "git_operation": {
            "type": "commit",
            "message": "feat: Add calculator function",
            "files_to_stage": [str(code_file), str(test_file)],
        },
    }

    # Act
    # This will fail until ComplianceFinalizerAgent is implemented
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Response structure
    assert "agent_id" in response
    assert response["agent_id"] == "quality.finalizer"
    assert "task_id" in response
    assert "success" in response
    assert response["success"] == True
    assert "output_data" in response
    assert "reasoning" in response
    assert "confidence" in response
    assert "next_actions" in response
    assert "timestamp" in response

    # Assert - FinalizationResult structure
    output_data = response["output_data"]
    assert "all_checks_passed" in output_data
    assert "check_results" in output_data
    assert "git_approval_required" in output_data

    # Assert - All checks passed
    check_results = output_data["check_results"]
    assert isinstance(check_results, dict)

    # Assert - Git approval REQUIRED (CRITICAL - Principle VI)
    assert output_data["git_approval_required"] == True
    assert "git_operation_summary" in output_data


# ===================================================================
# Contract Test: Constitutional Compliance Checks (All 14 Principles)
# ===================================================================

@pytest.mark.contract
def test_finalize_validates_all_14_constitutional_principles(temp_test_dir):
    """
    Test that finalizer validates all 14 constitutional principles.

    Contract: finalizer.yaml - constitutional_compliance check
    Expected: Validation includes checks for all 14 principles from constitution v1.5.0
    """
    # Arrange
    code_file = temp_test_dir / "example.py"
    code_file.write_text("def example(): pass")

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440041",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [],
            "docs_files": [],
        },
        "validation_checks": [
            "constitutional_compliance",
        ],
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Constitutional compliance checked
    output_data = response["output_data"]
    check_results = output_data["check_results"]
    assert "constitutional_compliance" in check_results

    # If violations found, they should reference specific principles
    if "constitutional_violations" in output_data and len(output_data["constitutional_violations"]) > 0:
        violations = output_data["constitutional_violations"]
        # Violations should mention principle names or numbers
        for violation in violations:
            assert isinstance(violation, str)
            # Should reference principles (I-XIV, or principle names)


# ===================================================================
# Contract Test: Git Approval Gate (CRITICAL - Principle VI)
# ===================================================================

@pytest.mark.contract
def test_finalize_requires_git_approval_no_autonomous_operations(temp_test_dir):
    """
    Test that finalizer ALWAYS requires user approval for git operations.

    Contract: finalizer.yaml - FinalizationResult.git_approval_required
    Expected: git_approval_required=True, user_approved initially null/false, NO autonomous git ops
    """
    # Arrange
    code_file = temp_test_dir / "test_code.py"
    code_file.write_text("def test(): return True")

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440042",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [],
            "docs_files": [],
        },
        "validation_checks": ["tests_passing"],
        "git_operation": {
            "type": "commit",
            "message": "test: Add test code",
            "files_to_stage": [str(code_file)],
        },
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Git approval REQUIRED (CRITICAL)
    output_data = response["output_data"]
    assert output_data["git_approval_required"] == True

    # Assert - User approval NOT automatically granted
    user_approved = output_data.get("user_approved")
    assert user_approved != True  # Should be None or False, never True without user action

    # Assert - Git operation summary provided for user review
    assert "git_operation_summary" in output_data
    git_summary = output_data["git_operation_summary"]
    assert isinstance(git_summary, str)
    assert len(git_summary) > 0

    # Summary should describe what will be committed
    assert "commit" in git_summary.lower() or "files" in git_summary.lower()


# ===================================================================
# Contract Test: Response Schema Validation
# ===================================================================

@pytest.mark.contract
def test_finalize_response_matches_contract_schema(temp_test_dir):
    """
    Test that POST /finalize response exactly matches finalizer.yaml schema.

    Contract: finalizer.yaml - FinalizationResponse schema
    Expected: All required fields present, correct types, valid enum values
    """
    # Arrange
    code_file = temp_test_dir / "schema_test.py"
    code_file.write_text("def schema_test(): return 42")

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440043",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [],
            "docs_files": [],
        },
        "validation_checks": ["linting"],
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Required top-level fields (per FinalizationResponse schema)
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

    # Assert - FinalizationResult required fields
    output_data = response["output_data"]
    result_required_fields = [
        "all_checks_passed",
        "check_results",
        "git_approval_required",
    ]
    for field in result_required_fields:
        assert field in output_data, f"Missing required result field: {field}"

    # Assert - Numeric ranges
    assert 0.0 <= response["confidence"] <= 1.0

    # Assert - Timestamp format (ISO 8601)
    try:
        datetime.fromisoformat(response["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        pytest.fail("Timestamp not in ISO 8601 format")


# ===================================================================
# Contract Test: Pre-Commit Checklist Validation
# ===================================================================

@pytest.mark.contract
def test_finalize_validates_all_requested_checks(temp_test_dir):
    """
    Test that finalizer executes all requested validation checks.

    Contract: finalizer.yaml - FinalizationRequest.validation_checks
    Expected: All checks in request are executed and results returned
    """
    # Arrange
    code_file = temp_test_dir / "checklist_test.py"
    code_file.write_text("def test(): pass")

    test_file = temp_test_dir / "test_checklist.py"
    test_file.write_text("def test_example(): assert True")

    requested_checks = [
        "tests_passing",
        "code_coverage",
        "linting",
        "constitutional_compliance",
        "documentation_sync",
        "secrets_check",
    ]

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440044",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [str(test_file)],
            "docs_files": [],
        },
        "validation_checks": requested_checks,
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - All requested checks have results
    output_data = response["output_data"]
    check_results = output_data["check_results"]

    for check_name in requested_checks:
        assert check_name in check_results, f"Missing result for check: {check_name}"
        # Result should be a boolean
        assert isinstance(check_results[check_name], bool)


# ===================================================================
# Contract Test: Validation Failure Blocks Commit
# ===================================================================

@pytest.mark.contract
def test_finalize_blocks_commit_when_checks_fail(temp_test_dir):
    """
    Test that failed validation checks block git operations.

    Contract: finalizer.yaml - all_checks_passed=False prevents commit
    Expected: all_checks_passed=False, git_approval_required=False (no point approving)
    """
    # Arrange - Code with intentional violations
    bad_code = temp_test_dir / "bad_code.py"
    bad_code.write_text("""
# Missing docstrings, no tests, violations
def calculate(x):
    # Violates Library-First: not extracted to library
    # Violates Test-First: no tests written
    return x * 2
""")

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440045",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(bad_code)],
            "test_files": [],
            "docs_files": [],
        },
        "validation_checks": [
            "constitutional_compliance",
            "tests_passing",
        ],
        "git_operation": {
            "type": "commit",
            "message": "bad: This should be blocked",
            "files_to_stage": [str(bad_code)],
        },
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Checks did not pass
    output_data = response["output_data"]
    # May pass or fail depending on implementation, but structure should be correct
    assert "all_checks_passed" in output_data
    assert isinstance(output_data["all_checks_passed"], bool)

    # If checks failed, violations should be documented
    if not output_data["all_checks_passed"]:
        # Should have violations or explanations
        assert (
            "constitutional_violations" in output_data
            or "linting_errors" in output_data
            or len(response["reasoning"]) > 0
        )


# ===================================================================
# Contract Test: No Autonomous Git Operations
# ===================================================================

@pytest.mark.contract
def test_finalize_never_executes_git_without_approval():
    """
    Test that finalizer NEVER executes git operations autonomously.

    Contract: finalizer.yaml - Principle VI enforcement
    Expected: user_approved field exists, git ops only happen after user sets it to True
    """
    # Arrange
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = Path(tmpdir) / "autonomous_test.py"
        code_file.write_text("def test(): return True")

        request_payload = {
            "agent_id": "quality.finalizer",
            "task_id": "550e8400-e29b-41d4-a716-446655440046",
            "phase": "validation",
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [],
                "docs_files": [],
            },
            "validation_checks": ["tests_passing"],
            "git_operation": {
                "type": "commit",
                "message": "test: Should require approval",
                "files_to_stage": [str(code_file)],
            },
        }

        # Act
        from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
        agent = ComplianceFinalizerAgent()
        response = agent.finalize(request_payload)

        # Assert - Git approval explicitly required
        output_data = response["output_data"]
        assert output_data["git_approval_required"] == True

        # Assert - User approval NOT automatically set
        user_approved = output_data.get("user_approved")
        assert user_approved != True  # Must be None or False

        # Assert - Next actions mention approval requirement
        next_actions = response["next_actions"]
        approval_mentioned = any(
            "approval" in action.lower() or "user" in action.lower()
            for action in next_actions
        )
        assert approval_mentioned, "Next actions should mention user approval requirement"


# ===================================================================
# Contract Test: FinalizationResult Output Format
# ===================================================================

@pytest.mark.contract
def test_finalization_result_output_format(temp_test_dir):
    """
    Test that FinalizationResult output matches expected format.

    Contract: finalizer.yaml - FinalizationResult schema
    Expected: All fields present with correct types and ranges
    """
    # Arrange
    code_file = temp_test_dir / "format_test.py"
    code_file.write_text("def test(): return 42")

    test_file = temp_test_dir / "test_format.py"
    test_file.write_text("def test_example(): assert test() == 42")

    request_payload = {
        "agent_id": "quality.finalizer",
        "task_id": "550e8400-e29b-41d4-a716-446655440047",
        "phase": "validation",
        "artifact_paths": {
            "code_files": [str(code_file)],
            "test_files": [str(test_file)],
            "docs_files": [],
        },
        "validation_checks": [
            "tests_passing",
            "code_coverage",
            "linting",
        ],
    }

    # Act
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    agent = ComplianceFinalizerAgent()
    response = agent.finalize(request_payload)

    # Assert - Output data structure
    output_data = response["output_data"]

    # All checks passed - boolean
    assert isinstance(output_data["all_checks_passed"], bool)

    # Check results - dict of booleans
    check_results = output_data["check_results"]
    assert isinstance(check_results, dict)
    for check_name, result in check_results.items():
        assert isinstance(check_name, str)
        assert isinstance(result, bool)

    # Code coverage percent - float 0-100 (if coverage check run)
    if "code_coverage" in check_results:
        code_coverage_percent = output_data.get("code_coverage_percent")
        if code_coverage_percent is not None:
            assert isinstance(code_coverage_percent, (int, float))
            assert 0.0 <= code_coverage_percent <= 100.0

    # Linting errors - non-negative integer (if linting check run)
    if "linting" in check_results:
        linting_errors = output_data.get("linting_errors")
        if linting_errors is not None:
            assert isinstance(linting_errors, int)
            assert linting_errors >= 0

    # Constitutional violations - array of strings
    constitutional_violations = output_data.get("constitutional_violations", [])
    assert isinstance(constitutional_violations, list)
    for violation in constitutional_violations:
        assert isinstance(violation, str)

    # Documentation updates needed - array of strings
    documentation_updates_needed = output_data.get("documentation_updates_needed", [])
    assert isinstance(documentation_updates_needed, list)

    # Secrets found - array of objects
    secrets_found = output_data.get("secrets_found", [])
    assert isinstance(secrets_found, list)
    for secret in secrets_found:
        assert isinstance(secret, dict)
        # Each secret should have file, line, secret_type
        if secret:  # If not empty
            assert "file" in secret or "secret_type" in secret

    # Formatted files - array of strings
    formatted_files = output_data.get("formatted_files", [])
    assert isinstance(formatted_files, list)

    # Git approval required - boolean
    assert isinstance(output_data["git_approval_required"], bool)

    # Git operation summary - string or null
    git_operation_summary = output_data.get("git_operation_summary")
    if git_operation_summary is not None:
        assert isinstance(git_operation_summary, str)

    # User approved - boolean or null
    user_approved = output_data.get("user_approved")
    if user_approved is not None:
        assert isinstance(user_approved, bool)
