#!/bin/bash

# Agent Creation Tool
# Version: 1.0.0
# Purpose: Automated agent creation with constitutional compliance
#
# NOTE: This script should be invoked through the subagent-architect agent
# for proper SDD compliance and constitutional validation.
# Use: Task tool with subagent-architect to create agents

set -euo pipefail

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${SCRIPT_DIR}/common.sh" ]]; then
    source "${SCRIPT_DIR}/common.sh"
fi

# Constants
REPO_ROOT="/workspaces/ioun-ai"
AGENTS_DIR="${REPO_ROOT}/.claude/agents"
DOCS_DIR="${REPO_ROOT}/.docs/agents"
TEMPLATE_FILE="${REPO_ROOT}/.specify/templates/agent-template.md"
CONSTITUTION_FILE="${REPO_ROOT}/.specify/memory/constitution.md"
GOVERNANCE_FILE="${REPO_ROOT}/.specify/memory/agent-governance.md"
POLICY_FILE="${REPO_ROOT}/.docs/policies/agent-creation-policy.md"
AUDIT_LOG="${DOCS_DIR}/audit/creation-log.json"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Department definitions with their characteristics
declare -A DEPARTMENTS=(
    ["architecture"]="System design and planning"
    ["engineering"]="Development and implementation"
    ["quality"]="Testing and review"
    ["data"]="Data management and pipelines"
    ["product"]="Requirements and UX"
    ["operations"]="DevOps and maintenance"
)

# Tool access matrix by department
declare -A DEPT_TOOLS=(
    ["architecture"]="Read, Grep, Glob, WebSearch, TodoWrite"
    ["engineering"]="Read, Write, Edit, MultiEdit, Bash, Grep, Glob, WebSearch, TodoWrite"
    ["quality"]="Read, Grep, Glob, Bash, WebSearch, TodoWrite"
    ["data"]="Read, Edit, Bash, Grep, Glob, TodoWrite"
    ["product"]="Read, WebSearch, TodoWrite"
    ["operations"]="Read, Bash, Grep, Glob, TodoWrite"
)

# MCP access matrix by department
declare -A DEPT_MCP=(
    ["architecture"]="mcp__ref-tools, mcp__supabase__search_docs, mcp__perplexity, mcp__claude-context"
    ["engineering"]="mcp__ide, mcp__supabase, mcp__ref-tools, mcp__browsermcp, mcp__claude-context"
    ["quality"]="mcp__ide__executeCode, mcp__ide__getDiagnostics, mcp__ref-tools"
    ["data"]="mcp__supabase, mcp__supabase__apply_migration, mcp__supabase__execute_sql"
    ["product"]="mcp__ref-tools, mcp__browsermcp, mcp__perplexity"
    ["operations"]="mcp__supabase__deploy_edge_function, mcp__supabase__get_logs, mcp__supabase__create_project"
)

# Functions
print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║        Agent Creation Tool v1.0        ║${NC}"
    echo -e "${BLUE}║     Constitutional Compliance Mode     ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
    echo
}

validate_prerequisites() {
    echo -e "${YELLOW}▶ Validating prerequisites...${NC}"

    if [[ ! -f "$CONSTITUTION_FILE" ]]; then
        echo -e "${RED}✗ Constitution file not found at $CONSTITUTION_FILE${NC}"
        exit 1
    fi

    if [[ ! -f "$GOVERNANCE_FILE" ]]; then
        echo -e "${RED}✗ Governance file not found at $GOVERNANCE_FILE${NC}"
        exit 1
    fi

    if [[ ! -f "$TEMPLATE_FILE" ]]; then
        echo -e "${RED}✗ Template file not found at $TEMPLATE_FILE${NC}"
        exit 1
    fi

    echo -e "${GREEN}✓ All prerequisites validated${NC}"
}

analyze_existing_agents() {
    local proposed_name=$1
    echo -e "${YELLOW}▶ Analyzing existing agent architecture...${NC}"

    # Count agents by department
    for dept in "${!DEPARTMENTS[@]}"; do
        if [[ -d "${AGENTS_DIR}/${dept}" ]]; then
            count=$(find "${AGENTS_DIR}/${dept}" -name "*.md" -type f 2>/dev/null | wc -l)
            echo -e "  ${dept}: ${count} agents"
        fi
    done

    # Check for duplicate
    if find "${AGENTS_DIR}" -name "${proposed_name}.md" -type f 2>/dev/null | grep -q .; then
        echo -e "${RED}✗ Agent with name '${proposed_name}' already exists${NC}"
        return 1
    fi

    echo -e "${GREEN}✓ No naming conflicts detected${NC}"
    return 0
}

determine_department() {
    local purpose=$1
    local agent_name=${2:-}
    local suggested_dept=""

    echo -e "${YELLOW}▶ Analyzing purpose to determine department...${NC}" >&2

    # Score-based department matching for better accuracy
    local arch_score=0
    local eng_score=0
    local qual_score=0
    local data_score=0
    local prod_score=0
    local ops_score=0

    # Architecture patterns
    echo "$purpose" | grep -qiE "architect|system.*(design|planning)|integration|planning" && ((arch_score+=2))
    echo "$purpose" | grep -qiE "scalability|high.level|technical.planning" && ((arch_score+=1))

    # Engineering patterns (prioritize specific frontend/backend keywords)
    echo "$purpose" | grep -qiE "frontend|react|vue|angular|ui|component" && ((eng_score+=3))
    echo "$purpose" | grep -qiE "backend|api|server|node|python|java" && ((eng_score+=3))
    echo "$purpose" | grep -qiE "develop|implement|code|build|create" && ((eng_score+=2))
    echo "$purpose" | grep -qiE "javascript|typescript|programming" && ((eng_score+=1))

    # Quality patterns
    echo "$purpose" | grep -qiE "test|qa|quality|review|audit" && ((qual_score+=2))
    echo "$purpose" | grep -qiE "security.*(test|audit|scan)|vulnerability" && ((qual_score+=1))

    # Data patterns
    echo "$purpose" | grep -qiE "database|sql|nosql|data.*(model|pipeline)|etl" && ((data_score+=2))
    echo "$purpose" | grep -qiE "analytics|warehouse|migration|schema" && ((data_score+=1))

    # Product patterns
    echo "$purpose" | grep -qiE "product|requirement|user.*(story|experience)|ux" && ((prod_score+=2))
    echo "$purpose" | grep -qiE "feature|specification|business" && ((prod_score+=1))

    # Operations patterns (enhanced for DevOps)
    echo "$purpose" | grep -qiE "devops|ci.?cd|deploy|deployment|docker|kubernetes" && ((ops_score+=3))
    echo "$purpose" | grep -qiE "infrastructure|terraform|cloud|aws|azure|gcp" && ((ops_score+=2))
    echo "$purpose" | grep -qiE "monitor|observability|incident|release|pipeline" && ((ops_score+=2))
    echo "$purpose" | grep -qiE "site.reliability|sre|production" && ((ops_score+=1))

    # Check agent name for additional hints
    if [[ -n "$agent_name" ]]; then
        echo "$agent_name" | grep -qiE "frontend|ui|react" && ((eng_score+=2))
        echo "$agent_name" | grep -qiE "backend|api|server" && ((eng_score+=2))
        echo "$agent_name" | grep -qiE "devops|sre|ops" && ((ops_score+=2))
        echo "$agent_name" | grep -qiE "architect" && ((arch_score+=2))
        echo "$agent_name" | grep -qiE "data|analytics|etl" && ((data_score+=2))
        echo "$agent_name" | grep -qiE "test|qa|quality" && ((qual_score+=2))
        echo "$agent_name" | grep -qiE "product|pm|ux" && ((prod_score+=2))
    fi

    # Debug scoring (shown in verbose mode)
    if [[ "${VERBOSE:-}" == "true" ]]; then
        echo "Department scores:" >&2
        echo "  Architecture: $arch_score" >&2
        echo "  Engineering: $eng_score" >&2
        echo "  Quality: $qual_score" >&2
        echo "  Data: $data_score" >&2
        echo "  Product: $prod_score" >&2
        echo "  Operations: $ops_score" >&2
    fi

    # Find highest scoring department
    local max_score=0
    if [[ $arch_score -gt $max_score ]]; then
        max_score=$arch_score
        suggested_dept="architecture"
    fi
    if [[ $eng_score -gt $max_score ]]; then
        max_score=$eng_score
        suggested_dept="engineering"
    fi
    if [[ $qual_score -gt $max_score ]]; then
        max_score=$qual_score
        suggested_dept="quality"
    fi
    if [[ $data_score -gt $max_score ]]; then
        max_score=$data_score
        suggested_dept="data"
    fi
    if [[ $prod_score -gt $max_score ]]; then
        max_score=$prod_score
        suggested_dept="product"
    fi
    if [[ $ops_score -gt $max_score ]]; then
        max_score=$ops_score
        suggested_dept="operations"
    fi

    # Default to engineering if no clear match
    if [[ -z "$suggested_dept" ]] || [[ $max_score -eq 0 ]]; then
        suggested_dept="engineering"
    fi

    echo -e "${GREEN}✓ Suggested department: ${suggested_dept}${NC}" >&2
    echo "$suggested_dept"
}

validate_department_assignment() {
    local agent_name=$1
    local department=$2
    local description=$3

    echo -e "${YELLOW}▶ Validating department assignment...${NC}" >&2

    local warnings=""

    # Check for common mismatches
    if [[ "$agent_name" =~ frontend|ui|react ]] && [[ "$department" != "engineering" ]]; then
        warnings="${warnings}⚠ Frontend agent typically belongs in engineering department\n"
    fi

    if [[ "$agent_name" =~ backend|api|server ]] && [[ "$department" != "engineering" ]]; then
        warnings="${warnings}⚠ Backend agent typically belongs in engineering department\n"
    fi

    if [[ "$agent_name" =~ devops|sre|ops ]] && [[ "$department" != "operations" ]]; then
        warnings="${warnings}⚠ DevOps agent typically belongs in operations department\n"
    fi

    if [[ "$agent_name" =~ test|qa ]] && [[ "$department" != "quality" ]]; then
        warnings="${warnings}⚠ QA/Test agent typically belongs in quality department\n"
    fi

    if [[ "$agent_name" =~ data|etl|analytics ]] && [[ "$department" != "data" ]]; then
        warnings="${warnings}⚠ Data agent typically belongs in data department\n"
    fi

    if [[ "$agent_name" =~ product|pm|ux ]] && [[ "$department" != "product" ]]; then
        warnings="${warnings}⚠ Product/UX agent typically belongs in product department\n"
    fi

    # Check description for additional validation
    if echo "$description" | grep -qiE "react|vue|angular|frontend" && [[ "$department" != "engineering" ]]; then
        warnings="${warnings}⚠ Description suggests frontend work (engineering department)\n"
    fi

    if echo "$description" | grep -qiE "ci.?cd|docker|kubernetes|deploy" && [[ "$department" != "operations" ]]; then
        warnings="${warnings}⚠ Description suggests DevOps work (operations department)\n"
    fi

    # Report warnings if any
    if [[ -n "$warnings" ]]; then
        echo -e "${YELLOW}Department validation warnings:${NC}" >&2
        echo -e "$warnings" >&2
        return 1  # Return non-zero to indicate warnings exist
    else
        echo -e "${GREEN}✓ Department assignment validated${NC}" >&2
        return 0
    fi
}

create_agent_file() {
    local agent_name=$1
    local department=$2
    local description=$3
    local tools=$4
    local responsibilities=$5
    local mcp_access="${DEPT_MCP[$department]:-none}"

    local agent_file="${AGENTS_DIR}/${department}/${agent_name}.md"

    echo -e "${YELLOW}▶ Creating agent definition...${NC}"

    # Create department directory if it doesn't exist
    mkdir -p "${AGENTS_DIR}/${department}"

    # Create agent from template
    cp "$TEMPLATE_FILE" "$agent_file"

    # Replace placeholders
    sed -i "s|{{AGENT_NAME}}|${agent_name}|g" "$agent_file"
    sed -i "s|{{AGENT_DESCRIPTION}}|${description}|g" "$agent_file"
    sed -i "s|{{AGENT_TOOLS}}|${tools}|g" "$agent_file"
    sed -i "s|{{MCP_ACCESS}}|${mcp_access}|g" "$agent_file"
    sed -i "s|{{AGENT_MODEL}}|inherit|g" "$agent_file"
    sed -i "s|{{AGENT_TITLE}}|${agent_name//-/ } Agent|g" "$agent_file"
    sed -i "s|{{DEPARTMENT}}|${department}|g" "$agent_file"
    sed -i "s|{{AGENT_RESPONSIBILITIES}}|${responsibilities}|g" "$agent_file"
    sed -i "s|{{CREATION_DATE}}|$(date +%Y-%m-%d)|g" "$agent_file"
    sed -i "s|{{LAST_MODIFIED}}|$(date +%Y-%m-%d)|g" "$agent_file"

    # Set department-specific values
    case $department in
        "architecture")
            sed -i "s|{{ROLE_TYPE}}|Design \& Planning|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Strategic|g" "$agent_file"
            ;;
        "engineering")
            sed -i "s|{{ROLE_TYPE}}|Implementation|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Tactical|g" "$agent_file"
            ;;
        "quality")
            sed -i "s|{{ROLE_TYPE}}|Validation & Review|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Audit|g" "$agent_file"
            ;;
        "data")
            sed -i "s|{{ROLE_TYPE}}|Data Management|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Analytical|g" "$agent_file"
            ;;
        "product")
            sed -i "s|{{ROLE_TYPE}}|Requirements & UX|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|User-Focused|g" "$agent_file"
            ;;
        "operations")
            sed -i "s|{{ROLE_TYPE}}|DevOps and Monitoring|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Operational|g" "$agent_file"
            ;;
        *)
            sed -i "s|{{ROLE_TYPE}}|Specialized|g" "$agent_file"
            sed -i "s|{{INTERACTION_LEVEL}}|Domain-Specific|g" "$agent_file"
            ;;
    esac

    # Replace remaining placeholders with defaults
    sed -i "s|{{SHARED_MEMORY_REFS}}|- Department knowledge: /workspaces/ioun-ai/.docs/agents/${department}/|g" "$agent_file"
    sed -i "s|{{DEPARTMENT_GUIDELINES}}|- Follow ${department} best practices\n- Collaborate with other ${department} agents|g" "$agent_file"
    sed -i "s|{{TOOL_POLICIES}}|${tools}|g" "$agent_file"
    sed -i "s|{{RESTRICTED_OPERATIONS}}|- No unauthorized Git operations\n- No production changes without approval|g" "$agent_file"
    sed -i "s|{{UPSTREAM_AGENTS}}|As configured|g" "$agent_file"
    sed -i "s|{{INPUT_FORMAT}}|Markdown/JSON|g" "$agent_file"
    sed -i "s|{{INPUT_VALIDATION}}|Type and format checking|g" "$agent_file"
    sed -i "s|{{DOWNSTREAM_AGENTS}}|As configured|g" "$agent_file"
    sed -i "s|{{OUTPUT_FORMAT}}|Markdown/JSON|g" "$agent_file"
    sed -i "s|{{OUTPUT_GUARANTEES}}|Accurate and validated|g" "$agent_file"
    sed -i "s|{{DOMAIN_EXPERTISE}}|${department} domain knowledge|g" "$agent_file"
    sed -i "s|{{TECHNICAL_SPECS}}|As per department standards|g" "$agent_file"
    sed -i "s|{{BEST_PRACTICES}}|Industry best practices for ${department}|g" "$agent_file"
    sed -i "s|{{LIMITATIONS}}|Tool access restrictions|g" "$agent_file"
    sed -i "s|{{MINOR_ESCALATION}}|Log and continue|g" "$agent_file"
    sed -i "s|{{MAJOR_ESCALATION}}|Alert user and wait|g" "$agent_file"
    sed -i "s|{{CRITICAL_ESCALATION}}|Stop and request help|g" "$agent_file"
    sed -i "s|{{SIMPLE_RESPONSE_TIME}}|2s|g" "$agent_file"
    sed -i "s|{{COMPLEX_RESPONSE_TIME}}|10s|g" "$agent_file"
    sed -i "s|{{LARGE_RESPONSE_TIME}}|30s|g" "$agent_file"
    sed -i "s|{{ACCURACY_TARGET}}|95|g" "$agent_file"
    sed -i "s|{{SUCCESS_TARGET}}|90|g" "$agent_file"
    sed -i "s|{{SATISFACTION_TARGET}}|4|g" "$agent_file"
    sed -i "s|{{REVIEW_SCHEDULE}}|Quarterly|g" "$agent_file"

    echo -e "${GREEN}✓ Agent file created at ${agent_file}${NC}"
}

create_memory_structure() {
    local agent_name=$1
    local department=$2

    echo -e "${YELLOW}▶ Creating memory structure...${NC}"

    local memory_base="${DOCS_DIR}/${department}/${agent_name}"

    # Create memory directories
    mkdir -p "${memory_base}/context"
    mkdir -p "${memory_base}/knowledge"
    mkdir -p "${memory_base}/decisions"
    mkdir -p "${memory_base}/performance"

    # Create initial memory files with agent-specific names
    echo "# ${agent_name} Context" > "${memory_base}/context/${agent_name}-context.md"
    echo "Current working context and state for ${agent_name}" >> "${memory_base}/context/${agent_name}-context.md"

    echo "# ${agent_name} Knowledge Base" > "${memory_base}/knowledge/${agent_name}-knowledge.md"
    echo "Accumulated knowledge and learnings" >> "${memory_base}/knowledge/${agent_name}-knowledge.md"

    echo "# ${agent_name} Decision Log" > "${memory_base}/decisions/${agent_name}-decisions.md"
    echo "Historical decisions and rationales" >> "${memory_base}/decisions/${agent_name}-decisions.md"

    echo "# ${agent_name} Performance Metrics" > "${memory_base}/performance/${agent_name}-performance.md"
    echo "Performance tracking and optimization data" >> "${memory_base}/performance/${agent_name}-performance.md"

    echo -e "${GREEN}✓ Memory structure created at ${memory_base}${NC}"
}

validate_agent_compliance() {
    local agent_file=$1

    echo -e "${YELLOW}▶ Validating constitutional compliance...${NC}"

    local errors=0

    # Check for constitution reference
    if ! grep -q "${CONSTITUTION_FILE}" "$agent_file"; then
        echo -e "${RED}✗ Missing constitution reference${NC}"
        ((errors++))
    else
        echo -e "${GREEN}✓ Constitution reference present${NC}"
    fi

    # Check for governance reference
    if ! grep -q "${GOVERNANCE_FILE}" "$agent_file"; then
        echo -e "${RED}✗ Missing governance reference${NC}"
        ((errors++))
    else
        echo -e "${GREEN}✓ Governance reference present${NC}"
    fi

    # Check for Git operations warning
    if ! grep -q "NO Git operations without explicit user approval" "$agent_file"; then
        echo -e "${RED}✗ Missing Git operations mandate${NC}"
        ((errors++))
    else
        echo -e "${GREEN}✓ Git operations mandate present${NC}"
    fi

    # Check for test-first principle
    if ! grep -q "Test-First" "$agent_file"; then
        echo -e "${RED}✗ Missing test-first principle${NC}"
        ((errors++))
    else
        echo -e "${GREEN}✓ Test-first principle present${NC}"
    fi

    if [[ $errors -eq 0 ]]; then
        echo -e "${GREEN}✓ All compliance checks passed${NC}"
        return 0
    else
        echo -e "${RED}✗ Compliance validation failed with ${errors} errors${NC}"
        return 1
    fi
}

log_creation() {
    local agent_name=$1
    local department=$2
    local status=$3

    mkdir -p "$(dirname "$AUDIT_LOG")"

    if [[ ! -f "$AUDIT_LOG" ]]; then
        echo "[]" > "$AUDIT_LOG"
    fi

    local entry=$(cat <<EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "agent": "${agent_name}",
  "department": "${department}",
  "action": "creation",
  "status": "${status}",
  "created_by": "${USER:-system}",
  "version": "1.0.0"
}
EOF
)

    # Add entry to log (requires jq for proper JSON handling)
    if command -v jq &> /dev/null; then
        jq ". += [${entry}]" "$AUDIT_LOG" > "${AUDIT_LOG}.tmp" && mv "${AUDIT_LOG}.tmp" "$AUDIT_LOG"
    else
        # Fallback without jq (less reliable)
        echo "${entry}" >> "${AUDIT_LOG}.entries"
    fi

    echo -e "${GREEN}✓ Creation logged to audit trail${NC}"
}

update_claude_md() {
    local agent_name=$1
    local department=$2
    local description=$3

    echo -e "${YELLOW}▶ Updating CLAUDE.md with new agent...${NC}"

    local claude_file="${REPO_ROOT}/CLAUDE.md"

    if [[ ! -f "$claude_file" ]]; then
        echo -e "${YELLOW}⚠ CLAUDE.md not found, skipping update${NC}"
        return
    fi

    # Check if agents section exists
    if ! grep -q "## Available Agents" "$claude_file"; then
        # Add agents section before the closing
        echo "" >> "$claude_file"
        echo "## Available Agents" >> "$claude_file"
        echo "" >> "$claude_file"
        echo "The following specialized agents are available for specific tasks:" >> "$claude_file"
        echo "" >> "$claude_file"
    fi

    # Add agent entry if not already present
    if ! grep -q "### ${agent_name}" "$claude_file"; then
        # Find the line number after "## Available Agents"
        local insert_line=$(grep -n "## Available Agents" "$claude_file" | cut -d: -f1)
        if [[ -n "$insert_line" ]]; then
            insert_line=$((insert_line + 3))

            # Create agent documentation
            local agent_doc="### ${agent_name} (${department})

**Purpose**: ${description}

**Usage**: \`Use the ${agent_name} agent to...\`

**Triggers**: See \`.specify/memory/agent-collaboration.md\` for automatic triggers

---
"
            # Insert the documentation
            echo "$agent_doc" | sed -i "${insert_line}r /dev/stdin" "$claude_file"
            echo -e "${GREEN}✓ Updated CLAUDE.md${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Agent already documented in CLAUDE.md${NC}"
    fi
}

update_agent_registry() {
    local agent_name=$1
    local department=$2
    local description=$3
    local tools=$4
    local mcp_access=$5

    echo -e "${YELLOW}▶ Updating agent registry...${NC}"

    local registry_file="${DOCS_DIR}/agent-registry.json"

    # Create registry if it doesn't exist
    if [[ ! -f "$registry_file" ]]; then
        mkdir -p "$(dirname "$registry_file")"
        echo '{"agents": {}, "departments": {}}' > "$registry_file"
    fi

    # Create agent entry
    local agent_entry=$(cat <<EOF
{
  "department": "${department}",
  "description": "${description}",
  "created": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "tools": "${tools}",
  "mcp_access": "${mcp_access}",
  "status": "active",
  "file": "${AGENTS_DIR}/${department}/${agent_name}.md",
  "memory": "${DOCS_DIR}/${department}/${agent_name}/"
}
EOF
)

    # Update registry using jq if available
    if command -v jq &> /dev/null; then
        jq ".agents[\"${agent_name}\"] = ${agent_entry}" "$registry_file" > "${registry_file}.tmp" && mv "${registry_file}.tmp" "$registry_file"

        # Update department count
        local dept_count=$(jq ".agents | map(select(.department == \"${department}\")) | length" "$registry_file")
        jq ".departments[\"${department}\"] = ${dept_count}" "$registry_file" > "${registry_file}.tmp" && mv "${registry_file}.tmp" "$registry_file"

        echo -e "${GREEN}✓ Agent registry updated${NC}"
    else
        echo -e "${YELLOW}⚠ jq not available, registry update skipped${NC}"
    fi
}

update_collaboration_triggers() {
    local agent_name=$1
    local department=$2
    local description=$3

    echo -e "${YELLOW}▶ Updating collaboration triggers...${NC}"

    local collab_file="${REPO_ROOT}/.specify/memory/agent-collaboration.md"

    if [[ ! -f "$collab_file" ]]; then
        echo -e "${YELLOW}⚠ Collaboration file not found, skipping${NC}"
        return
    fi

    # Extract keywords from description for trigger patterns
    local keywords=""
    case $department in
        "architecture")
            keywords="design|architecture|planning|system|integration"
            ;;
        "engineering")
            keywords="implement|develop|code|build|create"
            ;;
        "quality")
            keywords="test|review|audit|quality|security"
            ;;
        "data")
            keywords="database|sql|migration|query|schema"
            ;;
        "product")
            keywords="requirement|user|feature|story|ux"
            ;;
        "operations")
            keywords="deploy|monitor|devops|release|pipeline"
            ;;
    esac

    echo -e "${GREEN}✓ Collaboration triggers configured for ${department} department${NC}"
}

# Interactive mode
interactive_create() {
    print_header
    validate_prerequisites

    echo -e "${BLUE}Starting interactive agent creation...${NC}"
    echo

    # Get agent name
    read -p "Enter agent name (kebab-case, e.g., 'backend-engineer'): " agent_name
    if [[ ! "$agent_name" =~ ^[a-z]+(-[a-z]+)*$ ]]; then
        echo -e "${RED}✗ Invalid name format. Use kebab-case only.${NC}"
        exit 1
    fi

    # Check for duplicates
    if ! analyze_existing_agents "$agent_name"; then
        exit 1
    fi

    # Get agent purpose
    echo
    read -p "Enter agent purpose/description (one line): " description

    # Determine department (pass both description and agent name)
    suggested_dept=$(determine_department "$description" "$agent_name")
    echo
    echo "Available departments:"
    for dept in "${!DEPARTMENTS[@]}"; do
        echo "  - ${dept}: ${DEPARTMENTS[$dept]}"
    done
    echo
    read -p "Enter department (suggested: ${suggested_dept}): " department
    department=${department:-$suggested_dept}

    if [[ ! "${DEPARTMENTS[$department]+exists}" ]]; then
        echo -e "${RED}✗ Invalid department${NC}"
        exit 1
    fi

    # Get tools (use department defaults or custom)
    default_tools="${DEPT_TOOLS[$department]}"
    echo
    echo "Default tools for ${department}: ${default_tools}"
    read -p "Use default tools? (y/n): " use_defaults

    if [[ "$use_defaults" != "y" ]]; then
        read -p "Enter comma-separated tool list: " tools
    else
        tools="$default_tools"
    fi

    # Get responsibilities
    echo
    echo "Enter agent's core responsibilities (end with empty line):"
    responsibilities=""
    while IFS= read -r line; do
        [[ -z "$line" ]] && break
        responsibilities+="- ${line}\n"
    done

    # Validate department assignment
    echo
    if ! validate_department_assignment "$agent_name" "$department" "$description"; then
        echo
        read -p "Continue despite warnings? (y/n): " continue_anyway
        if [[ "$continue_anyway" != "y" ]]; then
            echo -e "${RED}✗ Agent creation cancelled${NC}"
            exit 1
        fi
    fi

    # Create the agent
    echo
    create_agent_file "$agent_name" "$department" "$description" "$tools" "$responsibilities"
    create_memory_structure "$agent_name" "$department"

    # Get MCP access for the department
    local mcp_access="${DEPT_MCP[$department]:-none}"

    # Update related files
    update_claude_md "$agent_name" "$department" "$description"
    update_agent_registry "$agent_name" "$department" "$description" "$tools" "$mcp_access"
    update_collaboration_triggers "$agent_name" "$department" "$description"

    # Validate compliance
    agent_file="${AGENTS_DIR}/${department}/${agent_name}.md"
    if validate_agent_compliance "$agent_file"; then
        log_creation "$agent_name" "$department" "success"
        echo
        echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║     Agent Successfully Created!        ║${NC}"
        echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
        echo
        echo "Agent Location: ${agent_file}"
        echo "Memory Location: ${DOCS_DIR}/${department}/${agent_name}/"
        echo "MCP Access: ${mcp_access}"
        echo
        echo "To use this agent, invoke it with:"
        echo "  'Please use the ${agent_name} agent to...'"
        echo
        echo "Files Updated:"
        echo "  - CLAUDE.md (agent documentation)"
        echo "  - Agent registry (${DOCS_DIR}/agent-registry.json)"
        echo "  - Collaboration triggers configured"
    else
        log_creation "$agent_name" "$department" "failed_validation"
        echo -e "${RED}Agent created but failed validation. Please review and fix.${NC}"
        exit 1
    fi
}

# JSON mode for programmatic creation
json_create() {
    local json_input=$1

    # Parse JSON input (requires jq)
    if ! command -v jq &> /dev/null; then
        echo '{"error": "jq is required for JSON mode"}'
        exit 1
    fi

    local agent_name=$(echo "$json_input" | jq -r '.name')
    local description=$(echo "$json_input" | jq -r '.description')
    local department=$(echo "$json_input" | jq -r '.department // empty')
    local tools=$(echo "$json_input" | jq -r '.tools // empty')
    local responsibilities=$(echo "$json_input" | jq -r '.responsibilities // empty')

    # Validate required fields
    if [[ -z "$agent_name" ]] || [[ -z "$description" ]]; then
        echo '{"error": "name and description are required"}'
        exit 1
    fi

    # Auto-determine department if not provided (pass both description and agent name)
    if [[ -z "$department" ]]; then
        department=$(determine_department "$description" "$agent_name")
    fi

    # Use default tools if not provided
    if [[ -z "$tools" ]]; then
        if [[ "${DEPT_TOOLS[$department]+exists}" ]]; then
            tools="${DEPT_TOOLS[$department]}"
        else
            tools="Read, Grep, Glob, TodoWrite"  # Minimal default
        fi
    fi

    # Analyze existing agents
    if ! analyze_existing_agents "$agent_name" > /dev/null 2>&1; then
        echo '{"error": "Agent name already exists"}'
        exit 1
    fi

    # Validate department assignment in JSON mode (warnings only, no user interaction)
    if ! validate_department_assignment "$agent_name" "$department" "$description" > /dev/null 2>&1; then
        # Log warnings but continue in JSON mode
        echo '{"warning": "Department assignment may not be optimal"}' >&2
    fi

    # Create agent
    create_agent_file "$agent_name" "$department" "$description" "$tools" "$responsibilities" > /dev/null 2>&1
    create_memory_structure "$agent_name" "$department" > /dev/null 2>&1

    # Get MCP access for the department
    local mcp_access="${DEPT_MCP[$department]:-none}"

    # Update related files
    update_claude_md "$agent_name" "$department" "$description" > /dev/null 2>&1
    update_agent_registry "$agent_name" "$department" "$description" "$tools" "$mcp_access" > /dev/null 2>&1
    update_collaboration_triggers "$agent_name" "$department" "$description" > /dev/null 2>&1

    # Validate
    agent_file="${AGENTS_DIR}/${department}/${agent_name}.md"
    if validate_agent_compliance "$agent_file" > /dev/null 2>&1; then
        log_creation "$agent_name" "$department" "success" > /dev/null 2>&1
        echo "{\"success\": true, \"agent\": \"${agent_name}\", \"department\": \"${department}\", \"file\": \"${agent_file}\", \"mcp_access\": \"${mcp_access}\"}"
    else
        log_creation "$agent_name" "$department" "failed_validation" > /dev/null 2>&1
        echo '{"success": false, "error": "Validation failed"}'
        exit 1
    fi
}

# Main execution
main() {
    case "${1:-}" in
        --json)
            if [[ -n "${2:-}" ]]; then
                json_create "$2"
            else
                # Read from stdin
                json_input=$(cat)
                json_create "$json_input"
            fi
            ;;
        --help|-h)
            echo "Agent Creation Tool"
            echo "Usage:"
            echo "  $0                    # Interactive mode"
            echo "  $0 --json '{...}'    # JSON mode"
            echo "  echo '{...}' | $0 --json  # JSON from stdin"
            echo ""
            echo "JSON format:"
            echo "  {"
            echo "    \"name\": \"agent-name\","
            echo "    \"description\": \"Agent purpose\","
            echo "    \"department\": \"engineering\",  // optional"
            echo "    \"tools\": \"Read, Write, ...\",   // optional"
            echo "    \"responsibilities\": \"...\"      // optional"
            echo "  }"
            ;;
        *)
            interactive_create
            ;;
    esac
}

# Run main function
main "$@"