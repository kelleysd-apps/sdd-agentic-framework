# Specification-Driven Development (SDD) Agent Framework

A constitutional AI development framework that enforces specification-driven development through intelligent agent orchestration and workflow automation.

## 🎖️ Attribution

This framework builds upon **[GitHub's spec-kit](https://github.com/github/spec-kit)**, which provides the core Specification-Driven Development (SDD) methodology. And is built using Claude code, if you plan to use other LLM's for this framework it will need to be tweaked a bit or just used as a reference to build your own. 

### Original SDD Framework
- **spec-kit by GitHub** - The foundational SDD approach, templates, and workflow automation
- Licensed under MIT License
- Original repository: https://github.com/github/spec-kit

### Extensions and Enhancements
This implementation extends spec-kit with:
- **Enhanced AI governance** - Constitutional principles and enforced quality gates
- **DS-STAR Multi-Agent System** - Google's proven pattern with 5 specialized agents:
  - Quality gates (VerificationAgent, FinalizerAgent) - Binary decisions at each workflow stage
  - Intelligent routing (RouterAgent) - Multi-agent orchestration with dependency graphs
  - Self-healing (AutoDebugAgent) - Automatic error repair with >70% fix rate target
  - Codebase intelligence (ContextAnalyzerAgent) - Semantic search with <2s retrieval
  - Constitutional validation - All 14 principles enforced before commits
- **Intelligent agent orchestration** - 13 specialized agents across 6 departments with MCP integration
- **Agent Skills system** - Progressive disclosure for procedural knowledge (30-50% context reduction)
- **Iterative refinement** - Up to 20 rounds with early stopping at 95% quality threshold
- **Governance policies** - 6 comprehensive policies (Testing, Security, Code Review, Deployment, Branching, Release)
- **Advanced workflow automation** - Validation scripts and command system
- **Memory and context management** - Persistent agent knowledge and collaboration patterns
- **Tool restriction framework** - Department-specific tool access control
- **Automatic documentation updates** - Self-maintaining CLAUDE.md and agent registry

---

## ⚠️ IMPORTANT: Project Initialization Instructions

**For New Projects Using This Framework:**

1. **Archive this README**:
   ```bash
   mv README.md FRAMEWORK_README.md
   ```

2. **Create your project's README**:
   ```bash
   # Create a new README.md for YOUR specific project
   echo "# Your Project Name" > README.md
   echo "" >> README.md
   echo "Description of your specific project..." >> README.md
   ```

3. **Keep the framework documentation**:
   - This framework guide will be moved to `FRAMEWORK_README.md`
   - Reference it when needed for framework features
   - Your new `README.md` should document YOUR project, not the framework

---

## 🎯 Framework Overview

This framework provides a structured approach to software development where:
- **Specifications drive implementation** - Every feature starts with a detailed specification
- **Constitutional compliance is mandatory** - All code adheres to project constitution principles
- **Agents handle specialized tasks** - Department-specific agents manage different aspects
- **Workflows are automated** - Scripts orchestrate the development lifecycle
- **Quality gates are enforced** - TDD and integration testing are non-negotiable

## 🚀 Quick Start for New Projects

### Prerequisites

- **Claude Code** (REQUIRED) - [Install first](https://claude.ai/code)
- **Node.js** v18+ and npm v9+
- **Git** - [Download](https://git-scm.com/)
- **Git Bash** (Windows users) - Included with Git for Windows

**🪟 Windows Users**: See [WINDOWS_SETUP.md](./WINDOWS_SETUP.md) for detailed Windows-specific setup instructions. You MUST use Git Bash, not PowerShell or CMD.

---

### 1. Fork or Copy Repository

```bash
# Option A: Clone and use init script (RECOMMENDED)
git clone https://github.com/kelleysd-apps/sdd-agentic-framework.git your-project-name
cd your-project-name
rm -rf .git
bash init-project.sh  # Interactive setup script

# Option B: Manual setup
git clone https://github.com/kelleysd-apps/sdd-agentic-framework.git your-project-name
cd your-project-name
rm -rf .git
git init
npm run setup          # macOS/Linux
npm run setup:windows  # Windows (Git Bash)
```

**Note for Windows users**: Always use Git Bash terminal, not PowerShell or CMD.

### 2. Configure Project Constitution

The constitution (`/.specify/memory/constitution.md` v1.5.0) defines your project's 14 enforceable principles:

**Core Immutable Principles** (I-III):
- **Principle I**: Library-First Architecture
- **Principle II**: Test-First Development (TDD)
- **Principle III**: Contract-First Design

**Quality & Safety Principles** (IV-IX):
- **Principle IV**: Idempotent Operations
- **Principle V**: Progressive Enhancement
- **Principle VI**: Git Operation Approval (CRITICAL)
- **Principle VII**: Observability and Structured Logging
- **Principle VIII**: Documentation Synchronization
- **Principle IX**: Dependency Management

**Workflow & Delegation Principles** (X-XIV):
- **Principle X**: Agent Delegation Protocol (CRITICAL)
- **Principle XI**: Input Validation and Output Sanitization
- **Principle XII**: Design System Compliance
- **Principle XIII**: Feature Access Control
- **Principle XIV**: AI Model Selection Protocol

⚠️ **Important**: When updating the constitution, follow `/.specify/memory/constitution_update_checklist.md`

### Validation Scripts

Run before commits and releases:
```bash
# Check constitutional compliance (all 14 principles)
./.specify/scripts/bash/constitutional-check.sh

# Verify framework sanitization
./.specify/scripts/bash/sanitization-audit.sh
```

### 3. Set Up MCP Integrations

Model Context Protocol (MCP) servers extend Claude's capabilities. The `/initialize-project` command will recommend MCPs based on your PRD, but you can also configure them manually.

#### Claude Helps with MCP Setup

Ask Claude to help you identify and configure MCPs:

```
"What MCP servers would benefit my project?"
"Help me install the supabase MCP server"
"Configure browser automation for E2E testing"
```

**Skill Reference**: `.claude/skills/integration/mcp-server-setup/SKILL.md`

#### Common MCP Servers by Category

| Category | MCP Server | Install Command | Purpose |
|----------|------------|-----------------|---------|
| **Database** | supabase | `npx -y @anthropic-ai/mcp-supabase` | PostgreSQL, Auth, Storage via Supabase |
| | postgres | `npx -y @anthropic-ai/mcp-postgres` | Direct PostgreSQL connections |
| | sqlite | `npx -y @anthropic-ai/mcp-sqlite` | Local SQLite databases |
| | firebase | `npx -y @anthropic-ai/mcp-firebase` | Firebase/Firestore projects |
| **Cloud** | aws | `npx -y @anthropic-ai/mcp-aws` | AWS services (S3, Lambda, etc.) |
| | gcp | `npx -y @anthropic-ai/mcp-gcp` | Google Cloud Platform |
| | azure | `npx -y @anthropic-ai/mcp-azure` | Microsoft Azure |
| | vercel | `npx -y @anthropic-ai/mcp-vercel` | Vercel deployment |
| **Testing** | browsermcp | `npx -y @anthropic-ai/mcp-browsermcp` | Browser automation, E2E testing |
| | playwright | `npx -y @anthropic-ai/mcp-playwright` | Playwright-based testing |
| **Search** | perplexity | `npx -y @anthropic-ai/mcp-perplexity` | AI-powered research |
| | context7 | `npx -y @anthropic-ai/mcp-context7` | Library documentation |
| **Projects** | github | `npx -y @anthropic-ai/mcp-github` | GitHub repos, issues, PRs |
| | linear | `npx -y @anthropic-ai/mcp-linear` | Linear project management |
| | notion | `npx -y @anthropic-ai/mcp-notion` | Notion workspaces |

#### MCP Configuration Example

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-supabase"],
      "env": {
        "SUPABASE_URL": "env:SUPABASE_URL",
        "SUPABASE_ANON_KEY": "env:SUPABASE_ANON_KEY"
      }
    }
  }
}
```

#### Department-Specific MCP Recommendations

| Department | Agents | Recommended MCPs |
|------------|--------|------------------|
| **Architecture** | backend-architect | aws/gcp/azure, postgres/supabase |
| **Engineering** | frontend-specialist, full-stack-developer | browsermcp, github, context7 |
| **Data** | database-specialist | postgres, supabase, firebase |
| **Quality** | testing-specialist, security-specialist | browsermcp, playwright |
| **Product** | specification-agent, planning-agent | github, notion, linear |
| **Operations** | devops-engineer, performance-engineer | aws/gcp/azure, docker |

### 4. Secrets Management

#### Environment Variables

1. Create `.env` file (already in .gitignore):
   ```bash
   # Service credentials
   DATABASE_URL=your-connection-string
   API_KEY=your-api-key

   # MCP tokens
   MCP_SERVICE_TOKEN=your-token
   ```

2. Create retrieval script (already in .gitignore):
   ```bash
   # retrieve-secrets.sh
   #!/bin/bash
   # Script to fetch secrets from your secret manager
   # Example: aws secretsmanager get-secret-value...
   ```

#### Best Practices

- **Never commit secrets** - Use .gitignore religiously
- **Use secret managers** - AWS Secrets Manager, HashiCorp Vault, etc.
- **Rotate regularly** - Implement secret rotation policies
- **Limit scope** - Use least-privilege access principles
- **Audit access** - Log and monitor secret usage

## 🎨 Agent Skills System

The framework includes an **Agent Skills** system that provides procedural "how-to" knowledge in addition to agent delegation. Skills use progressive disclosure (load only what's needed) for significant context efficiency.

### Skills vs Agents

- **Agents** (Delegation Layer): Handle specialized work autonomously, coordinate workflows, invoke other agents
- **Skills** (Capability Layer): Provide step-by-step procedural guidance, reference agents for delegation

### Core Skills Included

**SDD Workflow Skills**:
- `sdd-specification` - `/specify` command procedure
- `sdd-planning` - `/plan` command procedure
- `sdd-tasks` - `/tasks` command procedure

**Validation Skills**:
- `constitutional-compliance` - Validate all 14 constitutional principles
- `domain-detection` - Identify domains and suggest appropriate agents

### Creating Custom Skills

Users can create custom skills without modifying the framework:

```bash
# Create skill directory
mkdir -p .claude/skills/{category}/{skill-name}

# Create SKILL.md with YAML frontmatter
cat > .claude/skills/{category}/{skill-name}/SKILL.md <<'EOF'
---
name: skill-name
description: What it does and when to use it (max 1024 chars)
allowed-tools: Read, Write, Bash
---

# Skill Name

## When to Use
[Trigger conditions]

## Procedure
1. Step 1
2. Step 2
...
EOF
```

See `.specify/templates/skill-template.md` for complete skill creation guide.

## 📋 Governance Policies

The framework includes 6 comprehensive policies establishing standards for all development activities:

1. **Testing Policy** - TDD enforcement (Principle II - IMMUTABLE), testing pyramid, coverage requirements
2. **Security Policy** - OWASP Top 10 mitigations, input validation, output sanitization (Principle XI)
3. **Code Review Policy** - Constitutional compliance checklist, review process, quality gates
4. **Deployment Policy** - Zero-downtime deployments, rollback procedures, feature flags
5. **Branching Strategy Policy** - Git workflows, branch naming, Principle VI compliance
6. **Release Management Policy** - Semantic versioning, release workflow, deprecation policy

All policies located in `.docs/policies/` and aligned with Constitution v1.5.0.

## 📚 Core Commands

### Feature Development

1. **`/specify`** - Create feature specification
   - **Agent**: specification-agent (auto-delegated)
   - Generates structured spec document
   - Optionally creates feature branch
   - Output: `specs/###-feature-name/spec.md`

2. **`/plan`** - Generate implementation plan
   - **Agent**: planning-agent (auto-delegated)
   - Creates technical design documents
   - Produces contracts and data models
   - Output: Full design artifact set

3. **`/tasks`** - Generate task list
   - **Agent**: tasks-agent (auto-delegated)
   - Creates ordered implementation tasks
   - Marks parallel-executable items
   - Output: `specs/###-feature-name/tasks.md`

### Agent Management

**`/create-agent`** - Create specialized agent
- **Agent**: subagent-architect (auto-delegated)
```bash
/create-agent agent-name "Agent purpose and capabilities"
```

#### Agent Creation Features

When creating an agent, the system automatically:
- **Assigns to appropriate department** based on purpose keywords
- **Configures tool access** specific to department needs
- **Sets up MCP server access** for department-relevant services
- **Creates memory structure** for context and knowledge persistence
- **Updates documentation** in CLAUDE.md
- **Registers in agent registry** for tracking and management
- **Configures collaboration triggers** for automatic invocation

#### Example Departments and Their Capabilities

- **Architecture**: System design and planning
  - Tools: Read, Grep, Glob, WebSearch, TodoWrite
  - MCP: Documentation, search, and analysis servers

- **Engineering**: Code development
  - Tools: Full development suite including Write, Edit, Bash
  - MCP: IDE, database, browser, and documentation servers

- **Quality**: Testing and review
  - Tools: Read, analysis, and testing tools
  - MCP: Test execution and diagnostics servers

- **Data**: Database and analytics
  - Tools: Database and data manipulation tools
  - MCP: Database management and migration servers

- **Product**: Requirements and UX
  - Tools: Documentation and search tools
  - MCP: Documentation, browser, and search servers

- **Operations**: Deployment and monitoring
  - Tools: Deployment and monitoring tools
  - MCP: Deployment, logging, and infrastructure servers

## 🏗️ Project Structure

```
your-project/
├── .specify/                 # Framework core
│   ├── memory/              # Constitutional documents
│   │   ├── constitution.md  # 14 development principles (v1.5.0)
│   │   ├── constitution_update_checklist.md  # Change management
│   │   ├── agent-collaboration-triggers.md   # Agent delegation reference
│   │   ├── agent-governance.md  # Agent compliance rules
│   │   └── agent-collaboration.md  # Collaboration patterns
│   ├── scripts/bash/        # Automation scripts
│   │   ├── common.sh        # Shared functions + git approval
│   │   ├── constitutional-check.sh  # 14-principle validator
│   │   ├── sanitization-audit.sh    # Framework sanitization
│   │   ├── create-agent.sh  # Agent creation with auto-updates
│   │   └── ...
│   └── templates/           # Document templates
│       ├── agent-template.md  # Agent definition template
│       └── ...
│
├── .claude/                 # AI assistant configuration
│   ├── agents/             # Agent definitions by department
│   │   ├── architecture/
│   │   ├── engineering/
│   │   ├── quality/
│   │   ├── data/
│   │   ├── product/
│   │   └── operations/
│   └── commands/           # Command documentation
│
├── .docs/                   # Project documentation
│   ├── agents/             # Agent memory/context
│   │   ├── agent-registry.json  # Central agent registry
│   │   ├── audit/          # Creation and operation logs
│   │   └── {department}/   # Department agent memories
│   │       └── {agent}/
│   │           ├── context/
│   │           ├── knowledge/
│   │           ├── decisions/
│   │           └── performance/
│   └── policies/           # Operational policies
│
├── specs/                   # Feature specifications
│   └── ###-feature-name/   # Per-feature artifacts
│       ├── spec.md         # Requirements
│       ├── plan.md         # Technical approach
│       ├── research.md     # Decisions
│       ├── data-model.md   # Entities
│       ├── contracts/      # API specs
│       ├── quickstart.md   # Test guide
│       └── tasks.md        # Implementation
│
├── CLAUDE.md               # AI assistant instructions (auto-updated)
├── .env                    # Local secrets (gitignored)
└── retrieve-secrets.sh     # Secret fetching (gitignored)
```

## 🤖 Agent Collaboration

### Automatic Agent Invocation

Claude Code automatically uses specialized agents based on:

1. **Keyword Triggers** - Task keywords match department patterns
2. **Workflow Stage** - Specific stages require specialized agents
3. **Complexity** - Multi-faceted tasks trigger agent teams
4. **User Preference** - Explicit agent requests

### Collaboration Patterns

#### Sequential Workflow
```
Product Agent → Architecture Agent → Engineering Agent → Quality Agent → Operations Agent
```

#### Parallel Execution
```
[Parallel]
├── Engineering Agent A (API)
├── Engineering Agent B (Frontend)
└── Data Agent (Database)
```

#### Review Pattern
```
Engineering Agent → [Parallel Review: Architecture, Quality, Security]
```

### Agent Communication

- **Shared Memory** - Agents share context through `.docs/agents/shared/`
- **Message Passing** - Structured JSON messages between agents
- **Audit Trail** - All interactions logged for transparency
- **Handoff Protocol** - Clear ownership transfer between agents

## 🔄 Development Workflow

### Standard Feature Flow

1. **Specification Phase**
   ```bash
   /specify "User authentication system"
   # Creates spec, optionally branches
   ```

2. **Planning Phase**
   ```bash
   /plan
   # Generates design artifacts
   ```

3. **Task Generation**
   ```bash
   /tasks
   # Creates implementation checklist
   ```

4. **Implementation with Agents**
   - Agents automatically triggered based on task type
   - Follow TDD approach
   - Write tests first
   - Implement features
   - Verify with integration tests

### Git Operations

⚠️ **No automatic git operations without approval**

The framework will:
- Ask before creating branches
- Request approval for commits
- Confirm before any git operations

## 🛠️ Customization Guide

### Adapting Templates

Modify templates in `.specify/templates/` for your domain:
- `spec-template.md` - Requirement structure
- `plan-template.md` - Design approach
- `tasks-template.md` - Task generation
- `agent-file-template.md` - Agent creation

### Adding New Commands

1. Create command file in `.claude/commands/`
2. Add script in `.specify/scripts/bash/`
3. Update CLAUDE.md with command documentation

### Extending Agent Capabilities

1. Use `/create-agent` to define new agents
2. System automatically:
   - Determines appropriate department
   - Configures tool and MCP access
   - Updates CLAUDE.md documentation
   - Creates agent registry entry
   - Sets up memory structure
   - Configures collaboration triggers
3. Agents inherit constitutional compliance
4. Tool restrictions based on department
5. Memory persists in `.docs/agents/{department}/{agent}/`

## 🔍 Troubleshooting

### Common Issues

**Claude Code update fails with ENOTEMPTY error**
```
npm error ENOTEMPTY: directory not empty, rename '.../claude-code' -> '.../.claude-code-XXXXX'
```

This happens when a previous update was interrupted, leaving stale temp directories.

**Quick fix:**
```bash
npm_prefix=$(npm config get prefix)
rm -rf "$npm_prefix/lib/node_modules/@anthropic-ai/.claude-code-"* 2>/dev/null
npm install -g @anthropic-ai/claude-code
```

**Permanent fix - add to ~/.bashrc or ~/.zshrc:**
```bash
# Claude Code update helper - cleans stale temp dirs before updating
update-claude-code() {
    local npm_prefix=$(npm config get prefix)
    rm -rf "$npm_prefix/lib/node_modules/@anthropic-ai/.claude-code-"* 2>/dev/null
    npm install -g @anthropic-ai/claude-code
}
```

Then use `update-claude-code` instead of `npm install -g @anthropic-ai/claude-code`.

---

**"Constitution not found"**
- Ensure `.specify/memory/constitution.md` exists
- Check file permissions

**"MCP server not responding"**
- Verify MCP configuration in Claude
- Check environment variables
- Validate service credentials

**"Agent creation failed"**
- Check agent name format (kebab-case)
- Verify no duplicate agents
- Review script permissions

### Debug Mode

Enable verbose logging:
```bash
export SDD_DEBUG=true
# Run commands to see detailed output
```

## 📖 Best Practices

### For New Projects

1. **Start with the constitution** - Define your principles first
2. **Configure MCPs early** - Set up integrations before coding
3. **Use agents liberally** - Specialized agents improve quality
4. **Follow the workflow** - Spec → Plan → Tasks → Implement
5. **Maintain documentation** - Keep CLAUDE.md current

### For Team Collaboration

1. **Share constitution** - Ensure team alignment
2. **Document MCPs** - List required integrations
3. **Standardize secrets** - Use consistent naming
4. **Review agent outputs** - Verify agent decisions
5. **Update templates** - Evolve with project needs

## 🚦 Quality Gates

The framework enforces:
- **Specification approval** before planning
- **Design review** before task generation
- **Test-first** development approach
- **Integration testing** for all features
- **Constitutional compliance** in all code

## 📝 License

This framework is provided as-is for use in your projects. Adapt and modify as needed for your specific requirements.

## 🤝 Contributing

To improve the framework:
1. Follow constitutional principles
2. Document all changes
3. Update affected templates
4. Test automation scripts
5. Update this README

## 🙏 Acknowledgments

This framework builds upon proven research and open-source foundations:

### DS-STAR Multi-Agent System
The DS-STAR enhancement (v2.0.0) integrates multi-agent patterns from MIT's research on sophisticated multi-agent orchestration systems. The quality gates, intelligent routing, and self-healing capabilities are adapted from proven patterns in academic research on autonomous agent coordination.

**Key Research Influences**:
- Binary quality decision gates (VerificationAgent, FinalizerAgent)
- Dependency graph execution planning (RouterAgent)
- Automatic error repair patterns (AutoDebugAgent)
- Semantic context retrieval (ContextAnalyzerAgent)
- Iterative refinement with feedback accumulation

### Foundation
- **spec-kit** by GitHub - Base specification-driven development patterns
- **Claude Code** by Anthropic - AI-assisted development platform
- **Model Context Protocol (MCP)** - AI integration architecture

### Community
Special thanks to the specification-driven development community and researchers advancing multi-agent systems for software engineering.

---

**Remember**: The constitution is your north star. When in doubt, consult `/.specify/memory/constitution.md` for guidance.
