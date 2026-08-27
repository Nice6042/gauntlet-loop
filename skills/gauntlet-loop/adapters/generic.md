# Generic host adapter

Map logical roles to the strongest capabilities the host actually provides.

- Main Agent: orchestration, frozen contract, task graph, escalation, global review.
- Builder: isolated implementation context/workspace where possible.
- Critic: separate fresh context; different model family preferred when available.
- Combiner: integration workspace and system-level testing.
- Integration Critic: separate integration review context.

If parallel agents are unavailable, execute ready Loop Tasks sequentially while preserving role separation. If model routing is unavailable, use fresh isolated contexts. If evidence tools are unavailable, cap the verdict honestly. Never claim capabilities the host does not expose.
