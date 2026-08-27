# Delivery campaign state

## Frozen campaign contract

- Campaign ID and kind:
- Repository/base and starting artifact:
- Scope/non-goals and unchanged-behavior boundary:
- Stable requirements and acceptance IDs:
- Target environments:
- Baseline/reference artifacts and comparison dimensions:
- Completion/resource/repair-attempt/concurrency policies:
- Permissions and prohibited actions:
- Required evidence and checkpoint location:
- Owner approval and amendments:
- Accepted-risk authority and owner approvals:

## Role routing

| Task/role | Requested model | Requested effort | Actual model | Actual effort | Reason/substitution |
|---|---|---|---|---|---|

Record routes for Main Agent, Builder default/overrides, Critic
default/overrides, fresh closure Critic, independent Comparator, Combiner,
Integration Critic, Final System Critic, and final Main review.

## Requirement and task ledger

| Requirement/acceptance ID | Owning task | Observable surface | Baseline/reference | Task evidence | Integration evidence | State |
|---|---|---|---|---|---|---|


## Improvement claim ledger

| Claim ID | Dimension | Owning task(s) | Measurement policy | State | Evidence | Embedded full comparison receipt |
|---|---|---|---|---|---|---|
Every claimed dimension stays present from plan through `SYSTEM_VERIFIED`; no
claim may disappear because it was deferred.

## Task graph and workspaces

| Task ID/attempt | Objective/output | Workspace/writer | Dependencies | Interfaces | Closure policy | Persistent Critic report/verdict | Fresh closure report/verdict | State | Reviewed artifact |
|---|---|---|---|---|---|---|---|---|---|

Task states: `PLANNED`, `BUILDING`, `DONE_PENDING_REVIEW`,
`DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `SPEC_CONFLICT`, `BLOCKED`,
`TASK_REVISION_REQUIRED`, `TASK_INCONCLUSIVE`, `TASK_BLOCKED`,
`TASK_APPROVED`, or `TASK_APPROVED_WITH_ACCEPTED_RISKS`. The accepted-risk
state must link every stable risk ID to its owner approval receipt.

## Active scheduler ledger

| Task ID/attempt | Role | Workspace | Model/effort | State | Started | Finished/blocker/approval |
|---|---|---|---|---|---|---|

Record every `CONCURRENCY_UNDERFILLED` interval with start/end, reason, retry event, and policy amendment.

Active attempt states: `QUEUED`, `RUNNABLE`, `RUNNING`, `SUCCEEDED`, `FAILED`,
`BLOCKED`, `AWAITING_APPROVAL`, or `CANCELLED`. Transitions must agree with
`schemas/delivery-campaign.schema.json`; do not use free-form success states.

## Event ledger

| Event ID | Task ID/attempt | From | To | Reason/evidence | Timestamp |
|---|---|---|---|---|---|

Attempts and rulings are append-only; never erase failed work.

## Artifact and evidence ledger

| Artifact ID/hash | Producer task/role | Repository base/head | Contents/claim | Verification state | Location |
|---|---|---|---|---|---|

## Finding and ruling ledger

| Finding/ruling ID | Scope | Kind/metric/requirement | Status | Evidence | Owner/correction/recheck | Decision/cost if wrong | Closure/risk receipt |
|---|---|---|---|---|---|---|---|

## Wave and integration ledger

| Wave | Approved task artifacts/closure reports/risk receipts | Integration head/hash | Conflicts/reroutes | Integration Critic report/verdict | Main review/evidence | Later-wave tasks |
|---|---|---|---|---|---|---|

## Task-to-wave coverage

| Task ID | Task artifact | Closure receipt | Wave ID | Integration artifact | Status |
|---|---|---|---|---|---|

Every approved task must appear exactly once or in its documented dependent
wave path before `taskWaveCoverageComplete=true`.

## Final ledger

- Final artifact/head/hash:
- Requirement-to-evidence matrix:
- Target-surface and end-to-end receipts:
- Baseline/comparison delta:
- Supplied-reference comparison coverage: every declared claim ID/dimension mapped to sealed Comparator report/hash, parity, label mapping, and verdict:
- Deferred metrics and unresolved risks:
- Structured accepted-risk receipts: stable risk ID, owner identity, approval artifact ID, evidence, and tradeoff:
- Accepted-risk coverage: every accepted finding/risk/task mapped to its owner approval artifact with `COVERED` state:
- Persistent final Integration Critic report artifact/hash and verdict:
- Blind Final System Critic preliminary verdict and report artifact/hash:
- Improvement claims verified: true / false
- Improvement claim coverage: every stable claim ID/dimension mapped to a system comparison artifact with `COVERED` state:
- System improvement comparison receipts for every task-level/deferred claim: claim ID, dimension, baseline/candidate artifact IDs, parity fields and observations, sealed Comparator report ID/hash/verdict, label mapping, positive delta, and evidence:
- Final System Critic reconciliation verdict and report artifact/hash:
- Main verification receipt for the same artifact:
- Requirements reconciled: true / false
- Deferred metrics reconciled: true / false
- Open hard findings count:
- Installation/operation/deployment/rollback:
- Final campaign verdict:

Both successful delivery verdicts require every task closure gate, wave
Integration Critic, and Main wave review approved; persistent and blind final
Critics to approve the same artifact; final reconciliation and Main
verification receipts; all requirements and deferred metrics reconciled; and
zero open hard findings. `COMPLETE` has zero accepted-risk receipts.
`COMPLETE_WITH_DISCLOSED_ACCEPTED_RISKS` additionally requires at least one
structured stable-risk owner approval receipt with evidence and tradeoff.

Non-success terminal verdicts are selected by evidence:
`PARTIAL` for a named incomplete approved scope; `INCONCLUSIVE` for
unavailable/conflicting/non-comparable proof; `BLOCKED_BY_CAPABILITY`,
`BLOCKED_BY_PERMISSION`, or `BLOCKED_BY_DEPENDENCY` for the named blocker;
`FAILED` for terminal implementation/verification failure; and the explicit
budget/iteration exhaustion states when that frozen resource boundary ends the
campaign before its standard.
