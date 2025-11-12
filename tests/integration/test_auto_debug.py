"""
Integration Test: Self-Healing Auto-Debug (Scenario 3)
DS-STAR Multi-Agent Enhancement - Feature 001

Tests end-to-end auto-debug capability for automatic error resolution.

Test Coverage (T013):
- Syntax error auto-fix (FR-012, FR-013, FR-014, FR-015, FR-016)
- Type error auto-fix (FR-012, FR-013)
- Max 5 iteration limit (FR-015)
- Escalation with full context (FR-016)
- >70% fix rate target (FR-014)
"""

import uuid
import pytest
from tests.fixtures.setup_test_environment import (
    code_with_syntax_error,
    code_with_type_error,
    code_with_name_error,
)


@pytest.mark.integration
def test_autodebug_fixes_syntax_error_automatically(code_with_syntax_error):
    """Integration test: Auto-debug fixes syntax errors (FR-012, FR-013, FR-014)."""
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    from sdd.agents.shared.models import AgentInput

    agent = AutoDebugAgent()
    request = AgentInput(
        agent_id="engineering.autodebug",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "failed_code": code_with_syntax_error,
            "stack_trace": "SyntaxError: invalid syntax",
            "test_expectations": ["Function executes without error"],
            "max_iterations": 5,
        },
        context={},
    )

    response = agent.debug(request)

    # Assert - Error resolved
    assert response.success == True
    assert response.output_data.resolved == True
    assert response.output_data.total_iterations <= 3  # Should fix quickly
    assert response.output_data.error_pattern == "syntax"
    assert "final_code" in response.output_data


@pytest.mark.integration
def test_autodebug_handles_type_errors(code_with_type_error):
    """Integration test: Auto-debug attempts type error fixes (FR-012, FR-013)."""
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    from sdd.agents.shared.models import AgentInput

    agent = AutoDebugAgent()
    request = AgentInput(
        agent_id="engineering.autodebug",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "failed_code": code_with_type_error,
            "stack_trace": "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
            "test_expectations": ["Adds two numbers correctly"],
            "max_iterations": 5,
        },
        context={},
    )

    response = agent.debug(request)

    # Assert - Attempts made
    assert len(response.output_data.attempts) > 0
    assert all(attempt.error_pattern == "type" for attempt in response.output_data.attempts)


@pytest.mark.integration
def test_autodebug_respects_max_iterations_and_escalates():
    """Integration test: Auto-debug escalates after max iterations (FR-015, FR-016)."""
    complex_error = "def broken(): return unknown_function() + undefined_var"

    from sdd.agents.engineering.autodebug import AutoDebugAgent
    from sdd.agents.shared.models import AgentInput

    agent = AutoDebugAgent()
    request = AgentInput(
        agent_id="engineering.autodebug",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "failed_code": complex_error,
            "stack_trace": "NameError: name 'unknown_function' is not defined",
            "test_expectations": ["Function works correctly"],
            "max_iterations": 5,
        },
        context={},
    )

    response = agent.debug(request)

    # Assert - Max iterations respected
    assert response.output_data.total_iterations <= 5

    # Assert - Escalation if not resolved
    if not response.output_data.resolved:
        assert response.output_data.escalated == True
        assert "escalation_context" in response.output_data


@pytest.mark.integration
def test_autodebug_achieves_70_percent_fix_rate():
    """Integration test: Auto-debug achieves >70% fix rate target (FR-014)."""
    from sdd.agents.engineering.autodebug import AutoDebugAgent
    from sdd.agents.shared.models import AgentInput

    test_errors = [
        ("syntax", "def f():\n  if True\n    pass", "SyntaxError"),
        ("type", "result = '5' + 10", "TypeError"),
        ("name", "print(undefined)", "NameError"),
    ]

    agent = AutoDebugAgent()
    resolved_count = 0

    for error_type, code, trace in test_errors:
        request = AgentInput(
            agent_id="engineering.autodebug",
            task_id=f"test-fix-rate-{error_type}",
            phase="implementation",
            input_data={
                "failed_code": code,
                "stack_trace": trace,
                "test_expectations": ["Code executes"],
                "max_iterations": 5,
            },
            context={},
        )

        response = agent.debug(request)
        if response.output_data.resolved:
            resolved_count += 1

    fix_rate = (resolved_count / len(test_errors)) * 100
    assert fix_rate >= 70.0, f"Fix rate {fix_rate}% below 70% target"
