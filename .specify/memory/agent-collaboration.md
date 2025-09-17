# Agent Collaboration Framework

## Agent Usage Triggers for Claude Code

### Automatic Agent Invocation

Claude Code should automatically consider using specialized agents when:

#### Architecture Agent Triggers
- User asks about system design or architecture
- Planning new features or major refactoring
- Reviewing integration patterns
- Keywords: "design", "architecture", "structure", "planning", "integration"

#### Engineering Agent Triggers
- Implementing new features
- Writing or modifying code
- Creating libraries or modules
- Keywords: "implement", "develop", "code", "build", "create function"

#### Quality Agent Triggers
- Running tests or reviewing test coverage
- Code review requests
- Security or performance audits
- Keywords: "test", "review", "audit", "quality", "coverage", "security"

#### Data Agent Triggers
- Database schema changes
- Data migration tasks
- Query optimization
- Keywords: "database", "sql", "migration", "schema", "query"

#### Product Agent Triggers
- Defining requirements
- User story creation
- UX/UI discussions
- Keywords: "requirement", "user story", "feature", "UX", "interface"

#### Operations Agent Triggers
- Deployment tasks
- Monitoring setup
- CI/CD configuration
- Keywords: "deploy", "monitor", "devops", "release", "pipeline"

## Agent Collaboration Patterns

### Sequential Collaboration
When tasks have dependencies, agents work in sequence:

```
Product Agent (requirements) →
Architecture Agent (design) →
Engineering Agent (implementation) →
Quality Agent (testing) →
Operations Agent (deployment)
```

### Parallel Collaboration
When tasks are independent, agents work simultaneously:

```
[Parallel Execution]
├── Engineering Agent A (API development)
├── Engineering Agent B (Frontend development)
└── Data Agent (Database setup)
```

### Review Pattern
Critical changes require multi-agent review:

```
Engineering Agent (implementation) →
[Parallel Review]
├── Architecture Agent (design compliance)
├── Quality Agent (code quality)
└── Security Agent (vulnerability check)
```

## MCP Server Assignments by Department

### Architecture Department
```json
{
  "mcpServers": {
    "documentation": ["mcp__ref-tools", "mcp__supabase__search_docs"],
    "search": ["mcp__perplexity", "WebSearch"],
    "analysis": ["mcp__claude-context"]
  }
}
```

### Engineering Department
```json
{
  "mcpServers": {
    "ide": ["mcp__ide"],
    "database": ["mcp__supabase"],
    "documentation": ["mcp__ref-tools"],
    "browser": ["mcp__browsermcp"],
    "search": ["mcp__claude-context", "WebSearch"]
  }
}
```

### Quality Department
```json
{
  "mcpServers": {
    "testing": ["mcp__ide__executeCode"],
    "analysis": ["mcp__ide__getDiagnostics"],
    "documentation": ["mcp__ref-tools"]
  }
}
```

### Data Department
```json
{
  "mcpServers": {
    "database": ["mcp__supabase"],
    "migration": ["mcp__supabase__apply_migration"],
    "query": ["mcp__supabase__execute_sql"]
  }
}
```

### Product Department
```json
{
  "mcpServers": {
    "documentation": ["mcp__ref-tools"],
    "browser": ["mcp__browsermcp"],
    "search": ["WebSearch", "mcp__perplexity"]
  }
}
```

### Operations Department
```json
{
  "mcpServers": {
    "deployment": ["mcp__supabase__deploy_edge_function"],
    "monitoring": ["mcp__supabase__get_logs"],
    "infrastructure": ["mcp__supabase__create_project"]
  }
}
```

## Inter-Agent Communication Protocol

### Message Format
```json
{
  "from_agent": "sender-name",
  "to_agent": "recipient-name",
  "timestamp": "ISO-8601",
  "message_type": "request|response|notification",
  "payload": {
    "task": "description",
    "context": {},
    "priority": "high|medium|low",
    "deadline": "ISO-8601"
  },
  "thread_id": "uuid",
  "requires_response": boolean
}
```

### Handoff Protocol

1. **Initiation**: Source agent prepares handoff package
2. **Validation**: Verify target agent exists and is active
3. **Transfer**: Pass context and requirements
4. **Acknowledgment**: Target agent confirms receipt
5. **Execution**: Target agent performs task
6. **Completion**: Results passed back or to next agent

### Shared Memory Access

Agents share knowledge through structured memory:

```
.docs/agents/shared/
├── context/          # Current project context
├── decisions/        # Architectural decisions
├── knowledge/        # Domain knowledge base
└── workflows/        # Active workflow states
```

## Conflict Resolution

### Priority Levels
1. **User Directive** - Overrides all agent decisions
2. **Constitutional Requirement** - Cannot be overridden
3. **Department Lead Agent** - Has authority within department
4. **Individual Agent** - Follows department guidelines

### Disagreement Protocol
1. Document disagreement with rationale
2. Escalate to department lead agent
3. If unresolved, request user decision
4. Log decision for future reference

## Agent Selection Algorithm

```python
def select_agent(task):
    # 1. Analyze task keywords and context
    keywords = extract_keywords(task)
    context = analyze_context(task)

    # 2. Score each agent for relevance
    scores = {}
    for agent in available_agents:
        scores[agent] = calculate_relevance(agent, keywords, context)

    # 3. Check for multi-agent requirement
    if requires_collaboration(task):
        return select_agent_team(scores, task)

    # 4. Return highest scoring agent
    return max(scores, key=scores.get)
```

## Collaboration Rules

### Must Collaborate
- **Cross-department tasks**: Require agents from multiple departments
- **Complex features**: Architecture + Engineering + Quality
- **Production changes**: Engineering + Quality + Operations
- **Data migrations**: Data + Engineering + Operations

### Cannot Collaborate
- **Conflicting departments**: Product agents cannot override Engineering decisions
- **Security boundaries**: Agents cannot share credentials
- **Audit isolation**: Quality agents work independently for reviews

### Collaboration Triggers
- Task complexity exceeds single agent capability
- Multiple expertise areas required
- User explicitly requests multiple perspectives
- Constitutional requirement for review

## Performance Metrics

### Collaboration Efficiency
- Handoff time < 2 seconds
- Context preservation > 95%
- Task completion rate > 90%
- User satisfaction > 4/5

### Agent Utilization
- Balanced workload distribution
- No single agent bottleneck
- Parallel execution when possible
- Resource optimization

## Automation Rules

### Auto-invoke Agents When:
1. **Pattern Match**: Task matches agent expertise pattern
2. **Workflow Stage**: Specific workflow stage requires agent
3. **Quality Gate**: Review or validation needed
4. **User Preference**: User has set agent preferences

### Do Not Auto-invoke When:
1. User explicitly requests direct assistance
2. Task is trivial (< 2 minute execution)
3. Previous agent failure on similar task
4. User has disabled automation

## Updates Required When Agent Created

### Files to Update Automatically

1. **CLAUDE.md**
   - Add agent to available agents list
   - Include usage examples
   - Document trigger conditions

2. **Constitution.md** (if needed)
   - Add department-specific principles
   - Update collaboration rules

3. **Agent Registry**
   ```json
   {
     "agents": {
       "agent-name": {
         "department": "...",
         "created": "ISO-8601",
         "triggers": [],
         "mcp_access": [],
         "collaboration_rules": {}
       }
     }
   }
   ```

4. **Department Index**
   - Update department agent list
   - Refresh capability matrix
   - Update collaboration graph

---

**Note**: This framework ensures efficient agent collaboration while maintaining clear boundaries and constitutional compliance. All agents must respect these patterns for optimal system performance.