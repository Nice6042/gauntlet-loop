# Gauntlet Loop

Portable, explicitly invoked multi-agent delivery, improvement, and Bug Hunt
campaigns.

Gauntlet Loop provides two modes:

- **Delivery/Improvement:** dependency-safe Builder–Critic loops for projects,
  features, and targeted improvements.
- **Bug Hunt:** isolated Finder–Spec-Verifier–Fixer–Fix-Verifier area loops,
  followed by combined testing, adversarial integration review, merge, and Main
  Agent verification.

Both modes use frozen completion gates, role separation, reproducible evidence,
resumable state, per-role/task model and effort routing, and operator-selected
`ADAPTIVE`, `CEILING(N)`, or continuously replenished `SUSTAINED(N)`
concurrency.

Bug Hunt ships sealed prompts for Main Agent, Finder, Spec Verifier, Fixer,
fresh Fix Verifier, Combiner, Final Tester, and Integration Verifier, plus a
shared evidence/output-quality contract. Hosts route these templates to the
operator-selected model and effort.

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

Gauntlet Loop never activates implicitly. Ask explicitly and select the mode:

```text
Use Gauntlet Loop on this delivery task.
Use Gauntlet Loop in Bug Hunt mode on this repository.
```

The owner approves scope, exclusions, completion standard, comparisons,
models/effort, concurrency, isolation, resources, evidence, and permissions
before execution. A generic request to fix a bug does not activate the skill.

See `skills/gauntlet-loop/SKILL.md` for the canonical protocol,
`skills/gauntlet-loop/references/` for progressively loaded operating detail,
and `docs/installation.md` for installation.

## Research

The evidence and decisions behind version 1.1.0 are in
`docs/agent-skills-10k-research.md`, including the deduplicated repository
inventory and adopted/rejected patterns.

## License

Apache-2.0.
