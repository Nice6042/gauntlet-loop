# Delivery and Improvement campaign protocol

Use this mode when the owner explicitly asks Gauntlet Loop to create a project, add a feature, or improve an existing system. It is distinct from Bug Hunt: the work starts from an approved desired-state contract rather than discovered defect candidates.

## Pipeline

`Main Agent -> dependency-safe worktrees -> Builder -> Critic <-> Builder -> fresh task closure review when required -> Combiner -> Integration Critic <-> Combiner/Builder -> Main Review -> later waves -> fresh Final System Critic -> Main verification`

Every role follows `references/output-quality.md` and its bundled prompt. A Builder cannot approve itself. A Critic is read-only and cannot implement. Main, Combiner, and final-review roles cannot silently weaken the frozen contract.

## Campaign classification and baseline

The Main Agent classifies the campaign before planning:

- **New Project** — no existing product baseline; freeze intended behavior, architecture constraints, target surfaces, comparisons, and acceptance examples.
- **Feature Addition** — freeze the current artifact and unchanged-behavior boundary plus the new observable contract.
- **Improvement** — capture a reproducible baseline for every claimed improvement dimension before editing; a candidate is not better without demonstrated positive delta and no prohibited regression.

For supplied comparison references, freeze exactly which dimensions matter and which expression must not be copied. When fair comparison is feasible, a fresh `templates/comparison-prompt.md` Comparator receives anonymous artifact labels, the frozen dimensions, and a parity receipt; it seals its report before Main unblinds the labels. When blinding or parity is infeasible, record why and cap the comparison at `INCONCLUSIVE`; popularity, familiarity, Critic preference, or an unblinded self-comparison is not evidence.

Instantiate campaign orchestration with `templates/delivery-main-agent-prompt.md` and state with `templates/delivery-campaign-state.md`.

## Plan and task graph

The Main Agent:

1. converts the approved owner contract into stable requirement and acceptance IDs;
2. records repository/base, target environments, baseline evidence, comparisons,
   constraints, permissions, completion standard, resource/repair policy,
   task-closure and blinded-comparator policies, model/effort routes, and
   concurrency policy;
3. creates a dependency graph whose tasks have disjoint ownership or explicit serialization;
4. assigns one isolated branch/worktree or equivalent workspace and one writer per task;
5. defines interfaces, shared invariants, producer/consumer relationships, integration owner, evidence required from every task, and whether each improvement dimension is task-level or deferred to integration;
6. preflights every task against its own acceptance criteria and every task pair that shares a file, interface, asset, schema, or state transition;
7. creates the ready queue and applies `references/concurrency.md` without padding work;
8. persists the task briefs, rulings, attempts, artifacts, findings, and state transitions.

A plan is not authority to violate the owner specification. Record conflicts and Main rulings with consequence if wrong. Stop only for a genuinely unresolved owner decision, permission/safety boundary, or plan so defective that every path forward is guesswork.

After the owner approves and starts the campaign, do not pause for routine
continuation prompts. Resolve ordinary plan ambiguity with a recorded Main
Agent ruling containing the decision, reason, and cost if wrong. Stop only for
an irreversible/destructive action, a security-sensitive or external side
effect requiring authority, a genuinely blocking owner decision, or a plan
whose every remaining path is guesswork.

Use `templates/delivery-task.md` and `schemas/delivery-task.schema.json` for each sealed task.

## Builder protocol

Instantiate the Builder with `templates/builder-prompt.md`.

The Builder runs in a fresh isolated context per task and receives only the
sealed brief, required upstream artifacts/interfaces, baseline/comparison
evidence, workspace, applicable metrics, and permissions. It must inspect
existing patterns, prove its baseline where relevant, implement the smallest
complete task, exercise the real changed surface, and return a durable report
artifact.

## Model and effort routing

Use the least powerful operator-approved model that can handle each role:
mechanical isolated work may use a fast route; multi-file judgment and Critic
work use a capable route; architecture, integration, and final adjudication
use the strongest configured route. Escalate only when evidence shows task
complexity, ambiguity, or stalled progress requires it. Record requested and
actual model/effort and the reason for any substitution. Model strength never
replaces fresh context, role separation, or evidence.

Builder statuses are:

- `DONE_PENDING_REVIEW`
- `DONE_WITH_CONCERNS`
- `NEEDS_CONTEXT`
- `SPEC_CONFLICT`
- `BLOCKED`

Self-review catches omissions but never substitutes for independent review.

## Critic protocol

Instantiate a separate Critic with `templates/critic-prompt.md`. Give it the
frozen task brief, global constraints, baseline/reference artifacts, Builder
report, exact reviewed head/artifact, and complete task diff or output package.
Do not give it unsupported Builder claims as facts.

The Critic performs distinct passes:

1. **Contract compliance** — requirement and acceptance IDs, exact values,
   scope, unchanged behavior, and prohibited behavior.
2. **Observable correctness** — real behavior, edge/error/lifecycle paths,
   test-to-contract alignment, and regression boundary.
3. **Quality and integration** — applicable universal metrics, repository
   conventions, maintainability, security, performance, accessibility, and
   downstream readiness.
4. **Baseline/comparison delta** — only dimensions frozen for this task; no
   preference-based or unblinded superiority claim. Verify parity of
   baseline/candidate artifact, environment, workload/data, config/flags,
   warm-up/cache state, repetitions, and seed. Any material mismatch makes
   `sameMethod=false` and the delta `INCONCLUSIVE`.

Support/producer tasks may set improvement measurement
`DEFERRED_TO_INTEGRATION` and close without a local `BETTER` verdict when their
own acceptance and quality gates pass. The deferred dimension remains an open
system gate owned by Integration Critic/Comparator; it cannot disappear.

Every promised improvement dimension has one stable claim ID. Its claim record
travels from task plan through task/deferred state and embeds its own complete
comparison receipt. `TASK_VERIFIED` or `SYSTEM_VERIFIED` is invalid without
that claim-bound parity, observed values, sealed Comparator report/hash, label
mapping, positive verdict, and evidence. Campaign closure requires every claim
record—not merely a count or aggregate boolean—to be `SYSTEM_VERIFIED`.

Each pass produces evidence and a verdict even when it finds no gap. The
Critic emits stable findings with kind/status, metric, requirement IDs,
consequence, evidence, severity, owner, correction, tradeoff, reason, recheck
method, and closure proof. Vague polish requests and unapproved scope
expansion do not block closure.

Task verdicts are:

- `TASK_APPROVED`
- `TASK_APPROVED_WITH_ACCEPTED_RISKS`
- `TASK_REVISION_REQUIRED`
- `TASK_INCONCLUSIVE`
- `TASK_BLOCKED`

## Builder-Critic repair loop

For each finding, the Builder independently records `VERIFIED_FIXED`,
`VERIFIED_BLOCKED`, `BLOCKED_BY_MISSING_EVIDENCE`,
`FALSE_POSITIVE_WITH_PROOF`, `ACCEPTED_RISK_BY_OWNER`, or
`OUT_OF_SCOPE_ESCALATED`. A repair changes only the finding's verified cause
and required contract, reruns affected checks, and returns the complete
updated task.

The Critic re-audits the complete task after every repair. It verifies prior
findings and checks the repair diff for new breakage; it does not wander into
unrelated unchanged scope. New material breakage caused by the repair joins
the loop. Unrelated observations remain disclosed for Main triage.

Repeat under the frozen resource policy and the owner-selected maximum repair
attempts. A repair attempt is one Builder repair plus complete Critic
re-audit. At the configured cap, Main adjudicates every open finding:

- A disproven/contestable finding closes only as `FALSE_POSITIVE_WITH_PROOF`.
- A real residual finding keeps the task non-eligible unless the completion
  contract permits that residual and the owner explicitly accepts its stable
  risk ID after seeing evidence and tradeoffs; then use
  `ACCEPTED_RISK_BY_OWNER` and `TASK_APPROVED_WITH_ACCEPTED_RISKS`.
- A real unaccepted or load-bearing finding leaves `TASK_REVISION_REQUIRED`
  or `TASK_BLOCKED` and requires stop/replan.

Never silently park/close a finding or treat the cap as approval.

Repeated non-progress before the cap triggers diagnosis, re-planning, task
split, fresh Builder, stronger model/effort, specialist review, or truthful
non-success. An iteration cap never creates approval.

A task closes only when every required pass meets the configured gate,
required evidence exists, downstream contracts are ready, and the
owner-selected closure policy is satisfied. `FRESH_CLOSURE_REQUIRED` needs an
independent approved `FRESH_CLOSURE` review report for the exact artifact. A
task is integration-eligible only as `TASK_APPROVED` or
`TASK_APPROVED_WITH_ACCEPTED_RISKS` under the explicit owner-risk rule above.

Main constructs the task closure receipt only after proving that the selected
persistent review—and fresh closure review when required—both reviewed the
current Builder artifact/head/hash, and that no mutation event occurred after
the last selected review. The receipt records the exact approved artifact,
head/hash, last mutation event, selected review artifacts, and task verdict.
Any later mutation invalidates the receipt and reopens review.

## Wave integration and later waves

Use `templates/delivery-integration-roles.md` as separate Combiner, persistent
Integration Critic, and Final System Critic contexts. Use
`templates/comparison-prompt.md` for every feasible blinded comparison at task,
integration, and final-system scope; other roles consume its sealed report
rather than acting as their own comparator.

The Combiner authenticates approved task heads, Critic/closure reports,
accepted-risk receipts, and integration eligibility. It integrates in
dependency order and records every conflict. Mechanical conflicts may be
resolved only when approved semantics remain unchanged; material conflicts
route back to the owning Builder-Critic loop.

The persistent Integration Critic independently reviews the exact combined
artifact, deferred metrics and improvement dimensions, cross-task contracts,
conflict resolutions, end-to-end behavior, target surfaces, and
baseline/reference delta. It consumes sealed Comparator reports and verifies
parity/traceability; it does not replace the Comparator. Every deferred
improvement dimension must receive system-scope same-method evidence and the
configured positive delta before `improvementClaimsVerified=true`. Integration
findings use the same stable finding contract and loop through Combiner or
targeted task repair followed by complete integration re-audit.

After an integration verdict, Main compares the actual combined result with
the original owner contract. New work enters a finite later wave with sealed
tasks; integration does not become an uncontrolled patch phase.

## Final closure
Before blind final review, the persistent Integration Critic must re-audit and
approve the exact final artifact after the last repair/wave. Its report is the
persistent final-system verdict; an earlier wave artifact does not qualify.


A fresh Final System Critic first receives only the original contract, exact
final artifact/head, target environments, comparison contract, and neutral
evidence locations required to execute checks. It independently audits
requirement traceability, real output, regressions, system hard gates,
packaging/deployment/rollback, and artifact identity, then seals a blind
preliminary verdict. Only afterward does it receive rulings, prior reports,
accepted risks, and the unresolved/deferred ledger for reconciliation. Prior
agreement cannot erase contradictory observed evidence or upgrade a failed
blind hard gate.

The Main Agent then verifies the exact reviewed final artifact itself.
`COMPLETE_WITH_DISCLOSED_ACCEPTED_RISKS` additionally requires that every hard
gate permits those residuals and the owner explicitly accepts each stable risk
ID. Delivery states include:

- `COMPLETE` — every requirement and hard gate passes; blind/final Critic and Main verify the exact artifact; no accepted residual risks.
- `COMPLETE_WITH_DISCLOSED_ACCEPTED_RISKS` — the same gates pass, the completion contract permits residuals, and the owner explicitly accepts every stable risk ID.
- `PARTIAL` — a usable subset is delivered, but named approved scope remains incomplete; never present it as the requested complete deliverable.
- `INCONCLUSIVE` — a proof-critical claim cannot be decided because evidence is unavailable, conflicting, flaky, or not comparable.
- `BLOCKED_BY_CAPABILITY`, `BLOCKED_BY_PERMISSION`, or `BLOCKED_BY_DEPENDENCY` — the named blocker prevents the next required gate.
- `FAILED` — implementation or verification produced a terminal failure not represented by the blocker/resource states.
- `BUDGET_EXHAUSTED_NOT_WOWED` or `ITERATION_LIMIT_REACHED_NOT_WOWED` — the frozen resource policy ended before the completion standard.
No “improved,” “production-ready,” “Wowed,” or comparison-winning claim may exceed the frozen dimensions, target environments, tools, and observed evidence.
