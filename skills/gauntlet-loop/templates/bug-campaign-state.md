# Bug Hunt campaign state

## Frozen campaign contract

- Campaign ID:
- Repository and base commit:
- In-scope areas and exclusions:
- Target environments:
- Completion contract:
- Resource policy:
- Concurrency policy: `ADAPTIVE` / `CEILING(N)` / `SUSTAINED(N)`
- Permissions and prohibited actions:
- Required evidence:

## Role routing

| Role/task | Requested model | Requested effort | Actual model | Actual effort | Notes |
|---|---|---|---|---|---|
| Main Agent | | | | | |
| Finder | | | | | |
| Spec Verifier | | | | | |
| Fixer | | | | | |
| Fix Verifier | | | | | |
| Combiner | | | | | |
| Final Tester | | | | | |
| Integration Verifier | | | | | |
| Main final review | | | | | |

Add rows for per-area or per-task overrides.

## Area and workspace ledger

| Area ID | Scope | Branch/worktree | Base commit | Finder | Spec Verifier | Fixer | Fix Verifier | State |
|---|---|---|---|---|---|---|---|---|

## Active-agent ledger

| Task ID | Area | Role | Workspace | Model/effort | State | Started | Finished/blocker |
|---|---|---|---|---|---|---|---|

Record each `CONCURRENCY_UNDERFILLED` interval, its reason, and the event that restored or ended replenishment.

## Candidate ledger

| Bug ID | Area | Severity | Spec status | Review count | Fix status | Verification status | Evidence |
|---|---|---|---|---|---|---|---|

## Integration ledger

- Approved area commits:
- Unresolved specifications and blocked fixes:
- Integration commit/artifact:
- Conflict decisions:
- Final Tester evidence:
- Integration Verifier findings and dispositions:
- Merge commit:
- Main Agent post-merge evidence:
- Final campaign verdict:
