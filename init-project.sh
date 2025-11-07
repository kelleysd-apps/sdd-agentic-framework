#!/bin/bash

# Project Initialization Script for SDD Agentic Framework
# This script helps users quickly set up a new project based on this framework

set -e

# Source common functions for git approval
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/.specify/scripts/bash/common.sh" ]; then
    source "$SCRIPT_DIR/.specify/scripts/bash/common.sh"
fi

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}   SDD Framework Project Setup${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Get project name from user
read -p "Enter your project name (kebab-case): " PROJECT_NAME
if [ -z "$PROJECT_NAME" ]; then
    echo -e "${RED}Error: Project name cannot be empty${NC}"
    exit 1
fi

# Validate project name (kebab-case)
if ! [[ "$PROJECT_NAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo -e "${RED}Error: Project name must be in kebab-case (lowercase letters, numbers, and hyphens)${NC}"
    exit 1
fi

read -p "Enter project description: " PROJECT_DESCRIPTION
read -p "Enter author name: " AUTHOR_NAME

echo ""
echo -e "${BLUE}Initializing project: ${PROJECT_NAME}${NC}"
echo ""

# Update package.json
echo -e "${BLUE}Updating package.json...${NC}"
if [ -f "package.json" ]; then
    # Create a backup
    cp package.json package.json.backup

    # Update using sed (cross-platform compatible)
    sed -i.tmp "s/\"name\": \".*\"/\"name\": \"$PROJECT_NAME\"/" package.json
    sed -i.tmp "s/\"description\": \".*\"/\"description\": \"$PROJECT_DESCRIPTION\"/" package.json
    if [ ! -z "$AUTHOR_NAME" ]; then
        sed -i.tmp "s/\"author\": \".*\"/\"author\": \"$AUTHOR_NAME\"/" package.json
    fi
    rm -f package.json.tmp
    echo -e "${GREEN}✓${NC} package.json updated"
else
    echo -e "${RED}Warning: package.json not found${NC}"
fi

# Archive framework README and create project README
echo -e "${BLUE}Setting up documentation...${NC}"
if [ -f "README.md" ] && [ ! -f "FRAMEWORK_README.md" ]; then
    mv README.md FRAMEWORK_README.md
    echo -e "${GREEN}✓${NC} Framework documentation moved to FRAMEWORK_README.md"
fi

# Create new project README
cat > README.md << EOF
# $PROJECT_NAME

$PROJECT_DESCRIPTION

## 🚀 Getting Started

This project is built using the SDD Agentic Framework. For framework documentation, see \`FRAMEWORK_README.md\`.

### Prerequisites

- Node.js v18+
- npm v9+
- Claude Code access

### Installation

\`\`\`bash
# Install dependencies
npm install

# Run setup
npm run setup
\`\`\`

### Development Workflow

1. **Create Feature Specification**: \`/specify "feature-name"\`
2. **Generate Implementation Plan**: \`/plan\`
3. **Create Task List**: \`/tasks\`
4. **Implement with Agents**: Automatic agent orchestration

## 📚 Documentation

- **Framework Guide**: See \`FRAMEWORK_README.md\`
- **Setup Instructions**: See \`SETUP.md\`
- **Agent Documentation**: See \`AGENTS.md\`
- **Development Principles**: See \`.specify/memory/constitution.md\`

## 🤖 Available Commands

Execute these in Claude Code:

- \`/specify\` - Create feature specification
- \`/plan\` - Generate implementation plan
- \`/tasks\` - Create task list
- \`/create-agent\` - Create specialized agent

## 📁 Project Structure

\`\`\`
$PROJECT_NAME/
├── .specify/         # Framework core
├── .claude/          # AI assistant config
├── .docs/            # Documentation
├── specs/            # Feature specifications
└── src/              # Your source code
\`\`\`

## 🤝 Contributing

Follow the constitutional principles defined in \`.specify/memory/constitution.md\`.

## 📝 License

[Your License Here]

---

Built with [SDD Agentic Framework](https://github.com/kelleysd-apps/sdd-agentic-framework)
EOF

echo -e "${GREEN}✓${NC} Project README created"

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo -e "${BLUE}Initializing git repository...${NC}"
    echo ""

    # Constitutional Principle VI: Request approval for git operations
    if type request_git_approval &> /dev/null; then
        if ! request_git_approval "Git Initialization" "Initialize git repo with initial commit for $PROJECT_NAME"; then
            echo -e "${YELLOW}Git initialization skipped by user${NC}"
            echo -e "${YELLOW}You can initialize git manually later with: git init${NC}"
        else
            git init
            git add .
            git commit -m "Initial commit: $PROJECT_NAME setup with SDD Framework"
            echo -e "${GREEN}✓${NC} Git repository initialized"
        fi
    else
        # Fallback if common.sh not available
        read -p "Initialize git repository? (y/n): " INIT_GIT
        if [[ "$INIT_GIT" =~ ^[Yy]$ ]]; then
            git init
            git add .
            git commit -m "Initial commit: $PROJECT_NAME setup with SDD Framework"
            echo -e "${GREEN}✓${NC} Git repository initialized"
        else
            echo -e "${YELLOW}Git initialization skipped${NC}"
        fi
    fi
else
    echo -e "${YELLOW}ℹ${NC}  Git repository already exists"
fi

# Run the main setup script
echo ""
echo -e "${BLUE}Running framework setup...${NC}"
if [ -f ".specify/scripts/setup.sh" ]; then
    chmod +x .specify/scripts/setup.sh
    ./.specify/scripts/setup.sh
else
    echo -e "${RED}Warning: Setup script not found${NC}"
fi

# Cleanup process (with user approval)
echo ""
echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}   Cleanup Phase${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""
echo -e "${YELLOW}The following files are no longer needed after initialization:${NC}"
echo -e "  - init-project.sh (this script)"
echo -e "  - START_HERE.md (setup documentation)"
echo -e "  - FRAMEWORK_README.md (if you've created your own README)"
echo ""
read -p "Would you like to remove these initialization files? (y/n): " CLEANUP_CONFIRM

if [[ "$CLEANUP_CONFIRM" =~ ^[Yy]$ ]]; then
    echo -e "${BLUE}Cleaning up initialization files...${NC}"

    # Remove the init script itself
    if [ -f "init-project.sh" ]; then
        rm -f init-project.sh
        echo -e "${GREEN}✓${NC} Removed init-project.sh"
    fi

    # Remove START_HERE.md
    if [ -f "START_HERE.md" ]; then
        rm -f START_HERE.md
        echo -e "${GREEN}✓${NC} Removed START_HERE.md"
    fi

    # Ask about FRAMEWORK_README.md separately
    if [ -f "FRAMEWORK_README.md" ]; then
        read -p "Remove FRAMEWORK_README.md? You may want to keep this for reference (y/n): " REMOVE_FRAMEWORK_README
        if [[ "$REMOVE_FRAMEWORK_README" =~ ^[Yy]$ ]]; then
            rm -f FRAMEWORK_README.md
            echo -e "${GREEN}✓${NC} Removed FRAMEWORK_README.md"
        else
            echo -e "${YELLOW}ℹ${NC}  Keeping FRAMEWORK_README.md for reference"
        fi
    fi

    echo -e "${GREEN}✓${NC} Cleanup complete"
else
    echo -e "${YELLOW}ℹ${NC}  Skipping cleanup - you can manually remove these files later"
fi

echo ""
echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}   Project Setup Complete! 🎉${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""
echo -e "Your project '${PROJECT_NAME}' is ready for development!"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  1. Review and customize ${YELLOW}.specify/memory/constitution.md${NC}"
echo -e "  2. Configure environment variables in ${YELLOW}.env${NC}"
echo -e "  3. Open in Claude Code and start with ${YELLOW}/specify${NC}"
echo ""
echo -e "${YELLOW}Remember:${NC} The constitution is your guide!"
echo ""