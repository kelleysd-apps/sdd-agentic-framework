#!/bin/bash

# Auto-setup script for SDD Agentic Framework
# This script automatically configures the development environment on first run
# Supports macOS and Linux with automatic dependency installation

set -e

# Prevent recursive calls from npm postinstall hooks
if [ "$SDD_SETUP_RUNNING" = "true" ]; then
    echo "Setup already running, skipping recursive call"
    exit 0
fi
export SDD_SETUP_RUNNING=true

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}   SDD Framework Setup${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     PLATFORM=Linux;;
    Darwin*)    PLATFORM=macOS;;
    *)          PLATFORM="Unknown";;
esac

echo -e "${BLUE}Detected platform: ${PLATFORM}${NC}"
echo ""

# Check if Node.js is installed, guide installation if not
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed${NC}"
    echo ""
    echo -e "${YELLOW}Installing Node.js...${NC}"

    if [ "$PLATFORM" == "macOS" ]; then
        if command -v brew &> /dev/null; then
            echo -e "${BLUE}Using Homebrew to install Node.js...${NC}"
            brew install node
        else
            echo -e "${YELLOW}Homebrew not found. Please install from https://brew.sh/${NC}"
            echo -e "${YELLOW}Then install Node.js: brew install node${NC}"
            echo -e "${YELLOW}Or download directly from https://nodejs.org/${NC}"
            exit 1
        fi
    elif [ "$PLATFORM" == "Linux" ]; then
        echo -e "${BLUE}Installing Node.js via package manager...${NC}"
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y nodejs npm
        elif command -v yum &> /dev/null; then
            sudo yum install -y nodejs npm
        elif command -v dnf &> /dev/null; then
            sudo dnf install -y nodejs npm
        else
            echo -e "${YELLOW}Could not detect package manager${NC}"
            echo -e "${YELLOW}Please install Node.js from https://nodejs.org/${NC}"
            exit 1
        fi
    else
        echo -e "${YELLOW}Please install Node.js (v18 or higher) from https://nodejs.org/${NC}"
        exit 1
    fi
fi

NODE_VERSION=$(node -v)
echo -e "${GREEN}[OK]${NC} Node.js ${NODE_VERSION} detected"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm is not installed${NC}"
    echo -e "${YELLOW}npm should come with Node.js. Please reinstall Node.js from https://nodejs.org/${NC}"
    exit 1
fi

NPM_VERSION=$(npm -v)
echo -e "${GREEN}[OK]${NC} npm ${NPM_VERSION} detected"

# Check if Git is installed, guide installation if not
if ! command -v git &> /dev/null; then
    echo ""
    echo -e "${YELLOW}[WARNING] Git is not installed${NC}"
    echo ""

    if [ "$PLATFORM" == "macOS" ]; then
        echo -e "${BLUE}Installing Git via Homebrew...${NC}"
        if command -v brew &> /dev/null; then
            brew install git
        else
            echo -e "${YELLOW}Homebrew not found. Install from https://brew.sh/${NC}"
            echo -e "${YELLOW}Or install Xcode Command Line Tools: xcode-select --install${NC}"
        fi
    elif [ "$PLATFORM" == "Linux" ]; then
        echo -e "${BLUE}Installing Git...${NC}"
        if command -v apt-get &> /dev/null; then
            sudo apt-get install -y git
        elif command -v yum &> /dev/null; then
            sudo yum install -y git
        elif command -v dnf &> /dev/null; then
            sudo dnf install -y git
        fi
    fi
else
    GIT_VERSION=$(git --version)
    echo -e "${GREEN}[OK]${NC} ${GIT_VERSION}"
fi

# Check if Claude Code CLI is installed
echo ""
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}[WARNING] Claude Code CLI is not installed${NC}"
    echo ""
    echo -e "${BLUE}Claude Code is your AI assistant for this framework.${NC}"
    echo -e "${BLUE}It provides:${NC}"
    echo -e "  • Interactive guidance throughout development"
    echo -e "  • Troubleshooting support for any errors"
    echo -e "  • Automated workflows (/specify, /plan, /tasks, /create-prd)"
    echo ""
    echo -e "${YELLOW}To install Claude Code:${NC}"
    echo -e "  1. Visit: ${BLUE}https://claude.ai/code${NC}"
    echo -e "  2. Sign in or create an account"
    echo -e "  3. Follow installation instructions for ${PLATFORM}"
    echo -e "  4. Run: ${BLUE}claude login${NC}"
    echo ""
    read -p "Press Enter to continue without Claude Code, or Ctrl+C to install it first..."
else
    CLAUDE_VERSION=$(claude --version 2>&1 || echo "installed")
    echo -e "${GREEN}[OK]${NC} Claude Code CLI ${CLAUDE_VERSION}"
fi

echo ""

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo ""
    echo -e "${BLUE}Installing dependencies...${NC}"
    npm install
    echo -e "${GREEN}[OK]${NC} Dependencies installed"
else
    echo -e "${GREEN}[OK]${NC} Dependencies already installed"
fi

# Create .env file from template if it doesn't exist
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo ""
        echo -e "${BLUE}Creating .env file from template...${NC}"
        cp .env.example .env
        echo -e "${GREEN}[OK]${NC} .env file created"
        echo -e "${YELLOW}[INFO]${NC}  Please update .env with your project-specific configuration"
    fi
else
    echo -e "${GREEN}[OK]${NC} .env file exists"
fi

# Make all bash scripts executable
echo ""
echo -e "${BLUE}Setting up SDD workflow scripts...${NC}"
chmod +x .specify/scripts/bash/*.sh 2>/dev/null || true
echo -e "${GREEN}[OK]${NC} Scripts are executable"

# Check Claude configuration
if [ -d ".claude" ]; then
    echo -e "${GREEN}[OK]${NC} Claude Code configuration found"
else
    echo -e "${YELLOW}[INFO]  Claude Code configuration not found (optional)${NC}"
fi

echo ""
echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}   Setup Complete! 🎉${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""

echo -e "${BLUE}Recommended workflow for project initialization:${NC}"
echo ""
echo -e "${YELLOW}Step 1: Create a Product Requirements Document (PRD)${NC}"
echo -e "  The PRD serves as your Single Source of Truth (SSOT)"
echo -e "  It guides constitution customization, agent creation, and all feature work"
echo ""
echo -e "  ${BLUE}In Claude Code, run:${NC} ${GREEN}/create-prd${NC}"
echo ""
echo -e "${YELLOW}Step 2: Customize the Constitution${NC}"
echo -e "  Edit: ${GREEN}.specify/memory/constitution.md${NC}"
echo -e "  Use your PRD to customize all 14 principles for your project"
echo ""
echo -e "${YELLOW}Step 3: Create specialized agents (if needed)${NC}"
echo -e "  ${BLUE}In Claude Code, run:${NC} ${GREEN}/create-agent${NC}"
echo ""
echo -e "${YELLOW}Step 4: Start feature development${NC}"
echo -e "  ${BLUE}Available commands in Claude Code:${NC}"
echo -e "    ${GREEN}/specify${NC}      - Create feature specification"
echo -e "    ${GREEN}/plan${NC}         - Generate implementation plan"
echo -e "    ${GREEN}/tasks${NC}        - Create task list"
echo -e "    ${GREEN}/finalize${NC}     - Pre-commit compliance validation"
echo ""

# Offer to launch Claude Code
if command -v claude &> /dev/null; then
    echo ""
    read -p "Would you like to launch Claude Code now? (y/n): " launch_claude
    if [[ "$launch_claude" =~ ^[Yy]$ ]]; then
        echo ""
        echo -e "${BLUE}Launching Claude Code...${NC}"
        claude code .
    fi
else
    echo ""
    echo -e "${YELLOW}[TIP] Tip: Install Claude Code for AI-assisted development${NC}"
    echo -e "   Visit: ${BLUE}https://claude.ai/code${NC}"
fi

echo ""
echo -e "${BLUE}For more information:${NC}"
echo -e "  • ${GREEN}START_HERE.md${NC} - Complete setup and usage guide"
echo -e "  • ${GREEN}.specify/memory/constitution.md${NC} - Development principles"
echo -e "  • ${GREEN}CLAUDE.md${NC} - AI assistant instructions"
echo ""

exit 0