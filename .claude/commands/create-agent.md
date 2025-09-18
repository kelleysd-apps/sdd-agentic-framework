---
description: Create a new specialized subagent with constitutional compliance and proper department classification. MUST use the subagent-architect agent for SDD-compliant agent creation.
---

**IMPORTANT**: This command MUST invoke the subagent-architect agent to ensure proper SDD compliance and constitutional validation.

Given the agent name and description provided as arguments, do this:

0. **FIRST**: Use the Task tool to invoke the subagent-architect agent:
   ```
   Task: Create SDD-compliant agent
   Agent: subagent-architect
   Purpose: Ensure constitutional compliance and proper architecture
   ```

1. Parse the arguments:
   - If no arguments: Start interactive mode
   - If one argument: Use as agent name, ask for description
   - If two+ arguments: First is name, rest is description

2. Validate the agent name:
   - Must be in kebab-case format (lowercase with hyphens)
   - Check for existing agents with same name

3. Analyze the description to determine department:
   - Architecture: system, design, planning, integration keywords
   - Engineering: develop, backend, frontend, api, code keywords
   - Quality: test, qa, review, audit, security keywords
   - Data: database, sql, pipeline, analytics keywords
   - Product: requirement, user, ux, feature keywords
   - Operations: deploy, devops, monitor, incident keywords

4. Execute agent creation:
   ```bash
   echo '{"name": "AGENT_NAME", "description": "DESCRIPTION"}' | /workspaces/ioun-ai/.specify/scripts/bash/create-agent.sh --json
   ```

5. Verify the agent was created successfully:
   - Check for agent file in `.claude/agents/AGENT_NAME.md`
   - Verify constitutional compliance
   - Confirm memory structure created

6. Report results:
   - Show agent name, department, and location
   - Provide usage instructions: "Use the AGENT_NAME agent to..."
   - Display any validation warnings

The script will automatically:
- Set appropriate tool restrictions based on department
- Include constitutional references
- Create memory structure in `.docs/agents/`
- Log creation to audit trail

Note: All agents must comply with constitutional requirements and governance policies.