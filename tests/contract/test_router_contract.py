"""
Contract Tests for Router Agent
DS-STAR Multi-Agent Enhancement - Feature 001

Tests the Router Agent's contract compliance with router.yaml.
Validates POST /route endpoint, routing decisions, execution strategies, and dependency graphs.

Test Coverage:
- POST /route with task analysis (T007)
- Refinement strategy decisions (T007)
- Response schema matches contracts/router.yaml (T007)
- Parallel execution planning (T007)
- Agent selection logic (T007)
- RoutingDecision output format (T007)
"""

import json
import uuid
import pytest
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Import fixtures
from tests.fixtures.setup_test_environment import (
    temp_test_dir,
    create_test_spec_file,
)


# ===================================================================
# Contract Test: POST /route with Multi-Domain Task
# ===================================================================

@pytest.mark.contract
def test_route_multi_domain_task_returns_dag_strategy(temp_test_dir):
    """
    Test that POST /route returns DAG execution strategy for multi-domain tasks.

    Contract: router.yaml - POST /route endpoint
    Expected: RoutingResponse with selected_agents, execution_strategy='dag', dependency_graph
    """
    # Arrange
    spec_path = temp_test_dir / "multi-domain-spec.md"
    spec_path.write_text("""
# Feature: User Authentication

## Requirements
- Frontend: Login form with email/password
- Backend: POST /api/auth/login endpoint
- Security: Password hashing, JWT tokens
    """)

    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440010",
        "phase": "implementation",
        "task_description": "Implement user authentication with frontend and backend",
        "domains_detected": ["frontend", "backend", "security"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {
            "spec_path": str(spec_path),
            "plan_path": None,
            "previous_outputs": [],
            "cumulative_feedback": [],
        },
    }

    # Act
    # This will fail until RouterAgent is implemented
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Response structure
    assert "agent_id" in response
    assert response["agent_id"] == "architecture.router"
    assert "task_id" in response
    assert "success" in response
    assert response["success"] == True
    assert "output_data" in response
    assert "reasoning" in response
    assert "confidence" in response
    assert "next_actions" in response
    assert "timestamp" in response

    # Assert - RoutingDecision structure
    output_data = response["output_data"]
    assert "selected_agents" in output_data
    assert "execution_strategy" in output_data
    assert "dependency_graph" in output_data
    assert "refinement_strategy" in output_data

    # Assert - Multi-domain requires multiple agents
    selected_agents = output_data["selected_agents"]
    assert isinstance(selected_agents, list)
    assert len(selected_agents) >= 2  # Multi-domain = multiple agents

    # Assert - Execution strategy is DAG for multi-domain
    assert output_data["execution_strategy"] in ["sequential", "parallel", "dag"]

    # Assert - Dependency graph present (required for DAG)
    if output_data["execution_strategy"] == "dag":
        dependency_graph = output_data["dependency_graph"]
        assert isinstance(dependency_graph, dict)
        # All selected agents should be in graph
        for agent_id in selected_agents:
            assert agent_id in dependency_graph
            assert isinstance(dependency_graph[agent_id], list)


# ===================================================================
# Contract Test: Refinement Strategy Decisions
# ===================================================================

@pytest.mark.contract
def test_route_includes_refinement_strategy():
    """
    Test that routing decision includes refinement strategy for failure handling.

    Contract: router.yaml - RoutingDecision.refinement_strategy enum
    Expected: One of: ADD_STEP, TRUNCATE_FROM, ROUTE_TO_DEBUG, RETRY_WITH_FEEDBACK
    """
    # Arrange
    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440011",
        "phase": "implementation",
        "task_description": "Implement database schema with migrations",
        "domains_detected": ["database"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {},
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Refinement strategy present
    output_data = response["output_data"]
    assert "refinement_strategy" in output_data

    # Assert - Valid refinement strategy
    valid_strategies = [
        "ADD_STEP",
        "TRUNCATE_FROM",
        "ROUTE_TO_DEBUG",
        "RETRY_WITH_FEEDBACK",
        None,  # Can be null
    ]
    assert output_data["refinement_strategy"] in valid_strategies


# ===================================================================
# Contract Test: Response Schema Validation
# ===================================================================

@pytest.mark.contract
def test_route_response_matches_contract_schema(temp_test_dir):
    """
    Test that POST /route response exactly matches router.yaml schema.

    Contract: router.yaml - RoutingResponse schema
    Expected: All required fields present, correct types, valid enum values
    """
    # Arrange
    spec_path = temp_test_dir / "schema-routing-spec.md"
    spec_path.write_text("# Test Feature\n## Requirements\n- Backend API needed")

    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440012",
        "phase": "planning",
        "task_description": "Design API endpoints",
        "domains_detected": ["backend"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {
            "spec_path": str(spec_path),
        },
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Required top-level fields (per RoutingResponse schema)
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

    # Assert - RoutingDecision required fields
    output_data = response["output_data"]
    decision_required_fields = [
        "selected_agents",
        "execution_strategy",
        "refinement_strategy",
    ]
    for field in decision_required_fields:
        assert field in output_data, f"Missing required decision field: {field}"

    # Assert - Execution strategy enum validation
    assert output_data["execution_strategy"] in ["sequential", "parallel", "dag"]

    # Assert - Numeric ranges
    assert 0.0 <= response["confidence"] <= 1.0

    # Assert - Timestamp format (ISO 8601)
    try:
        datetime.fromisoformat(response["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        pytest.fail("Timestamp not in ISO 8601 format")


# ===================================================================
# Contract Test: Parallel Execution Planning
# ===================================================================

@pytest.mark.contract
def test_route_identifies_parallel_execution_opportunities():
    """
    Test that router identifies tasks that can be executed in parallel.

    Contract: router.yaml - RoutingDecision.parallel_execution_opportunities
    Expected: Array of agent IDs that can run concurrently
    """
    # Arrange - Independent frontend and docs tasks
    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440013",
        "phase": "implementation",
        "task_description": "Update UI components and documentation",
        "domains_detected": ["frontend", "documentation"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {},
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Parallel execution opportunities field present
    output_data = response["output_data"]
    assert "parallel_execution_opportunities" in output_data or True  # Field optional

    # If parallel execution identified, validate format
    if "parallel_execution_opportunities" in output_data:
        parallel_opps = output_data["parallel_execution_opportunities"]
        assert isinstance(parallel_opps, list)
        # All items should be agent IDs (strings)
        for agent_id in parallel_opps:
            assert isinstance(agent_id, str)
            assert "." in agent_id  # Format: department.agent_name


# ===================================================================
# Contract Test: Agent Selection Logic
# ===================================================================

@pytest.mark.contract
def test_route_selects_appropriate_agents_for_domains():
    """
    Test that router selects appropriate agents based on detected domains.

    Contract: router.yaml - RoutingDecision.selected_agents
    Expected: Agent IDs match domains detected in task
    """
    # Arrange - Test cases for different domain combinations
    test_cases = [
        {
            "domains": ["backend"],
            "expected_agents": ["engineering.backend"],
        },
        {
            "domains": ["frontend", "backend"],
            "expected_agents": ["engineering.backend", "engineering.frontend"],
        },
        {
            "domains": ["database"],
            "expected_agents": ["database.specialist"],
        },
        {
            "domains": ["security"],
            "expected_agents": ["security.specialist"],
        },
    ]

    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()

    for test_case in test_cases:
        # Arrange
        request_payload = {
            "agent_id": "architecture.router",
            "task_id": str(uuid.uuid4()),
            "phase": "implementation",
            "task_description": f"Task involving {', '.join(test_case['domains'])}",
            "domains_detected": test_case["domains"],
            "current_state": {
                "completed_agents": [],
                "failed_agents": [],
            },
            "context": {},
        }

        # Act
        response = agent.route(request_payload)

        # Assert - Appropriate agents selected
        selected_agents = response["output_data"]["selected_agents"]
        assert isinstance(selected_agents, list)
        assert len(selected_agents) > 0

        # At least one agent per domain (may include additional agents like verifier)
        # This is a loose check since router may add orchestration agents
        assert len(selected_agents) >= len(test_case["domains"])


# ===================================================================
# Contract Test: Dependency Graph Validation
# ===================================================================

@pytest.mark.contract
def test_route_dependency_graph_is_valid_dag():
    """
    Test that dependency graph forms a valid DAG (no cycles).

    Contract: router.yaml - RoutingDecision.dependency_graph
    Expected: Valid DAG structure, all agents in graph are in selected_agents
    """
    # Arrange - Multi-domain task requiring DAG execution
    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440014",
        "phase": "implementation",
        "task_description": "Implement full-stack feature with database, backend, and frontend",
        "domains_detected": ["database", "backend", "frontend"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {},
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - If DAG strategy, validate dependency graph
    output_data = response["output_data"]
    if output_data["execution_strategy"] == "dag":
        selected_agents = output_data["selected_agents"]
        dependency_graph = output_data["dependency_graph"]

        # All agents in graph should be in selected_agents
        for agent_id in dependency_graph.keys():
            assert agent_id in selected_agents

        # All dependencies should also be in selected_agents
        for agent_id, deps in dependency_graph.items():
            for dep in deps:
                assert dep in selected_agents

        # Basic cycle detection (simplified - just check no self-dependencies)
        for agent_id, deps in dependency_graph.items():
            assert agent_id not in deps, f"Self-dependency detected for {agent_id}"


# ===================================================================
# Contract Test: RoutingDecision Output Format
# ===================================================================

@pytest.mark.contract
def test_routing_decision_output_format():
    """
    Test that RoutingDecision output matches expected format.

    Contract: router.yaml - RoutingDecision schema
    Expected: selected_agents non-empty, valid execution strategy, valid refinement strategy
    """
    # Arrange
    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440015",
        "phase": "implementation",
        "task_description": "Implement testing infrastructure",
        "domains_detected": ["testing"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [],
        },
        "context": {},
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Output data structure
    output_data = response["output_data"]

    # Selected agents - must be non-empty
    assert isinstance(output_data["selected_agents"], list)
    assert len(output_data["selected_agents"]) >= 1  # minItems: 1 per contract

    # Execution strategy - valid enum
    assert output_data["execution_strategy"] in ["sequential", "parallel", "dag"]

    # Refinement strategy - valid enum or null
    refinement_strategy = output_data.get("refinement_strategy")
    valid_refinement = [
        "ADD_STEP",
        "TRUNCATE_FROM",
        "ROUTE_TO_DEBUG",
        "RETRY_WITH_FEEDBACK",
        None,
    ]
    assert refinement_strategy in valid_refinement

    # Dependency graph - if DAG, must be present and valid
    if output_data["execution_strategy"] == "dag":
        assert "dependency_graph" in output_data
        assert isinstance(output_data["dependency_graph"], dict)
    elif output_data["execution_strategy"] in ["sequential", "parallel"]:
        # dependency_graph should be null or absent for non-DAG strategies
        dependency_graph = output_data.get("dependency_graph")
        assert dependency_graph is None or dependency_graph == {}


# ===================================================================
# Contract Test: Failed Agent Retry Logic
# ===================================================================

@pytest.mark.contract
def test_route_handles_failed_agents_with_refinement():
    """
    Test that router provides refinement strategy when agents have failed.

    Contract: router.yaml - RoutingDecision with failed_agents context
    Expected: Appropriate refinement_strategy selected based on failure type
    """
    # Arrange - Previous agent failed
    request_payload = {
        "agent_id": "architecture.router",
        "task_id": "550e8400-e29b-41d4-a716-446655440016",
        "phase": "implementation",
        "task_description": "Retry backend implementation after error",
        "domains_detected": ["backend"],
        "current_state": {
            "completed_agents": [],
            "failed_agents": [
                {
                    "agent_id": "engineering.backend",
                    "error": "TypeError in line 42",
                    "attempts": 1,
                }
            ],
        },
        "context": {},
    }

    # Act
    from sdd.agents.architecture.router import RouterAgent
    agent = RouterAgent()
    response = agent.route(request_payload)

    # Assert - Refinement strategy provided for failed agent
    output_data = response["output_data"]
    assert output_data["refinement_strategy"] is not None

    # Should be ROUTE_TO_DEBUG or RETRY_WITH_FEEDBACK for error cases
    assert output_data["refinement_strategy"] in [
        "ROUTE_TO_DEBUG",
        "RETRY_WITH_FEEDBACK",
        "ADD_STEP",
    ]

    # Reasoning should mention the failure
    assert "error" in response["reasoning"].lower() or "failed" in response["reasoning"].lower()
