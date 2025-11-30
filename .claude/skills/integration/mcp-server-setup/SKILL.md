---
name: mcp-server-setup
description: |
  MCP (Model Context Protocol) server selection and configuration skill.
  Guides users through identifying, installing, and configuring MCP servers
  based on their project's PRD requirements. Should be executed after
  /initialize-project to extend Claude Code's capabilities for the project.
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, AskUserQuestion
---

# MCP Server Setup Skill

## Purpose

This skill guides the selection and installation of MCP (Model Context Protocol) servers after project initialization. MCP servers extend Claude Code's capabilities by providing:

- **Tool Access**: Database connections, cloud services, browsers, APIs
- **Context Enhancement**: Code indexing, documentation, knowledge bases
- **Automation**: CI/CD, deployment, testing infrastructure

## When to Use

**Trigger**: After `/initialize-project` completes, before first `/specify`

**Workflow Position**:
```
/create-prd → /initialize-project → [MCP Setup] → /specify → /plan → /tasks
```

## Constitutional Principles

| Principle | Enforcement |
|-----------|-------------|
| **IX (Dependency Management)** | MCP servers are dependencies requiring justification |
| **VI (Git Approval)** | Configuration changes need user approval |
| **XI (Input Validation)** | Validate MCP server sources before installation |

---

## MCP Server Categories

### Category 1: Core Infrastructure (Usually Pre-Installed)

These are typically available by default in Claude Code:

| Server | Purpose | Tools Provided |
|--------|---------|----------------|
| **filesystem** | File operations | Read, Write, Edit, Glob, Grep |
| **ide** | VS Code integration | getDiagnostics, executeCode |

### Category 2: Database & Backend

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **supabase** | Supabase projects | `npx -y @anthropic-ai/mcp-supabase` | PostgreSQL, Auth, Storage via Supabase |
| **postgres** | Direct PostgreSQL | `npx -y @anthropic-ai/mcp-postgres` | Direct PostgreSQL connections |
| **sqlite** | SQLite databases | `npx -y @anthropic-ai/mcp-sqlite` | Local SQLite databases |
| **prisma** | Prisma ORM | `npx -y @prisma/mcp-prisma` | Projects using Prisma |
| **firebase** | Firebase/Firestore | `npx -y @anthropic-ai/mcp-firebase` | Firebase projects |

### Category 3: Cloud & Deployment

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **aws** | AWS services | `npx -y @anthropic-ai/mcp-aws` | AWS infrastructure |
| **gcp** | Google Cloud | `npx -y @anthropic-ai/mcp-gcp` | GCP projects |
| **azure** | Microsoft Azure | `npx -y @anthropic-ai/mcp-azure` | Azure deployments |
| **vercel** | Vercel deployment | `npx -y @anthropic-ai/mcp-vercel` | Vercel hosting |
| **netlify** | Netlify deployment | `npx -y @anthropic-ai/mcp-netlify` | Netlify hosting |
| **docker** | Container management | `npx -y @anthropic-ai/mcp-docker` | Docker/containerized apps |

### Category 4: Browser & Testing

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **browsermcp** | Browser automation | `npx -y @anthropic-ai/mcp-browsermcp` | E2E testing, web scraping |
| **playwright** | Playwright testing | `npx -y @anthropic-ai/mcp-playwright` | Playwright-based testing |
| **puppeteer** | Puppeteer control | `npx -y @anthropic-ai/mcp-puppeteer` | Puppeteer automation |

### Category 5: Search & Documentation

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **perplexity** | AI-powered search | `npx -y @anthropic-ai/mcp-perplexity` | Research, documentation lookup |
| **brave-search** | Brave Search API | `npx -y @anthropic-ai/mcp-brave-search` | Web search integration |
| **github** | GitHub API | `npx -y @anthropic-ai/mcp-github` | GitHub repos, issues, PRs |
| **notion** | Notion workspace | `npx -y @anthropic-ai/mcp-notion` | Notion documentation |
| **confluence** | Atlassian docs | `npx -y @anthropic-ai/mcp-confluence` | Confluence wikis |

### Category 6: Communication & Collaboration

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **slack** | Slack integration | `npx -y @anthropic-ai/mcp-slack` | Team notifications |
| **linear** | Linear project mgmt | `npx -y @anthropic-ai/mcp-linear` | Issue tracking with Linear |
| **jira** | Jira integration | `npx -y @anthropic-ai/mcp-jira` | Jira issue tracking |

### Category 7: Code & Context

| Server | Purpose | Install Command | When to Use |
|--------|---------|-----------------|-------------|
| **context7** | Library docs | `npx -y @anthropic-ai/mcp-context7` | Up-to-date library documentation |
| **memory** | Persistent memory | `npx -y @anthropic-ai/mcp-memory` | Cross-session context |
| **sequential-thinking** | Complex reasoning | `npx -y @anthropic-ai/mcp-sequential-thinking` | Multi-step problem solving |

---

## Selection Procedure

### Step 1: Analyze PRD Requirements

Read the PRD and extract:

1. **Technology Stack** (from Technical Constraints section)
   - Database type (PostgreSQL, MySQL, SQLite, MongoDB, etc.)
   - Cloud provider (AWS, GCP, Azure, Vercel, etc.)
   - Frontend framework (React, Vue, Next.js, etc.)

2. **Integration Requirements** (from Integration Requirements section)
   - External APIs
   - Third-party services
   - Communication tools

3. **Testing Strategy** (from Principle II section)
   - E2E testing needs
   - Browser automation requirements

### Step 2: Map Requirements to MCPs

Create a mapping table:

```markdown
## MCP Selection for [Project Name]

| Requirement | Source (PRD Section) | Recommended MCP | Priority |
|-------------|---------------------|-----------------|----------|
| PostgreSQL database | Technical Constraints | supabase or postgres | Required |
| AWS deployment | Technical Constraints | aws | Required |
| E2E testing | Principle II | browsermcp | Required |
| GitHub integration | Integration Requirements | github | Recommended |
| Slack notifications | Integration Requirements | slack | Optional |
```

### Step 3: Present Recommendations to User

```markdown
## Recommended MCP Servers

Based on your PRD, I recommend the following MCP servers:

### Required (for core functionality)
1. **supabase** - PostgreSQL database with auth and storage
2. **aws** - AWS S3 and Lambda deployment
3. **browsermcp** - E2E testing with browser automation

### Recommended (enhance workflow)
4. **github** - GitHub issues and PR integration
5. **context7** - Up-to-date documentation for your tech stack

### Optional (nice to have)
6. **slack** - Team notifications for deployments

Would you like me to install these? I'll configure each one and guide you through any API keys needed.
```

### Step 4: Install Selected MCPs

For each approved MCP:

1. **Check if already installed**:
   ```bash
   # MCPs are configured in Claude Code settings
   # Check ~/.claude/settings.json or project .claude.json
   ```

2. **Install and configure**:
   ```json
   // Add to Claude Code MCP configuration
   {
     "mcpServers": {
       "server-name": {
         "command": "npx",
         "args": ["-y", "@org/mcp-server-name"],
         "env": {
           "API_KEY": "env:SERVER_API_KEY"
         }
       }
     }
   }
   ```

3. **Guide user through credentials**:
   - Identify required environment variables
   - Provide instructions for obtaining API keys
   - Add to `.env` file (never commit!)

---

## Configuration Patterns

### Pattern 1: Database MCP

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-supabase"],
      "env": {
        "SUPABASE_URL": "env:SUPABASE_URL",
        "SUPABASE_ANON_KEY": "env:SUPABASE_ANON_KEY",
        "SUPABASE_SERVICE_ROLE_KEY": "env:SUPABASE_SERVICE_ROLE_KEY"
      }
    }
  }
}
```

**.env additions**:
```bash
# Supabase credentials (from project settings)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### Pattern 2: Cloud Provider MCP

```json
{
  "mcpServers": {
    "aws": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-aws"],
      "env": {
        "AWS_ACCESS_KEY_ID": "env:AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY": "env:AWS_SECRET_ACCESS_KEY",
        "AWS_REGION": "env:AWS_REGION"
      }
    }
  }
}
```

### Pattern 3: Browser Automation MCP

```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-browsermcp"],
      "env": {}
    }
  }
}
```

### Pattern 4: Search/Documentation MCP

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "env:PERPLEXITY_API_KEY"
      }
    }
  }
}
```

---

## Department-to-MCP Mapping

Based on agent departments, recommend appropriate MCPs:

| Department | Agents | Recommended MCPs |
|------------|--------|------------------|
| **Architecture** | backend-architect | aws/gcp/azure, postgres/supabase |
| **Engineering** | frontend-specialist, full-stack-developer | browsermcp, github, context7 |
| **Data** | database-specialist | postgres, supabase, firebase |
| **Quality** | testing-specialist, security-specialist | browsermcp, playwright |
| **Product** | specification-agent, planning-agent, tasks-agent | github, notion, linear |
| **Operations** | devops-engineer, performance-engineer | aws/gcp/azure, docker |

---

## Claude Assistance

Claude can help with MCP setup in several ways:

### 1. Identify Needed MCPs

Ask Claude:
```
"Based on my PRD at .docs/prd/prd.md, what MCP servers would benefit this project?"
```

### 2. Installation Guidance

Ask Claude:
```
"Help me install and configure the supabase MCP server"
```

### 3. Troubleshooting

Ask Claude:
```
"The postgres MCP isn't connecting. Here's the error: [paste error]"
```

### 4. Discovery

Ask Claude:
```
"What MCP servers are available for [specific need]?"
```

---

## Validation Checklist

After MCP setup, verify:

```
[ ] All required MCPs installed based on PRD
[ ] API keys/credentials configured in .env
[ ] .env is in .gitignore (never commit secrets!)
[ ] MCPs tested with simple operations
[ ] Department agents have access to relevant MCPs
[ ] Documentation updated with MCP dependencies
```

---

## Common Issues

### MCP Won't Start

1. Check Node.js version (v18+ required)
2. Verify npx is available
3. Check for port conflicts
4. Review Claude Code logs

### Authentication Errors

1. Verify environment variables are set
2. Check API key validity
3. Ensure correct permissions/scopes
4. Test credentials independently

### MCP Not Available in Claude

1. Restart Claude Code after configuration
2. Check MCP configuration syntax (JSON validity)
3. Verify command path is correct
4. Check for npm package availability

---

## Security Considerations

1. **Credential Management**
   - Store all secrets in `.env`
   - Use `env:VAR_NAME` syntax in MCP config
   - Never hardcode credentials
   - Rotate credentials regularly

2. **Access Scope**
   - Use least-privilege API keys
   - Limit MCP access to needed resources
   - Review permissions before granting

3. **Audit Trail**
   - Log MCP usage for sensitive operations
   - Monitor for unusual activity
   - Document all configured MCPs

---

## Output Template

After completing MCP setup, provide this summary:

```markdown
## MCP Configuration Complete

**Project**: [Name]
**Date**: [Date]

### Installed MCPs

| MCP | Purpose | Status |
|-----|---------|--------|
| supabase | Database access | Configured |
| aws | Cloud deployment | Configured |
| browsermcp | E2E testing | Ready |

### Environment Variables Added

- `SUPABASE_URL` - Supabase project URL
- `SUPABASE_ANON_KEY` - Supabase anonymous key
- `AWS_ACCESS_KEY_ID` - AWS access key
- `AWS_SECRET_ACCESS_KEY` - AWS secret key

### Next Steps

1. Test each MCP with a simple operation
2. Run `/specify` for first feature
3. MCPs are now available to all agents

### Verification Commands

To test your MCP connections, try:
- "Query the users table" (tests supabase)
- "List S3 buckets" (tests aws)
- "Open https://example.com in browser" (tests browsermcp)
```

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-11-30
**Constitutional Version**: 1.6.0
