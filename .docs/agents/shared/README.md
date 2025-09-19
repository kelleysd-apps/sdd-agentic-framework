# Agent Shared Memory

This directory contains shared knowledge and state that all agents can access for coordination and context preservation.

## Directory Structure

### `/context/`
Current project context and state information shared across agent workflows.
- Active feature specifications
- Current implementation state
- User preferences and constraints
- Project configuration

### `/decisions/`
Architectural and design decisions made during agent collaboration.
- Technical choices with rationale
- Trade-offs and alternatives considered
- Constraints and requirements driving decisions
- Decision audit trail

### `/knowledge/`
Domain knowledge base accumulated across agent interactions.
- Common patterns and solutions
- Project-specific conventions
- Technology stack details
- External API documentation references

### `/workflows/`
Active workflow states for multi-agent orchestrations.
- In-progress workflow definitions
- Checkpoint states for recovery
- Inter-agent handoff packages
- Workflow execution history

## Access Protocol

### Reading Shared Memory
All agents have read access to shared memory. Use appropriate file locking when reading during active workflows.

### Writing Shared Memory
1. Agents must document the source and timestamp of updates
2. Use atomic writes to prevent corruption
3. Maintain version history for critical decisions
4. Clean up stale workflow states after completion

### Context Serialization Format
```json
{
  "workflow_id": "uuid",
  "timestamp": "ISO-8601",
  "phase": "current-phase",
  "agents_involved": ["agent-1", "agent-2"],
  "context": {
    "original_request": "user request",
    "constraints": [],
    "decisions": {},
    "progress": {}
  },
  "checkpoints": []
}
```

## Maintenance

- Workflow states older than 7 days should be archived
- Decision records are permanent and should not be deleted
- Context files should be updated atomically
- Knowledge base requires periodic consolidation

## Integration with Task Orchestrator

The task-orchestrator agent is responsible for:
1. Creating workflow state files when orchestrating
2. Managing context handoffs between agents
3. Cleaning up completed workflow states
4. Consolidating decisions into the decision log