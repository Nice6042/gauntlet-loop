# Bug Hunt campaign protocol

Use this mode only when the owner explicitly asks Gauntlet Loop to find and fix bugs in an existing system. It is not the default delivery/improvement workflow.

## Pipeline

`Main Agent -> isolated area worktrees -> Finder -> Spec Verifier <-> Finder -> Fixer -> fresh Fix Verifier <-> Fixer -> Combiner -> Final Tester -> Integration Verifier -> merge -> Main Agent verification`

A role cannot approve its own output. Finder and Spec Verifier are read-only. Fixer is the only area writer. Fix Verifier is fresh and independent from both the Finder and Fixer.

## Campaign planning and isolation

The Main Agent must:

1. freeze scope, target environments, permissions, completion contract, model/effort routing, concurrency policy, and required evidence;
2. map the system into dependency-safe areas with explicit owned files, shared interfaces, test surfaces, and cross-area dependencies;
3. create one isolated branch/worktree or equivalent workspace per area;
4. assign exactly one Finder to each area and one writer at a time to each worktree;
5. reserve shared or cross-area files for the Combiner unless the area contracts assign a single integration owner;
6. create a ready queue and maintain the operator-selected concurrency policy;
7. record base commit, worktree, area owner, role/model/effort, and artifact locations.

Do not claim full-system coverage unless the area map accounts for every
in-scope component, search surface, target environment, and exclusion. Freeze
the search frontier before discovery and record later scope amendments.

## Finder protocol

The Finder inspects and exercises only its assigned area. It searches for reproducible defects in behavior, correctness, edge cases, data integrity, security, privacy, reliability, concurrency, error handling, performance, compatibility, UX, accessibility, tests, and integration contracts.

The Finder must:

1. inspect the authority for expected behavior before judging a discrepancy;
2. reproduce or otherwise prove each candidate with the strongest feasible
   evidence and classify evidence as direct, correlational, testimonial, or
   absence;
3. distinguish a defect from an enhancement, preference, unsupported
   environment, duplicate, flake, or expected behavior;
4. trace the defect backward to a gap-free causal chain, affected callers, and
   boundaries; when causality is unclear, rank falsifiable hypotheses and name
   the observation that would disprove each;
5. assign a causal fingerprint from root-cause mechanism, trigger/state,
   observable outcome, and affected contract; use locations as evidence, not
   as the deduplication key;
6. propose the smallest complete fix that removes the cause rather than
   suppressing the symptom;
7. analyze compatibility, migration, regression, security, performance, and
   interaction risks;
8. specify a check that fails for the defect and defends the repaired
   observable contract;
9. batch all area candidates into a stable finding ledger and one
   specification per candidate;
10. avoid modifying production source or tests during discovery.

Every candidate receives a stable ID. A Finder may return zero candidates; no
quota or forced finding is allowed. Preserve rejected and duplicate candidates
so later Finders do not rediscover them. Required fields are defined in
`../templates/bug-spec.md`.

## Spec Verifier protocol

A separate Spec Verifier adversarially reviews the complete candidate batch. It independently checks evidence, reproduces the behavior where feasible, traces the claimed root cause, inspects missed callers and boundaries, challenges alternatives, and determines whether the proposed repair is simple, complete, robust, and maintainable.

The Spec Verifier decides each candidate independently:

- `SPEC_APPROVED`
- `SPEC_REVISION_REQUIRED`
- `FALSE_POSITIVE`
- `DUPLICATE`
- `EXPECTED_BEHAVIOR`
- `BLOCKED_BY_MISSING_EVIDENCE`
- `INCONCLUSIVE`
- `OUT_OF_SCOPE`

A rejection must contain a stable finding ID, exact disputed claim, evidence, expected correction, and verification method. Vague preferences do not block approval.

## Three-decision specification loop

Each candidate may receive at most three Spec Verifier decisions. The initial decision counts as decision one.

For `SPEC_REVISION_REQUIRED`, `BLOCKED_BY_MISSING_EVIDENCE`, or `INCONCLUSIVE`:

1. the Finder independently verifies every challenge;
2. it repairs valid gaps or rejects invalid criticism with evidence;
3. it returns the complete updated specification and finding disposition;
4. the same Spec Verifier re-audits the complete specification;
5. `spec_review_count` increments on each verifier decision.

Approval is per specification. Previously approved specifications remain approved unless new evidence invalidates them. Only disputed specifications loop; the verifier still checks batch-level interactions.

If the third decision does not approve a specification, close it as `SPEC_REVIEW_LIMIT_REACHED`. This is a non-success state, not evidence that the bug is absent. Approved specifications proceed without waiting for unrelated unresolved specifications unless a recorded dependency requires them to remain together.

The discovery batch closes only when every candidate has a terminal specification status. Preserve false positives, duplicates, exclusions, and unresolved candidates in the ledger.

## Fixer batch protocol

One Fixer receives the complete approved batch for an area after specification review closes. Fixing as one batch exposes overlapping code paths and interaction risks that isolated per-bug patches can miss.

Before editing, the Fixer must reproduce each approved bug and validate that implementation evidence still supports the specification. It must not improvise around a materially wrong specification. Use `SPEC_INVALIDATED_DURING_IMPLEMENTATION` and return the candidate to specification review when new evidence changes the root cause or required design.

For the approved batch, the Fixer:

1. orders fixes by dependency and shared code path;
2. preserves or creates the smallest deterministic pre-fix reproduction and
   observes it fail for the intended reason where feasible;
3. implements the smallest complete root-cause corrections;
4. migrates every affected caller and removes obsolete paths;
5. adds or updates only contract-defending tests;
6. reruns each original reproduction and observes it pass, then runs focused
   tests and applicable area regression checks;
7. inspects interactions among all fixes in the batch;
8. records changed artifacts, commands, outputs, exit states, limitations, and
   per-bug proof;
9. returns the complete area result, not isolated patch excerpts.

Per-bug implementation statuses are:

- `FIX_IMPLEMENTED_PENDING_REVIEW`
- `SPEC_INVALIDATED_DURING_IMPLEMENTATION`
- `FIX_BLOCKED_BY_DEPENDENCY`
- `FIX_BLOCKED_BY_PERMISSION`
- `FIX_NOT_ATTEMPTED`

## Fresh Fix Verifier loop

After the Fixer finishes the area batch, spawn a fresh Fix Verifier that has not participated as Finder or Fixer. Give it the approved specifications, original evidence, complete diff, updated system, and test evidence. Do not give it unsupported success claims as facts.

The Fix Verifier independently:

1. reruns every feasible original reproduction;
2. verifies the root cause is removed rather than masked;
3. checks specification fidelity and every affected caller or boundary;
4. reviews the complete batch for interacting defects and partial fixes;
5. runs or inspects focused, regression, security, reliability, performance, and compatibility checks as applicable;
6. looks for unrelated changes, weakened assertions, false-positive tests, and evidence gaps;
7. assigns stable findings with severity, proof, correction, and recheck method.

The Fixer verifies every finding, repairs valid gaps or disproves invalid ones with evidence, reruns affected checks, and returns the complete updated area. The Fix Verifier then re-audits the complete area. Repeat until the configured completion contract is met or a truthful resource/blocker terminal state is reached. An iteration or cost cap never creates approval.

Per-bug review decisions include `REGRESSION_VERIFIED`, `FIX_REVISION_REQUIRED`,
`FIX_FAILED`, `INCONCLUSIVE`, and `BLOCKED`. Agreement among agents is
corroboration, not proof; severity and closure follow reproduced evidence.

Area terminal statuses include:

- `AREA_APPROVED`
- `AREA_APPROVED_WITH_UNRESOLVED_SPECS`
- `AREA_FIX_REVIEW_NOT_CLOSED`
- `AREA_BLOCKED`
- `AREA_NO_VERIFIED_BUGS`

`AREA_NO_VERIFIED_BUGS` means no bug was verified within the recorded scope and evidence; it does not prove that no bug exists.

## Combination and final verification

After every area reaches a terminal state, the Combiner creates or uses an integration workspace and:

1. verifies area commits, ledgers, approvals, unresolved items, and artifact identity;
2. integrates approved area commits in dependency order;
3. resolves conflicts without silently changing approved behavior;
4. routes material semantic conflicts back to the responsible Fixer and Fix Verifier;
5. runs cross-area and system-level checks and records integrated evidence.

A fresh Final Tester exercises the actual combined system against the original reproductions, system contracts, target environments, and regression surfaces. A separate Integration Verifier adversarially reviews the combined result, conflict resolutions, test adequacy, and unresolved ledger. Findings return to the Combiner or responsible area loop and require complete re-verification.

Merge only the integration state approved by the configured contract. The Main Agent then independently verifies the merged commit against the campaign plan, area ledgers, original reproductions, final evidence, exclusions, and unresolved states. A failed post-merge check reopens the campaign; it cannot be reported as success.

Campaign terminal states distinguish `COMPLETE_WITH_VERIFIED_FIXES`,
`CLEAN_EXHAUSTED`, `PARTIAL_COVERAGE`, `INCONCLUSIVE`, `BLOCKED`, and `FAILED`.
`CLEAN_EXHAUSTED` means the frozen search frontier was exercised and no
verified open bug remains within the recorded evidence boundary. It never means
that the system is universally bug-free.

## Non-negotiable invariants

- No Finder approves its own specification.
- No Fixer approves its own implementation.
- No unapproved specification is implemented as if validated.
- No worktree is written by concurrent agents.
- No isolated area approval implies integration approval.
- No resource limit, review limit, missing capability, or unavailable evidence becomes a pass.
- No claim of exhaustive discovery exceeds the recorded scope, tools, environments, and evidence.
