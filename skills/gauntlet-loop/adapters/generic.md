# Generic host adapter

Map logical roles to the strongest capabilities the host actually provides.

- Main Agent: orchestration, frozen contract, ready queue, replenishment, escalation, and global review.
- Builder/Fixer: isolated implementation context and workspace; only one writer per workspace.
- Critic/Spec Verifier/Fix Verifier: separate read-only context; different model family preferred where available.
- Finder: read-only area investigation and evidence-backed specification.
- Combiner: separate integration workspace, conflict ownership, and system checks.
- Final Tester: fresh execution of the actual combined system and original reproductions.
- Integration Critic/Verifier: separate adversarial integration-review context.

Map every requested role, model, and effort independently. Record substitutions.

If parallel agents are unavailable, execute ready tasks sequentially while preserving role separation. If model routing is unavailable, use fresh isolated contexts. If worktrees are unavailable, use the safest equivalent isolation and retain a single writer. If evidence tools are unavailable, cap the verdict honestly.

For `SUSTAINED(N)`, replenish finished slots while useful compatible work is ready. Host limits and dependency barriers create recorded `CONCURRENCY_UNDERFILLED` states; they do not justify placeholder tasks or false compliance. Never claim capabilities the host does not expose.
