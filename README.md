# Specification-Driven Development (SDD) Agent Framework

A constitutional AI development framework that enforces specification-driven development through intelligent agent orchestration and workflow automation.

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

### 1. Fork or Copy Repository

```bash
# Clone this framework for your new project
git clone [framework-repo] your-project-name
cd your-project-name

# Remove existing git history to start fresh
rm -rf .git
git init
git add .
git commit -m "Initial commit from SDD framework"
```

### 2. Configure Project Constitution

The constitution (`/.specify/memory/constitution.md`) defines your project's development principles. Review and adjust:

- **Article I**: Library-First Development approach
- **Article II**: CLI Interface standards
- **Article III**: Test-First Development requirements
- **Article IV**: Integration Testing gates
- **Article V**: Observability standards
- **Article VI**: Versioning strategy
- **Article VII**: Simplicity constraints

⚠️ **Important**: When updating the constitution, follow `/.specify/memory/constitution_update_checklist.md`

### 3. Set Up MCP Integrations

Model Context Protocol (MCP) servers extend Claude's capabilities. Configure based on your project needs:

#### Required MCP Servers

1. **File System Access** (usually pre-configured)
   - Enables file read/write operations
   - Required for all framework operations

2. **Project-Specific MCPs**
   ```json
   // Example MCP configuration structure
   {
     "mcpServers": {
       "your-service": {
         "command": "npx",
         "args": ["-y", "@your-org/mcp-server"],
         "env": {
           "API_KEY": "env:YOUR_API_KEY"
         }
       }
     }
   }
   ```

#### Common MCP Integrations

- **Database**: For schema management and migrations (e.g., `mcp__supabase`)
- **Cloud Providers**: AWS, GCP, Azure for deployment
- **Documentation**: API docs, knowledge bases (e.g., `mcp__ref-tools`)
- **IDE Integration**: Code execution and diagnostics (e.g., `mcp__ide`)
- **Browser Control**: Web automation and testing (e.g., `mcp__browsermcp`)
- **Search & AI**: Enhanced search and AI capabilities (e.g., `mcp__perplexity`)
- **Context Management**: Code indexing and search (e.g., `mcp__claude-context`)

#### Department-Specific MCP Access

Each department gets appropriate MCP servers:
- **Architecture**: Documentation, search, analysis tools
- **Engineering**: IDE, database, browser automation
- **Quality**: Test execution, diagnostics
- **Data**: Database management, migrations
- **Product**: Documentation, browser, search
- **Operations**: Deployment, logging, infrastructure

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

## 📚 Core Commands

### Feature Development

1. **`/specify`** - Create feature specification
   - Generates structured spec document
   - Optionally creates feature branch
   - Output: `specs/###-feature-name/spec.md`

2. **`/plan`** - Generate implementation plan
   - Creates technical design documents
   - Produces contracts and data models
   - Output: Full design artifact set

3. **`/tasks`** - Generate task list
   - Creates ordered implementation tasks
   - Marks parallel-executable items
   - Output: `specs/###-feature-name/tasks.md`

### Agent Management

**`/create-agent`** - Create specialized agent
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

#### Departments and Their Capabilities

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
│   │   ├── constitution.md  # Development principles
│   │   ├── constitution_update_checklist.md
│   │   ├── agent-governance.md  # Agent compliance rules
│   │   └── agent-collaboration.md  # Collaboration patterns
│   ├── scripts/bash/        # Automation scripts
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

---

**Remember**: The constitution is your north star. When in doubt, consult `/.specify/memory/constitution.md` for guidance.