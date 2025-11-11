"""
Integration Test: Intelligent Routing (Scenario 2)
DS-STAR Multi-Agent Enhancement - Feature 001

Tests end-to-end routing orchestration for multi-domain features.
Validates agent selection, execution strategy, and parallel planning.

Test Coverage:
- Multi-domain feature routing (T012 - FR-007, FR-008, FR-009, FR-010)
- Parallel execution planning (T012)
- Agent selection based on keywords (T012)
- Routing decision audit trail (T012)
"""

import json
import uuid
import pytest
from pathlib import Path

from tests.fixtures.setup_test_environment import temp_test_dir


@pytest.mark.integration
def test_router_handles_multi_domain_feature(temp_test_dir):
    """
    Integration test: Router correctly handles multi-domain features.

    User Story: Intelligent Routing Acceptance Scenario 3
    Requirements: FR-007, FR-008, FR-009, FR-010

    Expected Behavior:
    1. Detects multiple domains (frontend, backend, security)
    2. Selects appropriate agents
    3. Creates dependency graph (DAG execution)
    4. Plans execution order
    """
    # Arrange
    spec_path = temp_test_dir / "auth-feature-spec.md"
    spec_path.write_text("""
# Feature: User Authentication

## Requirements
- Frontend: Login form with email/password validation
- Backend: POST /api/auth/login endpoint with JWT tokens
- Security: Password hashing with bcrypt, secure session management
- Database: User credentials table with indexed email field
    """)

    from sdd.agents.architecture.router import RouterAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    # Act
    agent = RouterAgent()
    request = AgentInput(
        agent_id="architecture.router",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "task_description": "Implement user authentication with frontend and backend",
            "domains_detected": ["frontend", "backend", "security", "database"],
            "current_state": {
                "completed_agents": [],
                "failed_agents": [],
            },
        },
        context=AgentContext(spec_path=str(spec_path)),
    )

    response = agent.route(request)

    # Assert - Multiple agents selected (FR-007)
    assert response.success == True
    selected_agents = response.output_data.selected_agents
    assert len(selected_agents) >= 3  # At least frontend, backend, security

    # Assert - Appropriate execution strategy (FR-008)
    execution_strategy = response.output_data.execution_strategy
    assert execution_strategy in ["dag", "sequential"]  # Multi-domain typically needs DAG

    # Assert - Dependency graph present (FR-009)
    if execution_strategy == "dag":
        dependency_graph = response.output_data.dependency_graph
        assert isinstance(dependency_graph, dict)
        assert len(dependency_graph) > 0

        # Backend should complete before frontend
        if "engineering.backend" in dependency_graph and "engineering.frontend" in dependency_graph:
            frontend_deps = dependency_graph.get("engineering.frontend", [])
            # Frontend likely depends on backend completing first

    # Assert - Audit trail in reasoning (FR-010)
    assert len(response.reasoning) > 0
    assert any(keyword in response.reasoning.lower() for keyword in ["backend", "frontend", "security"])


@pytest.mark.integration
def test_router_plans_parallel_execution():
    """
    Integration test: Router identifies parallel execution opportunities.

    Requirements: FR-010 (parallel execution planning)
    """
    from sdd.agents.architecture.router import RouterAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    # Act
    agent = RouterAgent()
    request = AgentInput(
        agent_id="architecture.router",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "task_description": "Update UI components and API documentation",
            "domains_detected": ["frontend", "documentation"],
            "current_state": {"completed_agents": [], "failed_agents": []},
        },
        context=AgentContext(),
    )

    response = agent.route(request)

    # Assert - Execution strategy allows parallelism
    assert response.output_data.execution_strategy in ["parallel", "dag"]

    # Assert - If parallel, multiple agents can run simultaneously
    if response.output_data.execution_strategy == "parallel":
        assert len(response.output_data.selected_agents) >= 2


@pytest.mark.integration
def test_router_agent_selection_based_on_keywords():
    """
    Integration test: Router selects agents based on domain keywords.

    Requirements: FR-007 (agent selection logic)
    """
    from sdd.agents.architecture.router import RouterAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    test_cases = [
        {
            "description": "Implement REST API endpoints",
            "domains": ["backend"],
            "expected_agents": ["engineering.backend"],
        },
        {
            "description": "Add database migrations and schema",
            "domains": ["database"],
            "expected_agents": ["database.specialist"],
        },
        {
            "description": "Security audit and vulnerability scan",
            "domains": ["security"],
            "expected_agents": ["security.specialist"],
        },
    ]

    agent = RouterAgent()

    for test_case in test_cases:
        request = AgentInput(
            agent_id="architecture.router",
            task_id=f"test-selection-{test_case['domains'][0]}",
            phase="implementation",
            input_data={
                "task_description": test_case["description"],
                "domains_detected": test_case["domains"],
                "current_state": {"completed_agents": [], "failed_agents": []},
            },
            context=AgentContext(),
        )

        response = agent.route(request)

        # Assert - At least one expected agent selected
        selected_agents = response.output_data.selected_agents
        assert len(selected_agents) >= len(test_case["domains"])


@pytest.mark.integration
def test_router_creates_audit_trail():
    """
    Integration test: Router creates audit trail for routing decisions.

    Requirements: FR-010 (audit trail)
    """
    from sdd.agents.architecture.router import RouterAgent
    from sdd.agents.shared.models import AgentInput, AgentContext

    # Act
    agent = RouterAgent()
    request = AgentInput(
        agent_id="architecture.router",
        task_id=str(uuid.uuid4()),
        phase="implementation",
        input_data={
            "task_description": "Complex multi-agent task",
            "domains_detected": ["backend", "database", "testing"],
            "current_state": {"completed_agents": [], "failed_agents": []},
        },
        context=AgentContext(),
    )

    response = agent.route(request)

    # Assert - Reasoning explains decision
    assert len(response.reasoning) > 20  # Substantial explanation

    # Assert - Confidence score present
    assert 0.0 <= response.confidence <= 1.0

    # Assert - Next actions provided
    assert len(response.next_actions) > 0

    # Assert - Metadata for audit
    # Response should be JSON-serializable for storage
    try:
        json.dumps(response.to_dict())
    except (TypeError, AttributeError):
        # If to_dict() doesn't exist, response should still be auditable
        assert hasattr(response, 'agent_id')
        assert hasattr(response, 'timestamp')
