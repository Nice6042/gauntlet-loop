# Concurrency and replenishment contract

The operator chooses the campaign concurrency policy during intake. Concurrency controls useful subagents, not quality gates or permissions.

## Policies

- `ADAPTIVE` — Main Agent chooses the smallest useful active set as the ready graph changes.
- `CEILING(N)` — run up to `N` useful subagents; never exceed `N`.
- `SUSTAINED(N)` — maintain `N` useful active subagents whenever at least `N` dependency-ready, non-conflicting tasks exist. Refill a vacated slot in the same orchestration turn.

`N` is a positive integer within host, owner, cost, permission, and repository limits. The Main Agent does not count toward `N`. A subagent counts only while executing a useful assigned contract. Completed, failed, cancelled, blocked, waiting, parked, or idle agents do not count.

## Scheduler

Before execution, the Main Agent creates:

- a dependency graph;
- a priority-ordered ready queue;
- sealed task contracts and ownership boundaries;
- worktree/workspace assignments;
- per-task role, model, and effort settings;
- an active-agent ledger containing task ID, area, role, workspace, model, effort, start time, state, and blockers.

For `SUSTAINED(N)`, the Main Agent must:

1. launch `min(N, ready_count)` useful tasks initially;
2. observe completions and state transitions;
3. mark a finished or blocked agent as no longer active;
4. promote newly unblocked work;
5. immediately launch the highest-priority compatible ready task for each vacant slot;
6. continue replenishing until the campaign closes or fewer than `N` useful tasks are runnable;
7. record every underfilled interval and reason.

Plan enough genuinely independent work to use the requested parallelism, but never invent work to satisfy a number.

## Valid underfill

`SUSTAINED(N)` is a hard scheduling target, not permission to violate correctness. Fewer than `N` active agents is allowed only when documented as `CONCURRENCY_UNDERFILLED` with one or more reasons:

- fewer than `N` useful tasks remain;
- dependencies or an integration barrier block the remaining tasks;
- work overlaps a single-writer workspace or shared mutation boundary;
- the host rejects more agents or lacks the requested model/effort route;
- an owner cost, tool, permission, or side-effect boundary prevents launch;
- continuing would duplicate investigation or corrupt independent review.

The Main Agent must retry replenishment when the blocking state changes. It must never quietly downgrade `SUSTAINED(N)` to adaptive execution.

## Isolation and counting rules

- One writer at a time per branch/worktree/workspace.
- Read-only agents may inspect the same base when their scopes are disjoint and independence is preserved.
- Finder and verifier tasks may run concurrently across areas, not on the same finding when one depends on the other's output.
- A verifier waiting for a Finder handoff is not active work and does not count.
- A spawned placeholder, duplicate review, status watcher, or agent with no runnable contract does not count.
- Main Agent orchestration, Combiner integration, and required serial merge barriers may temporarily expose valid underfill.
- Never exceed a `CEILING(N)` or `SUSTAINED(N)` target to compensate for expected completion.

## Dynamic decomposition

When the ready queue falls below the sustained target, the Main Agent should
look for real safe decomposition before accepting underfill:

- split an unstarted area along stable ownership boundaries;
- separate independent test, compatibility, security, performance, or
  accessibility surfaces when they have distinct evidence contracts;
- create a targeted task for a newly proven finding;
- assign independent final-review tasks only when the completion contract
  requires them.

Do not split one coherent write set among concurrent writers, ask multiple
agents to rediscover the same bugs as padding, weaken fresh-context reviewer
independence, or start an unapproved later wave to fill slots.

## Queue control and policy changes

The Main Agent owns one ready queue with atomic task claims and stable IDs.
Finder, specification review, fix, re-verification, and integration views may
be filtered from the same ledger but cannot become conflicting sources of
truth. Apply backpressure: do not launch more discovery merely to hold `N` when
the verification or repair queue is saturated and additional findings would
reduce evidence quality.

Wave membership is finite. Dynamic findings enter the current wave only when
their dependencies and ownership fit its frozen integration cohort; otherwise
queue them for a Main-approved later wave. Integration barriers may legitimately
underfill the pool.

An operator change to policy or `N` is a timestamped campaign amendment. Raising
`N` triggers immediate safe replenishment. Lowering `N` normally stops
replenishment until active work falls within the new limit; do not destroy
valid in-flight work unless safety, cost, or explicit owner policy requires it.

## Completion, failure, retry, and resume

When full or blocked, wait for the first task to settle rather than for the
whole wave. Atomically record its attempt, evidence/error, released workspace,
and newly unblocked successors before replenishing.

Every retry creates a new attempt under the same stable task ID. Classify the
cause as transient transport, rate limit, timeout, semantic failure,
programming error, or side-effect state unknown. Only replay-safe transient
failures may be retried mechanically under the frozen resource policy.
Semantic failures return to the appropriate Finder, Verifier, Fixer, or Main
decision; unknown side effects require evidence, deduplication, or explicit
approval before replay.

Persist the ready frontier, active assignments, completed attempts, evidence,
blocked reasons, and pending approvals. An approval request has its own stable
ID and exact proposed action. Waiting-for-approval tasks do not count as active.
On resume, reconcile active leases and never rerun a completed side effect only
because its acknowledgement was lost.

## Model and effort routing

The operator may set defaults and per-task overrides for every logical role:

- Main Agent
- Builder
- Critic
- Finder
- Spec Verifier
- Fixer
- Fix Verifier
- fresh closure critic
- Combiner
- Final Tester
- Integration Verifier
- final Main-Agent review

Record requested and actual model/effort. If the host cannot honor a route, disclose the substitution before relying on its verdict. A stronger model does not remove role separation or evidence requirements.
