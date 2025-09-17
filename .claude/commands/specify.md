---
description: Create or update the feature specification from a natural language feature description.
---

Given the feature description provided as an argument, do this:

1. Check if user wants to create a new branch:
   - Ask user: "Would you like to create a new feature branch, or work on the current branch?"
   - If new branch requested: Run `.specify/scripts/bash/create-new-feature.sh --json "$ARGUMENTS"`
   - If current branch: Use current branch and create spec file at `specs/[current-branch]/spec.md`
2. Load `.specify/templates/spec-template.md` to understand required sections.
3. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings.
4. Report completion with branch name, spec file path, and readiness for the next phase.

Note: Branch creation and any Git operations require explicit user approval.
