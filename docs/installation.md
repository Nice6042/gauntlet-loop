# Installation

## Agent Skills CLI

```bash
npx -y skills@latest add Nice6042/gauntlet-loop --skill gauntlet-loop --yes
```

## Codex

```bash
codex plugin marketplace add Nice6042/gauntlet-loop
codex plugin add gauntlet-loop@gauntlet-loop
```

## Claude Code

```bash
claude plugin marketplace add Nice6042/gauntlet-loop
claude plugin install gauntlet-loop@gauntlet-loop
```

## Manual

Copy `skills/gauntlet-loop/` into the skills directory supported by your host. Preserve the complete directory, including references, rubrics, templates, schemas, scripts, and adapters.

## Verify

Confirm that the installed skill is named `gauntlet-loop` and that `SKILL.md` is present. Activation is explicit only: `Use Gauntlet Loop on this task.`
