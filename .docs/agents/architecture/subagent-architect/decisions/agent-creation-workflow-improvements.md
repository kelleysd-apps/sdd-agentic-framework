# Agent Creation Workflow Improvements Needed

**Date**: 2025-09-18
**Issue**: subagent-architect agent failed to properly execute agent creation tasks

## Problems Identified

### 1. Tool Permission Limitations

**Current State**:
- subagent-architect has: Read, Grep, Glob, WebSearch, TodoWrite
- **Missing Critical Tools**:
  - `Bash` - Cannot execute create-agent.sh script
  - `Write/Edit` - Cannot customize agent files after creation

**Impact**: Agent can only provide instructions, not execute creation

**Solution Options**:
1. Add Bash tool to subagent-architect
2. Create a separate "agent-creator" with execution permissions
3. Have subagent-architect delegate to Claude Code for execution

### 2. Department Classification Logic Flaws

**Current Issues**:
- Keyword matching is too simplistic and order-dependent
- "design" keyword incorrectly classifies frontend work as architecture
- "deployment" doesn't match "deploy" pattern for operations

**Examples of Misclassification**:
- `frontend-specialist`: Had "design" → Incorrectly went to Architecture
- `devops-engineer`: Had "deployment" → Missed Operations match

**Solution**: Improve keyword matching:
```bash
# Better approach:
# 1. Score each department based on keyword matches
# 2. Pick highest scoring department
# 3. Consider context and combinations
```

### 3. Missing Validation & Correction

**Current State**:
- No validation that department matches agent purpose
- No ability to override incorrect classification
- Manual fixes required after creation

**Needed Features**:
- Department validation based on agent type
- Ability to specify department explicitly
- Post-creation validation and correction

## Recommended Fixes

### Immediate Fix: Update subagent-architect Tools

```yaml
# Current
tools: Read, Grep, Glob, WebSearch, TodoWrite

# Recommended
tools: Read, Write, Edit, Bash, Grep, Glob, TodoWrite
```

### Script Improvements

1. **Better Department Detection**:
   - Use weighted scoring instead of first-match
   - Consider multiple keywords together
   - Allow explicit department override

2. **Add Validation**:
   ```bash
   validate_department_match() {
     local agent_name=$1
     local department=$2

     # Check if agent type matches department
     if [[ "$agent_name" =~ frontend|ui|react ]] && [[ "$department" != "engineering" ]]; then
       echo "Warning: Frontend agent in wrong department"
     fi
   }
   ```

3. **Post-Creation Checks**:
   - Verify files created in correct locations
   - Validate registry entries
   - Check department counts

### Workflow Improvements

1. **Two-Phase Creation**:
   - Phase 1: Validate and prepare (subagent-architect)
   - Phase 2: Execute creation (needs Bash access)

2. **Add Confirmation Step**:
   ```
   Suggested department: architecture
   Is this correct? (y/n/specify):
   ```

3. **Better Error Handling**:
   - Rollback on failure
   - Clear error messages
   - Automatic correction attempts

## Lessons Learned

1. **Agent Tool Restrictions**: Architecture agents need execution tools for creation tasks
2. **Keyword Matching**: Simple grep patterns insufficient for complex classification
3. **Validation Critical**: Must validate department assignment before file creation
4. **Manual Intervention**: Current workflow requires too much manual correction

## Action Items

- [ ] Update subagent-architect tool permissions
- [ ] Improve create-agent.sh department detection
- [ ] Add validation and correction mechanisms
- [ ] Create test suite for agent creation
- [ ] Document proper workflow in agent knowledge base

## Testing Recommendations

Test agent creation with:
- Frontend agents (should go to engineering)
- Backend agents (should go to engineering)
- DevOps agents (should go to operations)
- Data agents (should go to data department)
- Architecture agents (should go to architecture)

Ensure each type is correctly classified without manual intervention.