"""
Contract Tests for Auto-Debug Agent
DS-STAR Multi-Agent Enhancement - Feature 001

Tests the Auto-Debug Agent's contract compliance with autodebug.yaml.
Validates POST /debug endpoint, error classification, repair attempts, and escalation logic.

Test Coverage:
- POST /debug with syntax error (T008)
- POST /debug with type error (T008)
- Max iteration limit (5 attempts) (T008)
- Response schema matches contracts/autodebug.yaml (T008)
- Escalation after max iterations (T008)
- DebugSession output format (T008)
"""

import json
import uuid
import pytest
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Import fixtures
from tests.fixtures.setup_test_environment import (
    code_with_syntax_error,
    code_with_type_error,
    code_with_name_error,
    code_with_null_error,
    code_with_import_error,
    temp_test_dir,
)


# ===================================================================
# Contract Test: POST /debug with Syntax Error
# ===================================================================

@pytest.mark.contract
def test_debug_syntax_error_resolves_in_one_iteration(code_with_syntax_error):
    """
    Test that POST /debug successfully resolves syntax errors in one iteration.

    Contract: autodebug.yaml - POST /debug endpoint with syntax error
    Expected: DebugSession with resolved=True, total_iterations=1, error_pattern='syntax'
    """
    # Arrange
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440020",
        "phase": "implementation",
        "failed_code": code_with_syntax_error,
        "stack_trace": "  File 'test.py', line 3\n    if x > 5\n            ^\nSyntaxError: invalid syntax",
        "test_expectations": [
            "Function returns True when x > 5",
            "Function prints 'Greater than 5'",
        ],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    # This will fail until AutoDebugAgent is implemented
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Response structure
    assert "agent_id" in response
    assert response["agent_id"] == "engineering.autodebug"
    assert "task_id" in response
    assert "success" in response
    assert response["success"] == True  # Agent executed successfully
    assert "output_data" in response
    assert "reasoning" in response
    assert "confidence" in response
    assert "next_actions" in response
    assert "timestamp" in response

    # Assert - DebugSession structure
    output_data = response["output_data"]
    assert "resolved" in output_data
    assert "total_iterations" in output_data
    assert "error_pattern" in output_data
    assert "attempts" in output_data

    # Assert - Syntax error resolved
    assert output_data["resolved"] == True
    assert output_data["total_iterations"] == 1  # Should fix on first try
    assert output_data["error_pattern"] == "syntax"

    # Assert - Final code provided
    assert "final_code" in output_data
    assert output_data["final_code"] is not None
    assert ":" in output_data["final_code"]  # Colon added

    # Assert - Not escalated
    assert output_data.get("escalated") != True


# ===================================================================
# Contract Test: POST /debug with Type Error
# ===================================================================

@pytest.mark.contract
def test_debug_type_error_attempts_repair(code_with_type_error):
    """
    Test that POST /debug attempts to repair type errors.

    Contract: autodebug.yaml - POST /debug with type error
    Expected: DebugSession with error_pattern='type', repair attempts logged
    """
    # Arrange
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440021",
        "phase": "implementation",
        "failed_code": code_with_type_error,
        "stack_trace": "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        "test_expectations": [
            "Function adds two integers and returns result",
        ],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Debug session created
    output_data = response["output_data"]
    assert output_data["error_pattern"] == "type"

    # Assert - Attempts logged
    assert "attempts" in output_data
    attempts = output_data["attempts"]
    assert isinstance(attempts, list)
    assert len(attempts) > 0

    # Assert - Each attempt has required fields
    for attempt in attempts:
        assert "iteration" in attempt
        assert "error_pattern" in attempt
        assert "repair_action" in attempt
        assert "test_result" in attempt
        assert attempt["error_pattern"] == "type"
        assert attempt["test_result"] in ["passed", "failed", "error"]


# ===================================================================
# Contract Test: Max Iteration Limit (5 attempts)
# ===================================================================

@pytest.mark.contract
def test_debug_respects_max_iteration_limit():
    """
    Test that auto-debug respects maximum iteration limit of 5.

    Contract: autodebug.yaml - DebugRequest.max_iterations (max: 5)
    Expected: total_iterations <= 5, escalated=True if not resolved
    """
    # Arrange - Complex logic error that won't resolve easily
    complex_logic_error = """
def calculate_fibonacci(n):
    if n < 0:
        return -1  # Wrong logic
    return n * 2  # Completely wrong algorithm
"""
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440022",
        "phase": "implementation",
        "failed_code": complex_logic_error,
        "stack_trace": "AssertionError: Expected fibonacci(5) == 5, got 10",
        "test_expectations": [
            "fibonacci(0) == 0",
            "fibonacci(1) == 1",
            "fibonacci(5) == 5",
            "fibonacci(10) == 55",
        ],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Max iterations respected
    output_data = response["output_data"]
    assert output_data["total_iterations"] <= 5

    # Assert - If not resolved, should be escalated
    if not output_data["resolved"]:
        assert output_data.get("escalated") == True
        assert "escalation_context" in output_data


# ===================================================================
# Contract Test: Response Schema Validation
# ===================================================================

@pytest.mark.contract
def test_debug_response_matches_contract_schema(code_with_syntax_error):
    """
    Test that POST /debug response exactly matches autodebug.yaml schema.

    Contract: autodebug.yaml - DebugResponse schema
    Expected: All required fields present, correct types, valid enum values
    """
    # Arrange
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440023",
        "phase": "implementation",
        "failed_code": code_with_syntax_error,
        "stack_trace": "SyntaxError: invalid syntax",
        "test_expectations": ["Function executes without error"],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Required top-level fields (per DebugResponse schema)
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

    # Assert - DebugSession required fields
    output_data = response["output_data"]
    session_required_fields = [
        "resolved",
        "total_iterations",
        "error_pattern",
    ]
    for field in session_required_fields:
        assert field in output_data, f"Missing required session field: {field}"

    # Assert - Error pattern enum validation
    valid_error_patterns = ["syntax", "type", "name", "null", "import", "logic", "unknown"]
    assert output_data["error_pattern"] in valid_error_patterns

    # Assert - Numeric ranges
    assert 1 <= output_data["total_iterations"] <= 5
    assert 0.0 <= response["confidence"] <= 1.0

    # Assert - Timestamp format (ISO 8601)
    try:
        datetime.fromisoformat(response["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        pytest.fail("Timestamp not in ISO 8601 format")


# ===================================================================
# Contract Test: Escalation After Max Iterations
# ===================================================================

@pytest.mark.contract
def test_debug_escalates_after_max_iterations():
    """
    Test that debug agent escalates to human after max iterations without resolution.

    Contract: autodebug.yaml - DebugSession.escalated field
    Expected: escalated=True, escalation_context with attempted_repairs and recommendation
    """
    # Arrange - Error that requires human intervention (architectural decision)
    architectural_issue = """
def process_payment(amount, currency):
    # Needs architectural decision: sync or async payment processing?
    # Needs decision: which payment gateway?
    # This is beyond automated repair
    pass
"""
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440024",
        "phase": "implementation",
        "failed_code": architectural_issue,
        "stack_trace": "NotImplementedError: Payment processing not implemented",
        "test_expectations": [
            "Processes payment successfully",
            "Returns transaction ID",
        ],
        "max_iterations": 2,  # Low limit to force escalation
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Not resolved, escalated to human
    output_data = response["output_data"]

    # If not resolved within 2 iterations, should escalate
    if not output_data["resolved"]:
        assert output_data["escalated"] == True

        # Assert - Escalation context provided
        assert "escalation_context" in output_data
        escalation_context = output_data["escalation_context"]

        assert "original_error" in escalation_context
        assert "attempted_repairs" in escalation_context
        assert isinstance(escalation_context["attempted_repairs"], list)

        # Should have tried at least once
        assert len(escalation_context["attempted_repairs"]) > 0

        # Recommendation provided
        if "recommendation" in escalation_context:
            assert isinstance(escalation_context["recommendation"], str)
            assert len(escalation_context["recommendation"]) > 0


# ===================================================================
# Contract Test: DebugSession Output Format
# ===================================================================

@pytest.mark.contract
def test_debug_session_output_format(code_with_syntax_error):
    """
    Test that DebugSession output matches expected format.

    Contract: autodebug.yaml - DebugSession schema
    Expected: resolved boolean, attempts array with proper structure, final_code if resolved
    """
    # Arrange
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440025",
        "phase": "implementation",
        "failed_code": code_with_syntax_error,
        "stack_trace": "SyntaxError: invalid syntax",
        "test_expectations": ["Code executes"],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - Output data structure
    output_data = response["output_data"]

    # Resolved - boolean
    assert isinstance(output_data["resolved"], bool)

    # Total iterations - integer 1-5
    assert isinstance(output_data["total_iterations"], int)
    assert 1 <= output_data["total_iterations"] <= 5

    # Error pattern - valid enum
    assert output_data["error_pattern"] in [
        "syntax", "type", "name", "null", "import", "logic", "unknown"
    ]

    # Attempts - array of DebugAttempt
    assert "attempts" in output_data
    attempts = output_data["attempts"]
    assert isinstance(attempts, list)
    assert len(attempts) == output_data["total_iterations"]

    # Each attempt has required fields
    for i, attempt in enumerate(attempts, start=1):
        assert "iteration" in attempt
        assert attempt["iteration"] == i
        assert "error_pattern" in attempt
        assert "repair_action" in attempt
        assert "test_result" in attempt
        assert attempt["test_result"] in ["passed", "failed", "error"]

    # If resolved, final_code must be present
    if output_data["resolved"]:
        assert "final_code" in output_data
        assert output_data["final_code"] is not None
        assert isinstance(output_data["final_code"], str)
        assert len(output_data["final_code"]) > 0

    # If escalated, escalation_context must be present
    if output_data.get("escalated"):
        assert "escalation_context" in output_data


# ===================================================================
# Contract Test: Error Pattern Classification
# ===================================================================

@pytest.mark.contract
def test_debug_classifies_error_patterns_correctly(
    code_with_syntax_error,
    code_with_type_error,
    code_with_name_error,
    code_with_null_error,
    code_with_import_error,
):
    """
    Test that debug agent correctly classifies different error patterns.

    Contract: autodebug.yaml - DebugSession.error_pattern enum
    Expected: Correct error_pattern classification for each error type
    """
    # Arrange - Test cases for each error pattern
    test_cases = [
        {
            "code": code_with_syntax_error,
            "stack_trace": "SyntaxError: invalid syntax",
            "expected_pattern": "syntax",
        },
        {
            "code": code_with_type_error,
            "stack_trace": "TypeError: unsupported operand type(s)",
            "expected_pattern": "type",
        },
        {
            "code": code_with_name_error,
            "stack_trace": "NameError: name 'undefined_variable' is not defined",
            "expected_pattern": "name",
        },
        {
            "code": code_with_null_error,
            "stack_trace": "AttributeError: 'NoneType' object has no attribute 'upper'",
            "expected_pattern": "null",
        },
        {
            "code": code_with_import_error,
            "stack_trace": "ModuleNotFoundError: No module named 'nonexistent_module'",
            "expected_pattern": "import",
        },
    ]

    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()

    for i, test_case in enumerate(test_cases):
        # Arrange
        request_payload = {
            "agent_id": "engineering.autodebug",
            "task_id": str(uuid.uuid4()),
            "phase": "implementation",
            "failed_code": test_case["code"],
            "stack_trace": test_case["stack_trace"],
            "test_expectations": ["Code executes without error"],
            "max_iterations": 5,
            "context": {},
        }

        # Act
        response = agent.debug(request_payload)

        # Assert - Error pattern correctly classified
        output_data = response["output_data"]
        assert output_data["error_pattern"] == test_case["expected_pattern"], \
            f"Expected {test_case['expected_pattern']}, got {output_data['error_pattern']}"


# ===================================================================
# Contract Test: Repair Summary Generation
# ===================================================================

@pytest.mark.contract
def test_debug_generates_repair_summary_on_success(code_with_syntax_error):
    """
    Test that successful repairs include a repair_summary field.

    Contract: autodebug.yaml - DebugSession.repair_summary (nullable)
    Expected: repair_summary present and descriptive if resolved=True
    """
    # Arrange
    request_payload = {
        "agent_id": "engineering.autodebug",
        "task_id": "550e8400-e29b-41d4-a716-446655440026",
        "phase": "implementation",
        "failed_code": code_with_syntax_error,
        "stack_trace": "SyntaxError: invalid syntax",
        "test_expectations": ["Code executes"],
        "max_iterations": 5,
        "context": {},
    }

    # Act
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    agent = AutoDebugAgent()
    response = agent.debug(request_payload)

    # Assert - If resolved, repair_summary should be present
    output_data = response["output_data"]
    if output_data["resolved"]:
        assert "repair_summary" in output_data
        repair_summary = output_data["repair_summary"]

        # Should be a non-empty string describing the fix
        assert isinstance(repair_summary, str)
        assert len(repair_summary) > 10  # Meaningful description

        # Should mention what was fixed
        assert any(keyword in repair_summary.lower()
                   for keyword in ["added", "fixed", "corrected", "repaired", "colon", "syntax"])
