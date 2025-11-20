# START HERE - SDD Agentic Framework Setup Guide

## 🚨 CRITICAL FIRST STEP: Install Claude Code

**Before proceeding with ANY setup steps, you MUST have Claude Code installed and configured.**

### Why Claude Code First?

This framework is designed to work **with Claude Code as your AI development assistant**. Claude Code:
- ✅ Provides **interactive guidance** throughout setup
- ✅ Helps **troubleshoot any errors** during installation
- ✅ Assists with **project customization** and configuration
- ✅ Executes **framework commands** (`/specify`, `/plan`, `/tasks`, `/create-prd`)
- ✅ **Coordinates multi-agent workflows** for feature development

**Without Claude Code, you cannot use this framework effectively.**

### Install Claude Code

1. **Get Access**: Visit [claude.ai/code](https://claude.ai/code)
2. **Install CLI**: Follow the installation instructions for your platform
3. **Verify Installation**: Run `claude --version` in your terminal
4. **Login**: Run `claude login` and authenticate

Once Claude Code is installed, **use it to help you with ALL remaining setup steps**. If you encounter ANY errors or issues during setup, ask Claude Code for help!

---

## 📋 Prerequisites

### Required Software

- **Claude Code** - [Install First](https://claude.ai/code) ⚠️ **REQUIRED BEFORE STARTING**
- **Node.js** (v18.0.0 or higher) - [Download](https://nodejs.org/)
- **npm** (v9.0.0 or higher) - Comes with Node.js
- **Git** - [Download](https://git-scm.com/)
- **Bash/Git Bash** (Windows users) - Comes with Git for Windows

### Optional: DS-STAR Multi-Agent Features

For enhanced quality gates, intelligent routing, and self-healing capabilities:

- **Python** (v3.9 or higher) - [Download](https://python.org/)
- **pip** - Python package manager (comes with Python)

**Note**: The framework works without Python through graceful degradation. DS-STAR features will be disabled with warnings, and manual review is recommended.

### Optional Integrations

- **GitHub CLI** (`gh`) - For pull request management
- **Secret Manager CLI** - If using external secret management (optional)

## 🚀 Initial Setup

### Platform-Specific Notes

#### Windows Users 🪟

**📖 Detailed Windows Guide Available**: See [WINDOWS_SETUP.md](./WINDOWS_SETUP.md) for a complete Windows-specific setup guide with screenshots and troubleshooting.

This framework requires bash scripts. You have two options:

**Option 1: Git Bash (Recommended) ⭐**
- Git Bash is automatically installed with Git for Windows
- Open "Git Bash" (not Windows PowerShell or CMD)
- All commands work natively in Git Bash
- This is the easiest option for Windows users
- **Full guide**: [WINDOWS_SETUP.md](./WINDOWS_SETUP.md)

**Option 2: WSL2 (Advanced)**
- Install Windows Subsystem for Linux 2 (WSL2)
- Use Ubuntu or your preferred Linux distribution
- Follow Linux setup instructions

**⚠️ DO NOT use Windows PowerShell or CMD** - bash scripts will not work!

**Need help?** See [WINDOWS_SETUP.md](./WINDOWS_SETUP.md) for detailed Windows setup instructions.

#### macOS/Linux Users 🐧🍎
- Use your default terminal
- All commands work natively

---

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

**IMPORTANT**: If you encounter ANY errors during setup, ask Claude Code for help!

The framework includes an automatic setup script:

```bash
# macOS/Linux
npm run setup

# Windows (Git Bash) - Use this if npm run setup fails
npm run setup:windows

# Alternative: Run script directly with bash
bash .specify/scripts/setup.sh
```

**💡 Troubleshooting Tip**: If you see an error like `'.' is not recognized`, you're in the wrong terminal. Open Git Bash instead of PowerShell/CMD. Try `npm run setup:windows` instead.

This script will:
- ✅ Check Node.js and npm versions
- ✅ Install dependencies
- ✅ Create `.env` file from template
- ✅ Make bash scripts executable
- ✅ Verify Claude configuration
- ✅ Install DS-STAR Python dependencies (if Python available)

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
# Optional: Add any project-specific secrets
# SECRET_TOKEN=your_token_here

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
└── START_HERE.md            # This file
```

## 🤖 Using the Framework

### Core Commands

Execute these in Claude Code:

| Command | Purpose | Output | DS-STAR Enhancement |
|---------|---------|---------|---------------------|
| `/specify` | Create feature specification | `specs/###-feature-name/spec.md` | ✅ Automatic refinement loop |
| `/plan` | Generate implementation plan | Design artifacts | ✅ Quality verification gate |
| `/tasks` | Create task list | `specs/###-feature-name/tasks.md` | - |
| `/finalize` | Pre-commit validation | Compliance report | ✅ Constitutional compliance |
| `/create-agent` | Create specialized agent | Agent definition + registry | - |

### Workflow Example

```bash
# 1. Create a new feature specification
/specify "User authentication with JWT"
# DS-STAR: Automatically refines spec until quality threshold met (≥0.90)

# 2. Generate implementation plan
/plan
# DS-STAR: Verifies plan quality (≥0.85) before allowing task generation

# 3. Create task list
/tasks

# 4. Create specialized agents if needed
/create-agent auth-specialist "JWT authentication and session management expert"

# 5. Implementation begins automatically with appropriate agents
# DS-STAR: RouterAgent coordinates multi-agent workflows
# DS-STAR: AutoDebugAgent provides self-healing (>70% fix rate)

# 6. Before committing
/finalize
# DS-STAR: Validates all 14 constitutional principles
# Provides manual git commands to execute
```

### DS-STAR Quality Gates

When Python is available, the framework automatically:
- **Refines specifications** up to 20 rounds until quality thresholds met
- **Verifies plans** before task generation (blocks if insufficient)
- **Routes tasks** to appropriate agents with dependency management
- **Auto-repairs errors** with >70% success rate target
- **Validates compliance** before commits (all 14 principles)

**Configuration**: See `.specify/config/refinement.conf` for thresholds

## 🔍 Troubleshooting

### 🤖 When in Doubt, Ask Claude Code!

**This is the most important troubleshooting advice**: If you encounter ANY error during setup or usage:

1. **Open Claude Code** in your project directory
2. **Paste the error message** into the conversation
3. **Ask for help**: "I got this error during setup, can you help me fix it?"
4. **Follow Claude's guidance** - it has full context of the framework

Claude Code has access to:
- All framework documentation
- Constitutional principles
- Setup scripts and configurations
- Your project state and environment

**Claude Code is your first line of support.** Use it!

---

### Common Issues

#### Windows: `'.' is not recognized` Error

**Problem**: You're in PowerShell or CMD instead of Git Bash

**Solution**:
1. Close PowerShell/CMD
2. Open **Git Bash** (installed with Git for Windows)
3. Navigate to your project: `cd /c/Users/YourName/your-project`
4. Run commands in Git Bash

**Ask Claude Code**: "I'm on Windows and getting a '.' is not recognized error. How do I fix this?"

#### "Permission denied" when running scripts

```bash
chmod +x .specify/scripts/bash/*.sh
chmod +x .specify/scripts/setup.sh
```

**Ask Claude Code**: "I'm getting permission denied errors. Can you help?"

#### "Module not found" errors

```bash
rm -rf node_modules package-lock.json
npm install
```

**Ask Claude Code**: "I'm getting module not found errors after npm install. What should I do?"

#### "Constitution not found" errors

Ensure the file exists and has correct permissions:
```bash
ls -la .specify/memory/constitution.md
```

**Ask Claude Code**: "The constitution file isn't being found. Can you check what's wrong?"

#### MCP server connection issues

1. Verify MCP is configured in Claude
2. Check environment variables
3. Validate service credentials

**Ask Claude Code**: "I'm having MCP server connection issues. Can you help me debug?"

### Debug Mode

Enable verbose logging:
```bash
export SDD_DEBUG=true
npm run setup
```

### Still Stuck?

1. **Try Claude Code first** - Paste your error and ask for help
2. Check the framework documentation in `FRAMEWORK_README.md`
3. Review the constitution at `.specify/memory/constitution.md`
4. Create an issue on GitHub with the error details

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

### Primary Support: Claude Code 🤖

**Claude Code is your built-in AI assistant and primary support resource.**

When you need help:
1. **Open Claude Code** in your project directory
2. **Describe your issue** or paste error messages
3. **Ask specific questions** about setup, configuration, or usage
4. **Request guidance** on best practices and framework features

Claude Code can:
- ✅ Debug errors in real-time
- ✅ Explain framework concepts and principles
- ✅ Guide you through setup and configuration
- ✅ Help customize the constitution for your project
- ✅ Assist with feature development workflows
- ✅ Answer questions about agents, commands, and workflows

### Additional Resources

1. **CLAUDE.md** - Instructions for Claude Code (auto-consulted)
2. **FRAMEWORK_README.md** - Comprehensive framework documentation
3. **Constitution** - `.specify/memory/constitution.md` (14 core principles)
4. **GitHub Issues** - [Report bugs or request features](https://github.com/kelleysd-apps/sdd-agentic-framework/issues)

### Example: Getting Help from Claude Code

```
You: "I'm setting up the framework on Windows and getting
      errors when running npm run setup. Can you help?"

Claude: "I can help! It looks like you might be in PowerShell
         instead of Git Bash. Here's what to do..."
```

**Remember**: Claude Code has full context of your project and the framework. It's designed to be your first line of support!

## ✅ Setup Checklist

- [ ] **Claude Code installed and configured** ⚠️ **DO THIS FIRST**
- [ ] Git Bash installed (Windows users) or terminal ready (macOS/Linux)
- [ ] Node.js v18+ installed
- [ ] Repository cloned/forked
- [ ] Opened project in correct terminal (Git Bash on Windows)
- [ ] `npm run setup` completed successfully (asked Claude for help if errors)
- [ ] `.env` file configured
- [ ] Project name updated in `package.json`
- [ ] Constitution reviewed (with Claude Code's guidance)
- [ ] README.md customized for your project
- [ ] First feature specification created using `/specify`
- [ ] Git repository initialized with your remote

## 🎯 Next Steps

**All of these steps should be done WITH Claude Code open to assist you:**

1. **Open Claude Code**: Navigate to your project directory and start Claude Code
2. **Review Constitution**: Ask Claude Code to explain `.specify/memory/constitution.md`
3. **Customize for Your Project**: Use `/create-prd` to define your product requirements
4. **Create First Feature**: Run `/specify` in Claude Code for your first feature
5. **Configure Integrations**: Set up needed MCP servers (ask Claude for guidance)
6. **Start Development**: Follow the SDD workflow with Claude Code as your assistant

### Recommended First Commands in Claude Code

```bash
# 1. Ask Claude Code for an overview
"Can you explain how this SDD framework works?"

# 2. Create a PRD for your project (optional but recommended)
/create-prd

# 3. Create your first feature specification
/specify "your-feature-name"

# 4. Get help anytime
"I need help understanding [topic]"
```

---

**Remember**:
- Claude Code is your co-pilot - use it for EVERYTHING!
- The constitution is your guide: `.specify/memory/constitution.md`
- When in doubt, ask Claude Code!