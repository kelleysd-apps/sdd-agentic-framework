# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CRITICAL: Read Constitution First

**ALWAYS read `/workspaces/ioun-ai/.specify/memory/constitution.md` BEFORE starting any work.**

The constitution is the SINGLE SOURCE OF TRUTH for:
- Core development principles and rules
- Workflow requirements and gates
- Quality standards and constraints
- All architectural decisions

No work should proceed without first understanding and applying the constitution's principles. All features, code, and decisions must comply with constitutional requirements.

## Project Overview

This is a specification-driven development framework that uses structured templates and workflows to generate and implement features. The project uses a TDD approach with contract-first design patterns as defined in the constitution.

## Commands

### Feature Specification Workflow

1. **Create feature specification**: Use `/specify` command
   - **REQUIRES USER APPROVAL**: Will ask if you want a new feature branch created
   - If approved, will ask for desired branch format/name
   - Default format when approved: `###-feature-name`
   - Generates spec file at `specs/###-feature-name/spec.md`
   - Script: `.specify/scripts/bash/create-new-feature.sh --json "$ARGUMENTS"`

2. **Generate implementation plan**: Use `/plan` command
   - Reads feature spec and constitution
   - Generates research, data models, contracts, and quickstart docs
   - Script: `.specify/scripts/bash/setup-plan.sh --json`
   - Stops before task generation

3. **Generate tasks**: Use `/tasks` command
   - Creates dependency-ordered task list from design artifacts
   - Script: `.specify/scripts/bash/check-task-prerequisites.sh --json`
   - Marks parallel-executable tasks with [P]

### Agent Management Commands

1. **Create new agent**: Use `/create-agent` command
   - Creates specialized subagent with constitutional compliance
   - Auto-determines department based on purpose
   - Sets appropriate tool restrictions
   - Initializes memory structure
   - Script: `.specify/scripts/bash/create-agent.sh --json`
   - Example: `/create-agent backend-engineer "API and database specialist"`

## Key Architecture

### Directory Structure
```
.specify/
├── memory/
│   ├── constitution.md      # Core development principles
│   └── constitution_update_checklist.md
├── scripts/bash/            # Workflow automation scripts
├── templates/               # Document templates
│   ├── spec-template.md     # Feature specification
│   ├── plan-template.md     # Implementation plan (9-step process)
│   ├── tasks-template.md    # Task list generation
│   └── agent-file-template.md

specs/###-feature-name/       # Per-feature documentation
├── spec.md                  # Feature requirements
├── plan.md                  # Technical approach
├── research.md              # Technical decisions
├── data-model.md            # Entity definitions
├── contracts/               # API contracts
├── quickstart.md            # Test scenarios
└── tasks.md                 # Implementation tasks
```

### Workflow Scripts

- **common.sh**: Shared functions for branch/path management
- **create-new-feature.sh**: Initialize feature branch and spec
- **setup-plan.sh**: Prepare implementation planning
- **check-task-prerequisites.sh**: Verify design artifacts exist
- **update-agent-context.sh**: Update AI assistant context files

### Development Principles

ALL development principles are defined in `/workspaces/ioun-ai/.specify/memory/constitution.md`.

The constitution supersedes all other practices and must be consulted for:
- Architecture decisions and patterns
- Testing requirements and gates
- Quality standards and constraints
- Workflow requirements
- Any exceptions or complexity justifications

Never proceed with implementation without verifying constitutional compliance.

**Note**: When updating the constitution, the `/workspaces/ioun-ai/.specify/memory/constitution_update_checklist.md` MUST be followed to ensure all dependent documents are updated.

### Git Operations (CRITICAL)

**NO automatic Git operations without user approval.** This includes:
- Branch creation, switching, or deletion
- Commits and commit messages
- Pushes, pulls, and merges
- Any modifications to Git history

When Git operations are needed:
1. Always ask the user for explicit approval first
2. For branch creation, ask how they want it formatted/named
3. Never assume permission for Git operations
4. SDD functions and scripts must not perform Git operations autonomously

## Working with Features

When implementing features:
1. Always work from feature branches (###-feature-name format)
2. Follow TDD: Write tests → Get approval → Fail tests → Implement
3. Each contract requires a test, each entity needs a model
4. Use parallel execution markers [P] for independent tasks
5. All paths must be absolute from repository root

## Testing Approach

Check feature-specific quickstart.md and contracts/ directory for:
- Contract tests (one per endpoint)
- Integration test scenarios (from user stories)
- Validation requirements

No standard test framework is assumed - check each feature's plan.md for tech stack decisions.