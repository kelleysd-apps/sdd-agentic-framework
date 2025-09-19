# SDD Agentic Framework - Setup Guide

## 📋 Prerequisites

### Required Software

- **Node.js** (v18.0.0 or higher) - [Download](https://nodejs.org/)
- **npm** (v9.0.0 or higher) - Comes with Node.js
- **Git** - [Download](https://git-scm.com/)
- **Claude Code** - [Access](https://claude.ai/code)

### Optional Integrations

- **GitHub CLI** (`gh`) - For pull request management
- **Bitwarden CLI** - If using Bitwarden secrets manager

## 🚀 Initial Setup

### 1. Clone or Fork the Repository

For a new project based on this framework:

```bash
# Option A: Use as template (recommended)
gh repo create my-project --template kelleysd-apps/sdd-agentic-framework --clone
cd my-project

# Option B: Fork and clone
gh repo fork kelleysd-apps/sdd-agentic-framework --clone --remote
cd sdd-agentic-framework

# Option C: Manual clone
git clone https://github.com/kelleysd-apps/sdd-agentic-framework.git my-project
cd my-project
rm -rf .git
git init
```

### 2. Run Automatic Setup

The framework includes an automatic setup script:

```bash
npm run setup
```

This script will:
- ✅ Check Node.js and npm versions
- ✅ Install dependencies
- ✅ Create `.env` file from template
- ✅ Make bash scripts executable
- ✅ Verify Claude configuration

### 3. Customize for Your Project

#### Update Project Information

Edit `package.json`:
```json
{
  "name": "your-project-name",
  "version": "1.0.0",
  "description": "Your project description",
  "author": "Your Name",
  "license": "Your License"
}
```

#### Configure Environment Variables

Edit `.env` (created from `.env.example`):
```bash
# Optional: Bitwarden Secrets Manager
BWS_ACCESS_TOKEN=your_token_here

# Add your project-specific variables
DATABASE_URL=your_connection_string
API_KEY=your_api_key
```

#### Update Project Documentation

1. Archive the framework README:
   ```bash
   mv README.md FRAMEWORK_README.md
   ```

2. Create your project README:
   ```bash
   cat > README.md << 'EOF'
   # Your Project Name

   Description of your project...

   ## Getting Started

   See FRAMEWORK_README.md for framework documentation.
   EOF
   ```

## 🔧 Configuration

### Constitution Setup

The constitution defines your project's development principles. Review and customize:

```bash
# Edit the constitution
code .specify/memory/constitution.md
```

Key sections to customize:
- **Article I**: Library vs Application approach
- **Article III**: Testing requirements
- **Article VII**: Complexity constraints
- **Article X**: Agent delegation rules

⚠️ **Important**: When updating, follow `.specify/memory/constitution_update_checklist.md`

### MCP (Model Context Protocol) Setup

MCP servers extend Claude's capabilities. Configure based on your needs:

#### Available MCP Integrations

| Category | MCP Server | Purpose | Setup Required |
|----------|------------|---------|----------------|
| **Database** | `mcp__supabase` | Supabase integration | API keys |
| **IDE** | `mcp__ide` | Code execution | Auto-configured |
| **Browser** | `mcp__browsermcp` | Web automation | Chrome/Firefox |
| **Search** | `mcp__perplexity` | Enhanced search | API key |
| **Docs** | `mcp__ref-tools` | Documentation access | URLs config |

#### Department-Specific Access

Each department gets appropriate MCP servers automatically:

```javascript
// Example: Engineering department
{
  tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"],
  mcpServers: ["mcp__ide", "mcp__supabase", "mcp__browsermcp"]
}
```

## 📁 Project Structure

```
your-project/
├── .specify/                 # Framework core (DO NOT DELETE)
│   ├── memory/              # Constitutional documents
│   ├── scripts/             # Automation scripts
│   └── templates/           # Document templates
├── .claude/                 # AI assistant configuration
│   ├── agents/              # Agent definitions
│   └── commands/            # Command documentation
├── .docs/                   # Project documentation
│   └── agents/              # Agent memory/context
├── specs/                   # Feature specifications
├── .env                     # Local environment (gitignored)
├── .env.example             # Environment template
├── package.json             # Project configuration
├── CLAUDE.md                # AI instructions (auto-updated)
├── README.md                # Your project readme
├── FRAMEWORK_README.md      # Framework documentation
└── SETUP.md                 # This file
```

## 🤖 Using the Framework

### Core Commands

Execute these in Claude Code:

| Command | Purpose | Output |
|---------|---------|---------|
| `/specify` | Create feature specification | `specs/###-feature-name/spec.md` |
| `/plan` | Generate implementation plan | Design artifacts |
| `/tasks` | Create task list | `specs/###-feature-name/tasks.md` |
| `/create-agent` | Create specialized agent | Agent definition + registry |

### Workflow Example

```bash
# 1. Create a new feature specification
/specify "User authentication with JWT"

# 2. Generate implementation plan
/plan

# 3. Create task list
/tasks

# 4. Create specialized agents if needed
/create-agent auth-specialist "JWT authentication and session management expert"

# 5. Implementation begins automatically with appropriate agents
```

## 🔍 Troubleshooting

### Common Issues

#### "Permission denied" when running scripts

```bash
chmod +x .specify/scripts/bash/*.sh
chmod +x .specify/scripts/setup.sh
```

#### "Module not found" errors

```bash
rm -rf node_modules package-lock.json
npm install
```

#### "Constitution not found" errors

Ensure the file exists and has correct permissions:
```bash
ls -la .specify/memory/constitution.md
```

#### MCP server connection issues

1. Verify MCP is configured in Claude
2. Check environment variables
3. Validate service credentials

### Debug Mode

Enable verbose logging:
```bash
export SDD_DEBUG=true
npm run setup
```

## 🛠️ Advanced Configuration

### Custom Agent Departments

Add new departments by creating directories:
```bash
mkdir -p .claude/agents/your-department
mkdir -p .docs/agents/your-department
```

### Custom Commands

1. Create command documentation:
   ```bash
   touch .claude/commands/your-command.md
   ```

2. Create command script:
   ```bash
   touch .specify/scripts/bash/your-command.sh
   chmod +x .specify/scripts/bash/your-command.sh
   ```

3. Update CLAUDE.md (happens automatically on next agent creation)

### Git Hooks (Optional)

Add pre-commit hooks for quality control:
```bash
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
npm run lint
npm run typecheck
EOF
chmod +x .git/hooks/pre-commit
```

## 📚 Additional Resources

- **Framework Documentation**: See `FRAMEWORK_README.md`
- **Agent Documentation**: See `AGENTS.md`
- **Change History**: See `CHANGELOG.md`
- **Constitution**: See `.specify/memory/constitution.md`
- **Claude Instructions**: See `CLAUDE.md`

## 🤝 Getting Help

1. Check the framework documentation
2. Review the constitution for principles
3. Consult CLAUDE.md for AI guidance
4. Create an issue on GitHub

## ✅ Setup Checklist

- [ ] Node.js v18+ installed
- [ ] Repository cloned/forked
- [ ] `npm run setup` completed successfully
- [ ] `.env` file configured
- [ ] Project name updated in `package.json`
- [ ] Constitution reviewed
- [ ] README.md customized for your project
- [ ] First feature specification created
- [ ] Git repository initialized with your remote

## 🎯 Next Steps

1. **Define Your Constitution**: Customize `.specify/memory/constitution.md`
2. **Create First Feature**: Run `/specify` in Claude Code
3. **Configure Integrations**: Set up needed MCP servers
4. **Start Development**: Follow the SDD workflow

---

**Remember**: The constitution is your guide. When in doubt, consult `.specify/memory/constitution.md`.