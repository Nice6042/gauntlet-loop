# Owner intake

## Campaign

- Campaign mode: Delivery/Improvement / Bug Hunt
- Desired final deliverable:
- Starting artifacts/repository and base commit:
- In-scope areas:
- Explicit exclusions:
- Target platforms/environments:
- Must-have requirements:
- Prohibited behavior/non-goals:
- Comparison references and comparison dimensions:
- Completion standard: Absolute Wowed / Strict Wowed / User-Defined / Main-Agent Recommended
- Resource policy: quality-first / budget-capped / iteration-capped / adaptive
- Permission boundaries:
- Required evidence/tests/reproductions:
- Checkpoint location:

## Model and effort routing

- Main Agent:
- Builder:
- Critic:
- Finder:
- Spec Verifier:
- Fixer:
- Fix Verifier:
- Fresh closure critic:
- Combiner:
- Final Tester:
- Integration Verifier:
- Main final review:
- Per-task overrides:

Record requested and actual routes when the host substitutes a model or effort.

## Concurrency and isolation

- Policy: ADAPTIVE / CEILING(N) / SUSTAINED(N)
- `N`, when applicable:
- Cost/usage constraints:
- Maximum host-supported concurrency:
- Worktree/workspace policy:
- Single-writer and shared-file ownership:
- Valid underfill constraints:

For `SUSTAINED(N)`, the Main Agent must replenish useful active slots whenever
enough compatible dependency-ready work exists. It must record, not hide, every
unavoidable `CONCURRENCY_UNDERFILLED` interval.

## Bug Hunt additions

- Area coverage map and exclusions:
- One Finder per area:
- Spec Verifier decision limit: 3
- Fix Verifier loop resource policy:
- Original reproduction requirements:
- Final Tester target environments:
- Merge and post-merge verification policy:

## Additional constraints

-
