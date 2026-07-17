# Fable Method — Command Reference

Trigger commands for the four Fable Method skills installed in this
marketplace (`fable-method`, `fable-loop`, `fable-judge`, `fable-domain`).

Source: [Sahir619/fable-method](https://github.com/Sahir619/fable-method).

## Slash commands

| Skill | Command | What it does |
|-------|---------|--------------|
| **fable-method** | `/fable-method <task>` | Run the full problem-solving loop (classify → define done → gather evidence → decide → act → verify → report). |
| | `/fable-method plan` | Stop after producing the plan; take no action. |
| | `/fable-method audit` | Grade the work already done in the conversation against the loop, step by step. |
| | `/fable-method report` | Rewrite the answer you were about to send in outcome-first form. |
| **fable-loop** | `/fable-loop <task>` | End-to-end orchestrated run: parallel evidence subagents → one committed plan → surgical execution → adversarial verification → honest report. |
| **fable-judge** | `/fable-judge` | Judge the most recent completed work in the conversation (or a diff / directory / branch you name). |
| | `/fable-judge suite <target>` | Run the fable-method trap suite against a skill or model. **Requires the upstream `eval/` directory, which is not bundled here** — clone `Sahir619/fable-method` first. |
| **fable-domain** | `/fable-domain <sector>` | Discuss, research, and generate a trusted skill bundle for a domain (workflow + flowchart + adapter + trap + smoke eval). |

## Natural-language triggers

You don't have to use the slash form — these phrases invoke the same skills:

- **fable-method** — "use the fable method", "approach this like Fable"
- **fable-loop** — "run the fable loop", "do this the way Fable would"
- **fable-judge** — "judge this work", "verify what it did", "did that actually work?"
- **fable-domain** — "make a skill for &lt;domain&gt;", "add a domain to the fable method"

## Notes

- These commands work in a Claude Code environment where the skills are
  installed. Install this marketplace with
  `/plugin marketplace add coreyhaines31/marketingskills` then
  `/plugin install marketing-skills`.
- `/fable-judge suite` depends on the upstream `eval/` harness, which is a
  ~768K dev/test directory deliberately left out of this content marketplace.
  Clone [Sahir619/fable-method](https://github.com/Sahir619/fable-method) to
  run suite mode.
- Only `fable-method` declares an explicit `trigger:` in its frontmatter
  (`/fable-method`); the others are invoked by name or by the phrases above.
