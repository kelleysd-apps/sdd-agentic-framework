# Specify Constitution

## Core Principles

### I. Library-First
Every feature MUST begin its existence as a standalone library. No feature shall be implemented directly within application code without first being abstracted into a reusable library component. Libraries must be self-contained with their own tests, documentation, and clear boundaries. Library interfaces must be designed for reusability beyond the immediate use case. No "organizational" libraries—each must have a clear, singular purpose.

### II. Command-Line Interface
Every library MUST expose its primary functionality through a CLI. The CLI is the primary interface for both human operators and system integrations. All operations must follow text in/text out principles with proper exit codes. Configuration happens through arguments, environment variables, or config files—never hard-coded. CLIs must support both human-readable and machine-parseable (JSON) output formats.

### III. Test-First Development (NON-NEGOTIABLE)
TDD is mandatory: Write tests → Get user approval → Tests fail → Then implement. No exceptions. Every library must have unit tests with >80% code coverage. Every integration point must have contract tests. Every user-facing feature must have end-to-end tests. Tests are documentation and must be readable as such. Test code follows the same quality standards as production code.

### IV. Contract-Driven Integration
Libraries communicate through well-defined contracts, not shared code. All contracts must be versioned and backward compatible within major versions. Contract changes require migration paths and deprecation notices. Integration tests must verify contract compliance, not implementation details. Mock implementations must be provided for testing.

### V. Observability Built-In
Every library must support structured logging with configurable verbosity. All operations must emit metrics about performance and errors. Distributed tracing must be supported for request flows. Health checks must be exposed for monitoring. Debug modes must provide detailed operational insights.

### VI. Documentation as Code
Documentation lives with code and is part of the definition of "done." Every library must have README with purpose, usage, and examples. Every public API must have comprehensive docstrings. Every architectural decision must be recorded in ADRs. Every complex algorithm must have explanatory comments. Documentation must be verified as part of CI/CD.

### VII. Progressive Enhancement
Start with the simplest solution that could possibly work. Add complexity only when proven necessary through actual use cases. YAGNI (You Aren't Gonna Need It) is the default position. Premature optimization is the root of all evil. Features must be feature-flagged and incrementally rollable.

### VIII. Idempotent Operations
All operations should be safely repeatable without side effects. State mutations must be explicit and reversible. Failure recovery must be automated where possible. Partial failures must not leave inconsistent state. All data modifications must support dry-run mode.

### IX. Secure by Default
Security is not optional or an afterthought. All inputs must be validated and sanitized. All outputs must be properly escaped. Secrets must never be logged or committed. Authentication and authorization must be enforced at every boundary. Dependencies must be regularly audited for vulnerabilities.

## Development Workflow

### Git Operations

#### User Approval Requirements (NON-NEGOTIABLE)
- **NO automatic branch creation without explicit user approval**
- When branch creation is needed, MUST ask user:
  1. If they want a new branch created
  2. How they want it formatted/named
- **ALL Git operations require user confirmation:**
  - Branch creation/switching/deletion
  - Commits and commit messages
  - Pushes, pulls, and merges
  - Any modifications to Git history
- SDD functions and automated tools MUST NOT perform Git operations autonomously

#### Branch Standards
- Feature branches follow pattern: ###-feature-name (when user approves)
- Commits must be atomic with clear messages
- Force pushes forbidden on main/master
- All changes require pull request review
- Squash merging preferred for feature branches

### Quality Gates
Before any code can be merged:
- All tests must pass (unit, integration, e2e)
- Code coverage must meet minimum threshold (80%)
- Linting and formatting checks must pass
- Security scanning must show no critical issues
- Documentation must be updated

### Review Requirements
- Every PR requires at least one approval
- Authors cannot approve their own PRs
- Architectural changes require team consensus
- Breaking changes require migration plan
- Performance impacts require benchmarks

## Technology Constraints

### Approved Stack
Development environments and tools should be explicitly defined per project. No implicit assumptions about available tools or frameworks. All dependencies must be declared and version-pinned. Breaking changes to dependencies require team approval.

### Performance Standards
Response time targets must be defined and measured. Memory usage must be bounded and monitored. CPU usage must be optimized for efficiency. Network calls must be minimized and batched. Storage must be used efficiently with cleanup policies.

## Exceptions and Amendments

### Constitutional Authority
This constitution represents the team's shared agreement on development practices. Violations require explicit justification and team approval. Temporary exceptions must have expiration dates and remediation plans. Permanent changes require constitutional amendment.

### Amendment Process
1. Propose change with rationale and impact analysis
2. Team discussion and consensus building
3. Trial period for significant changes
4. Formal adoption or rejection
5. Documentation update and team notification
6. **MANDATORY**: Follow `/memory/constitution_update_checklist.md` to update all dependent documents

### Enforcement
- Constitution compliance is part of code review
- Violations block merging until resolved
- Patterns of violation trigger team discussion
- Good faith efforts to comply are expected
- Education preferred over punishment

**Version**: 1.0.0
**Ratified**: [Date of adoption]
**Last Amended**: [Date of last change]