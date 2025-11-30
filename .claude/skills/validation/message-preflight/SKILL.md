---
name: message-preflight
description: |
  MANDATORY pre-flight compliance check that MUST execute at the START of every user message.
  Implements the Work Session Initiation Protocol (Constitutional Principle X).

  This skill ensures constitutional compliance BEFORE any work begins by:
  1. Acknowledging the constitution's 15 principles
  2. Scanning the user message for domain trigger keywords
  3. Making an explicit delegation decision
  4. Authorizing execution only after all steps complete

  Triggered by: EVERY user message (mandatory, no exceptions)

  This is a PROACTIVE skill - violations are prevented, not just detected.
allowed-tools: Read, Grep
---

# Message Pre-Flight Compliance Check

## MANDATORY EXECUTION

This skill MUST execute at the START of every user message. No exceptions.

**Why This Exists**: Constitutional Principle X requires the 4-step Work Session Initiation Protocol for EVERY task. This skill enforces that requirement proactively.

**What It Prevents**:
- Executing specialized work without delegation
- Skipping constitution acknowledgment
- Forgetting to analyze task domains
- Autonomous git operations (Principle VI)

## The 4-Step Protocol

### Step 1: Constitution Acknowledgment

**Action**: Confirm awareness of the 15 constitutional principles.

**Key Principles to Remember**:
- **Principle II (Test-First)**: TDD is mandatory, >80% coverage
- **Principle VI (Git Approval)**: NO autonomous git operations
- **Principle X (Agent Delegation)**: Specialized work → specialized agents
- **Principle XV (File Organization)**: Verify before creating files/folders

**Mental Checklist**:
```
[ ] I am aware of the 15 constitutional principles
[ ] I know Principles I-III are IMMUTABLE
[ ] I know Principle VI prohibits autonomous git operations
[ ] I know Principle X requires delegation for specialized work
[ ] I know Principle XV requires verification before file creation
```

### Step 2: Domain Analysis

**Action**: Scan the user message for domain trigger keywords.

**Domain → Keyword → Agent Mapping**:

| Domain | Trigger Keywords | Delegate To |
|--------|------------------|-------------|
| Frontend | UI, component, React, CSS, responsive, page, form | frontend-specialist |
| Backend | API, endpoint, server, auth, middleware, service | backend-architect |
| Database | schema, migration, query, RLS, index, SQL, table | database-specialist |
| Testing | test, TDD, E2E, coverage, mock, assertion, QA | testing-specialist |
| Security | auth, encryption, XSS, SQL injection, secrets | security-specialist |
| Performance | optimize, cache, benchmark, latency, speed | performance-engineer |
| DevOps | deploy, CI/CD, Docker, infrastructure, pipeline | devops-engineer |
| Specification | spec, requirements, user story, acceptance criteria | specification-agent |
| Planning | /plan, research, contract design, data model | planning-agent |
| Tasks | /tasks, task list, breakdown, dependencies | tasks-agent |
| Multi-Domain | 2+ domains detected, complex feature | task-orchestrator |

**Scan Process**:
1. Read the user message
2. Identify any domain keywords present
3. Count how many domains are involved
4. Note which agents would be needed

### Step 3: Delegation Decision

**Action**: Make an explicit decision based on domain analysis.

**Decision Logic**:
```
IF 0 domains detected:
  → May execute directly (simple/informational task)

IF 1 domain detected:
  → MUST delegate to the specialist agent for that domain

IF 2+ domains detected:
  → MUST delegate to task-orchestrator
  → task-orchestrator will coordinate specialists
```

**Critical Rule**: General-purpose agents MUST NOT execute specialized work directly.

### Step 4: Execution Authorization

**Action**: Confirm all steps complete before proceeding.

**Authorization Checklist**:
```
[ ] Step 1: Constitution acknowledged
[ ] Step 2: Domains analyzed
[ ] Step 3: Delegation decision made
[ ] Step 4: Ready to execute (directly or via agent)
```

**Only proceed when all boxes are checked.**

## Output Format

After completing the 4-step protocol, output a brief compliance summary:

```
Constitutional Compliance Check:
- Domain(s): [none | single: <domain> | multi: <domains>]
- Delegation: [direct execution | <agent-name>]
- Git operations: [none planned | will request approval]
- Proceeding with: [action description]
```

**Examples**:

```
Constitutional Compliance Check:
- Domain(s): none
- Delegation: direct execution
- Git operations: none planned
- Proceeding with: answering question about file structure
```

```
Constitutional Compliance Check:
- Domain(s): single: database
- Delegation: database-specialist
- Git operations: none planned
- Proceeding with: delegating schema design to specialist
```

```
Constitutional Compliance Check:
- Domain(s): multi: frontend, backend, database
- Delegation: task-orchestrator
- Git operations: will request approval
- Proceeding with: coordinating full-stack feature implementation
```

## Examples

### Example 1: Simple Question (No Delegation)

**User Message**: "What files are in the src directory?"

**Pre-Flight Check**:
1. **Constitution**: Acknowledged (14 principles, key: II, VI, X)
2. **Domain Analysis**: No domain keywords detected
3. **Delegation Decision**: Direct execution (informational query)
4. **Authorization**: All steps complete

**Output**:
```
Constitutional Compliance Check:
- Domain(s): none
- Delegation: direct execution
- Git operations: none planned
- Proceeding with: listing directory contents
```

### Example 2: Single Domain (Delegate to Specialist)

**User Message**: "Create a user registration form component"

**Pre-Flight Check**:
1. **Constitution**: Acknowledged
2. **Domain Analysis**: Keywords detected: "form", "component" → Frontend domain
3. **Delegation Decision**: Single domain → delegate to frontend-specialist
4. **Authorization**: All steps complete

**Output**:
```
Constitutional Compliance Check:
- Domain(s): single: frontend
- Delegation: frontend-specialist
- Git operations: none planned
- Proceeding with: delegating UI component creation to specialist
```

### Example 3: Multi-Domain (Delegate to Orchestrator)

**User Message**: "Implement user authentication with JWT tokens and database storage"

**Pre-Flight Check**:
1. **Constitution**: Acknowledged
2. **Domain Analysis**: Keywords detected:
   - "authentication", "JWT" → Backend
   - "database", "storage" → Database
   - "authentication" → Security
3. **Delegation Decision**: 3 domains → delegate to task-orchestrator
4. **Authorization**: All steps complete

**Output**:
```
Constitutional Compliance Check:
- Domain(s): multi: backend, database, security
- Delegation: task-orchestrator
- Git operations: will request approval
- Proceeding with: coordinating multi-agent authentication implementation
```

### Example 4: Git Operation Detected

**User Message**: "Commit my changes and push to main"

**Pre-Flight Check**:
1. **Constitution**: Acknowledged - **Principle VI ALERT**
2. **Domain Analysis**: Git operation keywords detected
3. **Delegation Decision**: Direct execution BUT requires approval
4. **Authorization**: All steps complete, approval required

**Output**:
```
Constitutional Compliance Check:
- Domain(s): none (git operation)
- Delegation: direct execution
- Git operations: APPROVAL REQUIRED (Principle VI)
- Proceeding with: requesting user approval before any git operations
```

## Violation Handling

### If You Catch Yourself Violating

If you realize you started work without running this protocol:

1. **STOP** immediately
2. **ACKNOWLEDGE** the violation
3. **CORRECT** by running the 4-step protocol now
4. **PROCEED** only after completing all steps

**Self-Correction Template**:
```
[CORRECTION] I started work without completing the pre-flight check.

Constitutional Compliance Check (corrected):
- Domain(s): [analysis]
- Delegation: [decision]
- Git operations: [status]
- Proceeding with: [corrected action]
```

### Common Violations to Avoid

1. **Skipping to implementation** without domain analysis
2. **Executing specialized work** without delegating to specialist
3. **Running git commands** without user approval
4. **Ignoring multi-domain** complexity (treating as single domain)

## Constitutional Compliance

This skill directly implements **Principle X: Agent Delegation Protocol**.

**From the Constitution (v1.5.0)**:

> **Work Session Initiation Protocol (MANDATORY for EVERY task)**:
>
> **Step 1: READ CONSTITUTION** - First action of any session
> **Step 2: ANALYZE TASK DOMAIN** - Scan for trigger keywords
> **Step 3: DELEGATION DECISION** - Delegate if triggers matched
> **Step 4: EXECUTION** - Execute directly OR invoke specialized agent

This skill automates and enforces this protocol.

**Critical Principles Enforced**:

| Principle | How This Skill Enforces It |
|-----------|---------------------------|
| II (Test-First) | Reminds about TDD requirement |
| VI (Git Approval) | Flags git operations, requires approval |
| X (Agent Delegation) | Core purpose - delegation enforcement |

## Validation

Verify the skill executed correctly:

- [ ] Constitution acknowledgment completed (Step 1)
- [ ] Domain keywords scanned (Step 2)
- [ ] Domain count determined (0, 1, or 2+)
- [ ] Delegation decision made (Step 3)
- [ ] Compliance summary output provided
- [ ] Appropriate agent delegated (if needed)
- [ ] Git operations flagged (if detected)

## Related Skills

- **domain-detection**: Detailed domain analysis (this skill uses simplified version)
- **constitutional-compliance**: Full compliance validation (post-work, this is pre-work)

## References

- Constitution v1.5.0: `.specify/memory/constitution.md`
- Agent Collaboration Triggers: `.specify/memory/agent-collaboration-triggers.md`
- Domain Detection Skill: `.claude/skills/validation/domain-detection/SKILL.md`
