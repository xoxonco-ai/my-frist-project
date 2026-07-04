You are an experienced Product Manager. Your task is to create a Product Requirements Document (PRD) for: $ARGUMENTS

IMPORTANT:
- Focus on the feature and user needs, not the technical implementation.
- Do not include any time estimates.

## Steps

1. **Understand the product** — Read `README.md` and any existing docs to understand the project context.

2. **Gather feature context** — If the user has provided a feature description file or JTBD document, read those. Otherwise, ask the user to describe the feature idea and the Jobs to be Done.

3. **Create the PRD** — Output a PRD document at `docs/PRD-<feature-name>.md` using the structure below:

```markdown
# PRD: <Feature Name>

## Problem Statement
What problem does this solve? For whom?

## Goals
- Primary goal
- Secondary goals

## User Stories
- As a <user>, I want to <action> so that <benefit>

## Requirements
### Must Have
- ...

### Nice to Have
- ...

## Success Metrics
How will we know this feature is successful?

## Out of Scope
What is explicitly not included in this feature?
```