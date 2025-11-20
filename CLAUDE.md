# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CRITICAL: Read Constitution First

**ALWAYS read `.specify/memory/constitution.md` BEFORE starting any work.**

The constitution (v1.5.0) contains **14 enforceable principles**:
- **3 Immutable Principles** (I-III): Library-First, Test-First, Contract-First
- **6 Quality & Safety Principles** (IV-IX): Idempotency, Progressive Enhancement, Git Approval, Observability, Documentation Sync, Dependency Management
- **5 Workflow & Delegation Principles** (X-XIV): Agent Delegation, Input Validation, Design System, Access Control, AI Model Selection

The constitution is the SINGLE SOURCE OF TRUTH for:
- Core development principles and rules
- Workflow requirements and gates
- Quality standards and constraints
- All architectural decisions
- Agent delegation protocol

### Work Session Initiation Protocol (MANDATORY)

Every task must follow these 4 steps:
1. **READ CONSTITUTION** - First action, no exceptions
2. **ANALYZE TASK DOMAIN** - Identify trigger keywords
3. **DELEGATION DECISION** - Delegate if specialized work
4. **EXECUTION** - Execute directly or via specialized agent

No work should proceed without first understanding and applying the constitution's principles. All features, code, and decisions must comply with constitutional requirements.

## Project Overview

This is a specification-driven development framework that uses structured templates and workflows to generate and implement features. The project uses a TDD approach with contract-first design patterns as defined in the constitution.

## Commands

### Product Requirements (Phase 0)

**Create Product Requirements Document**: Use `/create-prd` command
   - **AGENT**: Executed by prd-specialist (auto-delegated per Principle X)
   - **PURPOSE**: Establishes Single Source of Truth (SSOT) for entire project
   - Creates comprehensive PRD at `.docs/prd/prd.md`
   - Script: `.specify/scripts/bash/create-prd.sh [project_name]`
   - **INTEGRATED**: Part of `init-project.sh` workflow
   - **Outputs**:
     - Product vision, goals, and success metrics
     - User personas and journeys
     - Core features and requirements with acceptance criteria
     - Constitutional customizations (all 14 principles)
     - Technical constraints and integration requirements
     - Release strategy and MVP definition
     - Custom agent planning
     - Quick reference guide
   - **Workflow Integration**:
     - `/specify` → References PRD for user stories, personas, acceptance criteria
     - `/plan` → References PRD for technical constraints, architecture principles
     - Constitution → Updated with project-specific guidance from PRD
     - Custom agents → Created based on needs identified in PRD
   - **When to Use**:
     - Starting a new project (first step before any features)
     - Establishing product foundation and strategy
     - Defining framework customizations for your context
     - Aligning stakeholders on vision and priorities
   - **Usage**:
     ```bash
     /create-prd                # Interactive mode
     /create-prd MyProject      # With project name
     ```

### Feature Specification Workflow

1. **Create feature specification**: Use `/specify` command
   - **AGENT**: Executed by specification-agent (auto-delegated per Principle X)
   - **REQUIRES USER APPROVAL**: Will ask if you want a new feature branch created
   - If approved, will ask for desired branch format/name
   - Default format when approved: `###-feature-name`
   - Generates spec file at `specs/###-feature-name/spec.md`
   - Script: `.specify/scripts/bash/create-new-feature.sh --json "$ARGUMENTS"`
   - **DS-STAR Enhancement**: Automatically invokes refinement loop after spec generation
     - Verifies specification quality against thresholds (completeness ≥0.90)
     - Iteratively refines until sufficient or max 20 rounds
     - Provides actionable feedback for improvements
     - Escalates to human if quality threshold not met

2. **Generate implementation plan**: Use `/plan` command
   - **AGENT**: Executed by planning-agent (auto-delegated per Principle X)
   - Reads feature spec and constitution
   - Generates research, data models, contracts, and quickstart docs
   - Script: `.specify/scripts/bash/setup-plan.sh --json`
   - Stops before task generation
   - **DS-STAR Enhancement**: Automatically invokes verification gate after plan generation
     - Verifies plan quality against thresholds (completeness ≥0.85, spec alignment ≥0.90)
     - Blocks progression to `/tasks` if quality insufficient
     - Provides actionable feedback for improvements
     - MUST address feedback before proceeding

3. **Generate tasks**: Use `/tasks` command
   - **AGENT**: Executed by tasks-agent (auto-delegated per Principle X)
   - Creates dependency-ordered task list from design artifacts
   - Script: `.specify/scripts/bash/check-task-prerequisites.sh --json`
   - Marks parallel-executable tasks with [P]

4. **Validate compliance**: Use `/finalize` command (NEW - DS-STAR Enhancement)
   - **PURPOSE**: Pre-commit constitutional compliance validation
   - Validates all 14 constitutional principles before git operations
   - Script: `.specify/scripts/bash/finalize-feature.sh --json`
   - **CRITICAL**: NEVER performs git operations autonomously (Principle VI)
   - Checks performed:
     - Tests passing and coverage >80%
     - No linting errors
     - Code style compliance (black, isort)
     - Documentation synchronized (CLAUDE.md, README, specs, API docs)
     - No secrets in code (.env templates updated)
     - Constitutional compliance across all principles
   - Output: Compliance report with pass/fail status
   - Suggests manual git commands for user execution
   - **Usage Pattern**:
     ```bash
     # After implementation complete
     ./.specify/scripts/bash/finalize-feature.sh

     # If all checks pass, manually execute suggested git commands
     git add <files>
     git commit -m "message"
     git push origin <branch>
     ```

### Agent Management Commands

1. **Create new agent**: Use `/create-agent` command
   - **AGENT**: Executed by subagent-architect (auto-delegated per Principle X)
   - Creates specialized subagent with constitutional compliance
   - Auto-determines department based on purpose
   - Sets appropriate tool restrictions
   - Initializes memory structure
   - Script: `.specify/scripts/bash/create-agent.sh --json`
   - Example: `/create-agent backend-engineer "API and database specialist"`

### Agent Delegation Protocol

**Constitutional Principle X** requires specialized work be delegated to specialized agents.

See `.specify/memory/agent-collaboration-triggers.md` for:
- Domain trigger keywords (Frontend, Backend, Database, Testing, Security, Performance, DevOps, etc.)
- Single-agent vs multi-agent decision tree
- Context handoff format
- 13 specialized agents across 6 departments

**Quick Reference**: If task contains domain keywords (test, UI, database, API, security, etc.) → Delegate to specialized agent

## Key Architecture

### Directory Structure
```
.specify/
├── memory/
│   ├── constitution.md                    # Core principles (v1.5.0 - 14 principles)
│   ├── constitution_update_checklist.md   # Mandatory change management
│   └── agent-collaboration-triggers.md    # Agent delegation reference
├── scripts/bash/                          # Workflow automation scripts
│   ├── common.sh                          # Shared functions + git approval
│   ├── constitutional-check.sh            # 14-principle compliance validator
│   ├── sanitization-audit.sh              # Framework sanitization checker
│   ├── create-new-feature.sh              # Feature initialization + refinement
│   ├── setup-plan.sh                      # Planning workflow + verification
│   ├── check-task-prerequisites.sh        # Task generation validator
│   └── finalize-feature.sh                # Pre-commit compliance validation (NEW)
├── templates/                             # Document templates
│   ├── spec-template.md                   # Feature specification
│   ├── plan-template.md                   # Implementation plan (9-step)
│   ├── tasks-template.md                  # Task list generation
│   └── agent-file-template.md             # New agent template
├── config/                                # Configuration files (NEW - DS-STAR)
│   └── refinement.conf                    # Refinement engine settings

src/sdd/                                    # DS-STAR agent libraries (NEW)
├── agents/
│   ├── quality/
│   │   ├── verifier.py                    # Quality gate verification
│   │   └── finalizer.py                   # Pre-commit compliance
│   ├── architecture/
│   │   ├── router.py                      # Intelligent agent routing
│   │   └── context_analyzer.py            # Codebase intelligence
│   └── engineering/
│       └── autodebug.py                   # Automatic error repair
├── refinement/
│   ├── engine.py                          # Iterative refinement loop
│   └── models.py                          # Refinement state models
├── feedback/                              # Feedback accumulation
├── context/                               # Context intelligence
└── metrics/                               # Performance metrics

.docs/agents/                              # Agent decision logs and state (NEW)
├── quality/verifier/decisions/            # Verification decisions
├── architecture/router/decisions/         # Routing decisions
└── shared/
    ├── refinement-state/                  # Iteration state persistence
    └── context-summaries/                 # Codebase context summaries

specs/###-feature-name/                     # Per-feature documentation
├── spec.md                                # Feature requirements
├── plan.md                                # Technical approach
├── research.md                            # Technical decisions
├── data-model.md                          # Entity definitions
├── contracts/                             # API contracts
├── quickstart.md                          # Test scenarios
└── tasks.md                               # Implementation tasks
```

### Workflow Scripts

- **common.sh**: Shared functions for branch/path management, git approval
- **create-new-feature.sh**: Initialize feature branch and spec + DS-STAR refinement loop
- **setup-plan.sh**: Prepare implementation planning + DS-STAR verification gate
- **check-task-prerequisites.sh**: Verify design artifacts exist
- **finalize-feature.sh**: Pre-commit compliance validation (no auto-git)
- **update-agent-context.sh**: Update AI assistant context files

### Validation Scripts

- **constitutional-check.sh**: Automated compliance checking for all 14 principles
- **sanitization-audit.sh**: Verifies framework sanitization (no project-specific elements)

Run before commits and releases:
```bash
./.specify/scripts/bash/constitutional-check.sh
./.specify/scripts/bash/sanitization-audit.sh
```

### Development Principles

ALL development principles are defined in `.specify/memory/constitution.md`.

The constitution supersedes all other practices and must be consulted for:
- Architecture decisions and patterns
- Testing requirements and gates
- Quality standards and constraints
- Workflow requirements
- Any exceptions or complexity justifications

Never proceed with implementation without verifying constitutional compliance.

**Note**: When updating the constitution, the `.specify/memory/constitution_update_checklist.md` MUST be followed to ensure all dependent documents are updated.

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

**DS-STAR Enhancement Note**: The `/finalize` command validates compliance but NEVER executes git commands. It provides a report and suggests commands for manual execution.

## Working with Features

When implementing features:
1. Always work from feature branches (###-feature-name format)
2. Follow TDD: Write tests → Get approval → Fail tests → Implement
3. Each contract requires a test, each entity needs a model
4. Use parallel execution markers [P] for independent tasks
5. All paths must be absolute from repository root
6. **NEW**: Use `/finalize` to validate compliance before committing

## Testing Approach

Check feature-specific quickstart.md and contracts/ directory for:
- Contract tests (one per endpoint)
- Integration test scenarios (from user stories)
- Validation requirements

No standard test framework is assumed - check each feature's plan.md for tech stack decisions.

## DS-STAR Multi-Agent Enhancements (Feature 001)

The framework now includes proven multi-agent patterns from Google's DS-STAR system:

### Quality Gates
- **Automatic Verification**: Specs and plans automatically verified for quality
- **Iterative Refinement**: Specs refined up to 20 rounds until quality thresholds met
- **Blocking Gates**: Insufficient plans block progression to tasks phase
- **Actionable Feedback**: Clear guidance provided for improvements

### Configuration
Quality thresholds and behavior configured in `.specify/config/refinement.conf`:
- `MAX_REFINEMENT_ROUNDS=20` - Maximum iterations before escalation
- `EARLY_STOP_THRESHOLD=0.95` - Stop if quality exceeds this
- `SPEC_COMPLETENESS_THRESHOLD=0.90` - Specification quality requirement
- `PLAN_QUALITY_THRESHOLD=0.85` - Plan quality requirement
- `TEST_COVERAGE_THRESHOLD=0.80` - Code coverage requirement (matches Principle II)

### Graceful Degradation
If DS-STAR components unavailable (Python not installed, dependencies missing):
- Workflow continues without quality gates
- Warning messages displayed
- Manual review recommended
- No workflow blocking

### Performance Targets
- Context retrieval: <2 seconds
- Debug iteration cycle: <30 seconds
- 3.5x improvement in task completion accuracy (target)
- >70% automatic fix rate for common errors (target)

## Available Agents

The following specialized agents are available for specific tasks:

### prd-specialist (product)

**Purpose**: Product Requirements Document (PRD) creation specialist for the /create-prd command (Phase 0 - Project Initialization). Expert in product strategy, user research, requirements gathering, business-technical alignment, and constitutional customization. Creates comprehensive PRDs that serve as Single Source of Truth (SSOT) for all project specifications, agent configurations, and framework customizations. Core competencies include: (1) Discovery & Vision Alignment - stakeholder interviews, vision validation, problem-solution fit, success definition, scope boundaries; (2) User Research & Persona Development - realistic persona creation, user journey mapping, pain point analysis, behavioral patterns, opportunity identification; (3) Requirements Definition & Structuring - feature categorization, user story writing, acceptance criteria definition, dependency mapping, priority assignment, constraint documentation; (4) Constitutional Customization - review and customize all 14 constitutional principles for project context, document exceptions with justification, define project-specific quality thresholds, map compliance requirements; (5) Technical Context & Constraints - define high-level boundaries without prescribing implementation, document required/prohibited technologies, performance/security/compliance requirements, integration constraints, scalability expectations; (6) Release Strategy & Phasing - MVP definition, feature phasing, timeline recommendations, success criteria, risk assessment; (7) Agent & Workflow Planning - identify specialized agents needed, define PRD integration with /specify and /plan commands, create SSOT reference mapping. Operates as Phase 0 in the SDD workflow pipeline, before specification-agent. Responsible for complete PRD creation including vision/goals/metrics, personas/journeys, features/requirements, constitutional guidance, technical constraints, release strategy, and agent planning. Must ensure PRD serves as authoritative reference for all downstream specification and planning work.

**Usage**: `Use the prd-specialist agent to...`

**Triggers**: Automatically invoked by /create-prd command. See `.specify/memory/agent-collaboration.md` for automatic triggers.

---

### planning-agent (product)

**Purpose**: Implementation planning specialist for the /plan command workflow phase. Expert in technical research, library evaluation, API contract design, data modeling, test scenario planning, and constitutional compliance validation. Translates feature specifications into executable implementation plans with research.md, data-model.md, contracts/, and quickstart.md artifacts. Core competencies include: (1) Phase 0 Research - technology stack selection, library/framework evaluation, best practices research, dependency analysis, pattern recommendations, resolving technical unknowns; (2) Phase 1 Design - API contract design using OpenAPI/GraphQL schemas, REST/GraphQL endpoint architecture, data entity modeling with fields/relationships/validation, contract test generation following TDD, integration test scenario extraction from user stories, project structure decisions for single/web/mobile applications; (3) Constitutional Validation - enforcing Library-First/Test-First/Contract-First principles, pre-research and post-design compliance checks, complexity tracking and justification documentation; (4) Quality Gates - validate all unknowns resolved before design phase, ensure contracts precede implementation, generate failing tests first, document architecture decisions with rationale and alternatives. Operates as Phase 2 in the SDD workflow pipeline between specification-agent (Phase 1) and tasks-agent (Phase 3). Responsible for the complete /plan command execution including Technical Context analysis, Constitution Check gates, research.md consolidation, contract schema generation, data model creation, quickstart test scenarios, and readiness validation for task generation phase. Must maintain audit trails, validate against 14 constitutional principles, and prepare comprehensive implementation plans optimized for AI agent execution.

**Usage**: `Use the planning-agent agent to...`

**Triggers**: See `.specify/memory/agent-collaboration.md` for automatic triggers

---

