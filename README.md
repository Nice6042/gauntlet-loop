# Gauntlet Loop

Portable, explicitly invoked Builder–Critic multi-agent quality campaigns.

Gauntlet Loop decomposes a goal into dependency-safe Loop Tasks, runs Builder–Critic repair cycles to a user-selected completion standard, integrates completed work through Combiner–Integration-Critic loops, and repeats in waves until the whole deliverable meets its frozen quality contract.

## Install

### Agent Skills CLI

```bash
npx -y skills@latest add Nice6042/gauntlet-loop --skill gauntlet-loop --yes
```

### Codex

```bash
codex plugin marketplace add Nice6042/gauntlet-loop
codex plugin add gauntlet-loop@gauntlet-loop
```

### Claude Code

```bash
claude plugin marketplace add Nice6042/gauntlet-loop
claude plugin install gauntlet-loop@gauntlet-loop
```

## Activate

Gauntlet Loop never activates implicitly. Ask explicitly:

```text
Use Gauntlet Loop on this task.
```

The owner then chooses the specification, comparison references, models/effort, concurrency, resource policy, and completion standard: Absolute Wowed, Strict Wowed, User-Defined, or Main-Agent Recommended.

See `skills/gauntlet-loop/SKILL.md` for the canonical protocol and `docs/` for architecture, installation, integration, security, and usage documentation.

## License

Apache-2.0.
