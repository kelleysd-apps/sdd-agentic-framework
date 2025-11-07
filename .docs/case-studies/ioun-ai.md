# Case Study: Ioun AI Mobile Application

**Project**: Ioun AI - D&D Companion App
**Duration**: October 2024 - November 2025 (13 months)
**Framework Version**: SDD Agentic Framework v0.x → v1.5.0
**Platform**: React Native / Expo
**Database**: Supabase (PostgreSQL)

---

## Executive Summary

Ioun AI is a mobile companion application for Dungeons & Dragons (D&D) players and Dungeon Masters. This case study documents how the SDD Agentic Framework was applied and evolved during the development of this production application.

### Key Metrics
- **Features Developed**: 10+ major features
- **Framework Evolution**: 50+ enhancements identified and backported
- **Constitution Growth**: 50 lines → 302 lines (6x expansion)
- **Agents Created**: 13 specialized agents across 6 departments
- **Development Time**: 13 months of active development

---

## Project Context

### Business Domain: D&D Companion Tools

The application serves two primary user types:
1. **Players**: Manage characters, track stats, participate in campaigns
2. **Dungeon Masters (DMs)**: Create campaigns, manage sessions, generate NPCs, track encounters

### Technology Stack

**Frontend**:
- React Native with Expo
- expo-router for navigation
- React Query for state management
- TypeScript for type safety

**Backend**:
- Supabase (PostgreSQL database)
- Row-Level Security (RLS) for authorization
- Real-time subscriptions
- Edge Functions for serverless compute

**Design System**:
- Dark neumorphism aesthetic
- Deep purple and blue color palette
- Glassmorphic overlays and soft shadows
- Custom component library

---

## Subscription Tier Implementation

### Tier Structure

**Player Tier** (Free):
- 3 active campaigns maximum
- Basic character management
- Dice roller and basic tools
- Read-only campaign participation

**DM Tier** ($9.99/month):
- Unlimited campaigns
- Advanced DM tools:
  - Encounter builder
  - Session notes and planning
  - AI-powered NPC generation
  - Initiative tracker
  - Campaign templates

**Prestige Tier** (Future):
- Advanced analytics
- Custom homebrew content tools
- Enhanced AI features
- Priority support

### Tier Enforcement Pattern

**Backend Enforcement (RLS)**:
```sql
-- Example: Campaign creation limit for Player tier
CREATE POLICY "player_tier_campaign_limit"
ON campaigns FOR INSERT
TO authenticated
WITH CHECK (
  -- DM tier can create unlimited campaigns
  (SELECT tier FROM user_profiles WHERE id = auth.uid()) = 'dm'
  OR
  -- Player tier limited to 3 active campaigns
  (SELECT COUNT(*)
   FROM campaigns
   WHERE user_id = auth.uid()
   AND status = 'active') < 3
);
```

**Frontend Enforcement (UI)**:
```typescript
const TierRestrictedFeature = () => {
  const { userTier, activeCampaigns } = useUserContext();
  const canCreate = userTier === 'dm' || activeCampaigns.length < 3;

  if (!canCreate) {
    return (
      <TierRestrictedBanner
        message="Player tier limited to 3 active campaigns"
        upgradeAction={() => navigation.navigate('Subscription')}
        tierRequired="DM"
        currentTier={userTier}
      />
    );
  }

  return <CreateCampaignButton />;
};
```

---

## Features Developed

### Feature 001: User Authentication & Profiles
- Email/password authentication
- OAuth providers (Google, Apple)
- User profile management
- Session handling
- Tier assignment and tracking

### Feature 002: Character Management
- Character creation wizard
- D&D 5e rules integration
- Character sheet (stats, inventory, spells)
- Character progression tracking
- Multi-character support

### Feature 003: Campaign Management (DM-only)
- Campaign creation and settings
- Player invitation system
- Campaign timeline and sessions
- Notes and planning tools
- Campaign archives

### Feature 004: Session Tools
- Dice roller with history
- Initiative tracker
- Encounter builder
- Condition tracking
- Quick reference guides

### Feature 005: AI-Powered NPC Generation (DM-only)
- AI-generated NPC personalities
- Stat block creation
- NPC relationship mapping
- Voice and mannerisms
- Campaign-specific context

---

## Design System: Dark Neumorphism

### Visual Principles

**Color Palette**:
```typescript
const colors = {
  background: {
    primary: '#1a1625',    // Deep purple-black
    secondary: '#241d33',  // Lighter purple
    tertiary: '#2f2640',   // Elevated surfaces
  },
  accent: {
    primary: '#6c5ce7',    // Vibrant purple
    secondary: '#a29bfe',  // Light purple
    tertiary: '#4834df',   // Deep blue-purple
  },
  text: {
    primary: '#e9e9eb',    // Near white
    secondary: '#b8b8c0',  // Muted gray
    tertiary: '#8e8e93',   // Dim gray
  },
};
```

**Neumorphic Shadows**:
```typescript
const neumorphicShadow = {
  light: '4px 4px 12px rgba(0, 0, 0, 0.4)',
  dark: '-4px -4px 12px rgba(255, 255, 255, 0.05)',
  combined: `
    4px 4px 12px rgba(0, 0, 0, 0.4),
    -4px -4px 12px rgba(255, 255, 255, 0.05)
  `,
};
```

**Glassmorphic Overlays**:
```typescript
const glassmorphism = {
  background: 'rgba(36, 29, 51, 0.8)',
  backdropFilter: 'blur(20px)',
  border: '1px solid rgba(255, 255, 255, 0.1)',
  boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
};
```

### Component Examples

**Elevated Card**:
```typescript
<View style={{
  backgroundColor: colors.background.tertiary,
  borderRadius: 20,
  padding: 20,
  ...neumorphicShadow.combined,
}}>
  {/* Card content */}
</View>
```

**Glass Modal**:
```typescript
<View style={{
  ...glassmorphism,
  borderRadius: 24,
  padding: 24,
}}>
  {/* Modal content */}
</View>
```

---

## Constitutional Principles in Practice

### Principle I: Library-First Architecture

**Example**: Dice Roller Library
```
src/
├── libs/
│   └── dice-roller/
│       ├── index.ts          # Public API
│       ├── roller.ts         # Core logic
│       ├── parser.ts         # Notation parsing
│       ├── __tests__/        # Unit tests
│       └── README.md         # Library docs
└── features/
    └── session-tools/
        └── DiceRollerScreen.tsx  # Uses library
```

**Benefits**:
- Dice roller reused in multiple features
- Tested independently
- Could be extracted to npm package
- Clear API boundaries

### Principle II: Test-First Development

**Example**: Campaign Creation Flow
1. **Write E2E test** for campaign creation
2. **Get user approval** on test scenarios
3. **Run test** (fails initially)
4. **Implement** feature
5. **Test passes** → Merge

**Test Coverage**:
- E2E tests: Critical user flows
- Contract tests: API endpoints (post-MVP)
- Unit tests: Complex business logic (post-MVP)

### Principle III: Contract-First Design

**Example**: NPC Generation API Contract
```typescript
// contracts/ai-npc-generation.ts
interface NPCGenerationRequest {
  campaign_id: string;
  race?: string;
  class?: string;
  personality_traits?: string[];
  context?: string;
}

interface NPCGenerationResponse {
  npc: {
    name: string;
    race: string;
    class: string;
    level: number;
    personality: string;
    backstory: string;
    stats: DND5eStats;
    appearance: string;
  };
  generation_time_ms: number;
}
```

### Principle VI: Git Operation Approval

**Implementation**:
- No automatic branch creation
- Slash command `/specify` asks before creating branch
- All commits require approval
- No automatic pushes or force pushes

### Principle X: Agent Delegation Protocol

**Example**: Feature 005 (NPC Generation)

```
User Request: "Implement AI-powered NPC generation for DMs"
↓
Constitutional Check: Reads constitution
↓
Domain Analysis: Detects keywords: "AI", "generation", "database", "frontend"
↓
Delegation Decision:
├─ specification-agent: Creates feature spec
├─ backend-architect: Designs AI integration
├─ database-specialist: Designs NPC storage schema
├─ frontend-specialist: Implements UI
├─ security-specialist: Reviews AI prompt injection risks
└─ testing-specialist: Creates test scenarios
↓
task-orchestrator: Coordinates multi-agent workflow
```

---

## Multi-Agent Workflow Example

### Feature: Campaign Management System

**Spec Phase** (specification-agent):
- Created comprehensive feature spec
- Defined user stories for Players and DMs
- Identified tier restrictions
- Output: `specs/003-campaign-management/spec.md`

**Plan Phase** (task-orchestrator + multiple agents):
1. **backend-architect**:
   - Designed campaign data model
   - Planned RLS policies for tier enforcement
   - Defined API endpoints

2. **database-specialist**:
   - Created `campaigns` table schema
   - Implemented RLS policies
   - Created indexes for performance

3. **frontend-specialist**:
   - Designed campaign list UI
   - Implemented create/edit flows
   - Added tier restriction UI

4. **security-specialist**:
   - Reviewed RLS policies
   - Validated tier enforcement
   - Checked for authorization bypasses

**Task Phase** (tasks-agent):
- Generated 15 implementation tasks
- Marked parallel-executable tasks with [P]
- Defined dependencies between tasks

**Implementation**:
- Tasks executed by appropriate agents
- TDD approach maintained
- Git operations approved by user
- Feature completed in 2 sprints

---

## Challenges & Solutions

### Challenge 1: Tier Enforcement Circumvention

**Problem**: Player tier users could bypass campaign limits through API calls

**Solution**:
- Dual-layer enforcement (frontend + backend RLS)
- Backend is source of truth
- Frontend provides UX guidance
- Security review for all tier-gated features

### Challenge 2: AI Cost Management

**Problem**: Unlimited AI NPC generation could be expensive

**Solution**:
- Tier-based rate limiting
- Caching of generated NPCs
- User feedback to improve prompts (reduce regenerations)
- Cost monitoring and alerts

### Challenge 3: Real-Time Session Coordination

**Problem**: Multiple players need real-time updates during sessions

**Solution**:
- Supabase real-time subscriptions
- Optimistic UI updates
- Conflict resolution strategies
- Graceful degradation offline

---

## Lessons Learned

### What Worked Well

1. **Constitutional Governance**: Clear principles prevented technical debt
2. **Agent Specialization**: Domain experts produced higher quality outputs
3. **TDD Approach**: Caught bugs early, reduced rework
4. **Library-First**: Enabled code reuse, easier testing
5. **Tier Enforcement Pattern**: Secure and user-friendly monetization

### What Could Be Improved

1. **Initial Setup Complexity**: First feature took longer to set up patterns
2. **Agent Coordination Overhead**: Manual coordination was time-consuming (led to task-orchestrator creation)
3. **Documentation Drift**: Needed constitution update checklist to prevent
4. **Context Token Usage**: Large agent files sometimes hit limits

### Recommendations for Future Projects

1. **Start with Core Agents**: Create key agents (frontend, backend, database, testing) first
2. **Establish Patterns Early**: First feature sets precedents, invest time
3. **Use task-orchestrator**: For complex features, worth the coordination overhead
4. **Version Constitution**: Track constitutional changes like code
5. **Monitor Costs**: Especially for AI-powered features

---

## Framework Evolution Contributions

This project contributed 50+ enhancements to the SDD framework:

### Constitutional Principles Added
- Principle VI: Git Operation Approval
- Principle X: Agent Delegation Protocol
- Principle XII: Design System Compliance
- Principle XIII: Subscription Tier Enforcement (now generalized as Feature Access Control)
- Principle XIV: AI Model Selection Protocol

### Agents Created
- task-orchestrator (2,000+ lines)
- subagent-architect
- 11 specialized domain agents

### Automation Added
- 4 slash commands with full workflow
- 11 bash automation scripts
- Multi-agent detection logic
- Constitutional compliance checking

### Documentation Created
- 24+ policy/workflow documents
- Agent collaboration triggers
- Testing strategy guide
- Constitution update checklist

---

## Conclusion

The Ioun AI project successfully validated the SDD Agentic Framework in a production environment. The framework's emphasis on constitutional governance, agent specialization, and automated workflows enabled consistent quality across a complex mobile application.

The enhancements identified during this project have been generalized and backported to the core framework, making them available for future adopters while preserving the project-specific examples here for reference.

### Project Status
- **Production**: Active development, approaching MVP launch
- **Users**: Beta testing with D&D community
- **Framework**: All enhancements backported to v1.0.0

---

**For more information about the SDD Agentic Framework, see the main repository documentation.**
