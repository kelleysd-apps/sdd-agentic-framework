# Complete Agent Creation Workflow for Subagent-Architect

## Overview
This document provides the COMPLETE workflow for creating agents, including all post-creation tasks that must be performed.

## Full Workflow with Code Examples

### Step 1: Parse Agent Specification

When receiving an agent creation request with custom prompt:
```yaml
name: agent-name
description: Agent purpose and capabilities
tools: Read, Write, Bash, MultiEdit  # Custom tools
model: sonnet  # Custom model
---
Full custom prompt content...
```

### Step 2: Create Base Agent

```bash
echo '{"name": "agent-name", "description": "description"}' | \
.specify/scripts/bash/create-agent.sh --json
```

### Step 3: Apply Custom Prompt (CRITICAL)

The script creates a generic template. You MUST update it:

```python
# Use MultiEdit to update the agent file
MultiEdit(
    file_path=".claude/agents/{department}/{agent-name}.md",
    edits=[
        {
            "old_string": "model: inherit",
            "new_string": "model: sonnet"  # Or specified model
        },
        {
            "old_string": "tools: {default_tools}",
            "new_string": "tools: Read, Write, Bash, MultiEdit"  # Specified tools
        },
        {
            "old_string": "# {agent name} Agent\n\n## Constitutional Adherence",
            "new_string": "# Agent Name\n\n{FULL_CUSTOM_PROMPT}\n\n## Constitutional Adherence"
        }
    ]
)
```

### Step 4: Fix Department if Needed

Check if department classification is correct:

```bash
# If frontend-specialist ended up in architecture instead of engineering:

# 1. Create correct department directory if needed
mkdir -p .claude/agents/engineering

# 2. Move agent file
mv .claude/agents/architecture/frontend-specialist.md \
   .claude/agents/engineering/

# 3. Move memory structure
mv .docs/agents/architecture/frontend-specialist \
   .docs/agents/engineering/
```

### Step 5: Update Registry

```python
# Update agent registry with correct tools
Edit(
    file_path=".docs/agents/agent-registry.json",
    old_string='"tools": "Read, Grep, Glob, WebSearch, TodoWrite"',
    new_string='"tools": "Read, Write, Bash, MultiEdit"'
)

# Fix department
Edit(
    file_path=".docs/agents/agent-registry.json",
    old_string='"department": "architecture"',
    new_string='"department": "engineering"'
)

# Update department counts
Edit(
    file_path=".docs/agents/agent-registry.json",
    old_string='"architecture": 3, "engineering": 1',
    new_string='"architecture": 2, "engineering": 2'
)
```

### Step 6: Update CLAUDE.md

```python
Edit(
    file_path="CLAUDE.md",
    old_string="### agent-name (architecture)",
    new_string="### agent-name (engineering)"
)
```

### Step 7: Update Audit Log

```python
Edit(
    file_path=".docs/agents/audit/creation-log.json",
    old_string='"department": "architecture"',
    new_string='"department": "engineering"'
)
```

## Real Examples from Recent Creations

### Frontend-Specialist Fix
- **Problem**: Classified as architecture due to "design" keyword
- **Fix**: Moved to engineering, updated all references

### DevOps-Engineer Fix
- **Problem**: Classified as architecture, "deployment" didn't match "deploy"
- **Fix**: Moved to operations department

### Backend-Architect Fix
- **Problem**: Default tools assigned instead of custom
- **Fix**: Updated to Read, Write, Bash, MultiEdit

## Common Issues and Solutions

### Issue 1: Wrong Department
**Cause**: Keyword matching picked wrong department
**Solution**: Move files, update registry, CLAUDE.md, audit log

### Issue 2: Default Tools Instead of Custom
**Cause**: Script uses department defaults
**Solution**: Update both agent file header and registry

### Issue 3: Model Not Updated
**Cause**: Template has 'inherit' by default
**Solution**: Change to specified model (sonnet/haiku)

### Issue 4: Generic Template Content
**Cause**: Script creates template, not custom content
**Solution**: Replace with full custom prompt using MultiEdit

## Validation Commands

```bash
# Check agent location
ls -la .claude/agents/{department}/{agent-name}.md

# Verify memory structure
ls -la .docs/agents/{department}/{agent-name}/*/*.md

# Check registry
grep "agent-name" .docs/agents/agent-registry.json

# Verify in CLAUDE.md
grep "agent-name" CLAUDE.md
```

## Required Tools for Subagent-Architect

To perform all these tasks, subagent-architect MUST have:
- **Read**: To check created files
- **Write**: To create new files if needed
- **Edit/MultiEdit**: To update files with custom content
- **Bash**: To execute creation script and move files
- **Grep**: To search for content
- **Glob**: To find files

## Checklist for Every Agent Creation

- [ ] Run create-agent.sh script
- [ ] Apply custom prompt to agent file
- [ ] Update tools from defaults to specified
- [ ] Update model from inherit to specified
- [ ] Verify correct department classification
- [ ] Move files if department wrong
- [ ] Update registry with correct tools
- [ ] Update registry department if moved
- [ ] Fix department counts in registry
- [ ] Update CLAUDE.md if department changed
- [ ] Update audit log if department changed
- [ ] Verify memory files use agent-specific naming
- [ ] Test agent can be invoked

## Summary

The create-agent.sh script is just the FIRST step. It creates a template that MUST be customized. Without the post-creation tasks, agents will:
- Have wrong tools
- Use generic prompts
- Be in wrong departments
- Have 'inherit' model instead of specified

ALWAYS complete ALL post-creation tasks for a properly functioning agent.