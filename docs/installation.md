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

Copy `skills/gauntlet-loop/` into the skills directory supported by your host.
Preserve the complete directory: `SKILL.md`, `references/`, `templates/`,
`schemas/`, and `adapters/`.

## Verify

Confirm that the installed skill contains `SKILL.md`,
`references/bug-hunt-protocol.md`, `references/concurrency.md`,
`references/output-quality.md`, all bundled `templates/*-prompt.md`,
`templates/integration-roles.md`, both state templates, and both schemas.
The installed skill name remains `gauntlet-loop`. Activation is explicit only:
`Use Gauntlet Loop on this delivery task.` or
`Use Gauntlet Loop in Bug Hunt mode on this repository.`
