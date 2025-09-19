#!/bin/bash

# Auto-setup script for SDD Agentic Framework
# This script automatically configures the development environment on first run

set -e

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}   SDD Framework Development Setup${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed${NC}"
    echo -e "${YELLOW}Please install Node.js (v18 or higher) from https://nodejs.org/${NC}"
    exit 1
fi

NODE_VERSION=$(node -v)
echo -e "${GREEN}✓${NC} Node.js ${NODE_VERSION} detected"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm is not installed${NC}"
    echo -e "${YELLOW}Please install npm${NC}"
    exit 1
fi

NPM_VERSION=$(npm -v)
echo -e "${GREEN}✓${NC} npm ${NPM_VERSION} detected"

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo ""
    echo -e "${BLUE}Installing dependencies...${NC}"
    npm install
    echo -e "${GREEN}✓${NC} Dependencies installed"
else
    echo -e "${GREEN}✓${NC} Dependencies already installed"
fi

# Create .env file from template if it doesn't exist
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo ""
        echo -e "${BLUE}Creating .env file from template...${NC}"
        cp .env.example .env
        echo -e "${GREEN}✓${NC} .env file created"
        echo -e "${YELLOW}⚠  Please update .env with your Bitwarden access token if needed${NC}"
    fi
else
    echo -e "${GREEN}✓${NC} .env file exists"
fi

# Make all bash scripts executable
echo ""
echo -e "${BLUE}Setting up SDD workflow scripts...${NC}"
chmod +x .specify/scripts/bash/*.sh 2>/dev/null || true
echo -e "${GREEN}✓${NC} Scripts are executable"

# Check Claude configuration
if [ -d ".claude" ]; then
    echo -e "${GREEN}✓${NC} Claude Code configuration found"
else
    echo -e "${YELLOW}ℹ  Claude Code configuration not found (optional)${NC}"
fi

echo ""
echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}   Setup Complete! 🎉${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""
echo -e "You can now start developing with the SDD framework."
echo -e ""
echo -e "${BLUE}Available commands in Claude Code:${NC}"
echo -e "  /specify     - Create new feature specification"
echo -e "  /plan        - Generate implementation plan"
echo -e "  /tasks       - Create task list"
echo -e "  /create-agent - Create specialized AI agent"
echo -e ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  1. Read ${YELLOW}.specify/memory/constitution.md${NC} for development principles"
echo -e "  2. Check ${YELLOW}CLAUDE.md${NC} for AI assistant guidance"
echo -e "  3. Review ${YELLOW}README.md${NC} for detailed documentation"
echo -e ""

exit 0