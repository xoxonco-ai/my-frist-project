Help the user create a comprehensive Product Requirement Prompt (PRP) for: $ARGUMENTS

A PRP is PRD + curated codebase intelligence + agent/runbook — the minimum viable packet an AI needs to ship production-ready code on the first pass.

## Research Process

1. **Codebase Exploration**
   - Explore the current project structure with `git ls-files`
   - Identify relevant files and patterns that should be followed
   - Ask the user about specific areas to focus on

2. **Documentation Review**
   - Check for any existing docs (README, docs/, etc.)
   - Identify documentation gaps
   - Ask the user if additional documentation should be referenced

3. **Web Research**
   - Research the feature/product concept
   - Look into relevant library documentation and example implementations

4. **Implementation Requirements**
   - Confirm implementation details with the user
   - Ask about external dependencies or libraries to consider

## PRP Structure

Create a PRP document (save to `PRPs/<feature-name>.md`) with the following sections:

```markdown
# PRP: <Feature Name>

## Goal
One-sentence description of what this implements.

## Context
- Relevant files and their purpose
- Patterns to follow
- External dependencies

## Implementation Blueprint
Step-by-step plan for implementation.

## Validation Criteria
- How to verify the implementation is correct
- Tests to write
- Edge cases to handle
```

## User Interaction

After completing initial research, present findings and confirm:
- The scope of the PRP
- Patterns to follow
- Implementation approach
- Validation criteria

If the user says "continue", proceed with PRP creation without further input.
