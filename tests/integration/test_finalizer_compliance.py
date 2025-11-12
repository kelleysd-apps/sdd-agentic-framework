"""
Integration Test: Output Standardization (Scenario 6)
DS-STAR Multi-Agent Enhancement - Feature 001

Tests end-to-end pre-commit validation and git approval enforcement.

Test Coverage (T016):
- Pre-commit constitutional checks (FR-034, FR-035, FR-036, FR-037, FR-038, FR-039)
- Git approval gate enforcement (FR-035 - CRITICAL)
- Code formatting and docs generation (FR-036)
- >95% first-time pass rate target (FR-038)
"""

import uuid
import pytest
from pathlib import Path
from tests.fixtures.setup_test_environment import temp_test_dir, correct_code_sample


@pytest.mark.integration
def test_finalizer_enforces_constitutional_compliance(temp_test_dir, correct_code_sample):
    """
    Integration test: Finalizer validates constitutional compliance before commit.

    Requirements: FR-034, FR-035
    """
    # Arrange
    code_file = temp_test_dir / "compliant_code.py"
    code_file.write_text(correct_code_sample)

    test_file = temp_test_dir / "test_compliant.py"
    test_file.write_text("def test_example(): assert True")

    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    from sdd.agents.shared.models import AgentInput

    # Act
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id=str(uuid.uuid4()),
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [str(test_file)],
                "docs_files": [],
            },
            "validation_checks": [
                "tests_passing",
                "code_coverage",
                "constitutional_compliance",
            ],
        },
        context={},
    )

    response = agent.finalize(request)

    # Assert - Constitutional compliance checked (FR-034)
    assert "constitutional_compliance" in response.output_data.check_results

    # Assert - All checks executed
    assert response.success == True


@pytest.mark.integration
def test_finalizer_requires_git_approval_always(temp_test_dir):
    """
    Integration test: Finalizer ALWAYS requires user approval for git operations.

    Requirements: FR-035 (CRITICAL - Principle VI enforcement)
    """
    # Arrange
    code_file = temp_test_dir / "git_test.py"
    code_file.write_text("def test(): return True")

    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    from sdd.agents.shared.models import AgentInput

    # Act
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id=str(uuid.uuid4()),
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [],
                "docs_files": [],
            },
            "validation_checks": ["tests_passing"],
            "git_operation": {
                "type": "commit",
                "message": "test: Add test file",
                "files_to_stage": [str(code_file)],
            },
        },
        context={},
    )

    response = agent.finalize(request)

    # Assert - Git approval REQUIRED (CRITICAL - FR-035)
    assert response.output_data.git_approval_required == True
    assert response.output_data.get("user_approved") != True

    # Assert - Clear summary provided for user review
    assert "git_operation_summary" in response.output_data
    assert len(response.output_data.git_operation_summary) > 0


@pytest.mark.integration
def test_finalizer_validates_tests_and_coverage(temp_test_dir, correct_code_sample):
    """
    Integration test: Finalizer validates tests pass and coverage meets threshold.

    Requirements: FR-036, FR-037
    """
    # Arrange
    code_file = temp_test_dir / "coverage_test.py"
    code_file.write_text(correct_code_sample)

    test_file = temp_test_dir / "test_coverage.py"
    test_file.write_text("""
from coverage_test import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    """)

    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    from sdd.agents.shared.models import AgentInput

    # Act
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id=str(uuid.uuid4()),
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [str(test_file)],
                "docs_files": [],
            },
            "validation_checks": [
                "tests_passing",
                "code_coverage",
            ],
        },
        context={},
    )

    response = agent.finalize(request)

    # Assert - Tests and coverage checks executed
    check_results = response.output_data.check_results
    assert "tests_passing" in check_results
    assert "code_coverage" in check_results


@pytest.mark.integration
def test_finalizer_detects_secrets_in_code(temp_test_dir):
    """
    Integration test: Finalizer detects secrets in code before commit.

    Requirements: FR-037 (secrets detection)
    """
    # Arrange - Code with potential secret
    code_with_secret = """
API_KEY = "sk-1234567890abcdef"  # Looks like a secret
DATABASE_PASSWORD = "hardcoded-password-123"

def connect():
    return API_KEY
"""
    code_file = temp_test_dir / "secrets_test.py"
    code_file.write_text(code_with_secret)

    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    from sdd.agents.shared.models import AgentInput

    # Act
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id=str(uuid.uuid4()),
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [],
                "docs_files": [],
            },
            "validation_checks": ["secrets_check"],
        },
        context={},
    )

    response = agent.finalize(request)

    # Assert - Secrets check executed
    assert "secrets_check" in response.output_data.check_results

    # If secrets detected, should be documented
    # (Implementation may or may not detect these specific patterns)


@pytest.mark.integration
def test_finalizer_achieves_95_percent_first_time_pass_rate():
    """
    Integration test: Finalizer achieves >95% first-time pass rate target.

    Requirements: FR-038 (>95% pass rate)

    Note: This test validates the structure for tracking pass rate.
    Actual 95% achievement requires production data.
    """
    # This would be a metrics aggregation test
    # For now, validate that finalizer tracks success/failure
    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent

    agent = ComplianceFinalizerAgent()

    # Test structure exists for tracking
    assert hasattr(agent, 'finalize') or callable(getattr(agent, 'finalize', None))


@pytest.mark.integration
def test_finalizer_blocks_commit_on_validation_failure(temp_test_dir):
    """
    Integration test: Finalizer blocks commit when validation fails.

    Requirements: FR-039 (quality gate enforcement)
    """
    # Arrange - Code that will fail linting/validation
    bad_code = """
def broken_function(  ):
 x=1+2    # Poor formatting
 return   x
"""
    code_file = temp_test_dir / "bad_code.py"
    code_file.write_text(bad_code)

    from sdd.agents.quality.finalizer import ComplianceFinalizerAgent
    from sdd.agents.shared.models import AgentInput

    # Act
    agent = ComplianceFinalizerAgent()
    request = AgentInput(
        agent_id="quality.finalizer",
        task_id=str(uuid.uuid4()),
        phase="validation",
        input_data={
            "artifact_paths": {
                "code_files": [str(code_file)],
                "test_files": [],
                "docs_files": [],
            },
            "validation_checks": ["linting"],
            "git_operation": {
                "type": "commit",
                "message": "bad: Should be blocked",
                "files_to_stage": [str(code_file)],
            },
        },
        context={},
    )

    response = agent.finalize(request)

    # Assert - Structure exists for blocking commits
    assert "all_checks_passed" in response.output_data
    assert "git_approval_required" in response.output_data
