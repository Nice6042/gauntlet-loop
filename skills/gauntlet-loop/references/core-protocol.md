# Core protocol

## Shared sequence

1. Explicit owner activation and campaign-mode selection.
2. Frozen scope, quality, resource, permission, model/effort, concurrency, isolation, and evidence policy.
3. Capability discovery and truthful degradation.
4. Dependency-safe task/area graph with sealed ownership and interface contracts.
5. Operator-selected `ADAPTIVE`, `CEILING(N)`, or `SUSTAINED(N)` scheduling.
6. Independent production and adversarial-review roles.
7. Complete re-audit after verified corrections.
8. Integration in a separate workspace with system-level evidence.
9. Fresh final review and Main Agent verification.
10. Honest delivery with limitations, unresolved states, artifact identity, and resumable state.

## Delivery/Improvement mode

`Builder -> Critic -> verified repair -> complete re-audit`

Run dependency-safe Loop Tasks, combine an approved wave, run an Integration Critic, and launch later waves until the frozen completion contract closes.

## Bug Hunt mode

`Finder -> Spec Verifier <-> Finder -> Fixer -> fresh Fix Verifier <-> Fixer`

Run one isolated worktree per area. Review candidate bug specifications for at most three verifier decisions, implement approved specifications as an area batch, independently verify fixes and regressions, then use a Combiner, Final Tester, Integration Verifier, merge gate, and Main Agent post-merge verification.

Never weaken the frozen completion contract, silently expand permissions, invent work to fill concurrency, implement an unapproved bug specification, or turn resource/review exhaustion into a pass.
