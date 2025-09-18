# Create Agent Workflow

## Integration with /create-agent Command

The `subagent-architect` agent is the designated authority for all agent creation tasks in the SDD framework.

### Automatic Invocation

This agent is automatically invoked when:

1. **User runs `/create-agent` command**
   - Command in `.claude/commands/create-agent.md` specifies to use subagent-architect
   - Ensures SDD compliance and constitutional validation

2. **User requests agent creation directly**
   - Keywords: "create agent", "new agent", "build agent", "design subagent"
   - Patterns defined in `.specify/memory/agent-collaboration.md`

3. **Agent architecture tasks**
   - Designing agent workflows
   - Validating constitutional compliance
   - Setting department boundaries

### Workflow Process

1. **Receive Request**
   - Parse agent name and description
   - Validate naming conventions (kebab-case)

2. **Constitutional Validation**
   - Ensure request aligns with constitution.md principles
   - Verify department classification is appropriate

3. **Execute Creation**
   - Call `.specify/scripts/bash/create-agent.sh` with JSON parameters
   - Monitor creation process for compliance

4. **Post-Creation Tasks**
   - Verify agent file created in `.claude/agents/{department}/`
   - Confirm memory structure in `.docs/agents/{department}/{agent}/`
   - Check registry updates
   - Validate CLAUDE.md documentation updates

### Command Integration

The `/create-agent` command (defined in `.claude/commands/create-agent.md`) now includes:
- Mandatory invocation of subagent-architect
- SDD compliance checks
- Constitutional validation steps

### Script Integration

The `create-agent.sh` script includes:
- Header note about subagent-architect usage
- Constitutional compliance validation
- Automatic documentation updates

### Documentation Updates

All relevant documentation has been updated:
- **CLAUDE.md**: Notes automatic subagent-architect invocation
- **README.md**: Highlights subagent-architect role
- **agent-collaboration.md**: Defines triggers for agent creation
- **agent-creation-policy.md**: Mandates subagent-architect usage

### Testing the Workflow

To test agent creation:
```bash
/create-agent test-agent "Test agent for validation purposes"
```

Expected behavior:
1. Claude Code recognizes /create-agent command
2. Automatically invokes subagent-architect agent
3. Agent validates and executes creation
4. Reports success with file locations

### Troubleshooting

If agent creation bypasses subagent-architect:
- Check `.specify/memory/agent-collaboration.md` triggers
- Verify CLAUDE.md agent list includes subagent-architect
- Ensure command file references agent invocation
- Review audit log for creation records