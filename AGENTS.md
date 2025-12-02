# SDD Framework Agent Registry

**Version**: 2.0.0
**Last Updated**: 2025-11-29
**Constitution**: v1.6.0 (15 Principles)
**Total Agents**: 14
**Departments**: 6

---

## Purpose

This file is the **Single Source of Truth (SSOT)** for agent information in the SDD Framework. It provides quick reference for agent selection, capabilities, and usage patterns.

**Relationship to CLAUDE.md**:
- `CLAUDE.md` → Workflow rules, compliance protocols, delegation triggers
- `AGENTS.md` → Agent registry, capabilities, selection guidance

**Both files MUST be updated together** when agents are added/modified (see Tandem Update Rules below).

---

## Agent Overview by Department

### Product Department (5 agents)
Specification, planning, and task management

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **prd-specialist** | PRD creation, product strategy | opus | Read, Write, Edit, Grep, Glob, AskUserQuestion, TodoWrite |
| **specification-agent** | Feature specs, user stories | opus | Read, Write, Bash, MultiEdit |
| **planning-agent** | Implementation planning, /plan command | opus | Read, Write, Bash, MultiEdit |
| **tasks-agent** | Task decomposition, /tasks command | opus | Read, Write, Bash, MultiEdit |
| **task-orchestrator** | Multi-agent coordination | opus | Task, Read, Grep, Glob, TodoWrite, Bash |

### Architecture Department (2 agents)
System design and agent architecture

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **subagent-architect** | Agent creation, SDD compliance | inherit | Read, Write, Edit, MultiEdit, Bash, Grep, Glob, TodoWrite |
| **backend-architect** | API design, system architecture | opus | Read, Write, Bash, MultiEdit |

### Engineering Department (2 agents)
Code development and implementation

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **frontend-specialist** | React/Next.js, UI development | opus | Read, Write, Bash, MultiEdit |
| **full-stack-developer** | End-to-end feature implementation | opus | Read, Write, Bash, MultiEdit |

### Quality Department (2 agents)
Testing and security

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **testing-specialist** | Test planning, TDD, QA | opus | Read, Write, Bash, MultiEdit |
| **security-specialist** | Security reviews, vulnerability assessment | opus | Read, Write, Bash, MultiEdit |

### Operations Department (2 agents)
Deployment and performance

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **devops-engineer** | CI/CD, Docker, cloud deployment | opus | Read, Write, Bash, MultiEdit |
| **performance-engineer** | Performance analysis, optimization | opus | Read, Write, Bash, MultiEdit |

### Data Department (1 agent)
Database and data management

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| **database-specialist** | Schema design, query optimization | opus | Read, Write, Bash, MultiEdit |

---

## Domain → Agent Mapping

Quick reference for agent selection based on task domain:

| Domain | Keywords | Primary Agent | Backup Agent |
|--------|----------|---------------|--------------|
| **PRD/Product** | PRD, product, vision, personas | prd-specialist | - |
| **Specification** | spec, requirements, user story | specification-agent | prd-specialist |
| **Planning** | /plan, research, contracts | planning-agent | backend-architect |
| **Tasks** | /tasks, task list, breakdown | tasks-agent | planning-agent |
| **Frontend** | UI, React, CSS, component | frontend-specialist | full-stack-developer |
| **Backend** | API, endpoint, server, service | backend-architect | full-stack-developer |
| **Database** | schema, SQL, migration, query | database-specialist | backend-architect |
| **Testing** | test, TDD, coverage, QA | testing-specialist | - |
| **Security** | auth, encryption, vulnerability | security-specialist | backend-architect |
| **Performance** | optimize, cache, latency | performance-engineer | backend-architect |
| **DevOps** | deploy, CI/CD, Docker | devops-engineer | - |
| **Agent Creation** | create agent, new agent | subagent-architect | - |
| **Multi-Domain** | 2+ domains detected | task-orchestrator | - |

---

## Usage Patterns

### Automatic Delegation (Principle X)

Agents are automatically invoked based on:
1. **Keywords** in user request matching domain patterns
2. **Slash commands** triggering specific agents
3. **Multi-domain detection** requiring orchestration
4. **Constitutional requirements** mandating delegation

### Manual Invocation

```
Use the [agent-name] agent to [task description]
```

Examples:
```
Use the planning-agent to create an implementation plan for user authentication
Use the testing-specialist to design test coverage for the payment module
Use the task-orchestrator to coordinate the full-stack feature implementation
```

### Slash Command → Agent Mapping

| Command | Agent | Purpose |
|---------|-------|---------|
| `/create-prd` | prd-specialist | Create Product Requirements Document |
| `/specify` | specification-agent | Create feature specification |
| `/plan` | planning-agent | Generate implementation plan |
| `/tasks` | tasks-agent | Generate task list |
| `/create-agent` | subagent-architect | Create new agent |

---

## Agent Collaboration Workflows

### Feature Development Pipeline

```
prd-specialist (Phase 0)
       ↓
specification-agent (/specify)
       ↓
planning-agent (/plan)
       ↓
tasks-agent (/tasks)
       ↓
[Specialized agents for implementation]
       ↓
testing-specialist (validation)
       ↓
security-specialist (review)
       ↓
devops-engineer (deployment)
```

### Multi-Agent Orchestration

When task involves 2+ domains:

```
User Request
      ↓
task-orchestrator (analyzes & decomposes)
      ↓
┌─────────────────────────────────────┐
│ Parallel Agent Execution            │
│ • frontend-specialist (UI)          │
│ • backend-architect (API)           │
│ • database-specialist (Schema)      │
└─────────────────────────────────────┘
      ↓
task-orchestrator (coordinates & merges)
      ↓
Result
```

### Agent Creation

```
/create-agent request
       ↓
subagent-architect (MANDATORY)
       ↓
Creates:
• Agent definition (.claude/agents/[dept]/)
• Agent memory (.docs/agents/[dept]/[agent]/)
• Updates AGENTS.md
```

---

## Constitutional Compliance

All agents enforce Constitution v1.6.0 (15 Principles):

### Immutable Principles (I-III)
- **I: Library-First** - Features as standalone libraries
- **II: Test-First** - TDD mandatory, >80% coverage
- **III: Contract-First** - Define contracts before implementation

### Critical Principles
- **VI: Git Approval** - NO autonomous git operations
- **X: Agent Delegation** - Specialized work → specialized agents
- **XV: File Organization** - Verify before creating files

### All Agents Must
- Reference constitution in their system prompt
- Enforce TDD and library-first patterns
- Request approval for git operations
- Maintain audit trails
- Follow file organization rules

---

## Agent File Locations

```
.claude/agents/
├── architecture/
│   ├── backend-architect.md
│   └── subagent-architect.md
├── data/
│   └── database-specialist.md
├── engineering/
│   ├── frontend-specialist.md
│   └── full-stack-developer.md
├── operations/
│   ├── devops-engineer.md
│   └── performance-engineer.md
├── product/
│   ├── prd-specialist.md
│   ├── planning-agent.md
│   ├── specification-agent.md
│   ├── task-orchestrator.md
│   └── tasks-agent.md
└── quality/
    ├── security-specialist.md
    └── testing-specialist.md

.docs/agents/
└── [mirrors .claude/agents/ structure]
    └── [agent-name]/
        ├── context/
        ├── knowledge/
        ├── decisions/
        └── performance/
```

---

## Quick Decision Tree

```
Creating PRD/product vision? ──────────────→ prd-specialist
Creating feature specification? ───────────→ specification-agent
Planning implementation? ──────────────────→ planning-agent
Breaking down into tasks? ─────────────────→ tasks-agent
Building UI components? ───────────────────→ frontend-specialist
Designing APIs/services? ──────────────────→ backend-architect
Working with database? ────────────────────→ database-specialist
Writing tests? ────────────────────────────→ testing-specialist
Security concerns? ────────────────────────→ security-specialist
Performance issues? ───────────────────────→ performance-engineer
Deploying/CI-CD? ──────────────────────────→ devops-engineer
Creating new agent? ───────────────────────→ subagent-architect
Multiple domains (2+)? ────────────────────→ task-orchestrator
```

---

## Tandem Update Rules

**CRITICAL**: CLAUDE.md and AGENTS.md must be updated together.

### When to Update AGENTS.md

- [ ] New agent created
- [ ] Agent deleted or deprecated
- [ ] Agent purpose/capabilities changed
- [ ] Agent tools modified
- [ ] Agent model changed
- [ ] Department restructured
- [ ] Slash command → agent mapping changed

### When to Update CLAUDE.md

- [ ] Domain → agent mapping changed
- [ ] Delegation triggers modified
- [ ] Workflow rules changed
- [ ] Constitutional compliance requirements changed
- [ ] Pre-flight check updates

### Both Files Must Update

- [ ] Agent count changes
- [ ] New department added
- [ ] Constitutional version changes
- [ ] Agent delegation protocol changes

### Update Protocol

```
1. Update constitution (if needed)
2. Update CLAUDE.md delegation rules
3. Update AGENTS.md registry
4. Update agent file itself
5. Update agent memory structure
6. Run constitutional-check.sh
7. Verify cross-references
```

---

## MCP Server Access by Department

The framework uses **Docker MCP Toolkit** as the primary method for MCP access, providing 310+ containerized servers via dynamic discovery.

### Docker MCP Toolkit Tools (Available to All Agents)

| Tool | Purpose |
|------|---------|
| `mcp-find` | Search 310+ servers in Docker catalog |
| `mcp-add` | Add server to current session dynamically |
| `mcp-config-set` | Configure server credentials |
| `mcp-exec` | Execute tools from any enabled server |
| `code-mode` | Combine multiple MCP tools in JavaScript |

### Department-Specific MCP Servers

| Department | Recommended Servers | Purpose |
|------------|---------------------|---------|
| Product | github-official, notion, linear | Project management, documentation |
| Architecture | aws/gcp/azure, postgres/supabase | Cloud, database design |
| Engineering | browsermcp, context7, github-official | Testing, docs, version control |
| Quality | browsermcp, playwright | E2E testing, browser automation |
| Data | supabase, postgres, firebase | Database operations |
| Operations | aws/gcp/azure, docker | Deployment, monitoring |

### MCP Access Pattern

Agents can dynamically add MCPs during task execution:
```
1. Use mcp-find to search for needed server
2. Use mcp-add to install server
3. Use mcp-exec to call server tools
```

**Fallback**: If server not in Docker catalog, add to `.mcp.json` with npx configuration.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2025-11-29 | Complete rewrite, added 5 product agents, updated to 14 total, constitution v1.6.0 |
| 1.0.0 | 2025-09-19 | Initial creation with 9 agents |

---

**Registry Maintainer**: subagent-architect
**Review Cycle**: On any agent change
**Cross-Reference**: CLAUDE.md, constitution.md, agent-collaboration-triggers.md
