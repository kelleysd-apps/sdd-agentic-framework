# Framework Sanitization Checklist

**Purpose**: Ensure all Ioun AI project-specific elements are properly generalized before backporting enhancements to the SDD framework.

**Version**: 1.0.0
**Date**: 2025-11-06
**Status**: Pre-Implementation Review

---

## Critical Issues Identified

### 1. Hardcoded Project Paths

**Location**: All agent files in `.claude/agents/**/*.md`

**Issue**: References to `/workspaces/ioun-ai/` hardcoded throughout

**Example**:
```markdown
# CURRENT (WRONG):
- **Primary Authority**: `/workspaces/ioun-ai/.specify/memory/constitution.md`
- Base Path: `/workspaces/ioun-ai/.docs/agents/engineering/full-stack-developer/`

# REQUIRED (CORRECT):
- **Primary Authority**: `/.specify/memory/constitution.md`
- Base Path: `/.docs/agents/{department}/{agent-name}/`
```

**Fix Required**: Replace all absolute paths with relative paths from project root

**Files Affected**: 20+ agent files (see grep results)

---

### 2. Automatic Git Operations Without Approval

**Location**:
- `.specify/scripts/bash/create-new-feature.sh` (line 43)
- `init-project.sh` (lines 142-144)

**Issue**: Scripts execute git commands without user approval, violating Constitutional Principle VI

**Example**:
```bash
# CURRENT (WRONG):
git checkout -b "$BRANCH_NAME"

# REQUIRED (CORRECT):
echo "Ready to create branch: $BRANCH_NAME"
read -p "Create this branch? (y/n): " CREATE_BRANCH
if [[ "$CREATE_BRANCH" =~ ^[Yy]$ ]]; then
    git checkout -b "$BRANCH_NAME"
    echo "Branch created"
else
    echo "Branch creation cancelled"
    exit 0
fi
```

**Fix Required**: Add user approval prompts before ALL git operations

**Constitutional Violation**: Principle VI - Git Operation Approval

---

### 3. Project-Specific Design System References

**Location**: Templates and agent files

**Issue**: References to "dark neumorphism" design system

**Example**:
```markdown
# CURRENT (PROJECT-SPECIFIC):
- Design System: Dark neumorphism with glassmorphic elements
- Color palette: deep purples, dark blues

# REQUIRED (GENERALIZED):
- Design System: [Project-specific design system compliance]
- Pattern: Consistent visual language across components
```

**Fix Required**: Generalize to "design system compliance" pattern, make specific system project-configurable

---

### 4. Subscription Tier Specific References

**Location**: Constitutional Principle XIII, templates

**Issue**: Specific tier names (Player/DM/Prestige) instead of generic pattern

**Example**:
```markdown
# CURRENT (PROJECT-SPECIFIC):
Player Tier (Free): 3 campaigns max
DM Tier ($9.99/month): Unlimited campaigns
Prestige Tier (Future): Advanced features

# REQUIRED (GENERALIZED):
Free Tier: Basic features with limitations
Premium Tier: Enhanced features
Enterprise Tier: Full feature set
```

**Fix Required**: Replace with generic tier pattern, provide as example/template

---

### 5. Domain-Specific Business Logic References

**Location**: Examples in PRD, agent context files

**Issue**: D&D-specific terminology (campaigns, characters, sessions, NPCs)

**Example**:
```markdown
# CURRENT (PROJECT-SPECIFIC):
- Campaign management
- Character creation
- NPC generation
- Session tools

# REQUIRED (GENERALIZED):
- Entity management
- Resource creation
- Content generation
- Workflow tools
```

**Fix Required**: Use generic terminology in framework, provide D&D example as separate use case

---

### 6. Platform-Specific Technology References

**Location**: Integration guides, MCP configurations

**Issue**: Expo/React Native specific configurations

**Example**:
```markdown
# CURRENT (PROJECT-SPECIFIC):
- Expo EAS build configuration
- React Native platform specifics
- expo-router navigation

# REQUIRED (GENERALIZED):
- Build system integration pattern
- Mobile platform considerations
- Navigation architecture pattern
```

**Fix Required**: Extract patterns, make technology-specific details optional examples

---

## Sanitization Requirements by Category

### A. Path Sanitization

**Requirement**: All file paths must be relative to project root or use placeholders

**Pattern**:
```markdown
WRONG: `/workspaces/ioun-ai/.specify/memory/constitution.md`
RIGHT: `/.specify/memory/constitution.md`
RIGHT: `{PROJECT_ROOT}/.specify/memory/constitution.md`
RIGHT: `$REPO_ROOT/.specify/memory/constitution.md`
```

**Verification**:
```bash
# No absolute project paths should exist
grep -r "/workspaces/ioun-ai" .claude/ .specify/ .docs/ && echo "FAIL: Absolute paths found" || echo "PASS"
```

**Files to Update**:
- [ ] All 20+ agent files in `.claude/agents/**/*.md`
- [ ] All bash scripts in `.specify/scripts/bash/*.sh`
- [ ] All templates in `.specify/templates/*.md`
- [ ] Documentation in `.docs/**/*.md`

---

### B. Git Operation Sanitization

**Requirement**: NO git operations without explicit user approval

**Pattern**:
```bash
# Function to request git approval
request_git_approval() {
    local operation=$1
    local details=$2

    echo "Git operation requested: $operation"
    echo "Details: $details"
    read -p "Approve this operation? (y/n): " APPROVAL

    if [[ ! "$APPROVAL" =~ ^[Yy]$ ]]; then
        echo "Operation cancelled by user"
        return 1
    fi
    return 0
}

# Usage
if request_git_approval "branch creation" "Branch: $BRANCH_NAME"; then
    git checkout -b "$BRANCH_NAME"
fi
```

**Verification**:
```bash
# Check for git commands without approval
grep -n "git checkout\|git commit\|git push\|git branch" .specify/scripts/bash/*.sh | \
  grep -v "request_git_approval\|read -p" && \
  echo "FAIL: Unapproved git operations found" || echo "PASS"
```

**Scripts to Update**:
- [ ] `.specify/scripts/bash/create-new-feature.sh` (line 43)
- [ ] `init-project.sh` (lines 142-144)
- [ ] Any future scripts with git operations
- [ ] Slash command implementations

---

### C. Design System Sanitization

**Requirement**: Generalize design system references to patterns, not specific implementations

**Pattern**:
```markdown
# Template with placeholder
## Design System Compliance

**Design System**: [Your project's design system name]

**Core Principles**:
- Consistent visual language
- Reusable component library
- Accessibility standards (WCAG 2.1 AA)
- Responsive design patterns

**Components to Follow**:
- Color palette: [Define your colors]
- Typography: [Define your fonts]
- Spacing system: [Define your spacing]
- Component library: [Link to your Storybook/docs]

### Example: Dark Neumorphism (from Ioun AI project)
- Deep purple and blue palette
- Soft shadows and highlights
- Glassmorphic overlays
- High contrast for accessibility
```

**Verification**:
```bash
# Should not contain specific design system names in requirements
grep -i "neumorphism\|neomorphism" .specify/templates/*.md && \
  echo "FAIL: Specific design system in templates" || echo "PASS"
```

**Files to Update**:
- [ ] `spec-template.md` - Make design system section generic
- [ ] `plan-template.md` - Generalize design references
- [ ] Constitutional Principle XII - Make pattern-based, not specific
- [ ] Agent files - Remove design system specifics

---

### D. Tier/Feature Gating Sanitization

**Requirement**: Replace specific tier names with generic patterns

**Pattern**:
```markdown
# Constitutional Principle XIII: Feature Access Control

## Pattern
All feature access restrictions must be enforced at TWO layers:

### Backend Enforcement (MANDATORY)
- Database row-level security (RLS) policies
- API authorization checks
- Access tier validated at data layer

### Frontend Enforcement (MANDATORY)
- UI access indicators
- Upgrade prompts for restricted features
- Graceful degradation for limited tiers

## Generic Tier Structure
```sql
-- Example tier enforcement pattern
CREATE TYPE access_tier AS ENUM ('free', 'premium', 'enterprise');

CREATE TABLE user_profiles (
  id UUID PRIMARY KEY,
  access_tier access_tier DEFAULT 'free'
);

-- Feature limit enforcement
CREATE POLICY "tier_based_limit"
ON resources FOR INSERT
WITH CHECK (
  (SELECT access_tier FROM user_profiles WHERE id = auth.uid()) = 'enterprise'
  OR (SELECT COUNT(*) FROM resources WHERE user_id = auth.uid()) < tier_limit(
    (SELECT access_tier FROM user_profiles WHERE id = auth.uid())
  )
);
```

## Project-Specific Example: Ioun AI Subscription Tiers
- **Player Tier** (Free): 3 campaigns, basic features
- **DM Tier** ($9.99/month): Unlimited campaigns, DM tools
- **Prestige Tier** (Future): Advanced analytics
```

**Verification**:
```bash
# Constitutional principle should not have specific tier names
grep -i "player tier\|dm tier\|prestige" .specify/memory/constitution.md && \
  echo "FAIL: Specific tiers in constitution" || echo "PASS"
```

**Files to Update**:
- [ ] `constitution.md` Principle XIII - Generalize to "Feature Access Control"
- [ ] `spec-template.md` - Use generic tier placeholders
- [ ] Templates - Replace tier names with `{tier_1}`, `{tier_2}`, etc.
- [ ] Provide Ioun AI tiers as example/case study

---

### E. Business Domain Sanitization

**Requirement**: Remove domain-specific terminology from framework, provide as examples

**Pattern**:
```markdown
# Generic Framework Documentation
## Entity Management Feature

Create a system for managing primary business entities with:
- CRUD operations (Create, Read, Update, Delete)
- Access control and permissions
- Audit trail and history
- Search and filtering
- Bulk operations

### Example Implementation: Campaign Management (D&D)
In the Ioun AI project, this pattern was used for campaign management:
- Entity: Campaign (game sessions and story arcs)
- Features: Player roster, session history, story notes
- Access: DM-only editing, player viewing
```

**Verification**:
```bash
# Framework core should not have D&D terminology
grep -i "campaign\|character\|npc\|dm\|session" \
  .specify/memory/constitution.md \
  .specify/templates/*.md && \
  echo "FAIL: Domain-specific terms in framework" || echo "PASS"
```

**Files to Update**:
- [ ] All templates - Remove D&D references, use generic terms
- [ ] Constitution - Use generic examples
- [ ] Agent files - Generic capabilities, not D&D-specific
- [ ] Create separate "Case Studies" document for Ioun AI examples

---

### F. Technology Stack Sanitization

**Requirement**: Extract patterns from tech-specific implementations

**Pattern**:
```markdown
# Generic Pattern: Mobile Build Integration

## Build System Integration Pattern

Your project may use various build systems (Expo EAS, Fastlane, Xcode Cloud, etc.).

### Integration Requirements
1. **Environment Configuration**: Separate dev/staging/prod configs
2. **Build Automation**: Scriptable build process
3. **Secrets Management**: Secure credential handling
4. **Artifact Storage**: Build output management
5. **Distribution**: Beta testing and app store deployment

### Example: Expo EAS Build (from Ioun AI)
```json
{
  "build": {
    "development": {
      "distribution": "internal",
      "env": {
        "API_URL": "https://dev.api.example.com"
      }
    }
  }
}
```

**Verification**:
```bash
# Framework should not require specific tech stack
grep -i "expo\|react native\|eas" \
  .specify/memory/constitution.md && \
  echo "FAIL: Specific tech stack required" || echo "PASS"
```

**Files to Update**:
- [ ] Integration documentation - Extract patterns
- [ ] MCP configurations - Make optional/examples
- [ ] Templates - Tech-agnostic
- [ ] Provide Expo/React Native as optional integration guide

---

## Verification Process

### Phase 1: Pre-Implementation Audit (Week 0)

**Before starting any backport work, run these checks:**

```bash
# 1. Path sanitization check
echo "Checking for hardcoded project paths..."
grep -r "/workspaces/ioun-ai" .claude/ .specify/ .docs/ && \
  echo "❌ FAIL: Absolute paths found" || echo "✅ PASS"

# 2. Git operation approval check
echo "Checking for unapproved git operations..."
grep -n "^\s*git\s" .specify/scripts/bash/*.sh | \
  grep -v "request.*approval\|read -p.*[Yy]" && \
  echo "❌ FAIL: Unapproved git ops" || echo "✅ PASS"

# 3. Design system check
echo "Checking for specific design system requirements..."
grep -i "neumorphism\|neomorphism" .specify/templates/*.md && \
  echo "❌ FAIL: Specific design system" || echo "✅ PASS"

# 4. Tier name check
echo "Checking for specific tier names..."
grep -i "player tier\|dm tier\|prestige" .specify/memory/constitution.md && \
  echo "❌ FAIL: Specific tiers in constitution" || echo "✅ PASS"

# 5. Domain terminology check
echo "Checking for domain-specific terms in framework..."
grep -i "campaign\|character\|npc\|session" \
  .specify/memory/constitution.md \
  .specify/templates/*.md && \
  echo "❌ FAIL: Domain terms in framework" || echo "✅ PASS"

# 6. Tech stack requirement check
echo "Checking for specific tech stack requirements..."
grep -i "expo\|react native\|eas" .specify/memory/constitution.md && \
  echo "❌ FAIL: Specific tech required" || echo "✅ PASS"
```

**All checks must PASS before proceeding with implementation.**

---

### Phase 2: During Implementation (Each Enhancement)

**For each enhancement being backported:**

- [ ] Review source files from Ioun AI implementation
- [ ] Identify project-specific elements
- [ ] Extract generic patterns
- [ ] Implement generalized version
- [ ] Run relevant verification script from above
- [ ] Add project-specific example to case studies doc
- [ ] Update migration guide if breaking changes

---

### Phase 3: Pre-Merge Review (Each PR)

**Before merging any backport PR:**

- [ ] Run all 6 verification scripts (must all PASS)
- [ ] Manually review changed files for:
  - Hardcoded paths
  - Unapproved git operations
  - Project-specific terminology
  - Tech stack assumptions
- [ ] Verify documentation uses generic examples
- [ ] Confirm case studies separate from framework core
- [ ] Test with new project initialization (`./init-project.sh`)

---

### Phase 4: Final Release Audit (End of Week 12)

**Before tagging v1.0.0 release:**

```bash
# Run comprehensive audit
./sanitization-audit.sh  # Create this script with all checks

# Manual verification
1. Initialize new test project: ./init-project.sh
2. Create feature: /specify "test feature"
3. Generate plan: /plan
4. Create tasks: /tasks
5. Verify no Ioun-specific references appear
6. Confirm git operations request approval
7. Test on Linux, macOS, WSL2
```

**Release Criteria**:
- [ ] All automated checks PASS
- [ ] Test project initialization successful
- [ ] No hardcoded paths in any files
- [ ] Git operations require approval
- [ ] Documentation is generic with optional examples
- [ ] Framework works without project-specific tech stack

---

## Sanitization Automation Script

**Create**: `.specify/scripts/bash/sanitization-audit.sh`

```bash
#!/bin/bash
# Comprehensive sanitization audit script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "======================================"
echo "  SDD Framework Sanitization Audit"
echo "======================================"
echo ""

PASS_COUNT=0
FAIL_COUNT=0

# Check 1: Hardcoded paths
echo "1. Checking for hardcoded project paths..."
if grep -r "/workspaces/ioun-ai" "$REPO_ROOT/.claude/" "$REPO_ROOT/.specify/" "$REPO_ROOT/.docs/" 2>/dev/null | grep -v "sdd-framework-enhancements"; then
    echo "   ❌ FAIL: Hardcoded paths found"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: No hardcoded paths"
    ((PASS_COUNT++))
fi
echo ""

# Check 2: Unapproved git operations
echo "2. Checking for unapproved git operations..."
if grep -n "^\s*git\s" "$REPO_ROOT/.specify/scripts/bash/"*.sh "$REPO_ROOT/"*.sh 2>/dev/null | \
   grep -v "request.*approval\|read -p\|echo\|comment\|^#" | grep "git checkout\|git commit\|git push\|git branch"; then
    echo "   ❌ FAIL: Unapproved git operations found"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: All git operations have approval"
    ((PASS_COUNT++))
fi
echo ""

# Check 3: Specific design system
echo "3. Checking for specific design system requirements..."
if grep -i "neumorphism\|neomorphism" "$REPO_ROOT/.specify/templates/"*.md 2>/dev/null | grep -v "example\|case study"; then
    echo "   ❌ FAIL: Specific design system in templates"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: Design system is generic"
    ((PASS_COUNT++))
fi
echo ""

# Check 4: Specific tier names
echo "4. Checking for specific tier names in constitution..."
if grep -i "player tier\|dm tier\|prestige" "$REPO_ROOT/.specify/memory/constitution.md" 2>/dev/null | grep -v "example\|case study"; then
    echo "   ❌ FAIL: Specific tiers in constitution"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: Tier enforcement is generic"
    ((PASS_COUNT++))
fi
echo ""

# Check 5: Domain-specific terms
echo "5. Checking for domain-specific terminology..."
if grep -i "\bcampaign\b|\bcharacter\b|\bnpc\b|\bsession\b" \
   "$REPO_ROOT/.specify/memory/constitution.md" \
   "$REPO_ROOT/.specify/templates/"*.md 2>/dev/null | \
   grep -v "example\|case study\|user session\|http session"; then
    echo "   ❌ FAIL: Domain-specific terms in framework"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: Framework uses generic terminology"
    ((PASS_COUNT++))
fi
echo ""

# Check 6: Tech stack requirements
echo "6. Checking for specific tech stack requirements..."
if grep -i "\bexpo\b|\breact native\b|\beas\b" "$REPO_ROOT/.specify/memory/constitution.md" 2>/dev/null | grep -v "example\|optional\|case study"; then
    echo "   ❌ FAIL: Specific tech stack required in constitution"
    ((FAIL_COUNT++))
else
    echo "   ✅ PASS: Tech stack is not prescribed"
    ((PASS_COUNT++))
fi
echo ""

# Results
echo "======================================"
echo "  Audit Results"
echo "======================================"
echo "✅ Passed: $PASS_COUNT"
echo "❌ Failed: $FAIL_COUNT"
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo "🎉 All checks passed! Framework is sanitized."
    exit 0
else
    echo "⚠️  Some checks failed. Review issues above."
    exit 1
fi
```

---

## Sign-Off Checklist

Before declaring sanitization complete:

- [ ] All 6 automated checks pass
- [ ] Manual review completed by 2+ people
- [ ] Test project initialized successfully
- [ ] No references to "Ioun" or "ioun-ai" except in PRD/SOW docs
- [ ] No D&D terminology in framework core
- [ ] All git operations have approval gates
- [ ] Paths are relative or use placeholders
- [ ] Design system is generalized pattern
- [ ] Tier enforcement is generic pattern
- [ ] Technology stack is not prescribed
- [ ] Case studies document created with project-specific examples
- [ ] Migration guide includes sanitization verification steps

---

**Sign-Off**:

**Developer**: _________________________ Date: _________

**Reviewer**: _________________________ Date: _________

**Framework Maintainer**: _________________________ Date: _________
