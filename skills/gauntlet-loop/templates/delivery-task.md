# Delivery task contract

## Identity and authority

- Campaign/task IDs:
- Campaign kind: New Project / Feature Addition / Improvement
- Repository and base/head:
- Task brief artifact ID/hash:
- Workspace/branch and single writer:
- Main Agent, Builder, Critic, fresh closure Critic, and independent Comparator:
- Closure policy: persistent Critic sufficient / fresh closure required
- Improvement measurement policy: not applicable / task level / deferred to integration
- Requested/actual model and effort per role:
- Status/attempt:

## Objective and boundaries

- Desired task output and observable behavior:
- Stable requirement/acceptance IDs:
- Owned files/components/assets/artifacts:
- Explicit non-goals and prohibited changes:
- Unchanged-behavior boundary:
- Permissions and external-action boundaries:

## Dependencies and interfaces

- Prerequisite task/artifact IDs and hashes:
- Produced interfaces/artifacts and downstream consumers:
- Measurement parity receipt: baseline/candidate artifact IDs, environment, workload/data, config/flags, warm-up/cache state, repetitions, seed, observed values, and matched status:
- Improvement claim ledger: stable claim ID, dimension, measurement policy, state, evidence, and embedded full comparison receipt:
- Comparator receipt: anonymous labels, sealed report artifact ID/hash/verdict, blinding state, and post-seal label-mapping artifact ID:
- Shared invariants and exact values/formats:
- Shared files and integration owner:
- Ready conditions and blockers:

## Baseline and comparisons

- Baseline method, environment, observation, and artifact:
- Supplied references and frozen comparison dimensions:
- Blinding/comparator policy:
- Claimed improvement dimensions and same-method evidence required:
- Tradeoffs that must remain visible:

## Quality and evidence contract

- Applicable universal metrics:
- Deferred/integration metrics and owner:
- Owner-excluded/not-applicable metrics and justification:
- Required focused checks:
- Required real-surface/target-environment exercise:
- Required regression boundary:
- Required visual/accessibility/performance/security evidence:
- Artifact identity/hash requirements:

## Acceptance matrix

| Requirement/acceptance ID | Exact expected behavior/value | Surface/environment | Pass evidence | Integration evidence |
|---|---|---|---|---|

## Builder report ledger

- Builder status:
- Changed artifacts and complete diff/output package:
- Verification receipts:
- Baseline/comparison delta:
- Assumptions, concerns, blockers, and unavailable evidence:
- Report artifact/hash:

## Critic ledger

For every review/repair round:

- Review kind, Critic, model/effort, reviewed artifact/hash:
- Critic report artifact ID/hash:
- Contract-compliance verdict/evidence:
- Observable-correctness verdict/evidence:
- Quality/integration verdict/evidence:
- Baseline/comparison verdict/evidence, full parity receipt, Comparator report artifact ID/hash/sealed verdict, and label-mapping artifact:
- Finding IDs, kinds, statuses, and dispositions:
- Complete task verdict:
- Accepted-risk IDs and explicit owner approvals, if any:

## Closure receipt

- Closure receipt artifact ID/hash:
- Exact approved artifact ID/head/hash:
- Last mutation event ID:
- Selected persistent Critic report artifact:
- Selected fresh closure report artifact or not required:
- Receipt verdict:
- Main identity check proving every selected review targeted the same current artifact and no later mutation occurred:


## Integration handoff

- Approved artifact/head/hash:
- Requirement/evidence traceability:
- Producer/consumer checks:
- Deferred metrics/findings:
- Combiner order/conflict constraints:
- Task integration eligibility: eligible only for `TASK_APPROVED`, or `TASK_APPROVED_WITH_ACCEPTED_RISKS` when the completion contract permits residuals and every stable risk ID has explicit owner acceptance. A task requiring fresh closure is ineligible until an approved `FRESH_CLOSURE` review report is recorded.
