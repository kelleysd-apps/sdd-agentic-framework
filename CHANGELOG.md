# Changelog

All notable changes to the SDD Agent Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-09-19

### Added
- **New Agents**
  - `testing-specialist` - Comprehensive QA and test automation specialist in quality department
  - `performance-engineer` - Performance analysis and optimization specialist in operations department

### Enhanced
- **Agent Creation Workflow**
  - Enforced constitutional requirement for subagent-architect delegation
  - Custom tool override capability for specific agent needs
  - Automatic department classification based on purpose keywords
  - Improved MCP access configuration per department

### Documentation
- Updated README.md with current agent inventory (9 agents across 5 departments)
- Added agent quick reference section
- Improved troubleshooting guide

## [1.1.0] - 2025-09-18

### Added
- **Core Agent Infrastructure**
  - Established 7 initial agents across 5 departments:
    - Architecture: `subagent-architect`, `backend-architect`
    - Engineering: `frontend-specialist`, `full-stack-developer`
    - Quality: `security-specialist`
    - Operations: `devops-engineer`
    - Data: `database-specialist`

- **Agent Management System**
  - Central agent registry (`/docs/agents/agent-registry.json`)
  - Audit logging for agent creation
  - Memory structure for agent context and knowledge
  - Department-based organization

- **Constitutional Framework**
  - Section X: Mandatory specialized agent delegation
  - Agent governance framework
  - Agent collaboration patterns
  - Department-specific tool and MCP access controls

### Enhanced
- **create-agent.sh Script**
  - Automated department assignment
  - Tool restriction by department
  - MCP server configuration
  - Registry and documentation auto-updates
  - Constitutional compliance validation

- **Workflow Automation**
  - `/create-agent` command with subagent-architect enforcement
  - Automatic CLAUDE.md updates
  - Agent file naming conventions
  - Memory structure initialization

### Changed
- **Git Operations Policy**
  - NO automatic git operations without explicit user approval
  - Branch creation requires user confirmation and naming preference
  - All commits, pushes, and merges need explicit permission

## [1.0.0] - 2025-09-17

### Initial Framework Release
- **Specification-Driven Development (SDD) Core**
  - Constitutional development principles
  - Library-First architecture mandate
  - Test-First Development (TDD) enforcement
  - Contract-driven integration patterns

- **Workflow Commands**
  - `/specify` - Feature specification creation
  - `/plan` - Implementation planning
  - `/tasks` - Task list generation
  - `/create-agent` - Agent creation (initial version)

- **Directory Structure**
  - `.specify/` - Framework core with templates and scripts
  - `.claude/` - AI assistant configuration
  - `.docs/` - Project documentation and policies
  - `specs/` - Feature specifications directory

- **Templates**
  - Feature specification template
  - Implementation plan template (9-step process)
  - Task list generation template
  - Agent file template

### Based On
- GitHub's spec-kit framework
- Extended with AI governance and agent orchestration
- Enhanced workflow automation and memory management

## Pre-1.0.0

### Foundation
- Initial commit from SDD framework base
- Basic directory structure setup
- Core constitutional principles established
- Initial templates and scripts

---

## Upgrade Guide

### From 1.1.0 to 1.2.0
1. No breaking changes
2. New agents available: `testing-specialist` and `performance-engineer`
3. Review updated agent collaboration patterns for optimal usage

### From 1.0.0 to 1.1.0
1. Review constitutional Section X for mandatory agent delegation
2. Update any custom scripts to use Task tool for agent invocation
3. Ensure all Git operations request user approval

## Future Roadmap

### Planned Features
- [ ] Agent performance metrics and optimization
- [ ] Cross-agent workflow templates
- [ ] Enhanced MCP integration patterns
- [ ] Agent capability evolution tracking
- [ ] Automated agent selection based on task analysis

### Under Consideration
- Product department agents
- Multi-agent orchestration improvements
- Agent learning and adaptation features
- Workflow visualization tools