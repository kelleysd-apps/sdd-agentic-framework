"""
Test Environment Setup and Fixtures
DS-STAR Multi-Agent Enhancement - Feature 001

This module provides reusable test fixtures for all test suites:
- Test specification samples (complete and incomplete)
- Test plan samples (valid and invalid)
- Test code samples (with various error types)
- Mock agent contexts and outputs
- Temporary directories for test artifacts

Usage:
    pytest tests/fixtures/setup_test_environment.py  # Run setup

    # In test files:
    from tests.fixtures.setup_test_environment import (
        incomplete_spec_sample,
        complete_spec_sample,
        # ...
    )
"""

import json
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import pytest


# ===================================================================
# Directory Setup
# ===================================================================

@pytest.fixture(scope="session")
def temp_test_dir():
    """Create temporary directory for test artifacts."""
    with tempfile.TemporaryDirectory(prefix="sdd_test_") as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="session")
def test_specs_dir(temp_test_dir):
    """Create specs directory in temp location."""
    specs_dir = temp_test_dir / "specs"
    specs_dir.mkdir(parents=True, exist_ok=True)
    return specs_dir


@pytest.fixture(scope="session")
def test_docs_dir(temp_test_dir):
    """Create .docs directory in temp location."""
    docs_dir = temp_test_dir / ".docs" / "agents"
    docs_dir.mkdir(parents=True, exist_ok=True)
    return docs_dir


# ===================================================================
# Specification Samples
# ===================================================================

@pytest.fixture
def incomplete_spec_sample() -> str:
    """Incomplete specification for testing quality gate blocking."""
    return """# Feature Specification: Test Feature

**Feature Branch**: `test-feature`
**Created**: 2025-11-10
**Status**: Draft

## Overview

This is a test feature for validation.

## Requirements

- FR-001: Do something
- FR-002: Do something else
"""


@pytest.fixture
def complete_spec_sample() -> str:
    """Complete specification for testing quality gate passing."""
    return """# Feature Specification: Complete Test Feature

**Feature Branch**: `test-complete-feature`
**Created**: 2025-11-10
**Status**: Draft

## Overview

This is a complete test feature with all required sections.

## User Stories

### Primary User Story

As a developer, I want to test the verification system, so that I can ensure quality gates work correctly.

### Additional Stories

- As a QA engineer, I want clear acceptance criteria, so that I can validate features effectively.
- As a product owner, I want specifications to be complete, so that development can proceed smoothly.

## Acceptance Criteria

1. **Given** a complete specification, **When** verification runs, **Then** it should pass.
2. **Given** an incomplete specification, **When** verification runs, **Then** it should fail with feedback.
3. **Given** a specification with all required sections, **When** completeness is evaluated, **Then** score should be >= 0.90.

### Edge Cases

- What happens when sections are empty?
- How does system handle malformed requirements?

## Requirements

### Functional Requirements

- **FR-001**: System MUST validate specification completeness
- **FR-002**: System MUST provide actionable feedback
- **FR-003**: System MUST calculate quality scores

### Key Entities

- **VerificationResult**: Contains quality score and feedback
- **SpecificationDocument**: Represents parsed spec file

## Review & Acceptance Checklist

### Content Quality
- [x] No implementation details
- [x] Focused on user value
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [x] All requirements testable
- [x] Success criteria measurable
- [x] Scope clearly bounded
"""


@pytest.fixture
def spec_with_clarifications() -> str:
    """Specification with NEEDS CLARIFICATION markers."""
    return """# Feature Specification: Unclear Feature

## Requirements

- **FR-001**: System MUST [NEEDS CLARIFICATION: authentication method not specified]
- **FR-002**: System MUST [NEEDS CLARIFICATION: data retention period unknown]
"""


# ===================================================================
# Plan Samples
# ===================================================================

@pytest.fixture
def valid_plan_sample() -> str:
    """Valid implementation plan for testing."""
    return """# Implementation Plan: Test Feature

## Technical Context

**Language**: Python 3.11+
**Dependencies**: pytest==7.4.3, pydantic==2.5.0
**Project Type**: single

## Constitution Check

### Principle I: Library-First Architecture
**Status**: PASS

### Principle II: Test-First Development
**Status**: PASS

### Principle III: Contract-First Design
**Status**: PASS
"""


@pytest.fixture
def invalid_plan_sample() -> str:
    """Invalid plan missing constitutional checks."""
    return """# Implementation Plan: Invalid Feature

## Technical Context

**Language**: Python 3.11+

## Some Random Section

No constitutional compliance checks.
"""


# ===================================================================
# Code Samples with Errors
# ===================================================================

@pytest.fixture
def code_with_syntax_error() -> str:
    """Python code with syntax error."""
    return """
def test_function():
    x = 10
    if x > 5
        print("Greater than 5")
"""


@pytest.fixture
def code_with_type_error() -> str:
    """Python code with type error."""
    return """
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers("10", 20)  # Type error
"""


@pytest.fixture
def code_with_name_error() -> str:
    """Python code with name error."""
    return """
def calculate():
    result = undefined_variable * 2  # NameError
    return result
"""


@pytest.fixture
def code_with_null_error() -> str:
    """Python code with null/None error."""
    return """
def process_data(data: dict) -> str:
    return data["key"].upper()  # AttributeError if data["key"] is None

process_data({"key": None})
"""


@pytest.fixture
def code_with_import_error() -> str:
    """Python code with import error."""
    return """
from nonexistent_module import some_function  # ModuleNotFoundError

def test():
    some_function()
"""


@pytest.fixture
def correct_code_sample() -> str:
    """Correct Python code for comparison."""
    return """
def add_numbers(a: int, b: int) -> int:
    \"\"\"Add two numbers and return the result.\"\"\"
    return a + b

def test_add_numbers():
    \"\"\"Test the add_numbers function.\"\"\"
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
"""


# ===================================================================
# Mock Agent Data Structures
# ===================================================================

@pytest.fixture
def mock_agent_input() -> Dict[str, Any]:
    """Mock AgentInput structure."""
    return {
        "agent_id": "quality.verifier",
        "task_id": "test-task-001",
        "phase": "specification",
        "input_data": {
            "artifact_type": "spec",
            "artifact_path": "/tmp/test-spec.md",
        },
        "context": {
            "spec_path": "/tmp/test-spec.md",
            "plan_path": None,
            "previous_outputs": [],
            "cumulative_feedback": [],
            "refinement_state": None,
        },
    }


@pytest.fixture
def mock_agent_output_success() -> Dict[str, Any]:
    """Mock successful AgentOutput."""
    return {
        "agent_id": "quality.verifier",
        "task_id": "test-task-001",
        "success": True,
        "output_data": {
            "decision": "sufficient",
            "quality_score": 0.92,
        },
        "reasoning": "Specification meets all quality thresholds",
        "confidence": 0.95,
        "next_actions": ["Proceed to planning phase"],
        "metadata": {"violations": []},
        "timestamp": datetime.now().isoformat(),
    }


@pytest.fixture
def mock_agent_output_failure() -> Dict[str, Any]:
    """Mock failed AgentOutput with feedback."""
    return {
        "agent_id": "quality.verifier",
        "task_id": "test-task-001",
        "success": True,  # Agent executed successfully
        "output_data": {
            "decision": "insufficient",
            "quality_score": 0.65,
        },
        "reasoning": "Specification lacks required sections",
        "confidence": 0.91,
        "next_actions": ["Add User Scenarios section", "Add Functional Requirements"],
        "metadata": {
            "violations": ["missing_user_scenarios", "incomplete_requirements"]
        },
        "timestamp": datetime.now().isoformat(),
    }


@pytest.fixture
def mock_verification_decision() -> Dict[str, Any]:
    """Mock VerificationDecision structure."""
    return {
        "decision": "insufficient",
        "quality_score": 0.72,
        "dimension_scores": {
            "completeness": 0.85,
            "constitutional_compliance": 0.65,
            "test_coverage": 0.70,
            "spec_alignment": 0.90,
        },
        "feedback": [
            "Add error handling strategy",
            "Specify retry logic",
            "Include performance requirements",
        ],
        "violations": ["missing_error_handling", "missing_performance_reqs"],
        "passed_checks": ["has_title", "has_requirements", "has_user_stories"],
    }


@pytest.fixture
def mock_routing_decision() -> Dict[str, Any]:
    """Mock RoutingDecision structure."""
    return {
        "strategy": "ADD_STEP",
        "selected_agents": ["backend-architect", "database-specialist"],
        "parallel_execution_plan": [
            {"agent": "backend-architect", "tasks": ["API design"]},
            {"agent": "database-specialist", "tasks": ["Schema design"]},
        ],
        "reasoning": "Feature requires both backend and database work",
        "estimated_duration": 3600,
        "dependencies": ["schema must complete before API endpoints"],
    }


@pytest.fixture
def mock_debug_session() -> Dict[str, Any]:
    """Mock DebugSession structure."""
    return {
        "session_id": "debug-001",
        "original_error": "SyntaxError: invalid syntax",
        "attempts": [
            {
                "round": 1,
                "error_type": "syntax",
                "analysis": "Missing colon in if statement",
                "fix_code": "if x > 5:",
                "test_result": "passed",
            }
        ],
        "final_status": "resolved",
        "iterations_used": 1,
    }


@pytest.fixture
def mock_context_summary() -> Dict[str, Any]:
    """Mock ContextSummary structure."""
    return {
        "task_id": "test-task-001",
        "relevant_files": [
            {
                "path": "src/auth/login.py",
                "description": "Handles user authentication",
                "relevance_score": 0.92,
            },
            {
                "path": "tests/test_auth.py",
                "description": "Auth test suite (coverage: 85%)",
                "relevance_score": 0.88,
            },
        ],
        "existing_patterns": [
            "Error handling: Custom exceptions in src/exceptions/",
            "Database access: Repository pattern in src/repositories/",
        ],
        "dependencies": ["FastAPI", "SQLAlchemy", "pytest"],
        "related_specs": ["specs/001-authentication/spec.md"],
        "constitutional_compliance": {
            "library_first": True,
            "test_first": True,
            "integration_tests_needed": True,
        },
    }


@pytest.fixture
def mock_refinement_state() -> Dict[str, Any]:
    """Mock RefinementState structure."""
    return {
        "task_id": "test-task-001",
        "phase": "planning",
        "iterations": [
            {
                "round": 1,
                "timestamp": "2025-11-10T10:30:00Z",
                "input": "Initial plan...",
                "output": "Generated plan...",
                "verification_result": "insufficient",
                "feedback": "Missing error handling strategy",
                "agent": "verifier-agent",
            }
        ],
        "cumulative_learnings": [
            "Must include error handling",
            "Need to specify retry logic",
        ],
        "current_round": 1,
        "max_rounds": 20,
        "early_stop_triggered": False,
    }


# ===================================================================
# Test Data Files
# ===================================================================

@pytest.fixture
def create_test_spec_file(test_specs_dir, complete_spec_sample):
    """Create a complete test specification file."""
    def _create(filename="test-spec.md", content=None):
        spec_file = test_specs_dir / filename
        spec_file.write_text(content or complete_spec_sample)
        return spec_file
    return _create


@pytest.fixture
def create_test_json_file(temp_test_dir):
    """Create a test JSON file with given data."""
    def _create(filename: str, data: Dict[str, Any]):
        json_file = temp_test_dir / filename
        json_file.write_text(json.dumps(data, indent=2))
        return json_file
    return _create


# ===================================================================
# Environment Variables
# ===================================================================

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up test environment variables."""
    import os
    os.environ["SDD_TEST_MODE"] = "true"
    os.environ["SDD_METRICS_DIR"] = ".docs/agents/shared/metrics/test"
    os.environ["PYTEST_CURRENT_TEST"] = "true"
    yield
    # Cleanup if needed
    os.environ.pop("SDD_TEST_MODE", None)
    os.environ.pop("SDD_METRICS_DIR", None)
    os.environ.pop("PYTEST_CURRENT_TEST", None)


# ===================================================================
# Setup Function (can be run directly)
# ===================================================================

def setup_test_directories():
    """
    Set up test directories when run as a script.

    Usage:
        python tests/fixtures/setup_test_environment.py
    """
    test_dirs = [
        "tests/unit",
        "tests/contract",
        "tests/integration",
        "tests/fixtures",
        ".docs/agents/shared/metrics/test",
        ".docs/agents/shared/refinement-state/test",
        ".docs/agents/shared/context-summaries/test",
    ]

    for dir_path in test_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}")

    print("\n✓ Test environment setup complete!")


if __name__ == "__main__":
    setup_test_directories()
