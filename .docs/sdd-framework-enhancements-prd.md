# SDD Agentic Framework Enhancements - Product Requirements Document

**Version**: 1.0.0  
**Date**: 2025-11-06  
**Status**: Draft for Review  
**Target Repository**: https://github.com/kelleysd-apps/sdd-agentic-framework  
**Source Implementation**: Ioun AI Mobile Application (D&D Companion App)  
**Document Owner**: Claude Code (Anthropic)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Document Purpose](#document-purpose)
3. [Current State Analysis](#current-state-analysis)
4. [Enhancements Catalog](#enhancements-catalog)
5. [Implementation Recommendations](#implementation-recommendations)
6. [Appendices](#appendices)

---

## Executive Summary

### Overview

The Specification-Driven Development (SDD) Agentic Framework has undergone significant evolution during its application in the Ioun AI mobile application project (October 2024 - November 2025). This PRD documents **50+ substantial enhancements** across 7 major categories, representing a maturation from a lightweight specification framework into a comprehensive multi-agent development system with constitutional governance.

### Evolution Timeline

- **October 2024**: Original SDD framework adopted from https://github.com/kelleysd-apps/sdd-agentic-framework
- **October 2024 - March 2025**: Core constitutional principles established through real-world feature development
- **March - June 2025**: Multi-agent architecture formalized with 13 specialized agents
- **June - September 2025**: Workflow automation and policy framework matured
- **September - November 2025**: Integration infrastructure and governance mechanisms hardened

### Key Metrics

**Framework Scale**:
- 302 lines in constitution.md (v1.5.0, up from ~50 lines in original)
- 14 constitutional principles (vs 3 in original framework)
- 13 specialized agents across 6 departments (vs 0 in original)
- 4 slash commands with full automation (vs 1 basic command)
- 11 bash automation scripts (vs 2 basic scripts)
- 4 enhanced templates with validation (vs 2 basic templates)
- 24+ policy/workflow/reference documents (vs 0 in original)

**Enhancement Categories**:
1. **Constitutional Framework** (12 enhancements)
2. **Agent Architecture & Delegation** (11 enhancements)
3. **Workflow Automation** (8 enhancements)
4. **Documentation & Policies** (9 enhancements)
5. **Templates & Patterns** (6 enhancements)
6. **Integration Infrastructure** (7 enhancements)
7. **Quality & Governance** (5 enhancements)

### Business Value

**For Framework Adopters**:
- **Faster onboarding**: New developers have clear constitutional guardrails and delegation patterns
- **Higher quality**: Automated validation prevents common mistakes before they enter codebase
- **Scalability**: Multi-agent architecture enables parallel development across specialized domains
- **Consistency**: Templates and policies ensure uniform approach across teams
- **Auditability**: Complete governance framework tracks decisions and enforces compliance

**For AI Coding Assistants**:
- **Clear boundaries**: Constitutional rules prevent inappropriate actions (e.g., unauthorized Git operations)
- **Specialized expertise**: Domain-specific agents provide deeper knowledge than general-purpose assistants
- **Workflow automation**: Slash commands reduce manual coordination overhead
- **Context preservation**: Structured templates maintain continuity across sessions

### Backport Priority

**CRITICAL (Must Have)**: Constitutional governance, agent delegation protocol, Git operation controls  
**HIGH (Should Have)**: Workflow automation scripts, enhanced templates, policy framework  
**MEDIUM (Nice to Have)**: Integration infrastructure, advanced governance mechanisms  
**LOW (Future)**: Project-specific customizations (Expo, dark neumorphism, etc.)

### Recommendation

**Proceed with phased backport** to original SDD framework repository over 12 weeks, prioritizing constitutional amendments and agent architecture first, followed by automation and policy infrastructure. See [Implementation Recommendations](#implementation-recommendations) for detailed sequencing.

---

## Document Purpose

### Scope

This PRD serves three primary purposes:

1. **Historical Record**: Documents the evolution of the SDD framework during 13 months of production use in a complex mobile application project
2. **Implementation Guide**: Provides detailed specifications for backporting enhancements to the original SDD framework repository
3. **Knowledge Transfer**: Enables future projects to adopt proven patterns without reinventing solutions

### Audience

**Primary Audiences**:
- **SDD Framework Maintainers**: Original repository owners evaluating which enhancements to incorporate
- **Framework Adopters**: Teams considering SDD framework for new projects
- **AI Tool Developers**: Engineers building multi-agent systems for software development

**Secondary Audiences**:
- **Developer Tool Researchers**: Academic/industry researchers studying AI-assisted development
- **Process Engineers**: Teams establishing development workflows and governance

### How to Use This Document

**For Backporting**:
1. Review [Current State Analysis](#current-state-analysis) to understand baseline
2. Study [Enhancements Catalog](#enhancements-catalog) for detailed specifications
3. Follow [Implementation Recommendations](#implementation-recommendations) for sequencing
4. Reference [Appendices](#appendices) for file structures and migrations

**For Adoption**:
1. Start with [Executive Summary](#executive-summary) for high-level overview
2. Review [Constitutional Framework](#category-1-constitutional-framework) enhancements for core principles
3. Evaluate [Agent Architecture](#category-2-agent-architecture--delegation) for delegation patterns
4. Assess which categories align with your project needs

**For Research**:
1. Study [Evolution Timeline](#evolution-timeline) for maturation patterns
2. Analyze [Breaking Changes](#breaking-changes) for lessons learned
3. Review [Appendix C](#appendix-c-constitutional-amendment-history) for decision history

### Document Conventions

**Enhancement IDs**: `ENH-{Category}-{Number}` (e.g., `ENH-CON-001` for first constitutional enhancement)  
**File Paths**: All paths relative to repository root unless otherwise specified  
**Version References**: Original framework = v0.x, Enhanced framework = v1.x  
**Priority Levels**: CRITICAL → HIGH → MEDIUM → LOW (backport priority)

---

## Current State Analysis

### Original Framework Capabilities

The SDD Agentic Framework (v0.x) from https://github.com/kelleysd-apps/sdd-agentic-framework provided:

#### Core Specification Workflow

**Templates**:
- `spec-template.md`: Feature specification structure
- `plan-template.md`: Implementation planning outline

**Scripts**:
- `create-new-feature.sh`: Initialize feature branch and spec file
- `update-agent-context.sh`: Refresh AI assistant context

**Memory**:
- `constitution.md`: Basic principles (~50 lines)
  - Library-first architecture
  - Test-driven development
  - Contract-first design

**Directory Structure**:
```
.specify/
├── memory/
│   └── constitution.md          # Core principles
├── scripts/bash/
│   ├── common.sh                # Shared utilities
│   ├── create-new-feature.sh    # Feature initialization
│   └── update-agent-context.sh  # Context refresh
└── templates/
    ├── spec-template.md         # Feature specification
    └── plan-template.md         # Implementation plan
```

#### Workflow Support

1. **Feature Initialization**: Create numbered feature branches with spec files
2. **Context Management**: Update `.claude/context/` files for AI assistants
3. **Template Generation**: Scaffold spec and plan documents

#### Design Philosophy

- **Specification-First**: Write detailed specs before implementation
- **Structured Documentation**: Use templates for consistency
- **AI-Friendly**: Maintain context files for coding assistants
- **Lightweight**: Minimal tooling overhead

### Limitations Identified

Through 13 months of production use, the following limitations emerged:

#### 1. Governance Gaps

**Problem**: No enforcement mechanism for constitutional principles
- Agents could ignore "library-first" and implement monoliths
- Test-driven development was suggested but not enforced
- No validation gates before implementation phases

**Impact**: Inconsistent adherence, technical debt accumulation

#### 2. Git Operation Risks

**Problem**: No controls on autonomous Git operations
- Agents could create branches without approval
- Commits happened automatically during workflow scripts
- Risk of unauthorized pushes or destructive operations

**Impact**: Loss of developer control, potential code safety issues

#### 3. Lack of Specialization

**Problem**: Single general-purpose agent for all domains
- Frontend, backend, database, security all handled by same agent
- No deep expertise in specialized areas
- Context switching overhead across disparate domains

**Impact**: Lower quality outputs, missed domain-specific best practices

#### 4. Manual Coordination Overhead

**Problem**: Developers manually orchestrate multi-step workflows
- Run multiple scripts in sequence
- Manually validate prerequisites
- Coordinate agent handoffs

**Impact**: Time waste, error-prone processes, broken workflows

#### 5. Insufficient Testing Strategy

**Problem**: Generic "write tests" guidance without specifics
- No distinction between unit/integration/E2E tests
- No guidance on test priorities or sequencing
- Contract testing not addressed

**Impact**: Inadequate test coverage, testing anti-patterns

#### 6. Template Rigidity

**Problem**: Templates lacked validation and adaptability
- No required fields enforcement
- No conditional sections based on feature type
- No integration with workflow automation

**Impact**: Incomplete specs, missing critical information

#### 7. Documentation Sprawl

**Problem**: No structured policy framework
- Best practices scattered across git history
- Decisions made ad-hoc without documentation
- No single source of truth for processes

**Impact**: Knowledge loss, inconsistent practices, onboarding friction

#### 8. Integration Blindspots

**Problem**: No consideration for external integrations
- Browser testing tools not addressed
- MCP server registry not managed
- Platform-specific tooling (Expo, EAS) not integrated

**Impact**: Manual integration work, fragmented tooling

### Enhanced Framework Capabilities

The Ioun AI implementation addresses these limitations with:

#### 1. Constitutional Governance (v1.5.0)

**Capabilities**:
- 14 enforceable principles with violation detection
- Mandatory compliance checks before implementation
- Amendment process with impact analysis
- Audit trail requirements

**Enforcement**:
- Pre-implementation validation gates
- Automated constitutional checks in scripts
- Agent delegation requirements (Section X)
- Git operation approval protocol (Section VI)

#### 2. Multi-Agent Architecture

**Capabilities**:
- 13 specialized agents across 6 departments
- Automatic domain detection and routing
- Task delegation protocol with triggers
- Context handoff mechanisms

**Departments**:
- **Engineering**: frontend-specialist, backend-architect, subagent-architect
- **Data**: database-specialist
- **Quality**: testing-specialist, security-specialist, performance-engineer
- **Product**: specification-agent, tasks-agent, task-orchestrator
- **Operations**: devops-engineer
- **Architecture**: structure-architect, neomorphism-designer

#### 3. Workflow Automation

**Capabilities**:
- 4 slash commands (`/specify`, `/plan`, `/tasks`, `/create-agent`)
- 11 automation scripts with JSON argument support
- Prerequisite validation before execution
- Multi-agent orchestration triggers

**Scripts**:
- Feature workflow: `create-new-feature.sh`, `setup-plan.sh`, `check-task-prerequisites.sh`
- Agent management: `create-agent.sh`, `detect-phase-domain.sh`
- Validation: `constitutional-check.sh`, `validate-spec.sh`

#### 4. Comprehensive Policy Framework

**Capabilities**:
- 24+ policy/workflow/reference documents
- Structured decision templates
- Migration guides for breaking changes
- Quick reference cards

**Categories**:
- **Policies**: File creation, EAS builds, browser testing, AI model selection
- **Workflows**: Feature development, agent delegation, testing strategy
- **References**: Agent triggers, design system, constitutional principles

#### 5. Enhanced Templates

**Capabilities**:
- Validation requirements in templates
- Conditional sections for feature types
- Integration with automation scripts
- Cross-references to policies

**Templates**:
- `spec-template.md`: Enhanced with tier gating, testing strategy, design system
- `plan-template.md`: 9-step process with research and contracts
- `tasks-template.md`: Dependency tracking, parallel execution markers
- `agent-file-template.md`: SDD-compliant agent creation

#### 6. Integration Infrastructure

**Capabilities**:
- MCP server registry (`mcp_servers.json`)
- Browser testing with Playwright
- Expo/EAS build integration
- Platform-specific tooling guides

**Integrations**:
- `mcp__ref-tools`: Reference documentation access
- `mcp__browsermcp`: Browser automation
- `mcp__perplexity`: Web research
- Playwright: E2E testing framework

#### 7. Quality & Governance Mechanisms

**Capabilities**:
- Automated compliance checking
- Constitution update checklists
- Violation detection protocols
- Audit trail requirements

**Mechanisms**:
- `constitutional-check.sh`: Pre-flight validation
- `constitution_update_checklist.md`: Change management
- Agent delegation enforcement (Section X)
- Git operation approval gates (Section VI)

### Comparison Matrix

| Capability | Original Framework | Enhanced Framework | Enhancement Type |
|-----------|-------------------|-------------------|------------------|
| **Constitutional Lines** | ~50 | 302 | Expansion (6x) |
| **Principles Count** | 3 | 14 | Addition |
| **Enforcement** | Suggested | Mandatory | Hardening |
| **Agent Count** | 1 (general) | 13 (specialized) | Specialization |
| **Slash Commands** | 1 basic | 4 automated | Automation |
| **Bash Scripts** | 2 | 11 | Expansion (5.5x) |
| **Templates** | 2 basic | 4 enhanced | Enhancement |
| **Policies** | 0 | 24+ | Addition |
| **Git Control** | None | Approval-gated | Governance |
| **Testing Strategy** | Generic | Tiered (E2E/Contract/Unit) | Specialization |
| **Integration Support** | None | MCP/Browser/Platform | Addition |
| **Validation Gates** | None | Multi-stage | Governance |

---

## Enhancements Catalog

### Category 1: Constitutional Framework

#### ENH-CON-001: Constitutional Expansion (v1.0 → v1.5.0)

**ID**: ENH-CON-001  
**Priority**: CRITICAL  
**Breaking**: Yes (enforcement requirements)

**Description**:
Expanded constitution from ~50 lines to 302 lines, adding 11 new principles and formalizing governance mechanisms.

**Original State**:
```markdown
# Constitution (v0.x)

## Core Principles
1. Library-First Architecture
2. Test-Driven Development
3. Contract-First Design
```

**Enhanced State**:
```markdown
# Constitution (v1.5.0)

## 14 Principles:
I. Library-First Architecture (Immutable)
II. Test-Driven Development (Immutable)
III. Contract-First Design (Immutable)
IV. Idempotent Operations
V. Progressive Enhancement
VI. Git Operation Approval (CRITICAL)
VII. Observability & Structured Logging
VIII. Documentation Synchronization
IX. Dependency Management
X. Agent Delegation Protocol (CRITICAL)
XI. Input Validation & Output Sanitization
XII. Design System Compliance
XIII. Subscription Tier Enforcement
XIV. AI Model Selection Protocol
```

**Rationale**:
- **Enforcement**: Original principles were suggestions; enhanced version makes them mandatory with validation
- **Safety**: Git operation approval prevents destructive actions
- **Quality**: Design system compliance and tier enforcement ensure consistency
- **Scalability**: Agent delegation enables specialized expertise
- **Auditability**: Structured logging and documentation requirements maintain history

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (302 lines, v1.5.0)
- `/workspaces/ioun-ai/.specify/memory/constitution_update_checklist.md` (amendment process)

**Key Sections**:
1. **Preamble**: Framework purpose and authority
2. **Core Immutable Principles** (I-III): Cannot be changed
3. **Quality & Safety Principles** (IV-VI): Operational safety
4. **Operational Excellence** (VII-IX): Best practices
5. **Development Workflow**: Mandatory gates and protocols
6. **Amendment Process**: How to update constitution
7. **Work Session Initiation Protocol**: MANDATORY for every task

**Dependencies**: None (foundation for all other enhancements)

**Benefits**:
- Clear governance structure
- Enforceable quality gates
- Safety mechanisms for destructive operations
- Audit trail for all decisions
- Foundation for multi-agent coordination

**Migration Path**:
1. Review existing constitution.md in original repo
2. Merge new principles (IV-XIV) without breaking existing I-III
3. Add enforcement sections (Work Session Initiation Protocol, Amendment Process)
4. Create constitution_update_checklist.md for change management
5. Update all documentation to reference new principles by number

**Rollback**: Cannot rollback without losing enforcement mechanisms; instead, phase in mandatory compliance

---

#### ENH-CON-002: Work Session Initiation Protocol

**ID**: ENH-CON-002  
**Priority**: CRITICAL  
**Breaking**: Yes (makes compliance mandatory for every task)

**Description**:
Establishes mandatory 4-step protocol that MUST be executed at the start of every work session, regardless of task simplicity.

**Protocol Steps**:
```markdown
1. READ CONSTITUTION
   - First action of any session
   - No exceptions, even for "simple" tasks
   - Applies to: file reading, status checks, answering questions

2. ANALYZE TASK DOMAIN
   - Use automated tools: detect-phase-domain.sh, constitutional-check.sh
   - Manual scan for trigger keywords (test, UI, database, security, etc.)
   - Reference: agent-collaboration-triggers.md

3. DELEGATION DECISION
   - IF domain keywords matched → STOP, delegate to specialized agent
   - IF no keywords → Verify by reading files, document why no delegation
   - NEVER execute specialized work directly

4. EXECUTION
   - ONLY after steps 1-3 complete
   - Execute directly OR invoke specialized agent via Task tool
```

**Rationale**:
- **Prevents violations**: Catches inappropriate direct execution before it happens
- **Enforces delegation**: Ensures specialized work goes to specialized agents
- **Maintains quality**: Constitutional principles applied consistently
- **Reduces errors**: Systematic approach prevents oversight

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Section: Development Workflow)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 45-140: MANDATORY TASK ANALYSIS CHECKLIST)
- `/workspaces/ioun-ai/.specify/scripts/bash/detect-phase-domain.sh` (automation)
- `/workspaces/ioun-ai/.specify/scripts/bash/constitutional-check.sh` (validation)

**Enforcement**:
- Documented in CLAUDE.md with examples
- Referenced in all agent context files
- Validated by constitutional-check.sh script
- Violation detection: Agents must self-report if protocol skipped

**Dependencies**: 
- ENH-CON-001 (constitutional framework)
- ENH-AGT-001 (agent delegation protocol)

**Benefits**:
- 100% compliance with delegation requirements
- Reduced constitutional violations
- Consistent quality across all work
- Clear audit trail

**Migration Path**:
1. Add "Work Session Initiation Protocol" section to constitution.md
2. Create detect-phase-domain.sh and constitutional-check.sh scripts
3. Update main instruction file (CLAUDE.md/AGENTS.md) with mandatory checklist
4. Train agents to execute protocol before any work
5. Monitor compliance for first 30 days, refine triggers

**Rollback**: Make protocol "recommended" instead of "mandatory"

---

#### ENH-CON-003: Git Operation Approval Protocol (Principle VI)

**ID**: ENH-CON-003  
**Priority**: CRITICAL  
**Breaking**: Yes (blocks autonomous Git operations)

**Description**:
Establishes strict controls requiring explicit user approval for ALL Git operations, preventing autonomous branch creation, commits, pushes, or destructive actions.

**Controlled Operations**:
```markdown
REQUIRES APPROVAL:
- Branch creation, switching, deletion
- Commits and commit messages
- Pushes, pulls, merges
- Any modifications to Git history
- Rebase, reset, cherry-pick
- Submodule operations

ALLOWED WITHOUT APPROVAL:
- git status (read-only)
- git diff (read-only)
- git log (read-only)
```

**Approval Flow**:
```markdown
1. AGENT DETECTS need for Git operation
2. AGENT ASKS USER: "Would you like me to [operation]? This will [consequences]"
3. USER RESPONDS: Explicit "yes" or approval
4. AGENT EXECUTES: Only after confirmation
5. AGENT REPORTS: Results and next steps
```

**Rationale**:
- **Safety**: Prevents accidental destructive operations
- **Control**: Developer maintains authority over repository state
- **Transparency**: All Git actions visible and approved
- **Auditability**: Clear record of who authorized what

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle VI)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 370-389: Git Operations CRITICAL section)
- `/workspaces/ioun-ai/.docs/quick-reference/sdd-agent-delegation.md` (enforcement examples)

**Git Safety Protocol**:
```markdown
NEVER:
- Update git config
- Run destructive commands (push --force, hard reset) without explicit request
- Skip hooks (--no-verify, --no-gpg-sign) without explicit request
- Force push to main/master (warn user even if requested)
- Use git commit --amend (unless user requested OR adding pre-commit hook edits)

ALWAYS:
- Check authorship before amending (git log -1 --format='%an %ae')
- Ask for branch name format when creating branches
- Show git status before and after operations
- Document commit messages with Claude Code attribution
```

**Dependencies**: ENH-CON-001 (constitutional framework)

**Benefits**:
- Zero unauthorized Git operations
- Developer maintains control
- Prevents costly mistakes
- Clear audit trail

**Migration Path**:
1. Add Principle VI to constitution.md
2. Update workflow scripts to remove autonomous Git operations
3. Add approval prompts to create-new-feature.sh
4. Update agent context files with Git safety protocol
5. Test with sample workflows, verify approval gates trigger

**Rollback**: Remove approval gates, add warning messages instead

---

#### ENH-CON-004: Agent Delegation Protocol (Principle X)

**ID**: ENH-CON-004  
**Priority**: CRITICAL  
**Breaking**: Yes (requires agent infrastructure)

**Description**:
Formalizes mandatory delegation of specialized domain work to specialized agents, prohibiting general-purpose agents from executing domain-specific tasks directly.

**Delegation Requirements**:
```markdown
MUST DELEGATE:
- Testing work → testing-specialist
- Frontend/UI development → frontend-specialist
- Database operations → database-specialist
- Security reviews → security-specialist
- Backend architecture → backend-architect
- Feature specifications → specification-agent
- Task generation → tasks-agent
- Agent creation → subagent-architect

DIRECT EXECUTION OK:
- File reading/searching
- Git status/diff/log (read-only)
- Diagnostics and checks
- Answering questions
- Administrative tasks
```

**Delegation Syntax**:
```python
# ✅ CORRECT: Direct invocation of specialized agent
Task(
  subagent_type="frontend-specialist",
  description="Implement tier enforcement UI",
  prompt="[detailed requirements, constraints, deliverables]"
)
```

**Trigger Matrix** (abbreviated):
| Keyword | Agent | Rationale |
|---------|-------|-----------|
| test, jest, spec | testing-specialist | Testing expertise |
| component, UI, tsx | frontend-specialist | Frontend expertise |
| schema, migration, sql | database-specialist | Database expertise |
| auth, encryption, token | security-specialist | Security expertise |

**Full matrix**: 40+ triggers in `agent-collaboration-triggers.md`

**Rationale**:
- **Quality**: Specialized agents have deeper domain knowledge
- **Consistency**: Domain-specific patterns applied uniformly
- **Scalability**: Parallel execution across domains
- **Expertise**: Best practices enforced by specialists

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle X)
- `/workspaces/ioun-ai/.specify/memory/agent-collaboration.md` (trigger matrix)
- `/workspaces/ioun-ai/.specify/memory/agent-collaboration-triggers.md` (40+ triggers)
- `/workspaces/ioun-ai/.docs/quick-reference/sdd-agent-delegation.md` (quick reference)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 75-140: HARD STOP section)

**Enforcement**:
- Work Session Initiation Protocol (Step 2: Analyze Task Domain)
- Automated detection: `detect-phase-domain.sh`
- Manual scan: Keyword triggers in collaboration matrix
- Violation detection: Agents self-report if executing specialized work directly

**Dependencies**:
- ENH-CON-002 (Work Session Initiation Protocol)
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-AGT-002 (Agent Registry & Capability Mapping)

**Benefits**:
- Higher quality outputs in specialized domains
- Consistent application of best practices
- Parallel development across domains
- Clear separation of concerns

**Migration Path**:
1. Add Principle X to constitution.md
2. Create agent-collaboration.md with trigger matrix
3. Implement detect-phase-domain.sh for automated detection
4. Update main instruction file with HARD STOP section
5. Create specialized agents (see Category 2)
6. Train agents on delegation protocol
7. Monitor compliance, refine triggers based on false positives/negatives

**Rollback**: Make delegation "recommended" instead of "mandatory"

---

#### ENH-CON-005: Design System Compliance (Principle XII)

**ID**: ENH-CON-005  
**Priority**: HIGH  
**Breaking**: No (project-specific)

**Description**:
Establishes mandatory compliance with design system for all UI components, prohibiting hardcoded values and enforcing theme-based styling.

**Compliance Requirements**:
```markdown
PROHIBITED:
❌ Hardcoded color values (#2C2C2E in styles)
❌ Hardcoded shadow values (shadowOffset/shadowRadius)
❌ Magic numbers for spacing (paddingLeft: 16)
❌ Legacy light neumorphic tokens (#E8EDF5, #7CA3D0)
❌ Custom shadow patterns (duplicating shadow logic)

REQUIRED:
✅ Theme via useTheme() hook
✅ Shadow utilities via useShadows() hook
✅ Gradient constants from GRADIENTS
✅ Spacing from theme.spacing.*
✅ Colors from theme.colors.*
```

**Compatible Rendering Mode**:
```markdown
FOR TEXT/TEXTINPUT COMPONENTS ONLY:
✅ Solid backgrounds (theme.colors.background.*)
✅ Simple single shadows (optional)
❌ NO LinearGradient components
❌ NO useShadows() dual-shadow system
❌ NO complex nested Views (≤2 layers max)

RATIONALE: Android rendering bugs with expo-linear-gradient + nested Views + complex shadows = text invisible
```

**Rationale**:
- **Consistency**: Uniform visual language across application
- **Maintainability**: Theme changes propagate automatically
- **Quality**: Prevents visual bugs from hardcoded values
- **Accessibility**: Centralized theme supports dark/light modes

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle XII)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 283-330: Dark Neumorphic Design System v2.4 Patterns)
- `/workspaces/ioun-ai/.docs/design/dark-neumorphic-design-system/` (complete design system)
- `/workspaces/ioun-ai/.docs/design/dark-neumorphic-design-system/09-compatibility/compatible-rendering-mode.md`

**Design System Structure**:
```
.docs/design/dark-neumorphic-design-system/
├── 01-foundation/
│   ├── colors.md
│   ├── spacing.md
│   └── typography.md
├── 02-components/
│   ├── buttons.md
│   ├── cards.md
│   └── inputs.md
├── 08-reference/
│   └── quick-reference.md
└── 09-compatibility/
    └── compatible-rendering-mode.md
```

**Enforcement**:
- Code review checklist (prohibitions documented)
- ESLint rules (future enhancement)
- Agent training on design system

**Dependencies**: None (project-specific, but pattern generalizable)

**Benefits**:
- 100% theme compliance in 200+ components
- Zero hardcoded values in codebase
- Consistent visual language
- Easy theme updates

**Migration Path** (for backport):
1. Extract design system compliance requirements from Principle XII
2. Create generic "Design System Compliance" principle
3. Document prohibited practices (hardcoded values, magic numbers)
4. Provide examples of theme-based approach
5. Add enforcement checklist to spec/plan templates
6. Make specific design system (neumorphic) optional, keep compliance pattern mandatory

**Rollback**: Remove enforcement, make compliance recommended

---

#### ENH-CON-006: Subscription Tier Enforcement (Principle XIII)

**ID**: ENH-CON-006  
**Priority**: MEDIUM  
**Breaking**: No (project-specific)

**Description**:
Establishes requirements for implementing subscription tier restrictions with both backend (RLS) and frontend (UI) enforcement.

**Tier Enforcement Requirements**:
```markdown
BACKEND ENFORCEMENT (MANDATORY):
- Row-Level Security (RLS) policies in database
- API-level authorization checks
- Tier limits enforced at data layer

FRONTEND ENFORCEMENT (MANDATORY):
- UI indicators for tier restrictions
- Upgrade prompts for premium features
- Graceful degradation for free tier

TESTING REQUIREMENTS:
- Test tier restrictions in RLS policies
- Test UI enforcement (upgrade prompts)
- Test edge cases (tier transitions)
```

**Example Tiers**:
```markdown
Player Tier (Free):
- 3 active campaigns max
- Basic features only

DM Tier ($9.99/month):
- Unlimited campaigns
- DM tools (encounter builder, session notes)
- AI-powered NPC generation

Prestige Tier (Future):
- Advanced analytics
- Custom homebrew tools
```

**Rationale**:
- **Revenue**: Enables SaaS business model
- **Security**: Backend enforcement prevents circumvention
- **UX**: Frontend enforcement provides clear upgrade paths
- **Testing**: Ensures tier restrictions work correctly

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle XIII)
- `/workspaces/ioun-ai/.docs/prd's/ioun_mobile_prd.md` (Section 5: Subscription Tiers)

**Pattern Example** (from Feature 005: Campaign Management):
```sql
-- Backend RLS enforcement
CREATE POLICY "player_tier_campaign_limit"
ON campaigns FOR INSERT
TO authenticated
WITH CHECK (
  (SELECT tier FROM user_profiles WHERE id = auth.uid()) = 'dm'
  OR (SELECT COUNT(*) FROM campaigns WHERE user_id = auth.uid() AND status = 'active') < 3
);
```

```typescript
// Frontend UI enforcement
const canCreateCampaign = userTier === 'dm' || activeCampaigns.length < 3;

{!canCreateCampaign && (
  <TierRestrictedBanner
    message="Player tier limited to 3 active campaigns"
    upgradeAction={() => navigation.navigate('Subscription')}
  />
)}
```

**Dependencies**: None (project-specific, but pattern generalizable)

**Benefits**:
- Clear monetization model
- Secure tier enforcement
- User-friendly upgrade paths
- Testable tier restrictions

**Migration Path** (for backport):
1. Extract tier enforcement pattern from Principle XIII
2. Create generic "Feature Gating" or "Access Control" principle
3. Document backend + frontend enforcement requirements
4. Provide examples from common access control patterns (roles, permissions, quotas)
5. Make specific tiers (Player/DM/Prestige) project-specific, keep pattern generic

**Rollback**: Remove principle, treat tier enforcement as project-specific requirement

---

#### ENH-CON-007: AI Model Selection Protocol (Principle XIV)

**ID**: ENH-CON-007  
**Priority**: HIGH  
**Breaking**: No (operational guidance)

**Description**:
Establishes default AI model (Claude Sonnet 4.5) with clear escalation criteria for using higher-capability models (Claude Opus 4.1).

**Model Selection Matrix**:
```markdown
DEFAULT: Claude Sonnet 4.5
- Model ID: claude-sonnet-4-5-20250929
- Use for: 90%+ of all agent tasks
- Cost: $3/MTok input, $15/MTok output
- Context: 200K tokens (1M beta)
- Rationale: Best balance of speed and intelligence for coding

ESCALATE TO: Claude Opus 4.1
- Model ID: claude-opus-4-1-20250805
- Cost: $15/MTok input, $75/MTok output (5x more expensive)
- Context: 200K tokens

ESCALATION TRIGGERS (any one):
1. Multi-step complex reasoning (5+ interconnected logical steps)
2. Safety-critical decisions (security, privacy, financial)
3. Research depth required (novel problem spaces)
4. Accuracy over speed (costly mistakes)
5. User explicitly requests highest-capability model
6. Repeated Sonnet failures (2+ times on same task)
```

**Decision Tree**:
```markdown
Task Type → Model → Rationale
Standard coding → Sonnet 4.5 → Best coding model, fast
Routine analysis → Sonnet 4.5 → Sufficient intelligence
Complex architecture → Sonnet 4.5 first → Try before escalating
Security critical → Opus 4.1 → Accuracy paramount
Novel research → Opus 4.1 → Deep reasoning needed
Failed 2x with Sonnet → Opus 4.1 → Escalation trigger met
```

**Rationale**:
- **Cost efficiency**: Sonnet 4.5 is 5x cheaper for most tasks
- **Performance**: Sonnet 4.5 is faster for standard coding
- **Quality gate**: Escalate only when complexity justifies cost
- **Auditability**: Document escalation reason

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle XIV)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 225-264: AI Model Selection Policy)
- All agent context files (`.claude/agents/**/*.md`)

**Agent Configuration**:
```markdown
# In each agent's context file
## Model Selection
- **Default Model**: Claude Sonnet 4.5 (`claude-sonnet-4-5`)
- **Escalation Triggers**: [list triggers relevant to agent domain]
- **Document Escalation**: Log reason in task description when using Opus 4.1
```

**Enforcement**:
- Documented in constitution and main instruction file
- Escalation logged in task descriptions
- Cost monitoring (future enhancement)

**Dependencies**: None (operational guidance)

**Benefits**:
- Reduced AI costs (5x savings on 90% of tasks)
- Faster execution (Sonnet 4.5 is faster)
- Clear escalation path for complex work
- Audit trail for model selection

**Migration Path** (for backport):
1. Add Principle XIV to constitution.md
2. Document default model and escalation triggers
3. Update agent context files with model selection guidance
4. Create decision tree/quick reference
5. Train agents on escalation criteria

**Rollback**: Remove model selection guidance, let agents choose freely

---

#### ENH-CON-008: Observability & Structured Logging (Principle VII)

**ID**: ENH-CON-008  
**Priority**: MEDIUM  
**Breaking**: No (implementation requirement)

**Description**:
Requires structured logging and metrics instrumentation for all operations to enable debugging, monitoring, and audit trails.

**Logging Requirements**:
```markdown
ALL OPERATIONS MUST LOG:
- Timestamp and duration
- User approval status (for gated operations)
- Tools used
- Outcome and any errors
- Constitutional compliance check result

STRUCTURED FORMAT:
{
  "timestamp": "2025-11-06T10:30:00Z",
  "operation": "create-feature",
  "user_approved": true,
  "tools": ["Write", "Bash"],
  "outcome": "success",
  "constitutional_compliance": true,
  "duration_ms": 1250,
  "metadata": {...}
}
```

**Audit Trail Requirements**:
```markdown
MUST MAINTAIN:
- All operations performed (who, what, when, why)
- Constitutional compliance checks
- Approval decisions (user approved/denied)
- Errors and resolutions
- Agent invocations and handoffs
```

**Rationale**:
- **Debugging**: Trace issues across multi-agent workflows
- **Compliance**: Verify constitutional adherence
- **Auditability**: Track all decisions and actions
- **Monitoring**: Detect patterns and anomalies

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle VII)
- All bash scripts in `.specify/scripts/bash/` (structured error handling)

**Script Pattern**:
```bash
# Example from create-new-feature.sh
log_operation() {
  local operation=$1
  local status=$2
  local message=$3
  
  echo "{\"timestamp\":\"$(date -Iseconds)\",\"operation\":\"$operation\",\"status\":\"$status\",\"message\":\"$message\"}" >> "$LOG_FILE"
}

# Usage
log_operation "create_feature" "success" "Feature 010 created"
```

**Agent Audit Requirements**:
```markdown
# In agent context files
## Audit Requirements

All operations must log:
- Timestamp and duration
- User approval status
- Tools used
- Outcome and any errors
- Constitutional compliance check
```

**Dependencies**: None (operational best practice)

**Benefits**:
- Full audit trail for compliance
- Debugging support for complex workflows
- Performance monitoring
- Error pattern detection

**Migration Path**:
1. Add Principle VII to constitution.md
2. Define structured logging format (JSON recommended)
3. Update bash scripts with logging functions
4. Add audit requirements to agent context files
5. Create log aggregation/analysis tools (future enhancement)

**Rollback**: Remove logging requirements, treat as optional best practice

---

#### ENH-CON-009: Documentation Synchronization (Principle VIII)

**ID**: ENH-CON-009  
**Priority**: HIGH  
**Breaking**: No (documentation requirement)

**Description**:
Establishes requirements for maintaining documentation in sync with code changes, including cross-references and update checklists.

**Synchronization Requirements**:
```markdown
WHEN CODE CHANGES:
- Update relevant documentation files
- Update cross-references
- Check for dependent documents
- Validate examples and code snippets

WHEN DOCUMENTATION CHANGES:
- Check for code inconsistencies
- Update related documentation
- Validate cross-references
- Update timestamps/versions
```

**Key Documentation Types**:
```markdown
1. CONSTITUTIONAL DOCUMENTS
   - constitution.md (core principles)
   - constitution_update_checklist.md (change process)
   - Must stay in sync with enforcement mechanisms

2. INSTRUCTION FILES
   - CLAUDE.md (Claude-specific guidance)
   - AGENTS.md (universal AI guidance)
   - Must stay in sync per ai-instruction-files-policy.md

3. POLICY DOCUMENTS
   - .docs/policies/*.md
   - Must stay in sync with workflow scripts

4. AGENT CONTEXT FILES
   - .claude/agents/**/*.md
   - Must stay in sync with agent implementations
```

**Synchronization Checklist**:
```markdown
# From constitution_update_checklist.md
When updating constitution.md:
□ Update CLAUDE.md with corresponding changes
□ Update AGENTS.md with corresponding changes
□ Update affected agent context files
□ Update workflow scripts with new requirements
□ Update policy documents
□ Update quick reference guides
□ Test workflows with updated requirements
□ Document breaking changes with migration paths
```

**Rationale**:
- **Consistency**: Code and docs stay aligned
- **Maintainability**: Changes propagate correctly
- **Onboarding**: New developers see accurate documentation
- **Compliance**: Documented requirements match actual enforcement

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle VIII)
- `/workspaces/ioun-ai/.specify/memory/constitution_update_checklist.md` (enforcement)
- `/workspaces/ioun-ai/.docs/policies/ai-instruction-files-policy.md` (CLAUDE.md ↔ AGENTS.md sync)

**Enforcement**:
- Checklist in constitution_update_checklist.md
- PR template requirement (future enhancement)
- Automated link checking (future enhancement)

**Dependencies**: None (documentation best practice)

**Benefits**:
- Zero documentation drift
- Accurate onboarding materials
- Consistent enforcement
- Clear change propagation

**Migration Path**:
1. Add Principle VIII to constitution.md
2. Create constitution_update_checklist.md
3. Document synchronization requirements for each doc type
4. Add synchronization checks to workflow scripts
5. Create automated validation tools (link checking, version matching)

**Rollback**: Remove synchronization requirements, treat as best practice

---

#### ENH-CON-010: Idempotent Operations (Principle IV)

**ID**: ENH-CON-010  
**Priority**: MEDIUM  
**Breaking**: No (implementation requirement)

**Description**:
Requires all operations to be safely repeatable, returning same result when executed multiple times with same inputs.

**Idempotency Requirements**:
```markdown
ALL OPERATIONS MUST:
- Check if result already exists before creating
- Use upsert patterns instead of insert
- Validate preconditions before execution
- Return consistent results for same inputs
- Handle partial completion gracefully

EXAMPLES:
✅ create-new-feature.sh: Checks if feature dir exists before creating
✅ setup-plan.sh: Skips existing files, creates only missing
✅ Database migrations: Check if already applied before running
❌ create-new-feature.sh (original): Would overwrite existing files
```

**Implementation Pattern**:
```bash
# Example from create-new-feature.sh
if [ -d "specs/$FEATURE_DIR" ]; then
  echo "Feature directory already exists: specs/$FEATURE_DIR"
  echo "Use --force to overwrite"
  exit 1
fi

# Proceed with creation only if doesn't exist
mkdir -p "specs/$FEATURE_DIR"
```

**Rationale**:
- **Safety**: Re-running commands doesn't cause data loss
- **Recovery**: Failed operations can be retried safely
- **Automation**: Scripts can be run in CI/CD without state tracking
- **Consistency**: Predictable behavior reduces errors

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle IV)
- All bash scripts in `.specify/scripts/bash/` (idempotency checks)

**Enforcement**:
- Precondition checks in all scripts
- Upsert patterns in database operations
- Validation before destructive operations

**Dependencies**: None (implementation best practice)

**Benefits**:
- Safe script re-execution
- Graceful recovery from failures
- CI/CD-friendly automation
- Reduced error risk

**Migration Path**:
1. Add Principle IV to constitution.md
2. Audit existing scripts for idempotency
3. Add precondition checks to non-idempotent operations
4. Document idempotency patterns
5. Test script re-execution scenarios

**Rollback**: Remove idempotency requirements, accept potential overwrites

---

#### ENH-CON-011: Progressive Enhancement (Principle V)

**ID**: ENH-CON-011  
**Priority**: LOW  
**Breaking**: No (design philosophy)

**Description**:
Establishes "start simple, add complexity only when proven necessary" as a core design principle.

**Progressive Enhancement Requirements**:
```markdown
START WITH:
- Simplest possible implementation
- Hardcoded values (before abstraction)
- Manual processes (before automation)
- Single-responsibility functions
- Clear, obvious code

ADD COMPLEXITY WHEN:
- Repetition proves abstraction needed (DRY)
- Performance measurements show bottleneck
- User feedback identifies pain point
- Scale demands optimization
- NOT speculatively "for the future"
```

**Examples**:
```markdown
✅ GOOD:
1. Implement feature with inline styles
2. Measure usage, identify repeated patterns
3. Extract to theme system
4. Document decision in ADR

❌ BAD:
1. Create complex abstraction framework upfront
2. Implement feature using framework
3. Framework over-engineered for actual needs
```

**Rationale**:
- **Speed**: Simple implementations ship faster
- **Clarity**: Easy to understand and maintain
- **Flexibility**: Easy to change direction
- **Evidence-based**: Complexity justified by real needs

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle V)

**Enforcement**:
- Code review philosophy
- Complexity justification requirement in specs
- "Why now?" question for abstractions

**Dependencies**: None (design philosophy)

**Benefits**:
- Faster feature delivery
- Lower cognitive overhead
- Easier refactoring
- Evidence-based architecture

**Migration Path**:
1. Add Principle V to constitution.md
2. Document progressive enhancement philosophy
3. Add complexity justification to spec template
4. Train reviewers to question premature abstraction

**Rollback**: Remove principle, allow speculative complexity

---

#### ENH-CON-012: Amendment Process Formalization

**ID**: ENH-CON-012  
**Priority**: HIGH  
**Breaking**: No (governance process)

**Description**:
Establishes formal process for amending constitution with impact analysis and stakeholder review.

**Amendment Process**:
```markdown
1. PROPOSAL
   - Identify need for constitutional change
   - Document rationale and impact
   - Draft amendment language

2. IMPACT ANALYSIS
   - Identify affected documents (using checklist)
   - Assess breaking changes
   - Plan migration path

3. STAKEHOLDER REVIEW
   - Review with project leads
   - Gather feedback
   - Refine amendment

4. IMPLEMENTATION
   - Update constitution.md
   - Update all affected documents (per checklist)
   - Update enforcement mechanisms
   - Document migration path

5. VALIDATION
   - Test workflows with new requirements
   - Verify documentation sync
   - Train agents on changes
```

**Amendment Checklist** (from `constitution_update_checklist.md`):
```markdown
When updating constitution.md:

INSTRUCTION FILES:
□ Update CLAUDE.md with corresponding changes
□ Update AGENTS.md with corresponding changes
□ Verify CLAUDE.md ↔ AGENTS.md sync per ai-instruction-files-policy.md

AGENT CONTEXT FILES:
□ Update affected specialized agents (.claude/agents/**/*.md)
□ Update task-orchestrator if delegation changes
□ Update subagent-architect if agent creation changes

WORKFLOW SCRIPTS:
□ Update bash scripts with new requirements
□ Update constitutional-check.sh validation
□ Test all slash commands

POLICY DOCUMENTS:
□ Update affected policies (.docs/policies/*.md)
□ Update workflow guides (.docs/workflows/*.md)
□ Update quick references (.docs/quick-reference/*.md)

TEMPLATES:
□ Update spec-template.md if requirements change
□ Update plan-template.md if workflow changes
□ Update tasks-template.md if task format changes

TESTING:
□ Test workflows with updated requirements
□ Verify enforcement mechanisms work
□ Check for unintended consequences

DOCUMENTATION:
□ Document breaking changes with migration paths
□ Update version number in constitution.md
□ Add amendment to Appendix (version history)
```

**Rationale**:
- **Governance**: Controlled evolution of framework
- **Consistency**: Changes propagate completely
- **Safety**: Impact analysis prevents breaking changes
- **Auditability**: Complete amendment history

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Section: Amendment Process)
- `/workspaces/ioun-ai/.specify/memory/constitution_update_checklist.md` (enforcement)

**Version History** (example):
```markdown
# Constitution Amendment History

## v1.5.0 (2025-10-15)
- Added Principle XIV (AI Model Selection Protocol)
- Rationale: Cost optimization while maintaining quality
- Breaking Changes: None
- Migration: Update agent configs with model selection guidance

## v1.4.0 (2025-09-29)
- Added Principle X (Agent Delegation Protocol)
- Rationale: Enforce specialized agent usage
- Breaking Changes: Requires agent infrastructure
- Migration: Create specialized agents, update delegation triggers
```

**Dependencies**: 
- ENH-CON-009 (Documentation Synchronization)

**Benefits**:
- Controlled constitutional evolution
- Complete change propagation
- Clear migration paths
- Audit trail for amendments

**Migration Path**:
1. Add "Amendment Process" section to constitution.md
2. Create constitution_update_checklist.md
3. Document amendment history in constitution.md appendix
4. Establish review process (project leads, stakeholder sign-off)
5. Test amendment process with sample change

**Rollback**: Remove formal process, allow ad-hoc constitution updates

---

### Category 2: Agent Architecture & Delegation

#### ENH-AGT-001: Multi-Agent Architecture (13 Specialized Agents)

**ID**: ENH-AGT-001  
**Priority**: CRITICAL  
**Breaking**: Yes (requires agent infrastructure)

**Description**:
Replaces single general-purpose agent with 13 specialized agents organized into 6 departments, each with domain expertise and restricted tooling.

**Agent Registry**:

**Engineering Department**:
```markdown
1. frontend-specialist
   - Expertise: React/Next.js, UI components, state management
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools, browsermcp
   - File: .claude/agents/engineering/frontend-specialist.md

2. backend-architect
   - Expertise: API design, service architecture, scalability
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools
   - File: .claude/agents/architecture/backend-architect.md

3. subagent-architect
   - Expertise: Creating SDD-compliant agents, constitutional workflows
   - Tools: Read, Grep, Glob, TodoWrite, Bash (for create-agent.sh)
   - MCP: ref-tools
   - File: .claude/agents/architecture/subagent-architect.md
```

**Data Department**:
```markdown
4. database-specialist
   - Expertise: Schema design, query optimization, data migrations
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools
   - File: .claude/agents/data/database-specialist.md
```

**Quality Department**:
```markdown
5. testing-specialist
   - Expertise: Test planning, test automation, QA, bug analysis
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools, browsermcp
   - File: .claude/agents/quality/testing-specialist.md

6. security-specialist
   - Expertise: Security reviews, vulnerability assessment, secure coding
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools
   - File: .claude/agents/quality/security-specialist.md

7. performance-engineer
   - Expertise: Performance analysis, bottleneck identification, scalability
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools
   - File: .claude/agents/operations/performance-engineer.md
```

**Product Department**:
```markdown
8. specification-agent
   - Expertise: Creating detailed software specifications, user stories
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools, perplexity (research)
   - File: .claude/agents/product/specification-agent.md

9. tasks-agent
   - Expertise: Breaking down technical plans into actionable tasks
   - Tools: Read, Grep, Glob, TodoWrite
   - MCP: ref-tools
   - File: .claude/agents/product/tasks-agent.md

10. task-orchestrator
    - Expertise: Multi-agent workflow coordination
    - Tools: Read, Grep, Glob, TodoWrite
    - MCP: ref-tools, browsermcp, perplexity
    - File: .claude/agents/product/task-orchestrator.md
```

**Operations Department**:
```markdown
11. devops-engineer
    - Expertise: CI/CD pipeline setup, Docker, cloud deployment
    - Tools: Read, Grep, Glob, TodoWrite, Bash
    - MCP: ref-tools
    - File: .claude/agents/operations/devops-engineer.md
```

**Architecture Department**:
```markdown
12. structure-architect
    - Expertise: File structure governance, directory organization
    - Tools: Read, Grep, Glob, TodoWrite
    - MCP: ref-tools
    - File: .claude/agents/architecture/structure-architect.md
```

**Design Department** (project-specific):
```markdown
13. neomorphism-designer
    - Expertise: Neumorphic UI design patterns
    - Tools: Read, Grep, Glob, TodoWrite
    - MCP: ref-tools
    - File: .claude/agents/design/neomorphism-designer.md
```

**Agent Template Structure**:
```markdown
# {Agent Name}

## Core Purpose
[1-2 sentence mission statement]

## Core Capabilities
[3-5 key expertise areas]

## Department Classification
**Department**: {department}
**Role Type**: {Specialist|Architect|Coordinator}
**Interaction Level**: {User-Focused|Agent-Focused}

## Memory References
**Primary Memory**: .docs/agents/{department}/{agent-name}/
**Context**: {path}/context/
**Knowledge**: {path}/knowledge/

## Working Principles
### Constitutional Principles Application
[How this agent applies constitutional principles]

### Department-Specific Guidelines
[Domain-specific best practices]

## Tool Usage Policies
**Authorized Tools**: [list]
**MCP Server Access**: [list]
**Restricted Operations**: [list]

## Collaboration Protocols
**Upstream Dependencies**: [agents this agent receives input from]
**Downstream Consumers**: [agents this agent provides output to]

## Specialized Knowledge
[Domain expertise, patterns, best practices]

## Error Handling
**Known Limitations**: [list]
**Escalation Procedures**: [when to escalate to user or other agents]

## Performance Standards
**Response Time Targets**: [benchmarks]
**Quality Metrics**: [accuracy, success rate, user satisfaction]

## Audit Requirements
[What must be logged for this agent]

## Update History
[Version, date, changes, approved by]
```

**Rationale**:
- **Quality**: Domain experts produce better outputs than generalists
- **Scalability**: Parallel execution across domains
- **Consistency**: Domain-specific patterns enforced uniformly
- **Maintainability**: Clear separation of concerns

**Implementation**:

**Files**:
- 13 agent context files in `.claude/agents/{department}/{agent-name}.md`
- `/workspaces/ioun-ai/AGENTS.md` (agent directory)
- `/workspaces/ioun-ai/.docs/architecture/sdd-agent-architecture.md` (architecture spec)

**Creation Process**:
```bash
# Via /create-agent command
.specify/scripts/bash/create-agent.sh --json '{
  "name": "frontend-specialist",
  "purpose": "React/Next.js development and UI component expertise",
  "department": "engineering"
}'
```

**Dependencies**:
- ENH-CON-004 (Agent Delegation Protocol)
- ENH-WFL-004 (/create-agent command)

**Benefits**:
- Specialized expertise in 13 domains
- Parallel development capability
- Consistent domain-specific patterns
- Clear agent responsibilities

**Migration Path**:
1. Create agent template (agent-file-template.md)
2. Implement create-agent.sh script
3. Create 13 specialized agents using template
4. Document agent registry in AGENTS.md
5. Update delegation triggers to reference agents
6. Train Claude Code on agent invocation patterns
7. Test multi-agent workflows

**Rollback**: Revert to single general-purpose agent, remove agent context files

---

#### ENH-AGT-002: Agent Registry & Capability Mapping

**ID**: ENH-AGT-002  
**Priority**: CRITICAL  
**Breaking**: No (documentation)

**Description**:
Establishes centralized registry mapping domains to agents with trigger keywords and capability descriptions.

**Registry Structure** (`AGENTS.md`):
```markdown
# Agent Directory

## Available Agents by Department

### Architecture
- **backend-architect**: Backend system design, API architecture, database schema design
- **subagent-architect**: Creating SDD-compliant subagents, constitutional agent workflows

### Engineering
- **frontend-specialist**: React/Next.js development, UI components, state management

### Quality
- **testing-specialist**: Test planning, test automation, quality assurance, bug analysis
- **security-specialist**: Security reviews, vulnerability assessment, secure coding practices
- **performance-engineer**: Performance analysis, bottleneck identification, scalability optimization

### Data
- **database-specialist**: Database schema design, query optimization, data migrations

### Product
- **specification-agent**: Creating detailed software specifications, user stories, functional requirements
- **tasks-agent**: Breaking down technical plans into actionable tasks, managing task dependencies

### Operations
- **devops-engineer**: CI/CD pipeline setup, Docker containerization, cloud deployment
- **performance-engineer**: Performance analysis, monitoring setup, load testing

### Design
- **neomorphism-designer**: Neumorphic design patterns, shadow systems, theme integration
```

**Capability Mapping** (`agent-collaboration.md`):
```markdown
# Agent Collaboration Triggers

## Domain → Agent Mapping

| Domain | Trigger Keywords | Agent | Rationale |
|--------|-----------------|-------|-----------|
| Testing | test, jest, spec, __tests__, contract, QA | testing-specialist | Testing expertise |
| Frontend | component, UI, screen, tsx, jsx, React, state | frontend-specialist | Frontend expertise |
| Database | schema, migration, table, query, sql, index | database-specialist | Database expertise |
| Security | auth, encryption, token, session, secure, password | security-specialist | Security expertise |
| Backend | API, endpoint, service, route, server, middleware | backend-architect | Backend architecture |
| Specification | spec, requirements, user story, PRD, feature | specification-agent | Specification creation |
| Task Planning | tasks, breakdown, dependencies, task list | tasks-agent | Task decomposition |
| Agent Creation | create agent, new agent, subagent | subagent-architect | Agent creation |
| DevOps | CI/CD, Docker, deploy, pipeline, build | devops-engineer | Infrastructure |
| Performance | performance, optimize, bottleneck, slow, latency | performance-engineer | Performance |
| Design | neomorphic, shadow, theme, design system | neomorphism-designer | Design system |
```

**Trigger Detection Script** (`detect-phase-domain.sh`):
```bash
#!/bin/bash
# Detects agent domain based on task content

detect_domain() {
  local task_content="$1"
  
  # Testing triggers
  if echo "$task_content" | grep -qiE '(test|jest|spec|__tests__|contract)'; then
    echo "testing-specialist"
    return 0
  fi
  
  # Frontend triggers
  if echo "$task_content" | grep -qiE '(component|UI|screen|tsx|jsx|React)'; then
    echo "frontend-specialist"
    return 0
  fi
  
  # Database triggers
  if echo "$task_content" | grep -qiE '(schema|migration|table|query|sql)'; then
    echo "database-specialist"
    return 0
  fi
  
  # ... (additional triggers)
  
  # No domain detected
  echo "general-purpose"
  return 1
}

# Usage: detect-phase-domain.sh "task description"
detect_domain "$1"
```

**Rationale**:
- **Discoverability**: Developers can find right agent for task
- **Automation**: Scripts can route tasks to correct agents
- **Consistency**: Standardized agent invocation patterns
- **Documentation**: Clear agent capabilities and responsibilities

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/AGENTS.md` (agent directory)
- `/workspaces/ioun-ai/.specify/memory/agent-collaboration.md` (trigger matrix)
- `/workspaces/ioun-ai/.specify/memory/agent-collaboration-triggers.md` (40+ detailed triggers)
- `/workspaces/ioun-ai/.specify/scripts/bash/detect-phase-domain.sh` (automated detection)
- `/workspaces/ioun-ai/.docs/quick-reference/sdd-agent-delegation.md` (quick reference)

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-CON-004 (Agent Delegation Protocol)

**Benefits**:
- Easy agent discovery
- Automated task routing
- Consistent delegation patterns
- Clear agent boundaries

**Migration Path**:
1. Create AGENTS.md with agent directory
2. Create agent-collaboration.md with trigger matrix
3. Implement detect-phase-domain.sh script
4. Document 40+ triggers in agent-collaboration-triggers.md
5. Create quick reference guide
6. Test trigger detection with sample tasks

**Rollback**: Remove registry files, use manual agent selection

---

#### ENH-AGT-003: Agent Context File Standardization

**ID**: ENH-AGT-003  
**Priority**: HIGH  
**Breaking**: No (documentation standard)

**Description**:
Establishes standardized structure for agent context files ensuring consistent capabilities, constraints, and documentation across all agents.

**Standard Sections** (from `agent-file-template.md`):
```markdown
1. Core Purpose (mission statement)
2. Core Capabilities (3-5 key expertise areas)
3. Department Classification (department, role type, interaction level)
4. Memory References (primary memory path, context, knowledge)
5. Working Principles
   - Constitutional Principles Application
   - Department-Specific Guidelines
6. Tool Usage Policies
   - Authorized Tools
   - MCP Server Access
   - Restricted Operations
7. Collaboration Protocols
   - Upstream Dependencies
   - Downstream Consumers
   - Input/Output Formats
8. Specialized Knowledge
   - Domain Expertise
   - Technical Specifications
   - Best Practices
9. Error Handling
   - Known Limitations
   - Escalation Procedures
10. Performance Standards
    - Response Time Targets
    - Quality Metrics
11. Audit Requirements
12. Update History
```

**Example** (frontend-specialist):
```markdown
# frontend-specialist Agent

## Core Purpose
Specialized agent for React/Next.js development, UI component implementation, and frontend state management following constitutional principles and design system compliance.

## Core Capabilities
- React Native/Expo component development
- TypeScript implementation with type safety
- State management (React Query, Context API)
- Dark neumorphic design system integration
- Frontend testing strategy (E2E with Playwright)

## Department Classification
**Department**: engineering
**Role Type**: Specialist
**Interaction Level**: User-Focused

## Memory References
**Primary Memory**: .docs/agents/engineering/frontend-specialist/
**Context**: .docs/agents/engineering/frontend-specialist/context/
**Knowledge**: .docs/agents/engineering/frontend-specialist/knowledge/

## Working Principles

### Constitutional Principles Application
1. **Library-First**: Extract reusable components to /components directory
2. **Test-First**: E2E tests for critical user flows before implementation
3. **Contract-First**: Define component props interface before implementation
4. **Design System Compliance**: MUST use theme via useTheme(), no hardcoded values

### Department-Specific Guidelines
- Follow React Native best practices
- Use TypeScript strict mode
- Implement responsive design patterns
- Optimize for performance (React.memo, useMemo, useCallback)

## Tool Usage Policies
**Authorized Tools**: Read, Grep, Glob, TodoWrite
**MCP Server Access**: mcp__ref-tools, mcp__browsermcp
**Restricted Operations**: No Git operations without approval

## Collaboration Protocols
**Upstream Dependencies**: 
- specification-agent (provides UI requirements)
- neomorphism-designer (provides design specs)

**Downstream Consumers**:
- testing-specialist (receives components for testing)

**Input Format**: Markdown specification with UI requirements
**Output Format**: TypeScript React Native components

## Specialized Knowledge

### Domain Expertise
- React Native component lifecycle
- Expo managed workflow
- TypeScript type system
- React Query for data fetching
- Dark neumorphic design patterns

### Technical Specifications
- React Native: 0.72+
- Expo SDK: 49+
- TypeScript: 5.0+
- React Query: 4.0+

### Best Practices
- Use functional components with hooks
- Implement error boundaries
- Optimize bundle size
- Follow accessibility guidelines

## Error Handling

### Known Limitations
- Cannot create backend APIs (delegate to backend-architect)
- Cannot modify database schema (delegate to database-specialist)
- Cannot write contract tests (delegate to testing-specialist)

### Escalation Procedures
1. **Minor issues**: Log and continue
2. **Domain boundary**: Delegate to appropriate specialist
3. **Critical issues**: Stop and request user guidance

## Performance Standards
**Response Time Targets**:
- Simple components: < 5 minutes
- Complex features: < 30 minutes
- Full screens: < 60 minutes

**Quality Metrics**:
- Type safety: 100% (no 'any' types)
- Design system compliance: 100%
- Test coverage: E2E for critical flows

## Audit Requirements
All operations must log:
- Component files created/modified
- Design system compliance check
- Type safety validation
- Delegation decisions

## Update History
| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0.0   | 2025-09-15 | Initial creation | create-agent.sh |
```

**Rationale**:
- **Consistency**: All agents documented uniformly
- **Clarity**: Clear capabilities and constraints
- **Maintainability**: Easy to update and audit
- **Onboarding**: New agents follow proven pattern

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/templates/agent-file-template.md` (template)
- All 13 agent context files follow this structure

**Validation**:
```bash
# Check if agent file follows template structure
validate_agent_file() {
  local agent_file=$1
  
  required_sections=(
    "Core Purpose"
    "Core Capabilities"
    "Department Classification"
    "Working Principles"
    "Tool Usage Policies"
    "Collaboration Protocols"
    "Specialized Knowledge"
  )
  
  for section in "${required_sections[@]}"; do
    if ! grep -q "## $section" "$agent_file"; then
      echo "ERROR: Missing section: $section"
      return 1
    fi
  done
  
  echo "Agent file valid"
  return 0
}
```

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-WFL-004 (/create-agent command)

**Benefits**:
- Uniform agent documentation
- Clear agent boundaries
- Easy agent discovery
- Simplified agent creation

**Migration Path**:
1. Create agent-file-template.md
2. Update create-agent.sh to use template
3. Audit existing agent files for compliance
4. Refactor non-compliant files to match template
5. Add validation step to create-agent.sh

**Rollback**: Remove template, allow free-form agent documentation

---

#### ENH-AGT-004: Department-Based Organization

**ID**: ENH-AGT-004  
**Priority**: MEDIUM  
**Breaking**: No (organizational structure)

**Description**:
Organizes agents into 6 departments (Engineering, Data, Quality, Product, Operations, Architecture/Design) with clear roles and interaction patterns.

**Department Structure**:
```markdown
.claude/agents/
├── architecture/
│   ├── backend-architect.md
│   ├── subagent-architect.md
│   └── structure-architect.md
├── data/
│   └── database-specialist.md
├── design/
│   └── neomorphism-designer.md
├── engineering/
│   └── frontend-specialist.md
├── operations/
│   ├── devops-engineer.md
│   └── performance-engineer.md
├── product/
│   ├── specification-agent.md
│   ├── task-orchestrator.md
│   └── tasks-agent.md
└── quality/
    ├── security-specialist.md
    └── testing-specialist.md
```

**Department Roles**:
```markdown
ARCHITECTURE:
- Role: Design and oversight
- Interaction: Cross-functional coordination
- Agents: backend-architect, subagent-architect, structure-architect

DATA:
- Role: Data modeling and persistence
- Interaction: Backend integration
- Agents: database-specialist

DESIGN:
- Role: Visual and UX design
- Interaction: Frontend collaboration
- Agents: neomorphism-designer

ENGINEERING:
- Role: Implementation and development
- Interaction: User-facing features
- Agents: frontend-specialist

OPERATIONS:
- Role: Infrastructure and deployment
- Interaction: System reliability
- Agents: devops-engineer, performance-engineer

PRODUCT:
- Role: Requirements and planning
- Interaction: Cross-functional coordination
- Agents: specification-agent, tasks-agent, task-orchestrator

QUALITY:
- Role: Testing and security
- Interaction: Validation and review
- Agents: testing-specialist, security-specialist
```

**Interaction Patterns**:
```markdown
TYPICAL WORKFLOW:
1. specification-agent (Product) → Creates feature spec
2. backend-architect (Architecture) → Designs architecture
3. database-specialist (Data) → Designs schema
4. frontend-specialist (Engineering) → Implements UI
5. testing-specialist (Quality) → Creates tests
6. security-specialist (Quality) → Reviews security
7. devops-engineer (Operations) → Deploys feature

COORDINATION:
- task-orchestrator coordinates multi-department workflows
- subagent-architect creates new agents when needed
- structure-architect ensures file organization consistency
```

**Rationale**:
- **Clarity**: Clear organizational structure
- **Discoverability**: Easy to find relevant agents
- **Scalability**: Can add agents to departments as needed
- **Collaboration**: Departments map to real-world teams

**Implementation**:

**Files**:
- Directory structure: `.claude/agents/{department}/`
- Department documentation: `.docs/agents/{department}/README.md`
- AGENTS.md lists agents by department

**Auto-Detection** (in create-agent.sh):
```bash
# Automatically determine department based on agent purpose
detect_department() {
  local purpose=$1
  
  case $purpose in
    *"test"*|*"QA"*|*"security"*) echo "quality" ;;
    *"frontend"*|*"UI"*|*"React"*) echo "engineering" ;;
    *"database"*|*"schema"*|*"query"*) echo "data" ;;
    *"design"*|*"theme"*|*"neumorphic"*) echo "design" ;;
    *"architect"*|*"structure"*) echo "architecture" ;;
    *"spec"*|*"task"*|*"orchestrat"*) echo "product" ;;
    *"devops"*|*"deploy"*|*"performance"*) echo "operations" ;;
    *) echo "engineering" ;; # default
  esac
}
```

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)

**Benefits**:
- Clear organizational structure
- Easy agent discovery by domain
- Scalable agent growth
- Natural collaboration patterns

**Migration Path**:
1. Create department directories in `.claude/agents/`
2. Move existing agents to appropriate departments
3. Update AGENTS.md to list by department
4. Add department detection to create-agent.sh
5. Create department README files

**Rollback**: Flatten directory structure, remove department organization

---

#### ENH-AGT-005: Task Orchestrator Agent

**ID**: ENH-AGT-005  
**Priority**: HIGH  
**Breaking**: No (new capability)

**Description**:
Introduces specialized agent for coordinating multi-agent workflows, managing context handoffs, and orchestrating complex features requiring multiple domains.

**Capabilities**:
```markdown
1. INTELLIGENT TASK ANALYSIS
   - Analyze complexity, scope, domain requirements
   - Identify single-agent vs multi-agent scenarios
   - Extract requirements, constraints, success criteria

2. AGENT SELECTION & ROUTING
   - Maintain awareness of available agents
   - Select optimal agent combinations
   - Handle fallback when agents unavailable

3. WORKFLOW ORCHESTRATION PATTERNS
   - Sequential: Task → Agent A → Agent B → Agent C → Result
   - Parallel: Task → Agent A + Agent B → Merged Results
   - Dynamic Routing: Task → Analysis → Route to Specialist
   - Validation: Primary Work → Review Agent → Quality Gate

4. CONTEXT MANAGEMENT
   - Maintain shared context across handoffs
   - Preserve requirements and decisions
   - Track progress and dependencies
   - Handle context compression for token efficiency

5. QUALITY ASSURANCE
   - Implement quality gates
   - Coordinate review patterns
   - Ensure consistency across outputs
   - Validate solutions meet requirements
```

**Auto-Invocation Trigger**:
```markdown
/plan COMMAND AUTO-INVOKES task-orchestrator when:
- Specification requires 2+ specialized domains
- Detection logic scans for keywords: frontend, backend, database, security, testing
- setup-plan.sh outputs: "✓ Multi-agent scenario detected (N domains)"
- Claude Code evaluates if task-orchestrator needed

EXAMPLE MULTI-DOMAIN SPEC:
# Feature: User Authentication System

## Frontend Requirements
- Login/signup forms with validation
- Session management UI components

## Backend Requirements
- JWT authentication endpoints
- Session management service layer

## Database Requirements
- User accounts table with indexes
- Session storage schema

## Security Requirements
- Password hashing with bcrypt
- Token expiration handling

DETECTION RESULT: 4 domains → task-orchestrator recommended

USER APPROVAL PROTOCOL:
1. Explain which agents will be coordinated
2. Request approval: "Would you like me to orchestrate these agents?"
3. Wait for explicit confirmation
4. Execute agent coordination with TodoWrite tracking
```

**Orchestration Decision Matrix**:
```markdown
WHEN TO USE SINGLE AGENT:
- Task clearly within one domain
- Simple, straightforward requirements
- No cross-functional dependencies
- Time-critical operations

WHEN TO ORCHESTRATE MULTIPLE AGENTS:
- Cross-domain requirements
- Complex features requiring multiple expertise areas
- Tasks requiring validation or review
- Production-critical changes
```

**Example Workflow** (New Feature Development):
```markdown
1. specification-agent: Define requirements and user stories
2. backend-architect: Design API and data architecture
3. frontend-specialist: Implement UI
4. testing-specialist: Create and run tests
5. security-specialist: Security review
6. devops-engineer: Deploy to staging

task-orchestrator:
- Coordinates sequence
- Passes context between agents
- Validates each stage
- Ensures requirements met
```

**Rationale**:
- **Coordination**: Complex workflows need orchestration
- **Context**: Prevents context loss in multi-agent handoffs
- **Quality**: Quality gates between stages
- **Efficiency**: Parallel execution where possible

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.claude/agents/product/task-orchestrator.md` (2,000+ lines)
- `/workspaces/ioun-ai/.specify/scripts/bash/setup-plan.sh` (multi-agent detection)

**Integration Points**:
```markdown
WITH /plan COMMAND:
- detect_multi_agent_requirements() function in setup-plan.sh
- Scans spec for domain keywords
- Recommends task-orchestrator when 2+ domains detected

WITH TodoWrite TOOL:
- Creates workflow task lists
- Tracks multi-agent progress
- Updates task status in real-time

WITH ANALYSIS TOOLS:
- Uses Read/Grep/Glob for codebase analysis
- Understands project structure
- Extracts relevant context
```

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-AGT-002 (Agent Registry)
- ENH-WFL-002 (/plan command)

**Benefits**:
- Seamless multi-agent coordination
- Context preservation across handoffs
- Quality gates between stages
- Parallel execution optimization

**Migration Path**:
1. Create task-orchestrator agent context file
2. Add multi-agent detection to setup-plan.sh
3. Document orchestration patterns
4. Implement context handoff format (JSON)
5. Test with multi-domain feature workflows

**Rollback**: Remove task-orchestrator, use manual agent coordination

---

(Continued in next section due to length...)

[The document continues with the remaining enhancements in Categories 2-7, Implementation Recommendations, and Appendices. Would you like me to continue with the next sections?]

#### ENH-AGT-006: Subagent Architect for Agent Creation

**ID**: ENH-AGT-006  
**Priority**: HIGH  
**Breaking**: No (new capability)

**Description**:
Introduces specialized agent responsible for creating new SDD-compliant agents with constitutional alignment and proper tooling restrictions.

**Responsibilities**:
```markdown
1. AGENT CREATION
   - Use agent-file-template.md for structure
   - Determine department based on purpose
   - Set appropriate tool restrictions
   - Initialize memory structure

2. CONSTITUTIONAL COMPLIANCE
   - Ensure agent follows all 14 principles
   - Configure Git operation restrictions
   - Set delegation requirements
   - Add audit trail requirements

3. INTEGRATION
   - Add agent to AGENTS.md registry
   - Update agent-collaboration.md triggers
   - Create agent memory directories
   - Update relevant documentation

4. VALIDATION
   - Validate agent file structure
   - Check for required sections
   - Verify tool restrictions
   - Test agent invocation
```

**Creation Flow**:
```markdown
USER: /create-agent backend-engineer "API and database specialist"

CLAUDE CODE DELEGATES TO:
Task(
  subagent_type="subagent-architect",
  prompt="Create agent: backend-engineer with purpose 'API and database specialist'"
)

SUBAGENT-ARCHITECT:
1. Reads agent-file-template.md
2. Determines department: "engineering" (based on "API")
3. Generates agent context file with:
   - Core purpose and capabilities
   - Constitutional principles application
   - Tool restrictions (Read, Grep, Glob, TodoWrite)
   - Collaboration protocols
   - Specialized knowledge
4. Creates memory structure: .docs/agents/engineering/backend-engineer/
5. Adds to AGENTS.md registry
6. Updates agent-collaboration.md with triggers
7. Returns success with file path
```

**Auto-Detection** (department):
```bash
# In create-agent.sh (called by subagent-architect)
detect_department() {
  local purpose=$1
  
  case $purpose in
    *"test"*|*"QA"*|*"security"*) echo "quality" ;;
    *"frontend"*|*"UI"*|*"React"*) echo "engineering" ;;
    *"database"*|*"schema"*|*"query"*) echo "data" ;;
    *"design"*|*"theme"*|*"neumorphic"*) echo "design" ;;
    *"architect"*|*"structure"*) echo "architecture" ;;
    *"spec"*|*"task"*|*"orchestrat"*) echo "product" ;;
    *"devops"*|*"deploy"*|*"performance"*) echo "operations" ;;
    *) echo "engineering" ;; # default
  esac
}
```

**Rationale**:
- **Consistency**: All agents follow same structure
- **Quality**: Constitutional compliance baked in
- **Efficiency**: Automated agent creation
- **Scalability**: Easy to add new agents as needed

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.claude/agents/architecture/subagent-architect.md` (agent context)
- `/workspaces/ioun-ai/.specify/scripts/bash/create-agent.sh` (automation script)
- `/workspaces/ioun-ai/.specify/templates/agent-file-template.md` (template)

**Script** (create-agent.sh):
```bash
#!/bin/bash
# Creates new SDD-compliant agent with constitutional alignment

set -euo pipefail

# Parse JSON arguments
ARGS=$(cat)
AGENT_NAME=$(echo "$ARGS" | jq -r '.name')
AGENT_PURPOSE=$(echo "$ARGS" | jq -r '.purpose')
DEPARTMENT=$(echo "$ARGS" | jq -r '.department // empty')

# Auto-detect department if not provided
if [ -z "$DEPARTMENT" ]; then
  DEPARTMENT=$(detect_department "$AGENT_PURPOSE")
fi

# Create agent context file
AGENT_FILE=".claude/agents/$DEPARTMENT/$AGENT_NAME.md"
mkdir -p "$(dirname "$AGENT_FILE")"

# Generate from template
generate_agent_file() {
  sed "s/{{AGENT_NAME}}/$AGENT_NAME/g; s/{{AGENT_PURPOSE}}/$AGENT_PURPOSE/g; s/{{DEPARTMENT}}/$DEPARTMENT/g" \
    .specify/templates/agent-file-template.md > "$AGENT_FILE"
}

generate_agent_file

# Create memory structure
mkdir -p ".docs/agents/$DEPARTMENT/$AGENT_NAME/context"
mkdir -p ".docs/agents/$DEPARTMENT/$AGENT_NAME/knowledge"

# Add to registry
echo "- **$AGENT_NAME**: $AGENT_PURPOSE" >> AGENTS.md

# Output success
echo "{\"status\":\"success\",\"agent_file\":\"$AGENT_FILE\",\"department\":\"$DEPARTMENT\"}"
```

**Dependencies**:
- ENH-AGT-003 (Agent Context File Standardization)
- ENH-WFL-004 (/create-agent command)

**Benefits**:
- Rapid agent creation (< 1 minute)
- Guaranteed constitutional compliance
- Consistent agent structure
- Reduced human error

**Migration Path**:
1. Create subagent-architect context file
2. Implement create-agent.sh script
3. Create agent-file-template.md
4. Add /create-agent command
5. Test agent creation workflow
6. Document agent creation process

**Rollback**: Remove subagent-architect, use manual agent creation

---

#### ENH-AGT-007: Agent Tool Restrictions

**ID**: ENH-AGT-007  
**Priority**: MEDIUM  
**Breaking**: No (safety mechanism)

**Description**:
Establishes tool restriction policies for each agent, limiting access to only required tools for their domain.

**Tool Categories**:
```markdown
FILE OPERATIONS:
- Read: Read file contents
- Grep: Search file contents
- Glob: Find files by pattern
- Write: Create/update files (restricted)
- Edit: Modify files (restricted)

EXECUTION:
- Bash: Execute shell commands (restricted)
- TodoWrite: Create task lists (universal)

MCP SERVERS:
- mcp__ref-tools: Reference documentation
- mcp__browsermcp: Browser automation
- mcp__perplexity: Web research
```

**Restriction Matrix**:
```markdown
| Agent | Read | Grep | Glob | Write | Edit | Bash | TodoWrite | MCP |
|-------|------|------|------|-------|------|------|-----------|-----|
| frontend-specialist | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools, browsermcp |
| backend-architect | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools |
| database-specialist | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools |
| testing-specialist | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools, browsermcp |
| security-specialist | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools |
| specification-agent | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools, perplexity |
| tasks-agent | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools |
| task-orchestrator | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ref-tools, browsermcp, perplexity |
| subagent-architect | ✅ | ✅ | ✅ | ❌ | ❌ | ✅* | ✅ | ref-tools |
| devops-engineer | ✅ | ✅ | ✅ | ❌ | ❌ | ✅* | ✅ | ref-tools |

* Bash access limited to specific scripts (create-agent.sh, deployment scripts)
```

**Rationale**:
- **Safety**: Prevents accidental file modifications
- **Clarity**: Agents know their boundaries
- **Auditability**: Clear record of what each agent can do
- **Consistency**: Standardized tool access patterns

**Implementation**:

**Files**:
- Each agent context file has "Tool Usage Policies" section
- Example from frontend-specialist:

```markdown
## Tool Usage Policies

### Authorized Tools
Read, Grep, Glob, TodoWrite

### MCP Server Access
mcp__ref-tools, mcp__browsermcp

### Restricted Operations
- No Git operations without approval
- No direct file writing (delegate to user/other tools)
- No Bash execution (delegate to devops-engineer)
- No database operations (delegate to database-specialist)
```

**Enforcement**:
- Documented in agent context files
- Validated during agent creation by subagent-architect
- Agents trained to respect restrictions

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-AGT-003 (Agent Context File Standardization)

**Benefits**:
- Clear agent boundaries
- Prevented accidental changes
- Safer multi-agent workflows
- Audit trail for tool usage

**Migration Path**:
1. Define tool restriction matrix
2. Add "Tool Usage Policies" to agent-file-template.md
3. Update all agent context files with restrictions
4. Document restricted operations
5. Train agents to respect boundaries

**Rollback**: Remove tool restrictions, allow full tool access

---

#### ENH-AGT-008: Agent Memory Structure

**ID**: ENH-AGT-008  
**Priority**: LOW  
**Breaking**: No (organizational structure)

**Description**:
Establishes standardized memory structure for agents with context and knowledge directories.

**Memory Structure**:
```
.docs/agents/{department}/{agent-name}/
├── context/                    # Session-specific context
│   ├── current-session.md      # Active work context
│   ├── recent-decisions.md     # Recent decision log
│   └── handoff-notes.md        # Context for handoffs
├── knowledge/                  # Persistent knowledge
│   ├── patterns.md             # Common patterns
│   ├── best-practices.md       # Domain best practices
│   └── troubleshooting.md      # Common issues
└── README.md                   # Agent overview
```

**Context Files**:
```markdown
PURPOSE: Short-term memory for active sessions
CONTENTS:
- Current work in progress
- Recent decisions and rationale
- Temporary notes for handoffs
- Session-specific data

LIFECYCLE: Cleared at end of session or feature completion
```

**Knowledge Files**:
```markdown
PURPOSE: Long-term memory for domain expertise
CONTENTS:
- Proven patterns and solutions
- Domain-specific best practices
- Common troubleshooting steps
- Lessons learned

LIFECYCLE: Persistent, updated as knowledge grows
```

**Example** (frontend-specialist/knowledge/patterns.md):
```markdown
# Frontend Component Patterns

## Dark Neumorphic Cards
Pattern: Raised card with dual shadows and gradient background

Implementation:
```typescript
const { theme } = useTheme();
const { raisedDual } = useShadows();

<View style={[raisedDual, { backgroundColor: theme.colors.background.card }]}>
  {children}
</View>
```

Rationale: Consistent with design system v2.4, avoids hardcoded values
```

**Rationale**:
- **Context Preservation**: Maintains session continuity
- **Knowledge Accumulation**: Builds domain expertise over time
- **Handoff Support**: Facilitates agent-to-agent context transfer
- **Learning**: Agents can reference past solutions

**Implementation**:

**Files**:
- Directory structure: `.docs/agents/{department}/{agent-name}/`
- Created automatically by create-agent.sh
- Referenced in agent context files:

```markdown
## Memory References
**Primary Memory**: .docs/agents/engineering/frontend-specialist/
**Context**: .docs/agents/engineering/frontend-specialist/context/
**Knowledge**: .docs/agents/engineering/frontend-specialist/knowledge/
```

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-AGT-006 (Subagent Architect)

**Benefits**:
- Persistent agent knowledge
- Context preservation across sessions
- Improved agent performance over time
- Better handoffs between agents

**Migration Path**:
1. Define memory structure
2. Update create-agent.sh to create directories
3. Create initial knowledge files for existing agents
4. Document memory management practices
5. Train agents to use memory effectively

**Rollback**: Remove memory directories, rely on agent context files only

---

#### ENH-AGT-009: Agent Collaboration Triggers (40+ Triggers)

**ID**: ENH-AGT-009  
**Priority**: HIGH  
**Breaking**: No (automation enhancement)

**Description**:
Expands trigger matrix from basic domain keywords to 40+ specific triggers with rationale and context detection.

**Trigger Categories**:

**Testing Domain** (8 triggers):
```markdown
| Trigger | Agent | Context |
|---------|-------|---------|
| test | testing-specialist | Any testing work |
| Test | testing-specialist | Capitalized (task titles) |
| testing | testing-specialist | Testing strategy discussions |
| jest | testing-specialist | Jest test framework |
| spec | testing-specialist | Test specifications |
| __tests__ | testing-specialist | Test directory pattern |
| contract | testing-specialist | Contract testing |
| integration | testing-specialist | Integration testing |
```

**Frontend Domain** (10 triggers):
```markdown
| Trigger | Agent | Context |
|---------|-------|---------|
| component | frontend-specialist | React components |
| UI | frontend-specialist | User interface work |
| screen | frontend-specialist | Screen implementations |
| form | frontend-specialist | Form components |
| validation | frontend-specialist | Input validation |
| tsx | frontend-specialist | TypeScript React files |
| jsx | frontend-specialist | JavaScript React files |
| React | frontend-specialist | React framework |
| state | frontend-specialist | State management |
| navigation | frontend-specialist | Navigation setup |
```

**Database Domain** (8 triggers):
```markdown
| Trigger | Agent | Context |
|---------|-------|---------|
| schema | database-specialist | Database schema |
| migration | database-specialist | Database migrations |
| table | database-specialist | Table definitions |
| query | database-specialist | SQL queries |
| sql | database-specialist | SQL operations |
| index | database-specialist | Database indexes |
| constraint | database-specialist | Database constraints |
| RLS | database-specialist | Row-Level Security |
```

**Security Domain** (6 triggers):
```markdown
| Trigger | Agent | Context |
|---------|-------|---------|
| auth | security-specialist | Authentication |
| authentication | security-specialist | Auth systems |
| encryption | security-specialist | Data encryption |
| token | security-specialist | Token management |
| session | security-specialist | Session handling |
| secure | security-specialist | Security hardening |
```

**Backend Domain** (6 triggers):
```markdown
| Trigger | Agent | Context |
|---------|-------|---------|
| API | backend-architect | API design |
| endpoint | backend-architect | API endpoints |
| service | backend-architect | Service layer |
| route | backend-architect | Route handlers |
| server | backend-architect | Server setup |
| middleware | backend-architect | Middleware |
```

**Additional Domains**: Design, DevOps, Performance, Specification, Task Planning (12+ more triggers)

**Detection Script** (enhanced detect-phase-domain.sh):
```bash
#!/bin/bash
# Enhanced domain detection with 40+ triggers

detect_domain() {
  local content="$1"
  local domains=()
  
  # Testing triggers (8)
  if echo "$content" | grep -qiE '(test|Test|testing|jest|spec|__tests__|contract|integration)'; then
    domains+=("testing-specialist")
  fi
  
  # Frontend triggers (10)
  if echo "$content" | grep -qiE '(component|UI|screen|form|validation|tsx|jsx|React|state|navigation)'; then
    domains+=("frontend-specialist")
  fi
  
  # Database triggers (8)
  if echo "$content" | grep -qiE '(schema|migration|table|query|sql|index|constraint|RLS)'; then
    domains+=("database-specialist")
  fi
  
  # Security triggers (6)
  if echo "$content" | grep -qiE '(auth|authentication|encryption|token|session|secure)'; then
    domains+=("security-specialist")
  fi
  
  # Backend triggers (6)
  if echo "$content" | grep -qiE '(API|endpoint|service|route|server|middleware)'; then
    domains+=("backend-architect")
  fi
  
  # ... (additional domains)
  
  # Output detected domains
  if [ ${#domains[@]} -eq 0 ]; then
    echo "general-purpose"
  elif [ ${#domains[@]} -eq 1 ]; then
    echo "${domains[0]}"
  else
    # Multiple domains detected → task-orchestrator
    echo "task-orchestrator: ${domains[*]}"
  fi
}

# Usage
detect_domain "$1"
```

**Rationale**:
- **Accuracy**: More triggers = better detection
- **Automation**: Reduces manual agent selection
- **Multi-domain**: Detects when orchestration needed
- **Comprehensive**: Covers all specialized domains

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/agent-collaboration-triggers.md` (40+ triggers documented)
- `/workspaces/ioun-ai/.specify/scripts/bash/detect-phase-domain.sh` (automated detection)
- `/workspaces/ioun-ai/.docs/quick-reference/sdd-agent-delegation.md` (quick reference)

**Dependencies**:
- ENH-AGT-002 (Agent Registry & Capability Mapping)
- ENH-CON-002 (Work Session Initiation Protocol)

**Benefits**:
- High-accuracy domain detection
- Reduced manual agent selection
- Multi-domain workflow detection
- Comprehensive trigger coverage

**Migration Path**:
1. Expand agent-collaboration-triggers.md to 40+ triggers
2. Enhance detect-phase-domain.sh with all triggers
3. Add multi-domain detection (for task-orchestrator)
4. Test detection accuracy with sample tasks
5. Refine triggers based on false positives/negatives

**Rollback**: Reduce to basic triggers (5-10), remove automated detection

---

#### ENH-AGT-010: Direct Agent Invocation Pattern

**ID**: ENH-AGT-010  
**Priority**: CRITICAL  
**Breaking**: Yes (changes invocation method)

**Description**:
Establishes pattern for directly invoking specialized agents via Task tool, eliminating need to load agent context files manually.

**Old Pattern** (context file loading):
```markdown
❌ INCORRECT (pre-enhancement):
1. User: "I need to create a test suite"
2. Claude Code: *loads testing-specialist.md as context*
3. Claude Code: *executes testing work directly*

PROBLEMS:
- Agent context not fully activated
- Constitutional principles not applied correctly
- No delegation audit trail
```

**New Pattern** (direct invocation):
```markdown
✅ CORRECT (post-enhancement):
1. User: "I need to create a test suite"
2. Claude Code: *detects "test" trigger*
3. Claude Code: Task(
     subagent_type="testing-specialist",
     description="Create test suite for campaign management",
     prompt="[detailed requirements]"
   )
4. Testing-specialist: *fully activated with context*
5. Testing-specialist: *executes work with constitutional compliance*
```

**Invocation Syntax**:
```python
Task(
  subagent_type="<agent-name>",  # e.g., "frontend-specialist"
  description="<brief task summary>",
  prompt="<detailed requirements, constraints, expected deliverables>"
)
```

**Context File Role**:
```markdown
AGENT CONTEXT FILES ARE:
✅ Reference documentation for agent capabilities
✅ Used for understanding agent expertise areas
✅ Training data for agent behavior

AGENT CONTEXT FILES ARE NOT:
❌ Required to be loaded before invocation
❌ Manually loaded by user/Claude Code
❌ Context window payload (Task tool handles this)
```

**Rationale**:
- **Activation**: Task tool properly activates agent with full context
- **Constitutional**: Ensures constitutional compliance applied
- **Audit**: Creates clear delegation audit trail
- **Efficiency**: No manual context loading required

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 75-140: Direct invocation pattern)
- `/workspaces/ioun-ai/.docs/architecture/sdd-agent-direct-invocation.md` (architecture spec)
- `/workspaces/ioun-ai/.docs/quick-reference/sdd-agent-delegation.md` (quick reference)

**Documentation** (from CLAUDE.md):
```markdown
## HARD STOP: Specialized Agent Delegation

**For specialized domain tasks, invoke the specialized agent DIRECTLY:**

**Correct Pattern:**
```python
# ✅ CORRECT: Direct invocation of specialized agent
Task(
  subagent_type="frontend-specialist",
  description="Implement tier enforcement UI",
  prompt="[detailed task description]"
)
```

**Domain → Agent Mapping:**
- Database operations → database-specialist
- Testing work → testing-specialist
- Frontend/UI development → frontend-specialist
- Backend/API design → backend-architect
- Security reviews → security-specialist

**When to reference `.claude/agents/` files:**
- ✅ To understand agent capabilities
- ✅ To review patterns and best practices
- ❌ NOT for invocation (agents are executable directly)
```

**Dependencies**:
- ENH-AGT-001 (Multi-Agent Architecture)
- ENH-CON-004 (Agent Delegation Protocol)

**Benefits**:
- Proper agent activation
- Constitutional compliance guaranteed
- Clear audit trail
- Simplified invocation process

**Migration Path**:
1. Document direct invocation pattern in CLAUDE.md
2. Create architecture spec (sdd-agent-direct-invocation.md)
3. Update quick reference guide
4. Train Claude Code on invocation syntax
5. Test agent invocations, verify proper activation
6. Phase out context file loading pattern

**Rollback**: Revert to context file loading, remove Task invocation pattern

---

#### ENH-AGT-011: Agent Violation Detection & Self-Reporting

**ID**: ENH-AGT-011  
**Priority**: MEDIUM  
**Breaking**: No (quality mechanism)

**Description**:
Establishes protocol for agents to detect and self-report when they execute specialized work directly instead of delegating.

**Violation Detection Protocol**:
```markdown
IF AGENT REALIZES mid-task that it's executing specialized work directly:

1. STOP IMMEDIATELY
   - Do not continue execution
   - Do not complete the implementation

2. ACKNOWLEDGE
   - "I detected I'm [writing tests/creating UI/etc.] directly"
   - "This should have been delegated to [specialist-agent]"

3. RE-DELEGATE
   - Use Task tool with correct agent
   - Pass all context and requirements

4. DISCARD
   - Let specialized agent redo the work
   - Do not try to salvage direct implementation

5. DOCUMENT
   - Log violation in dev log
   - Note detection trigger for future improvement
```

**Example**:
```markdown
USER: "Create a login form component"

CLAUDE CODE: *starts implementing directly*
```typescript
const LoginForm = () => {
  return <View>...</View>
}
```

CLAUDE CODE: *realizes "component" trigger should have delegated*

CLAUDE CODE: "I detected I'm creating UI components directly. This should have been delegated to frontend-specialist per Constitutional Principle X. Let me re-delegate this work."

Task(
  subagent_type="frontend-specialist",
  description="Create login form component",
  prompt="Create a login form component with..."
)
```

**Self-Detection Triggers**:
```markdown
DETECT VIOLATION WHEN:
- Writing tests directly (should be testing-specialist)
- Creating UI components directly (should be frontend-specialist)
- Modifying database schema directly (should be database-specialist)
- Implementing security features directly (should be security-specialist)
- Creating specifications directly (should be specification-agent)
- Generating tasks directly (should be tasks-agent)
```

**Rationale**:
- **Quality**: Ensures specialized work done by specialists
- **Learning**: Agents improve through violation detection
- **Audit**: Violations logged for process improvement
- **Recovery**: Clean re-delegation prevents low-quality output

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/CLAUDE.md` (Violation Self-Detection section)
- `/workspaces/ioun-ai/.specify/memory/constitution.md` (Principle X enforcement)
- Agent context files (self-detection requirements)

**Enforcement**:
- Documented in constitutional Work Session Initiation Protocol
- Agents trained to self-monitor during execution
- Violations logged in dev logs for analysis

**Dependencies**:
- ENH-CON-002 (Work Session Initiation Protocol)
- ENH-CON-004 (Agent Delegation Protocol)

**Benefits**:
- Reduced delegation violations
- Improved agent learning
- Quality assurance mechanism
- Process improvement data

**Migration Path**:
1. Document violation detection protocol in CLAUDE.md
2. Add self-detection requirements to agent context files
3. Train agents on violation detection
4. Establish violation logging process
5. Monitor violations, refine detection triggers

**Rollback**: Remove self-detection requirement, accept violations

---

### Category 3: Workflow Automation

#### ENH-WFL-001: /specify Command Enhancement

**ID**: ENH-WFL-001  
**Priority**: CRITICAL  
**Breaking**: Yes (requires user approval for branch creation)

**Description**:
Enhances /specify command to require user approval for branch creation and delegate specification creation to specification-agent.

**Original Workflow**:
```bash
# Original create-new-feature.sh
1. Parse feature number and name
2. Create feature branch automatically
3. Generate spec file
4. Return success
```

**Enhanced Workflow**:
```bash
# Enhanced create-new-feature.sh with approval gate
1. Parse feature number and name
2. ASK USER: "Would you like a new feature branch created?"
3. IF YES: Ask for desired branch format/name
4. IF YES: Create branch with approved format
5. IF NO: Create spec file in current branch
6. Generate spec file from template
7. Delegate to specification-agent for content
8. Return success with file path
```

**User Approval Protocol**:
```markdown
CLAUDE CODE: "This sounds like a new feature requiring specification. Would you like me to use the /specify command? This will:
- Generate a spec file at specs/###-feature-name/spec.md
- Optionally create a new feature branch (I'll ask you about this)
- Set up the foundation for implementation planning"

USER: "Yes, go ahead"

CLAUDE CODE: "Would you like a new feature branch created for this feature?"

USER: "Yes, use format 010-audio-recording"

CLAUDE CODE: *creates branch 010-audio-recording*
CLAUDE CODE: *generates spec file*
CLAUDE CODE: Task(
  subagent_type="specification-agent",
  description="Create specification for audio recording feature",
  prompt="[requirements and context]"
)
```

**Constitutional Compliance** (Principle VI):
```markdown
GIT OPERATION APPROVAL GATE:
✅ Branch creation requires explicit user approval
✅ User specifies branch name format
✅ User can decline branch creation
❌ NEVER create branches automatically
```

**Delegation Requirement** (Principle X):
```markdown
SPECIFICATION CREATION MUST BE DELEGATED:
✅ /specify command triggers specification-agent invocation
✅ Specification-agent creates detailed spec content
❌ NEVER create specifications directly without delegation
```

**Rationale**:
- **Safety**: User controls Git operations
- **Quality**: Specifications created by specialist
- **Flexibility**: User chooses branch strategy
- **Constitutional**: Enforces Principles VI and X

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/create-new-feature.sh` (approval gates)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 331-357: /specify command documentation)
- `/workspaces/ioun-ai/.claude/agents/product/specification-agent.md` (specialist)

**Script Changes**:
```bash
# create-new-feature.sh excerpt
if [ "$CREATE_BRANCH" = "true" ]; then
  # Branch creation requested - must have user approval
  if [ -z "$BRANCH_NAME" ]; then
    echo "ERROR: Branch creation requested but no branch name provided"
    echo "User approval required for Git operations (Constitutional Principle VI)"
    exit 1
  fi
  
  # Create branch (user already approved)
  git checkout -b "$BRANCH_NAME"
  echo "✓ Created branch: $BRANCH_NAME"
fi

# Generate spec file
mkdir -p "specs/$FEATURE_DIR"
cp .specify/templates/spec-template.md "specs/$FEATURE_DIR/spec.md"

# Output for specification-agent delegation
echo "{\"status\":\"success\",\"spec_file\":\"specs/$FEATURE_DIR/spec.md\",\"branch\":\"$BRANCH_NAME\"}"
```

**Dependencies**:
- ENH-CON-003 (Git Operation Approval Protocol)
- ENH-CON-004 (Agent Delegation Protocol)
- ENH-AGT-001 (specification-agent)

**Benefits**:
- User maintains Git control
- High-quality specifications from specialist
- Flexible branching strategies
- Constitutional compliance guaranteed

**Migration Path**:
1. Add approval gates to create-new-feature.sh
2. Remove automatic branch creation
3. Update /specify documentation with approval protocol
4. Create specification-agent
5. Test workflow with approval steps
6. Train Claude Code on new workflow

**Rollback**: Remove approval gates, allow automatic branch creation

---

#### ENH-WFL-002: /plan Command with Multi-Agent Detection

**ID**: ENH-WFL-002  
**Priority**: HIGH  
**Breaking**: No (enhanced capability)

**Description**:
Enhances /plan command to detect multi-domain specifications and automatically recommend task-orchestrator for coordination.

**Original Workflow**:
```bash
# Original setup-plan.sh
1. Read feature spec
2. Generate research.md
3. Generate data-model.md
4. Generate contracts/
5. Generate quickstart.md
6. Return success
```

**Enhanced Workflow**:
```bash
# Enhanced setup-plan.sh with multi-agent detection
1. Read feature spec
2. DETECT DOMAINS: Scan spec for keywords (frontend, backend, database, security, testing)
3. IF 2+ domains detected:
   - Output: "✓ Multi-agent scenario detected (N domains)"
   - Recommend: "Consider invoking task-orchestrator for coordination"
4. Generate research.md
5. Generate data-model.md
6. Generate contracts/
7. Generate quickstart.md
8. Return success with domain detection results
```

**Multi-Agent Detection Logic**:
```bash
# From setup-plan.sh
detect_multi_agent_requirements() {
  local spec_file=$1
  local domains=()
  
  # Scan spec for domain keywords
  grep -qiE '(frontend|UI|component|React)' "$spec_file" && domains+=("frontend")
  grep -qiE '(backend|API|endpoint|service)' "$spec_file" && domains+=("backend")
  grep -qiE '(database|schema|migration|table)' "$spec_file" && domains+=("database")
  grep -qiE '(security|auth|encryption|token)' "$spec_file" && domains+=("security")
  grep -qiE '(test|testing|QA|spec)' "$spec_file" && domains+=("testing")
  
  # Output result
  local domain_count=${#domains[@]}
  if [ $domain_count -ge 2 ]; then
    echo "✓ Multi-agent scenario detected ($domain_count domains: ${domains[*]})"
    echo "RECOMMENDATION: Invoke task-orchestrator for coordination"
    return 0
  else
    echo "Single-agent scenario (${domains[0]:-general})"
    return 1
  fi
}
```

**Task-Orchestrator Invocation** (auto-trigger):
```markdown
WHEN /plan DETECTS multi-domain spec:

CLAUDE CODE:
1. Read detection output from setup-plan.sh
2. Evaluate: "This specification requires coordination across frontend, backend, database, and security domains"
3. ASK USER: "This will coordinate frontend-specialist, backend-architect, database-specialist, and security-specialist. Would you like me to orchestrate these agents to generate the implementation plan?"
4. IF USER APPROVES:
   Task(
     subagent_type="task-orchestrator",
     description="Coordinate multi-agent planning for [feature]",
     prompt="Coordinate frontend-specialist, backend-architect, database-specialist, and security-specialist to generate implementation plan for [feature]"
   )
5. IF USER DECLINES:
   - Proceed with standard single-agent planning
```

**Rationale**:
- **Automation**: Detects complex scenarios automatically
- **Quality**: Multi-domain features get proper coordination
- **Efficiency**: Parallel agent execution where possible
- **User Control**: User approves orchestration before execution

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/setup-plan.sh` (detection logic)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 342-346: /plan documentation)
- `/workspaces/ioun-ai/.claude/agents/product/task-orchestrator.md` (orchestrator logic)

**Script Changes**:
```bash
# setup-plan.sh excerpt
# Detect multi-agent requirements
echo "Analyzing specification for multi-agent requirements..."
MULTI_AGENT_RESULT=$(detect_multi_agent_requirements "$SPEC_FILE")
echo "$MULTI_AGENT_RESULT"

# Generate planning artifacts
generate_research
generate_data_model
generate_contracts
generate_quickstart

# Output results
echo "{\"status\":\"success\",\"multi_agent\":\"$MULTI_AGENT_RESULT\"}"
```

**Dependencies**:
- ENH-AGT-005 (Task Orchestrator Agent)
- ENH-AGT-009 (Agent Collaboration Triggers)

**Benefits**:
- Automatic multi-domain detection
- Intelligent orchestration recommendations
- Improved planning quality
- Reduced manual coordination

**Migration Path**:
1. Add detect_multi_agent_requirements() to setup-plan.sh
2. Integrate detection into /plan workflow
3. Update /plan documentation with auto-invocation
4. Create task-orchestrator agent
5. Test with multi-domain specifications
6. Refine domain detection logic

**Rollback**: Remove detection logic, use manual orchestration decisions

---

#### ENH-WFL-003: /tasks Command with Dependency Tracking

**ID**: ENH-WFL-003  
**Priority**: HIGH  
**Breaking**: No (enhanced capability)

**Description**:
Enhances /tasks command to delegate task generation to tasks-agent and include dependency tracking with parallel execution markers.

**Original Workflow**:
```bash
# Basic task generation
1. Read plan.md
2. Generate simple task list
3. Number tasks sequentially
4. Return success
```

**Enhanced Workflow**:
```bash
# Enhanced check-task-prerequisites.sh with delegation
1. Verify prerequisites (spec.md, plan.md, research.md, data-model.md, contracts/)
2. IF prerequisites missing: Error with missing items
3. IF prerequisites complete:
   - Read all planning artifacts
   - Analyze dependencies
   - Delegate to tasks-agent:
     Task(
       subagent_type="tasks-agent",
       description="Generate dependency-ordered tasks for [feature]",
       prompt="[planning artifacts context]"
     )
4. tasks-agent generates tasks.md with:
   - Dependency-ordered tasks
   - [P] markers for parallel-executable tasks
   - Prerequisite links (Depends on: T###)
5. Validate tasks.md structure
6. Return success
```

**Dependency Tracking Format**:
```markdown
# Example tasks.md output

## Tasks

### T001: Create Campaign Model
**Status**: pending
**Type**: data-model
**Dependencies**: None
**Parallel**: [P] Can execute in parallel with T002, T003

Create Campaign TypeScript model with tier restrictions.

### T002: Create RLS Policies
**Status**: pending
**Type**: database
**Dependencies**: Depends on T001 (needs Campaign model)
**Parallel**: No (sequential)

Implement Row-Level Security policies for tier enforcement.

### T003: Design CampaignCard Component
**Status**: pending
**Type**: frontend
**Dependencies**: None
**Parallel**: [P] Can execute in parallel with T001, T002

Design neumorphic campaign card component.

### T004: Implement CampaignCard Component
**Status**: pending
**Type**: frontend
**Dependencies**: Depends on T001 (needs Campaign type), T003 (needs design)
**Parallel**: No (sequential after T001, T003)

Implement campaign card with theme compliance.
```

**Parallel Execution Markers**:
```markdown
[P] MARKER INDICATES:
- Task can execute in parallel with other [P] tasks
- No dependencies on pending tasks
- Safe for concurrent agent execution

USAGE:
- Identify [P] tasks in task list
- Launch multiple agents simultaneously for [P] tasks
- Coordinate results after parallel execution
```

**Prerequisite Validation**:
```bash
# From check-task-prerequisites.sh
validate_prerequisites() {
  local spec_dir=$1
  local missing=()
  
  [ ! -f "$spec_dir/spec.md" ] && missing+=("spec.md")
  [ ! -f "$spec_dir/plan.md" ] && missing+=("plan.md")
  [ ! -f "$spec_dir/research.md" ] && missing+=("research.md")
  [ ! -f "$spec_dir/data-model.md" ] && missing+=("data-model.md")
  [ ! -d "$spec_dir/contracts" ] && missing+=("contracts/")
  
  if [ ${#missing[@]} -gt 0 ]; then
    echo "ERROR: Missing prerequisites: ${missing[*]}"
    echo "Run /plan command first to generate planning artifacts"
    return 1
  fi
  
  return 0
}
```

**Rationale**:
- **Quality**: Task generation by specialist
- **Efficiency**: Parallel execution where possible
- **Safety**: Dependency tracking prevents order errors
- **Validation**: Prerequisites checked before task generation

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/check-task-prerequisites.sh` (validation + delegation)
- `/workspaces/ioun-ai/.claude/agents/product/tasks-agent.md` (specialist)
- `/workspaces/ioun-ai/.specify/templates/tasks-template.md` (enhanced template)

**Script Changes**:
```bash
# check-task-prerequisites.sh excerpt
# Validate prerequisites
validate_prerequisites "$SPEC_DIR" || exit 1

# Delegate to tasks-agent
echo "Prerequisites validated. Delegating to tasks-agent for task generation..."
# (Claude Code will invoke tasks-agent via Task tool)

# Validate generated tasks.md
if [ -f "$SPEC_DIR/tasks.md" ]; then
  echo "✓ tasks.md generated successfully"
  # Validate structure (has T### tasks, status fields, etc.)
  validate_tasks_structure "$SPEC_DIR/tasks.md"
else
  echo "ERROR: tasks.md not generated"
  exit 1
fi
```

**Dependencies**:
- ENH-AGT-001 (tasks-agent)
- ENH-CON-004 (Agent Delegation Protocol)
- ENH-TPL-003 (Enhanced tasks-template.md)

**Benefits**:
- High-quality task breakdowns from specialist
- Dependency tracking prevents errors
- Parallel execution optimization
- Prerequisite validation

**Migration Path**:
1. Add prerequisite validation to check-task-prerequisites.sh
2. Create tasks-agent
3. Enhance tasks-template.md with dependency fields
4. Update /tasks documentation with delegation
5. Test with complex multi-domain features
6. Refine dependency detection

**Rollback**: Remove prerequisite validation, generate tasks directly

---

#### ENH-WFL-004: /create-agent Command

**ID**: ENH-WFL-004  
**Priority**: HIGH  
**Breaking**: No (new capability)

**Description**:
Introduces /create-agent command for automated creation of SDD-compliant agents with constitutional alignment.

**Command Syntax**:
```markdown
/create-agent <agent-name> "<agent-purpose>"

EXAMPLE:
/create-agent backend-engineer "API and database specialist"
```

**Workflow**:
```markdown
1. USER: /create-agent backend-engineer "API and database specialist"

2. CLAUDE CODE DELEGATES TO:
   Task(
     subagent_type="subagent-architect",
     description="Create agent: backend-engineer",
     prompt="Create SDD-compliant agent with name 'backend-engineer' and purpose 'API and database specialist'"
   )

3. SUBAGENT-ARCHITECT:
   - Executes create-agent.sh via Bash tool
   - Passes JSON arguments: {"name": "backend-engineer", "purpose": "API and database specialist"}

4. CREATE-AGENT.SH:
   - Auto-detects department: "engineering" (from "API")
   - Generates agent file: .claude/agents/engineering/backend-engineer.md
   - Creates memory structure: .docs/agents/engineering/backend-engineer/
   - Adds to AGENTS.md registry
   - Updates agent-collaboration.md triggers
   - Returns success with file path

5. SUBAGENT-ARCHITECT REPORTS:
   "✓ Created agent: backend-engineer
   - File: .claude/agents/engineering/backend-engineer.md
   - Department: engineering
   - Purpose: API and database specialist
   - Memory: .docs/agents/engineering/backend-engineer/"
```

**Script** (create-agent.sh):
```bash
#!/bin/bash
# Creates SDD-compliant agent with constitutional alignment

set -euo pipefail

# Parse JSON arguments from stdin
ARGS=$(cat)
AGENT_NAME=$(echo "$ARGS" | jq -r '.name')
AGENT_PURPOSE=$(echo "$ARGS" | jq -r '.purpose')
DEPARTMENT=$(echo "$ARGS" | jq -r '.department // empty')

# Auto-detect department if not provided
if [ -z "$DEPARTMENT" ]; then
  DEPARTMENT=$(detect_department "$AGENT_PURPOSE")
fi

# Create agent context file from template
AGENT_FILE=".claude/agents/$DEPARTMENT/$AGENT_NAME.md"
mkdir -p "$(dirname "$AGENT_FILE")"

generate_agent_file() {
  sed -e "s/{{AGENT_NAME}}/$AGENT_NAME/g" \
      -e "s/{{AGENT_PURPOSE}}/$AGENT_PURPOSE/g" \
      -e "s/{{DEPARTMENT}}/$DEPARTMENT/g" \
      -e "s/{{DATE}}/$(date +%Y-%m-%d)/g" \
      .specify/templates/agent-file-template.md > "$AGENT_FILE"
}

generate_agent_file

# Create memory structure
mkdir -p ".docs/agents/$DEPARTMENT/$AGENT_NAME/context"
mkdir -p ".docs/agents/$DEPARTMENT/$AGENT_NAME/knowledge"

# Add to AGENTS.md registry
echo "- **$AGENT_NAME**: $AGENT_PURPOSE" >> AGENTS.md

# Output success
echo "{\"status\":\"success\",\"agent_file\":\"$AGENT_FILE\",\"department\":\"$DEPARTMENT\",\"memory\":\".docs/agents/$DEPARTMENT/$AGENT_NAME/\"}"
```

**Constitutional Compliance**:
```markdown
AGENT FILE INCLUDES:
✅ Constitutional Principles Application section
✅ Git operation restrictions (Principle VI)
✅ Agent delegation requirements (Principle X)
✅ Tool usage policies (restricted tools)
✅ Audit requirements (logging)
✅ Design system compliance (if applicable)
✅ Model selection guidance (Principle XIV)
```

**Rationale**:
- **Consistency**: All agents follow same structure
- **Quality**: Constitutional compliance baked in
- **Efficiency**: < 1 minute to create agent
- **Scalability**: Easy to add agents as needs grow

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/create-agent.sh` (automation script)
- `/workspaces/ioun-ai/.specify/templates/agent-file-template.md` (template)
- `/workspaces/ioun-ai/.claude/agents/architecture/subagent-architect.md` (orchestrator)
- `/workspaces/ioun-ai/CLAUDE.md` (Lines 358-363: /create-agent documentation)

**Dependencies**:
- ENH-AGT-006 (Subagent Architect)
- ENH-AGT-003 (Agent Context File Standardization)
- ENH-CON-004 (Agent Delegation Protocol)

**Benefits**:
- Rapid agent creation
- Guaranteed constitutional compliance
- Consistent agent structure
- Reduced human error

**Migration Path**:
1. Create create-agent.sh script
2. Create agent-file-template.md
3. Create subagent-architect agent
4. Add /create-agent documentation to CLAUDE.md
5. Test agent creation workflow
6. Create initial 13 agents using command

**Rollback**: Remove /create-agent command, use manual agent creation

---

#### ENH-WFL-005: JSON Argument Support for Scripts

**ID**: ENH-WFL-005  
**Priority**: MEDIUM  
**Breaking**: No (API enhancement)

**Description**:
Standardizes script interfaces to accept JSON arguments via stdin, enabling programmatic invocation from agents.

**Original Script Interface**:
```bash
# Old style: positional arguments
./create-new-feature.sh 010 "Audio Recording"
./setup-plan.sh 010
./check-task-prerequisites.sh 010
```

**Enhanced Script Interface**:
```bash
# New style: JSON via stdin
echo '{"feature_number": 010, "feature_name": "Audio Recording", "create_branch": true, "branch_name": "010-audio-recording"}' | ./create-new-feature.sh --json

echo '{"feature_number": 010}' | ./setup-plan.sh --json

echo '{"feature_number": 010}' | ./check-task-prerequisites.sh --json
```

**JSON Schema Examples**:

**create-new-feature.sh**:
```json
{
  "feature_number": 10,
  "feature_name": "Audio Recording",
  "create_branch": false,  // Optional, default false
  "branch_name": ""        // Required if create_branch = true
}
```

**setup-plan.sh**:
```json
{
  "feature_number": 10
}
```

**create-agent.sh**:
```json
{
  "name": "backend-engineer",
  "purpose": "API and database specialist",
  "department": "engineering"  // Optional, auto-detected
}
```

**Script Pattern**:
```bash
#!/bin/bash
# Standard JSON argument parsing

set -euo pipefail

# Check for --json flag
if [ "${1:-}" = "--json" ]; then
  # Parse JSON from stdin
  ARGS=$(cat)
  FEATURE_NUMBER=$(echo "$ARGS" | jq -r '.feature_number')
  FEATURE_NAME=$(echo "$ARGS" | jq -r '.feature_name // empty')
  CREATE_BRANCH=$(echo "$ARGS" | jq -r '.create_branch // false')
  BRANCH_NAME=$(echo "$ARGS" | jq -r '.branch_name // empty')
else
  # Legacy positional arguments (backward compatibility)
  FEATURE_NUMBER=$1
  FEATURE_NAME=$2
  CREATE_BRANCH=false
  BRANCH_NAME=""
fi

# Validate required arguments
if [ -z "$FEATURE_NUMBER" ]; then
  echo "ERROR: feature_number required"
  exit 1
fi

# Execute script logic
# ...

# Output JSON result
echo "{\"status\":\"success\",\"feature_number\":$FEATURE_NUMBER,\"spec_file\":\"specs/$FEATURE_DIR/spec.md\"}"
```

**Rationale**:
- **Programmatic**: Agents can invoke scripts with structured data
- **Extensible**: Easy to add new arguments without breaking API
- **Validation**: JSON schema enables input validation
- **Structured Output**: JSON results easy to parse

**Implementation**:

**Files**:
- All scripts in `.specify/scripts/bash/` updated with JSON support:
  - `create-new-feature.sh`
  - `setup-plan.sh`
  - `check-task-prerequisites.sh`
  - `create-agent.sh`
  - `detect-phase-domain.sh`
  - `constitutional-check.sh`

**Dependencies**:
- `jq` (JSON parsing utility, must be installed)

**Benefits**:
- Agent-friendly script invocation
- Structured input/output
- Extensible API
- Backward compatibility (supports positional args)

**Migration Path**:
1. Add `--json` flag support to all scripts
2. Implement JSON parsing with `jq`
3. Add JSON schema documentation
4. Update agent context files with JSON invocation examples
5. Test JSON invocation from agents
6. Maintain backward compatibility with positional args

**Rollback**: Remove `--json` flag, use positional arguments only

---

#### ENH-WFL-006: Constitutional Check Script

**ID**: ENH-WFL-006  
**Priority**: MEDIUM  
**Breaking**: No (validation tool)

**Description**:
Introduces constitutional-check.sh script for automated validation of constitutional compliance before operations.

**Script Purpose**:
```markdown
VALIDATES:
- Agent delegation requirements (Principle X)
- Git operation approval (Principle VI)
- Design system compliance (Principle XII)
- Test-first workflow (Principle II)
- Library-first architecture (Principle I)

USAGE:
constitutional-check.sh <task-type> <task-content>

EXAMPLE:
constitutional-check.sh "testing" "Create test suite for campaign management"
→ OUTPUT: "DELEGATE to testing-specialist (Principle X)"

constitutional-check.sh "git" "create branch 010-feature"
→ OUTPUT: "REQUIRES USER APPROVAL (Principle VI)"
```

**Validation Logic**:
```bash
#!/bin/bash
# Constitutional compliance validation

set -euo pipefail

TASK_TYPE=$1
TASK_CONTENT=$2

# Principle X: Agent Delegation
check_delegation() {
  local agent=$(detect_phase_domain.sh "$TASK_CONTENT")
  
  if [ "$agent" != "general-purpose" ]; then
    echo "DELEGATE to $agent (Constitutional Principle X)"
    return 1  # Requires delegation
  fi
  
  return 0  # OK for direct execution
}

# Principle VI: Git Operation Approval
check_git_approval() {
  if [[ "$TASK_CONTENT" =~ (branch|commit|push|merge|rebase|reset) ]]; then
    echo "REQUIRES USER APPROVAL (Constitutional Principle VI)"
    return 1  # Requires approval
  fi
  
  return 0  # Not a Git operation
}

# Principle XII: Design System Compliance
check_design_system() {
  if [[ "$TASK_CONTENT" =~ (UI|component|style|theme) ]]; then
    echo "CHECK: Must use theme system, no hardcoded values (Principle XII)"
    return 2  # Warning, not error
  fi
  
  return 0  # Not UI work
}

# Principle II: Test-First
check_test_first() {
  if [[ "$TASK_TYPE" = "implementation" ]] && [[ ! "$TASK_CONTENT" =~ test ]]; then
    echo "WARNING: Test-first required - write tests before implementation (Principle II)"
    return 2  # Warning
  fi
  
  return 0  # Tests mentioned or not implementation
}

# Run all checks
EXIT_CODE=0

check_delegation || EXIT_CODE=$?
check_git_approval || EXIT_CODE=$?
check_design_system || EXIT_CODE=$?
check_test_first || EXIT_CODE=$?

# Output result
case $EXIT_CODE in
  0) echo "✓ Constitutional compliance check passed" ;;
  1) echo "✗ Constitutional violation detected - action blocked" ;;
  2) echo "⚠ Constitutional warning - proceed with caution" ;;
esac

exit $EXIT_CODE
```

**Integration Points**:
```markdown
CALLED BY:
- Work Session Initiation Protocol (Step 2: Analyze Task Domain)
- Workflow scripts before execution (pre-flight check)
- Agents before direct execution

OUTPUTS TO:
- stdout (validation messages)
- exit code (0=pass, 1=block, 2=warn)

BLOCKS:
- Unauthorized Git operations
- Direct execution of specialized work
- Constitutional violations
```

**Rationale**:
- **Prevention**: Catches violations before they happen
- **Automation**: Reduces manual compliance checks
- **Education**: Explains which principle violated
- **Enforcement**: Blocks prohibited operations

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/constitutional-check.sh` (validation script)
- Integrated into: create-new-feature.sh, setup-plan.sh, check-task-prerequisites.sh

**Dependencies**:
- ENH-CON-001 (Constitutional Framework)
- ENH-WFL-007 (detect-phase-domain.sh)

**Benefits**:
- Automated constitutional compliance
- Prevention of violations
- Clear violation messages
- Reduced manual checks

**Migration Path**:
1. Create constitutional-check.sh script
2. Implement validation logic for each principle
3. Integrate into workflow scripts
4. Update Work Session Initiation Protocol to call script
5. Test with sample tasks
6. Refine validation logic based on false positives

**Rollback**: Remove script, use manual compliance checks

---

#### ENH-WFL-007: Domain Detection Script

**ID**: ENH-WFL-007  
**Priority**: HIGH  
**Breaking**: No (automation tool)

**Description**:
Introduces detect-phase-domain.sh script for automated detection of task domain and appropriate agent routing.

**Script Purpose**:
```markdown
DETECTS:
- Task domain based on 40+ keyword triggers
- Multiple domains requiring orchestration
- General-purpose tasks (no delegation needed)

RETURNS:
- Single agent name (e.g., "frontend-specialist")
- task-orchestrator for multi-domain
- "general-purpose" for no delegation

USAGE:
detect-phase-domain.sh "<task-content>"

EXAMPLE:
detect-phase-domain.sh "Create test suite for campaign management"
→ OUTPUT: "testing-specialist"

detect-phase-domain.sh "Build user authentication with JWT and login UI"
→ OUTPUT: "task-orchestrator: backend-architect frontend-specialist security-specialist"
```

**Detection Logic** (excerpted, see ENH-AGT-009 for full 40+ triggers):
```bash
#!/bin/bash
# Automated domain detection with 40+ triggers

set -euo pipefail

detect_domain() {
  local content="$1"
  local domains=()
  
  # Testing triggers (8)
  if echo "$content" | grep -qiE '(test|Test|testing|jest|spec|__tests__|contract|integration)'; then
    domains+=("testing-specialist")
  fi
  
  # Frontend triggers (10)
  if echo "$content" | grep -qiE '(component|UI|screen|form|validation|tsx|jsx|React|state|navigation)'; then
    domains+=("frontend-specialist")
  fi
  
  # Database triggers (8)
  if echo "$content" | grep -qiE '(schema|migration|table|query|sql|index|constraint|RLS)'; then
    domains+=("database-specialist")
  fi
  
  # Security triggers (6)
  if echo "$content" | grep -qiE '(auth|authentication|encryption|token|session|secure)'; then
    domains+=("security-specialist")
  fi
  
  # Backend triggers (6)
  if echo "$content" | grep -qiE '(API|endpoint|service|route|server|middleware)'; then
    domains+=("backend-architect")
  fi
  
  # ... (additional domains)
  
  # Output result
  if [ ${#domains[@]} -eq 0 ]; then
    echo "general-purpose"
  elif [ ${#domains[@]} -eq 1 ]; then
    echo "${domains[0]}"
  else
    # Multiple domains → orchestration needed
    echo "task-orchestrator: ${domains[*]}"
  fi
}

# Main
detect_domain "$1"
```

**Phase-Based Detection** (alternative mode):
```bash
# detect-phase-domain.sh PHASE_NUM tasks-file.md
# Analyzes tasks in specific phase to determine domain

detect_phase() {
  local phase_num=$1
  local tasks_file=$2
  
  # Extract tasks for phase
  local phase_tasks=$(grep -A 50 "### Phase $phase_num" "$tasks_file")
  
  # Detect domain from phase tasks
  detect_domain "$phase_tasks"
}
```

**Integration Points**:
```markdown
CALLED BY:
- Work Session Initiation Protocol (Step 2: Analyze Task Domain)
- constitutional-check.sh (delegation validation)
- setup-plan.sh (multi-agent detection)

USED FOR:
- Automated agent routing
- Multi-domain detection
- Delegation enforcement
```

**Rationale**:
- **Automation**: Eliminates manual agent selection
- **Accuracy**: 40+ triggers ensure correct routing
- **Orchestration**: Detects multi-domain scenarios
- **Consistency**: Standardized detection logic

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/scripts/bash/detect-phase-domain.sh` (detection script)
- Integrated into: constitutional-check.sh, setup-plan.sh, Work Session Initiation Protocol

**Dependencies**:
- ENH-AGT-009 (Agent Collaboration Triggers)
- ENH-AGT-002 (Agent Registry)

**Benefits**:
- Automated agent routing
- High detection accuracy
- Multi-domain orchestration
- Reduced manual coordination

**Migration Path**:
1. Create detect-phase-domain.sh script
2. Implement 40+ trigger detection logic
3. Add multi-domain detection
4. Integrate into workflow scripts
5. Test with sample tasks
6. Refine triggers based on accuracy

**Rollback**: Remove script, use manual agent selection

---

#### ENH-WFL-008: Workflow Script Idempotency

**ID**: ENH-WFL-008  
**Priority**: MEDIUM  
**Breaking**: No (safety enhancement)

**Description**:
Ensures all workflow scripts can be safely re-executed, checking preconditions and avoiding overwrites (Constitutional Principle IV).

**Idempotency Patterns**:

**Feature Creation** (create-new-feature.sh):
```bash
# Check if feature already exists
if [ -d "specs/$FEATURE_DIR" ]; then
  echo "Feature directory already exists: specs/$FEATURE_DIR"
  echo "Use --force to overwrite"
  exit 1
fi

# Check if branch already exists
if git rev-parse --verify "$BRANCH_NAME" >/dev/null 2>&1; then
  echo "Branch already exists: $BRANCH_NAME"
  echo "Use existing branch or choose different name"
  exit 1
fi
```

**Planning** (setup-plan.sh):
```bash
# Create files only if missing
[ ! -f "$SPEC_DIR/research.md" ] && generate_research
[ ! -f "$SPEC_DIR/data-model.md" ] && generate_data_model
[ ! -d "$SPEC_DIR/contracts" ] && generate_contracts
[ ! -f "$SPEC_DIR/quickstart.md" ] && generate_quickstart

echo "✓ Planning artifacts complete (generated missing files)"
```

**Agent Creation** (create-agent.sh):
```bash
# Check if agent already exists
if [ -f "$AGENT_FILE" ]; then
  echo "Agent already exists: $AGENT_FILE"
  echo "Use --force to overwrite or choose different name"
  exit 1
fi

# Check if agent in registry
if grep -q "^- \*\*$AGENT_NAME\*\*:" AGENTS.md; then
  echo "Agent already registered: $AGENT_NAME"
  echo "Remove from AGENTS.md before recreating"
  exit 1
fi
```

**Rationale**:
- **Safety**: Re-running scripts doesn't cause data loss
- **Recovery**: Failed operations can be retried
- **Automation**: CI/CD-friendly execution
- **Constitutional**: Enforces Principle IV

**Implementation**:

**Files**:
- All scripts in `.specify/scripts/bash/` implement idempotency checks

**Pattern**:
```bash
# Standard idempotency check pattern
check_preconditions() {
  # Check if output already exists
  if [ -f "$OUTPUT_FILE" ]; then
    if [ "${FORCE:-false}" = "true" ]; then
      rm -f "$OUTPUT_FILE"  # Force overwrite
    else
      echo "Output already exists: $OUTPUT_FILE"
      echo "Use --force to overwrite"
      exit 1
    fi
  fi
}

check_preconditions
# Proceed with operation
```

**Dependencies**:
- ENH-CON-010 (Idempotent Operations Principle)

**Benefits**:
- Safe script re-execution
- Graceful recovery from failures
- CI/CD compatibility
- Reduced error risk

**Migration Path**:
1. Audit all scripts for idempotency
2. Add precondition checks to non-idempotent operations
3. Implement --force flag for intentional overwrites
4. Test script re-execution scenarios
5. Document idempotency guarantees

**Rollback**: Remove precondition checks, accept potential overwrites

---

(Continued with Categories 4-7, Implementation Recommendations, and Appendices... Would you like me to continue with the remaining sections?)

### Category 4: Documentation & Policies

#### ENH-DOC-001: Comprehensive Policy Framework (24+ Policies)

**ID**: ENH-DOC-001  
**Priority**: HIGH  
**Breaking**: No (documentation addition)

**Description**:
Establishes structured policy framework with 24+ policy, workflow, and reference documents covering all aspects of development process.

**Policy Categories**:

**1. Development Policies** (6 files):
```markdown
.docs/policies/
├── file-creation-policy.md          # When/how to create files
├── eas-build-policy.md              # Expo Application Services builds
├── browser-testing-policy.md        # Browser testing with Playwright
├── ai-instruction-files-policy.md   # CLAUDE.md ↔ AGENTS.md sync
├── ai-model-selection-policy.md     # Model selection (Sonnet vs Opus)
└── test-strategy-policy.md          # Testing approach (E2E first, contracts post-MVP)
```

**2. Workflow Guides** (8 files):
```markdown
.docs/workflows/
├── feature-development-workflow.md        # End-to-end feature development
├── centralized-todo-workflow.md          # TODO tracking system
├── constitutional-compliance-workflow.md  # Compliance checking
├── agent-delegation-workflow.md          # Agent selection and routing
├── git-operation-workflow.md             # Git operations with approval
├── design-system-workflow.md             # Design system integration
├── testing-workflow.md                   # Testing strategy execution
└── multi-agent-orchestration-workflow.md # Complex feature coordination
```

**3. Quick References** (10 files):
```markdown
.docs/quick-reference/
├── sdd-agent-delegation.md           # Agent → domain mapping
├── constitutional-principles.md      # 14 principles summary
├── browser-testing.md                # Playwright quick start
├── expo-url-retrieval.md             # Expo Go URL retrieval
├── git-operation-approval.md         # Git approval protocol
├── design-system-quick-ref.md        # Design system patterns
├── workflow-commands.md              # /specify, /plan, /tasks, /create-agent
├── agent-collaboration-triggers.md   # 40+ trigger quick ref
├── testing-strategy.md               # Testing priorities
└── task-analysis-checklist.md        # Work session initiation
```

**Key Policies** (highlights):

**File Creation Policy**:
```markdown
PURPOSE: Prevent duplicate file creation and ensure correct file placement

PROTOCOL:
1. SEARCH FIRST: Use mcp__claude-context to search for existing files
2. CHECK TASKS: Consult tasks.md for exact file paths
3. DELEGATE: Use correct agent for file type
4. VERIFY: Confirm file doesn't exist before creating

ENFORCEMENT:
- Constitutional Principle (implied): No duplicate functionality
- Documented in: .docs/policies/file-creation-policy.md
```

**EAS Build Policy**:
```markdown
PURPOSE: Prevent duplicate builds and unnecessary costs

RULES:
1. DEFAULT: Use "preview" profile for standard cloud deployments
2. DEVELOPMENT: Only when user EXPLICITLY requests "development build"
3. PRODUCTION: Only for store submissions when explicitly requested
4. STOP after submission - Wait for user confirmation before second build
5. NO duplicate builds - Check status before resubmitting if timeout

ENFORCEMENT:
- Documented in: .docs/policies/eas-build-policy.md
- Updated: 2025-09-26 (Effective date)
```

**AI Instruction Files Policy**:
```markdown
PURPOSE: Keep CLAUDE.md and AGENTS.md synchronized

SYNC REQUIREMENTS:
- Universal project requirements MUST be in both files
- Claude-specific guidance ONLY in CLAUDE.md
- Non-Claude AI guidance ONLY in AGENTS.md
- When updating universal sections, update BOTH files
- Document sync in commit message

FILES:
- CLAUDE.md: Claude Code / Claude CLI exclusive
- AGENTS.md: All non-Claude AI assistants

ENFORCEMENT:
- Documented in: .docs/policies/ai-instruction-files-policy.md
- Note in both files: "SYNCHRONIZATION NOTE: ..."
```

**Test Strategy Policy** (Updated 2025-11-04):
```markdown
PURPOSE: MVP-focused testing approach

WHAT NOT TO CREATE:
❌ Contract tests (until post-MVP)
❌ Manual test tasks in specs
❌ TDD approach for MVP features

WHAT TO CREATE:
✅ E2E tests for critical user flows (when required)
✅ Implementation code first, tests later (if needed)
✅ User validation via actual usage

RATIONALE:
- Speed over coverage (MVP needs features, not test suites)
- User feedback first (build, ship, learn)
- Test what exists (don't test systems not built yet)

ENFORCEMENT:
- Documented in: .docs/reviews/2025-10-07-test-strategy-review.md
- Removed 14 contract test files (2025-11-04)
- Removed 6 manual test tasks (2025-11-04)
```

**Rationale**:
- **Consistency**: Standardized processes across team
- **Onboarding**: New developers have clear guidance
- **Compliance**: Documented requirements for audit
- **Efficiency**: No repeated policy discussions

**Implementation**:

**Files**:
- 24+ policy/workflow/reference documents in `.docs/`
- Cross-referenced in constitution, CLAUDE.md, AGENTS.md

**Dependencies**:
- ENH-CON-009 (Documentation Synchronization)

**Benefits**:
- Clear guidance for common scenarios
- Reduced decision fatigue
- Consistent application of practices
- Easy policy updates

**Migration Path** (for backport):
1. Extract project-specific policies (EAS builds, Expo, neumorphic design)
2. Identify universal policies (file creation, Git operations, testing)
3. Create policy template structure (.docs/policies/, .docs/workflows/, .docs/quick-reference/)
4. Port universal policies to original framework
5. Encourage framework adopters to add project-specific policies

**Rollback**: Remove policy documents, rely on ad-hoc decisions

---

#### ENH-DOC-002: Constitution Update Checklist

**ID**: ENH-DOC-002  
**Priority**: HIGH  
**Breaking**: No (governance process)

**Description**:
Provides structured checklist for constitutional amendments ensuring all dependent documents are updated.

**Checklist Structure**:
```markdown
# Constitution Update Checklist

When updating constitution.md, complete ALL of the following:

## Instruction Files
□ Update CLAUDE.md with corresponding changes
□ Update AGENTS.md with corresponding changes
□ Verify CLAUDE.md ↔ AGENTS.md sync per ai-instruction-files-policy.md

## Agent Context Files
□ Update affected specialized agents (.claude/agents/**/*.md)
□ Update task-orchestrator if delegation changes
□ Update subagent-architect if agent creation changes
□ Update agent-file-template.md if agent structure changes

## Workflow Scripts
□ Update bash scripts with new requirements
□ Update constitutional-check.sh validation logic
□ Test all slash commands (/specify, /plan, /tasks, /create-agent)
□ Verify idempotency maintained

## Policy Documents
□ Update affected policies (.docs/policies/*.md)
□ Update workflow guides (.docs/workflows/*.md)
□ Update quick references (.docs/quick-reference/*.md)
□ Add/update policy if new requirement introduced

## Templates
□ Update spec-template.md if requirements change
□ Update plan-template.md if workflow changes
□ Update tasks-template.md if task format changes
□ Update agent-file-template.md if agent structure changes

## Testing
□ Test workflows with updated requirements
□ Verify enforcement mechanisms work correctly
□ Check for unintended consequences
□ Validate no broken cross-references

## Documentation
□ Document breaking changes with migration paths
□ Update version number in constitution.md
□ Add amendment to version history (Appendix)
□ Update last modified date

## Approval
□ Review with project leads
□ Gather stakeholder feedback
□ Document approval decision
```

**Usage Example**:
```markdown
SCENARIO: Adding new Constitutional Principle XV (API Versioning)

CHECKLIST EXECUTION:
1. Update constitution.md with Principle XV
2. Update CLAUDE.md "Constitutional Principles" section
3. Update AGENTS.md "Constitutional Principles" section
4. Update backend-architect.md with API versioning requirements
5. Update api-design-policy.md with versioning rules
6. Update spec-template.md to include API version field
7. Update constitutional-check.sh to validate API versioning
8. Test /specify and /plan commands with new requirement
9. Document as breaking change if affects existing APIs
10. Increment version: v1.5.0 → v1.6.0
11. Add amendment to version history
12. Seek approval from project lead
```

**Rationale**:
- **Completeness**: Ensures no dependent docs missed
- **Consistency**: All docs stay in sync
- **Quality**: Prevents broken cross-references
- **Auditability**: Clear change propagation

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/memory/constitution_update_checklist.md`
- Referenced in constitution.md Amendment Process section

**Dependencies**:
- ENH-CON-012 (Amendment Process Formalization)
- ENH-CON-009 (Documentation Synchronization)

**Benefits**:
- No documentation drift
- Complete change propagation
- Reduced update errors
- Clear amendment process

**Migration Path**:
1. Create constitution_update_checklist.md
2. Document all dependent document types
3. Add to Amendment Process in constitution.md
4. Test with sample amendment
5. Refine checklist based on real amendments

**Rollback**: Remove checklist, use ad-hoc update process

---

#### ENH-DOC-003: AI Instruction Files (CLAUDE.md + AGENTS.md)

**ID**: ENH-DOC-003  
**Priority**: CRITICAL  
**Breaking**: No (documentation structure)

**Description**:
Establishes dual instruction file system: CLAUDE.md for Claude-specific guidance, AGENTS.md for universal AI guidance, with synchronization protocol.

**File Structure**:

**CLAUDE.md** (4,200+ lines):
```markdown
# CLAUDE.md

## WHO SHOULD USE THIS FILE
- Claude Code (claude.ai/code)
- Claude CLI
- Anthropic's official Claude coding interfaces

## CRITICAL: Read Constitution First
[Constitutional enforcement protocol]

## HARD STOP: Specialized Agent Delegation
[Agent delegation requirements with triggers]

## MANDATORY TASK ANALYSIS CHECKLIST
[4-step Work Session Initiation Protocol]

## Browser and E2E Testing Policy (MANDATORY)
[Playwright policy, Browser MCP fallback]

## EAS Build Policy (MANDATORY)
[Expo build guidelines, profile selection]

## Expo URL Retrieval (MANDATORY)
[Programmatic URL retrieval via ngrok API]

## AI Model Selection Policy (MANDATORY)
[Sonnet 4.5 default, Opus 4.1 escalation]

## Project Overview
[Ioun Mobile PRD summary, tech stack]

## Session Management
[Dev logs, file creation policy, centralized TODOs]

## Dark Neumorphic Design System v2.4 Patterns (UPDATED)
[Theme system, shadows, gradients, compatible rendering mode]

## Implemented Feature Patterns
[Reference implementations, proven patterns]

## Commands
[/specify, /plan, /tasks, /create-agent documentation]

## Key Architecture
[Directory structure, workflow scripts, principles]

## Testing Policy (Updated 2025-11-04)
[MVP-focused approach, no contract tests until post-MVP]

## Available Agents
[Agent directory, trigger matrix reference]
```

**AGENTS.md** (3,500+ lines):
```markdown
# AGENTS.md

## WHO SHOULD USE THIS FILE
- Cursor
- Windsurf
- GitHub Copilot
- Cody
- Continue
- All non-Claude AI coding assistants

## CRITICAL: Read Constitution First
[Constitutional enforcement protocol - SYNCED with CLAUDE.md]

## HARD STOP: Specialized Agent Delegation
[Agent delegation requirements - SYNCED with CLAUDE.md]

## MANDATORY TASK ANALYSIS CHECKLIST
[4-step protocol - SYNCED with CLAUDE.md]

[... Universal sections synced with CLAUDE.md ...]

## AI Assistant Compatibility
[Non-Claude specific guidance, adaptation instructions]

## Agent Invocation Patterns
[How non-Claude assistants should delegate to agents]
```

**Synchronization Protocol** (from ai-instruction-files-policy.md):
```markdown
UNIVERSAL CONTENT (must be in BOTH files):
- Constitutional enforcement protocol
- Agent delegation requirements
- Work Session Initiation Protocol
- Project overview and tech stack
- Session management (dev logs, file creation)
- Testing policy
- Available agents directory

CLAUDE-SPECIFIC CONTENT (CLAUDE.md only):
- Tool usage patterns (Task tool invocation)
- Claude-specific command syntax
- Claude Code UI configuration
- MCP server integration details

NON-CLAUDE CONTENT (AGENTS.md only):
- Compatibility notes for other AI assistants
- Alternative invocation patterns
- Adaptation instructions

SYNCHRONIZATION REQUIREMENTS:
- When updating universal sections, update BOTH files
- Document sync in commit message
- Cross-reference sync in file headers
- Verify sync with ai-instruction-files-policy.md

SYNC NOTE (in both files):
"SYNCHRONIZATION NOTE: This file is maintained in tandem with AGENTS.md [or CLAUDE.md]. When updating universal project requirements, both files MUST be updated. See .docs/policies/ai-instruction-files-policy.md for synchronization requirements."
```

**Rationale**:
- **Specialization**: Claude-specific guidance optimized for Claude
- **Universality**: Non-Claude assistants have clear guidance
- **Consistency**: Universal requirements in both files
- **Flexibility**: Can optimize for each AI assistant type

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/CLAUDE.md` (4,200+ lines, Claude-specific)
- `/workspaces/ioun-ai/AGENTS.md` (3,500+ lines, universal)
- `/workspaces/ioun-ai/.docs/policies/ai-instruction-files-policy.md` (sync protocol)

**Dependencies**:
- ENH-CON-009 (Documentation Synchronization)

**Benefits**:
- Optimized guidance for each AI assistant
- Consistent universal requirements
- Clear synchronization protocol
- Future-proof for new AI assistants

**Migration Path** (for backport):
1. Decide if dual file system needed (depends on AI assistant usage)
2. If yes: Create AGENTS.md with universal content
3. Keep CLAUDE.md with Claude-specific enhancements
4. Create ai-instruction-files-policy.md with sync protocol
5. Add sync notes to both files
6. If no: Single instruction file with AI-agnostic guidance

**Rollback**: Consolidate to single instruction file

---

#### ENH-DOC-004: Dev Log System

**ID**: ENH-DOC-004  
**Priority**: MEDIUM  
**Breaking**: No (documentation practice)

**Description**:
Establishes mandatory development log system for capturing work session outcomes, decisions, and handoff notes.

**Dev Log Structure**:
```markdown
# Development Log: {Feature/Topic}

**Date**: YYYY-MM-DD  
**Agent**: {Primary agent(s) involved}  
**Session Duration**: {hours}  
**Status**: {In Progress / Paused / Complete}

---

## Session Summary

{1-2 paragraph overview of work completed}

## Work Completed

### Feature Implementation
- {Task 1 completed}
- {Task 2 completed}
- {Task 3 completed}

### Decisions Made
1. **Decision**: {What was decided}
   - **Rationale**: {Why}
   - **Alternatives Considered**: {Options rejected}
   - **Impact**: {Who/what affected}

2. **Decision**: {Next decision}
   - ...

### Problems Encountered
- **Problem**: {Issue description}
  - **Solution**: {How resolved}
  - **Future Prevention**: {How to avoid}

## Technical Details

### Files Modified
```
{List of files created/modified with brief description}
```

### Code Patterns Established
- {Pattern 1}: {Description and rationale}
- {Pattern 2}: {Description and rationale}

### Testing Status
- {Test type}: {Status and coverage}

## Next Steps

### Immediate Priorities
1. {Next task}
2. {Next task}

### Blockers
- {Blocker 1}: {Description and mitigation}

### Handoff Notes
{Context for next developer/agent to continue work}

## Agent Context Updates

### Patterns to Document
- {Pattern to add to agent knowledge base}

### Lessons Learned
- {Lesson for agent improvement}

---

**Related Documents**:
- Spec: {link}
- Plan: {link}
- Tasks: {link}
```

**Example** (real dev log):
```markdown
# Development Log: Spec 010 Audio Recording Complete

**Date**: 2025-11-05  
**Agent**: Claude Code (Sonnet 4.5)  
**Session Duration**: 6 hours  
**Status**: Complete

---

## Session Summary

Completed audio recording feature (#010) with all 35 tasks finished. Removed contract test tasks per updated testing strategy (E2E first, contracts post-MVP). Updated constitutional section on testing policy to reflect MVP-focused approach.

## Work Completed

### Feature Implementation
- Implemented RecordingScreen with controls (record, pause, stop, delete)
- Added audio recording hook (useAudioRecording) with Expo AV
- Integrated with campaign context
- Added navigation flow

### Decisions Made
1. **Decision**: Remove contract test tasks from Spec 010
   - **Rationale**: Testing strategy updated (2025-11-04) - no contract tests until post-MVP
   - **Alternatives Considered**: Keep tests but mark "future" - rejected, adds confusion
   - **Impact**: 6 tasks removed, testing tasks now focus on E2E only

2. **Decision**: Update constitution with testing policy
   - **Rationale**: Formalize MVP testing approach as constitutional requirement
   - **Impact**: All future features follow E2E-first pattern

### Problems Encountered
- **Problem**: Task list included contract tests contradicting new policy
  - **Solution**: Removed T030-T035 (contract tests) and T040 (manual tests)
  - **Future Prevention**: Template updated, specs generated after 2025-11-04 won't include contract tests

## Technical Details

### Files Modified
```
mobile/src/screens/RecordingScreen.tsx (created)
mobile/src/hooks/useAudioRecording.ts (created)
mobile/src/navigation/AuthNavigator.tsx (updated - added Recording route)
.specify/memory/constitution.md (updated - testing policy)
specs/010-audio-recording/tasks.md (updated - removed contract tests)
```

### Code Patterns Established
- Audio recording hook pattern: State management + Expo AV integration
- Recording screen UI: Dark neumorphic controls with theme compliance

### Testing Status
- E2E: 1 test (audio-recording.spec.ts) - covers recording flow
- Contract: None (per updated policy)

## Next Steps

### Immediate Priorities
1. User testing with actual audio recording on device
2. Handle edge cases (permissions denied, storage full)

### Blockers
None

### Handoff Notes
Audio recording feature complete per Spec 010. All code follows design system v2.4 (theme-based, no hardcoded values). Ready for user testing.

## Agent Context Updates

### Patterns to Document
- Audio recording hook pattern (for audio-specialist agent if created)

### Lessons Learned
- Testing strategy must be documented in constitution to prevent spec inconsistencies

---

**Related Documents**:
- Spec: specs/010-audio-recording/spec.md
- Tasks: specs/010-audio-recording/tasks.md
- Testing Strategy: .docs/reviews/2025-10-07-test-strategy-review.md
```

**Rationale**:
- **Continuity**: Next session has full context
- **Decisions**: Rationale captured for future reference
- **Patterns**: Reusable solutions documented
- **Handoffs**: Smooth transition between developers/agents

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.docs/dev-logs/YYYY-MM-DD-{feature}.md` (one per significant session)
- Referenced in CLAUDE.md Session Management section

**Enforcement**:
- MANDATORY in CLAUDE.md: "Create a dev log at the end of each significant work session"
- Template provided in documentation

**Dependencies**:
- None (documentation best practice)

**Benefits**:
- Full session history
- Decision rationale preserved
- Pattern documentation
- Easy handoffs

**Migration Path**:
1. Create dev log template
2. Document in Session Management section
3. Add to session completion checklist
4. Encourage consistent use

**Rollback**: Remove dev log requirement, rely on Git history

---

#### ENH-DOC-005: Centralized TODO System

**ID**: ENH-DOC-005  
**Priority**: MEDIUM  
**Breaking**: No (organizational enhancement)

**Description**:
Establishes centralized TODO tracking system accessible via /todos command for managing uncompleted work across paused/blocked features.

**System Structure**:

**Two-Tier System**:
```markdown
TIER 1: /todos Command
- Quick access to top 10 priority tasks
- Displayed on command execution
- Sorted by priority and dependencies
- Ideal for "what should I work on next?"

TIER 2: CENTRALIZED_TODOS.md
- Complete archive of all pending work
- Organized by category (features, bugs, tech debt, code TODOs)
- Full context for each TODO
- Searchable reference
```

**File Structure** (CENTRALIZED_TODOS.md):
```markdown
# Centralized TODO Tracking

**Last Updated**: YYYY-MM-DD  
**Total Active TODOs**: {count}  
**High Priority**: {count}  
**Blocked**: {count}

---

## Priority TODOs (Top 10)

### 1. [HIGH] Feature Name - Task Description
**Source**: specs/###-feature-name/tasks.md (T###)  
**Reason**: Why this TODO exists  
**Priority**: HIGH  
**Estimated Effort**: {hours/days}  
**Depends On**: {Dependencies if any}  
**Status**: Active / Blocked

### 2. [MEDIUM] Bug Fix - Issue Description
**Source**: GitHub Issue #123  
**Reason**: User-reported bug  
**Priority**: MEDIUM  
**Estimated Effort**: 2 hours  
**Depends On**: None  
**Status**: Active

[... continues for top 10 ...]

---

## All TODOs by Category

### Feature TODOs (Paused/Incomplete Specs)

#### Spec 005: Campaign Management (2 TODOs)
- **T025**: Implement campaign filtering by status
  - **Reason**: Paused due to priority shift
  - **Context**: Requires backend filter API (not yet built)
  - **Estimated Effort**: 4 hours

- **T030**: Add campaign export feature
  - **Reason**: Post-MVP enhancement
  - **Context**: Depends on export service (future work)
  - **Estimated Effort**: 8 hours

#### Spec 007: Chat Interface (1 TODO)
- **T015**: Implement message search
  - **Reason**: Blocked by database full-text search setup
  - **Context**: Requires PostgreSQL FTS configuration
  - **Estimated Effort**: 6 hours

### Bug TODOs
- **Bug #123**: Fix audio playback on iOS
  - **Reported**: 2025-11-01
  - **Priority**: HIGH
  - **Status**: Active

### Technical Debt TODOs
- **TD-001**: Refactor authentication service
  - **Reason**: Current implementation tightly coupled
  - **Priority**: MEDIUM
  - **Estimated Effort**: 2 days

### Code-Level TODOs
- **TODO in RecordingScreen.tsx:45**: Add error handling for storage full
  - **File**: mobile/src/screens/RecordingScreen.tsx
  - **Line**: 45
  - **Priority**: HIGH
```

**Workflow**:
```markdown
DURING ACTIVE DEVELOPMENT:
- Use spec-based tasks.md files for active features
- Mark tasks as completed/pending in tasks.md

AFTER FEATURE COMPLETES/PAUSES:
- Migrate uncompleted tasks to CENTRALIZED_TODOS.md
- Add context: Why incomplete? What's blocking?
- Remove from tasks.md (feature done, todos archived)

WEEKLY REVIEW:
- Check CENTRALIZED_TODOS.md for next priorities
- Update statuses (blocked → active, active → complete)
- Prune completed TODOs

STARTING NEW WORK:
- Run /todos command for top 10 priorities
- OR search CENTRALIZED_TODOS.md for specific todos
```

**Rationale**:
- **Visibility**: All pending work in one place
- **Prioritization**: Clear priority ranking
- **Context**: Full context preserved for each TODO
- **Efficiency**: No scattered TODOs across files

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.docs/todos/CENTRALIZED_TODOS.md` (complete archive)
- `/workspaces/ioun-ai/.docs/workflows/centralized-todo-workflow.md` (process)
- `/todos` command (quick access)

**/todos Command**:
```bash
# Displays top 10 TODOs from CENTRALIZED_TODOS.md
cat .docs/todos/CENTRALIZED_TODOS.md | grep -A 7 "## Priority TODOs"
```

**Dependencies**:
- None (organizational enhancement)

**Benefits**:
- Single source of truth for pending work
- Easy prioritization
- No lost TODOs
- Clear context for each item

**Migration Path**:
1. Create CENTRALIZED_TODOS.md
2. Migrate TODOs from completed/paused specs
3. Add /todos command to CLAUDE.md
4. Document workflow in centralized-todo-workflow.md
5. Establish weekly review process

**Rollback**: Remove centralized file, use per-spec tasks.md only

---

(Continuing with remaining categories and implementation recommendations...)

### Category 5: Templates & Patterns

#### ENH-TPL-001: Enhanced Spec Template

**ID**: ENH-TPL-001  
**Priority**: HIGH  
**Breaking**: No (template enhancement)

**Description**:
Expands spec-template.md from basic structure to comprehensive specification with tier gating, design system, and testing strategy.

**Original Template** (~100 lines):
```markdown
# Feature: {Name}

## Overview
{Brief description}

## Requirements
{Functional requirements}

## Technical Approach
{High-level approach}
```

**Enhanced Template** (~400 lines):
```markdown
# Feature: {Name}

**Feature Number**: {###}  
**Status**: Draft / In Planning / In Development / Complete  
**Priority**: Critical / High / Medium / Low  
**Target Tier**: Player / DM / Prestige  
**Estimated Effort**: {hours/days/weeks}

---

## Executive Summary

### Problem Statement
{What problem does this solve?}

### Proposed Solution
{High-level solution approach}

### Success Criteria
{How do we know this is successful?}

---

## User Stories

### Primary User Stories
1. As a {user type}, I want to {action}, so that {benefit}
   - **Acceptance Criteria**:
     - {Criterion 1}
     - {Criterion 2}

### Secondary User Stories
{Optional/future user stories}

---

## Functional Requirements

### Core Requirements (Must Have)
1. {Requirement 1}
   - **Details**: {Specification}
   - **Rationale**: {Why needed}

### Enhanced Requirements (Should Have)
{Nice-to-have features}

### Future Enhancements (Could Have)
{Post-MVP features}

---

## Subscription Tier Enforcement

### Tier Access Matrix
| Feature | Player (Free) | DM ($9.99/mo) | Prestige (Future) |
|---------|--------------|---------------|-------------------|
| {Feature 1} | ✅ Full | ✅ Full | ✅ Full |
| {Feature 2} | ⚠️ Limited | ✅ Full | ✅ Enhanced |
| {Feature 3} | ❌ None | ✅ Full | ✅ Enhanced |

### Enforcement Requirements
**Backend (RLS)**:
- {RLS policy 1}

**Frontend (UI)**:
- {UI restriction 1}
- {Upgrade prompt trigger}

---

## Technical Approach

### Architecture Overview
{High-level architecture}

### Data Model
{Entity summary - details in data-model.md}

### API Contracts
{Contract summary - details in contracts/}

### Design System Compliance
**Theme Requirements**:
- Use `useTheme()` for colors
- Use `useShadows()` for shadows
- Use `GRADIENTS` for gradients
- NO hardcoded values

**Component Patterns**:
- {Pattern 1}

**Compatible Rendering Mode**:
- Text/TextInput: Solid backgrounds only (no gradients)

---

## Testing Strategy

### E2E Tests (Priority)
1. {Critical user flow 1}
2. {Critical user flow 2}

### Integration Tests (Post-MVP)
{Integration scenarios}

### Unit Tests (Post-MVP)
{Unit test targets}

**Test-First Approach**: 
Write E2E tests → Get user approval → Tests fail → Implement

---

## Dependencies

### External Dependencies
- {Dependency 1}: {Version/requirement}

### Internal Dependencies
- {Feature/component dependency}

### Blockers
- {Blocker if any}

---

## Migration & Rollback

### Migration Strategy
{How to deploy without breaking existing}

### Rollback Plan
{How to revert if issues}

---

## Success Metrics

### Quantitative Metrics
- {Metric 1}: {Target}

### Qualitative Metrics
- {User satisfaction criteria}

---

## Open Questions

1. {Question 1}
   - **Options**: {A, B, C}
   - **Recommendation**: {Option + rationale}

---

## Appendix

### Related Documents
- PRD: {link}
- Design Mockups: {link}
- Research: {link to research.md}

### Revision History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0   | YYYY-MM-DD | Initial draft | {Author} |
```

**Rationale**:
- **Completeness**: All aspects of feature covered
- **Tier Enforcement**: Constitutional Principle XIII compliance
- **Design System**: Constitutional Principle XII compliance
- **Testing**: Constitutional Principle II compliance

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/templates/spec-template.md` (enhanced)
- Used by: /specify command, specification-agent

**Dependencies**:
- ENH-CON-005 (Design System Compliance)
- ENH-CON-006 (Subscription Tier Enforcement)
- ENH-CON-002 (Test-First Development)

**Benefits**:
- Comprehensive specifications
- Constitutional compliance baked in
- Consistent spec structure
- Clear success criteria

**Migration Path**:
1. Expand spec-template.md with new sections
2. Make tier enforcement section conditional (for non-SaaS projects)
3. Make design system section conditional (for non-neumorphic projects)
4. Test with sample feature spec
5. Update specification-agent to use enhanced template

**Rollback**: Revert to basic template

---

#### ENH-TPL-002: Enhanced Plan Template (9-Step Process)

**ID**: ENH-TPL-002  
**Priority**: HIGH  
**Breaking**: No (template enhancement)

**Description**:
Expands plan-template.md from basic outline to comprehensive 9-step implementation planning process.

**Original Template** (~50 lines):
```markdown
# Implementation Plan: {Feature}

## Approach
{Implementation approach}

## Tasks
{High-level tasks}
```

**Enhanced Template** (~600 lines with 9 steps):
```markdown
# Implementation Plan: {Feature}

**Feature Number**: {###}  
**Planning Date**: YYYY-MM-DD  
**Estimated Duration**: {weeks}  
**Agent(s)**: {Agent name(s)}

---

## Step 1: Architectural Review

### Current Architecture Analysis
{Review existing architecture}

### Proposed Changes
{What will change}

### Impact Assessment
{What's affected by changes}

---

## Step 2: Research & Decision Log

**See**: research.md for detailed technical research

### Key Decisions
1. **Decision**: {What was decided}
   - **Options Considered**: {A, B, C}
   - **Selected**: {Option + rationale}
   - **Trade-offs**: {Pros and cons}

---

## Step 3: Data Model Design

**See**: data-model.md for complete entity definitions

### Entities
- {Entity 1}: {Purpose}
- {Entity 2}: {Purpose}

### Relationships
{Entity relationships}

---

## Step 4: Contract Design

**See**: contracts/ directory for API specifications

### API Endpoints
- `GET /api/{resource}`: {Purpose}
- `POST /api/{resource}`: {Purpose}

### Message Contracts
{Event/message definitions}

---

## Step 5: Library Extraction Plan

**Constitutional Requirement (Principle I)**: Library-First Architecture

### Libraries to Create
1. **Library**: {name}
   - **Location**: {path}
   - **Purpose**: {What it does}
   - **Exports**: {Public API}
   - **Dependencies**: {What it depends on}

---

## Step 6: Implementation Phases

### Phase 1: Foundation ({duration})
{Tasks for phase 1}

### Phase 2: Core Features ({duration})
{Tasks for phase 2}

### Phase 3: Refinement ({duration})
{Tasks for phase 3}

---

## Step 7: Testing Strategy

### E2E Test Scenarios
**See**: quickstart.md for detailed test scenarios

1. **Scenario**: {Test scenario 1}
   - **Given**: {Preconditions}
   - **When**: {Action}
   - **Then**: {Expected result}

### Testing Phases
- **Phase 1**: E2E tests for critical flows
- **Phase 2**: Integration tests (post-MVP)
- **Phase 3**: Unit tests (post-MVP)

---

## Step 8: Deployment Strategy

### Prerequisites
- {Prerequisite 1}

### Deployment Steps
1. {Step 1}
2. {Step 2}

### Rollback Procedure
{How to revert}

---

## Step 9: Success Validation

### Validation Criteria
- {Criterion 1}: {How to verify}

### Monitoring
- {Metric 1}: {Target}

---

## Dependencies & Prerequisites

### Must Complete Before Starting
- {Dependency 1}

### Parallel Work
- {Work that can happen concurrently}

---

## Risk Assessment

### Technical Risks
- **Risk**: {Risk 1}
  - **Impact**: {High/Medium/Low}
  - **Likelihood**: {High/Medium/Low}
  - **Mitigation**: {How to mitigate}

### Schedule Risks
- {Risk and mitigation}

---

## Appendix

### Related Artifacts
- Spec: specs/{###}-{name}/spec.md
- Research: specs/{###}-{name}/research.md
- Data Model: specs/{###}-{name}/data-model.md
- Contracts: specs/{###}-{name}/contracts/
- Quickstart: specs/{###}-{name}/quickstart.md
```

**Rationale**:
- **Comprehensive**: 9-step process covers all planning aspects
- **Constitutional**: Library-first, test-first, contract-first baked in
- **Structured**: Clear sequence and dependencies
- **Cross-referenced**: Links to research, data model, contracts, quickstart

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/templates/plan-template.md` (9-step enhanced)
- Used by: /plan command, generated artifacts (research.md, data-model.md, contracts/, quickstart.md)

**Dependencies**:
- ENH-CON-001 (Constitutional Principles I, II, III)
- ENH-WFL-002 (/plan command)

**Benefits**:
- Thorough planning process
- Constitutional compliance
- Clear implementation roadmap
- Risk identification

**Migration Path**:
1. Expand plan-template.md to 9 steps
2. Create sub-templates for research.md, data-model.md, quickstart.md
3. Update setup-plan.sh to generate all artifacts
4. Test with sample feature
5. Refine based on real-world usage

**Rollback**: Revert to basic plan template

---

#### ENH-TPL-003: Enhanced Tasks Template with Dependencies

**ID**: ENH-TPL-003  
**Priority**: HIGH  
**Breaking**: No (template enhancement)

**Description**:
Expands tasks-template.md to include dependency tracking, parallel execution markers, and status management.

**Original Template**:
```markdown
# Tasks: {Feature}

## Tasks

### T001: {Task name}
{Task description}

### T002: {Task name}
{Task description}
```

**Enhanced Template**:
```markdown
# Tasks: {Feature}

**Feature Number**: {###}  
**Total Tasks**: {count}  
**Completed**: {count} ({percentage}%)  
**In Progress**: {count}  
**Pending**: {count}  
**Last Updated**: YYYY-MM-DD

---

## Task Summary

### Dependency Chain
```
T001 (Foundation)
  ├─ T002 (depends on T001)
  │   └─ T005 (depends on T002)
  ├─ T003 (depends on T001)
  └─ T004 (depends on T001)

[P] T006, T007, T008 (parallel - no dependencies)
```

### Parallel Execution Opportunities
**Phase 1**: T001 (sequential)  
**Phase 2**: T002, T003, T004 [P] (parallel after T001)  
**Phase 3**: T005 (sequential after T002)  
**Phase 4**: T006, T007, T008 [P] (parallel, no dependencies)

---

## Tasks

### T001: {Task name}
**Status**: pending / in_progress / completed / blocked  
**Type**: data-model / database / frontend / backend / testing / documentation  
**Priority**: critical / high / medium / low  
**Estimated Effort**: {hours/days}  
**Dependencies**: None  
**Parallel**: [P] Can execute in parallel with T002, T003  
**Agent**: {Specialized agent for this task}

**Description**:
{Detailed task description}

**Acceptance Criteria**:
- {Criterion 1}
- {Criterion 2}

**Implementation Notes**:
{Technical details, file paths, patterns to use}

**Testing**:
- E2E: {E2E test requirement}
- Contract: {Post-MVP}

---

### T002: {Task name}
**Status**: pending  
**Type**: database  
**Priority**: high  
**Estimated Effort**: 4 hours  
**Dependencies**: Depends on T001 (needs {reason})  
**Parallel**: No (sequential after T001)  
**Agent**: database-specialist

**Description**:
{Task description}

[... continues for all tasks ...]

---

## Phase Breakdown

### Phase 1: Foundation (T001-T003)
**Duration**: {days}  
**Dependencies**: None  
**Deliverables**:
- {Deliverable 1}

### Phase 2: Core Implementation (T004-T010)
**Duration**: {days}  
**Dependencies**: Phase 1 complete  
**Deliverables**:
- {Deliverable 2}

### Phase 3: Testing & Refinement (T011-T015)
**Duration**: {days}  
**Dependencies**: Phase 2 complete  
**Deliverables**:
- {Deliverable 3}

---

## Blocked Tasks

### T007: {Task name}
**Blocked By**: {Blocker description}  
**Mitigation**: {Plan to unblock}  
**ETA**: {When unblocked}

---

## Appendix

### Task Status Definitions
- **pending**: Not yet started
- **in_progress**: Currently being worked on
- **completed**: Finished and verified
- **blocked**: Cannot proceed due to dependency/issue

### Agent Assignment Guidelines
- data-model tasks → specification-agent or backend-architect
- database tasks → database-specialist
- frontend tasks → frontend-specialist
- backend tasks → backend-architect
- testing tasks → testing-specialist
- documentation tasks → specification-agent

### Parallel Execution Marker [P]
Tasks marked [P] can be executed simultaneously with other [P] tasks in the same phase. This enables:
- Multiple agents working concurrently
- Faster feature delivery
- Optimal resource utilization
```

**Rationale**:
- **Dependencies**: Clear task ordering prevents errors
- **Parallelization**: [P] markers enable concurrent work
- **Status Tracking**: Progress visibility
- **Agent Assignment**: Correct agent for each task type

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/templates/tasks-template.md` (enhanced with dependencies)
- Used by: /tasks command, tasks-agent

**Dependencies**:
- ENH-WFL-003 (/tasks command with dependency tracking)
- ENH-AGT-001 (tasks-agent)

**Benefits**:
- Clear task dependencies
- Parallel execution optimization
- Progress tracking
- Correct agent delegation

**Migration Path**:
1. Expand tasks-template.md with dependency fields
2. Add parallel execution markers [P]
3. Add agent assignment guidance
4. Update tasks-agent to generate dependencies
5. Test with complex multi-domain feature

**Rollback**: Revert to simple task list

---

#### ENH-TPL-004: Agent File Template

**ID**: ENH-TPL-004  
**Priority**: HIGH  
**Breaking**: No (new template)

**Description**:
Introduces agent-file-template.md for creating SDD-compliant agents with constitutional alignment (see ENH-AGT-003 for full structure).

**Template Highlights**:
```markdown
# {{AGENT_NAME}} Agent

## Core Purpose
{{AGENT_PURPOSE}}

## Core Capabilities
{3-5 key expertise areas}

## Department Classification
**Department**: {{DEPARTMENT}}
**Role Type**: Specialist / Architect / Coordinator
**Interaction Level**: User-Focused / Agent-Focused

## Working Principles

### Constitutional Principles Application
1. **Library-First**: {How this agent applies Principle I}
2. **Test-First**: {How this agent applies Principle II}
3. **Contract-First**: {How this agent applies Principle III}
4. **Git Operations**: MUST request user approval (Principle VI)
5. **Agent Delegation**: {Domain boundaries} (Principle X)
6. **Design System**: {If applicable} (Principle XII)

### Department-Specific Guidelines
{Domain best practices}

## Tool Usage Policies
**Authorized Tools**: Read, Grep, Glob, TodoWrite
**MCP Server Access**: mcp__ref-tools
**Restricted Operations**: No Git operations, no direct file writing

## Specialized Knowledge
{Domain expertise, patterns, best practices}

## Update History
| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0.0   | {{DATE}} | Initial creation | create-agent.sh |
```

**Rationale**:
- **Consistency**: All agents follow same structure
- **Constitutional**: Compliance baked into template
- **Automation**: Used by create-agent.sh for rapid agent creation

**Implementation**:

**Files**:
- `/workspaces/ioun-ai/.specify/templates/agent-file-template.md`
- Used by: create-agent.sh, subagent-architect

**Dependencies**:
- ENH-AGT-006 (Subagent Architect)
- ENH-WFL-004 (/create-agent command)

**Benefits**: (See ENH-AGT-003)

**Migration Path**: (See ENH-AGT-006)

---

(Due to length, I'll now complete with Categories 6-7, Implementation Recommendations, and Appendices in a final comprehensive section...)
