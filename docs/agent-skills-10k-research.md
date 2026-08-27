# Agent-skill repository research

Snapshot: 2026-08-27

## Scope and method

Eight independent high-effort Luna scouts searched generic Agent Skills, Claude, Codex, IDE-agent ecosystems, catalogs, orchestration frameworks, and bug/debug/review workflows. Searches used GitHub repository/API/topic queries, alternate terminology, direct repository trees, and exact source files. The Main Agent deduplicated the results and cross-checked the broad `agent skills stars:>10000` query.

A repository qualifies when it had more than 10,000 stars during the snapshot and materially contained reusable skills, commands, rules, plugins, agent definitions, subagent workflows, a formal skill standard, or a concrete extension mechanism relevant to portable agent skills. General AI applications that only mention agents were excluded. Frameworks are retained only when an inspected extension/orchestration mechanism contributed a portable design lesson.

The search surfaced 96 qualifying or explicitly borderline repositories: 70 were source-inspected in depth by the scouts; 26 additional domain packs, single skills, or broad-query hits were retained for completeness but contributed little novel orchestration design. Star counts are snapshots. `~` marks a rounded GitHub UI value.

This is a query-bounded inventory, not a mathematical proof that GitHub contains no other qualifying repository. GitHub indexing, renamed repositories, private repositories, search caps, and star changes prevent that claim.

## Deduplicated inventory

| Repository | Stars | Classification |
|---|---:|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 278,463 | skills/orchestration |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 243,653 | skills/harness |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 238,670 | skill collection |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | ~237k | harness/skills |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | ~202k | host/extensions |
| [anthropics/skills](https://github.com/anthropics/skills) | 172,004 | official skills |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 168,062 | borderline prompt catalog |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 143,165 | host/plugins |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 121,711 | single skill |
| [openai/codex](https://github.com/openai/codex) | 119,130 | host/extensions |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 113,577 | skill collection |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 111,369 | skill-enabled tooling |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | ~107k | host/extensions |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | ~92.1k | plugin/tooling |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 90,204 | skill collection |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 81,352 | single skill |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 73,469 | catalog |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 69,535 | harness/plugins |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | ~68.4k | harness/plugins |
| [cline/cline](https://github.com/cline/cline) | ~67k | host/extensions |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | ~64.6k | archived workflow system |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 60,649 | framework/extensions |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 59,455 | single skill |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 57,672 | framework/skills |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | ~53.6k | host/extensions |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 53,073 | catalog |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | ~52.4k | workflow/skills |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 52,197 | catalog |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 47,375 | skill collection |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 45,839 | skill collection |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 45,528 | catalog/control plane |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 41,939 | framework/skills |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 40,668 | rules catalog |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 40,552 | framework/extensions |
| [wshobson/agents](https://github.com/wshobson/agents) | 39,185 | agents/plugins |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 38,299 | catalog/skills |
| [blader/humanizer](https://github.com/blader/humanizer) | 38,274 | single skill |
| [continuedev/continue](https://github.com/continuedev/continue) | ~35.6k | host/extensions |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 35,080 | skill collection |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 34,546 | official plugin catalog |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 32,887 | catalog |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | 32,870 | harness/skills |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 32,442 | official plugin |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 31,343 | skill collection |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 30,523 | official skill collection |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 30,422 | templates/catalog |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 29,773 | installer/registry |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 29,018 | framework/extensions |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 29,007 | framework/extensions |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,504 | framework/plugins |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | 27,519 | framework/skills |
| [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | ~27k | host/extensions |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 27,264 | single skill |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 26,385 | persistent skill |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 26,332 | framework/extensions |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 26,092 | skill authoring |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 25,714 | skill collection |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 25,401 | skill collection |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 25,067 | skill collection |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 25,008 | single skill |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 24,862 | single skill |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 24,773 | formal standard |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 24,673 | agent catalog |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 24,594 | engineering plugin |
| [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | ~24.3k | archived host/modes |
| [titanwings/distilly](https://github.com/titanwings/distilly) | 24,044 | skill authoring |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 23,940 | instruction standard |
| [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | ~23.8k | framework/plugins |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 21,621 | single skill/tool |
| [google/adk-python](https://github.com/google/adk-python) | 21,307 | framework/extensions |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | ~20.2k | plugin/tooling |
| [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | 20,141 | skill collection |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | ~20k | repair-agent config |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 19,530 | framework/extensions |
| [tanweai/pua](https://github.com/tanweai/pua) | 19,528 | single skill |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 18,960 | skill-enabled tool |
| [google/skills](https://github.com/google/skills) | 18,749 | official skills |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 17,846 | skill collection |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,647 | framework/workforce |
| [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | 16,406 | skill optimization |
| [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | 16,065 | catalog |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15,339 | review-loop skill |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 15,033 | skill security |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 14,843 | catalog |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 14,842 | skill authoring |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 14,421 | official skills |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 13,959 | skill collection |
| [qodo-ai/pr-agent](https://github.com/qodo-ai/pr-agent) | ~13k | review agent |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 12,095 | skill collection |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | 11,204 | skill collection |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 11,195 | skill collection |
| [huggingface/skills](https://github.com/huggingface/skills) | 10,964 | official skills |
| [numman-ali/openskills](https://github.com/numman-ali/openskills) | 10,716 | skill loader |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | 10,702 | loop tooling |
| [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | 10,247 | single skill |
| [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) | 10,009 | skill/hooks showcase |

## Highest-signal evidence

The strongest reusable patterns came from these exact sources:

- [`agentskills/agentskills` specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx): one self-contained skill directory, concise trigger description, shallow progressive references, and a roughly 500-line canonical body.
- [`anthropics/skills` skill creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md): positive and negative trigger evaluation, fresh-context baseline comparison, objective assertions, independent grading, and package-after-evaluation.
- [`obra/superpowers` systematic debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md): reproduce, trace, form a falsifiable hypothesis, make one root-cause correction, and obtain fresh proof before completion.
- [`anthropics/claude-code` code review command](https://github.com/anthropics/claude-code/blob/main/plugins/code-review/commands/code-review.md): parallel independent Finders followed by a separate validator for each candidate; unvalidated findings are filtered before reporting.
- [`EveryInc/compound-engineering-plugin` investigation protocol](https://github.com/EveryInc/compound-engineering-plugin/blob/main/skills/ce-debug/references/investigate.md): trace backward to the first invalid transition, distinguish verified assumptions, and require falsifiable predictions with a gap-free causal chain.
- [`github/awesome-copilot` quality playbook](https://github.com/github/awesome-copilot/blob/main/skills/quality-playbook/SKILL.md): stable bug IDs, append-only events, red/green evidence, explicit unresolved states, and reconciliation between reports and artifacts.
- [`bmad-code-org/BMAD-METHOD` review triage](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/ship/bmad-code-review/steps/step-03-triage.md): verify consequences before deduplication, recalculate severity from evidence, record every dismissal, and group only proven shared root causes.
- [`deepset-ai/haystack` async scheduler](https://github.com/deepset-ai/haystack/blob/main/haystack/core/pipeline/pipeline.py): bounded active work, wait for first completion, unlock successors, and immediately refill the priority queue.
- [`camel-ai/camel` workforce](https://github.com/camel-ai/camel/blob/master/camel/societies/workforce/workforce.py): dependency-ready, pending, in-flight, and completed sets with immediate reposting after each result.
- [`openai/openai-agents-python` run state](https://github.com/openai/openai-agents-python/blob/main/src/agents/run_state.py): versioned durable state, stable approval/tool identities, resume safety, and no blind replay of uncertain side effects.
- [`NVIDIA/SkillSpector`](https://github.com/NVIDIA/SkillSpector/blob/main/docs/ANALYSIS_RESOURCE_BOUNDS.md): static-first, bounded, fail-closed skill inspection; scanner output is evidence, not semantic certification.
- [`wshobson/agents` harness matrix](https://github.com/wshobson/agents/blob/main/docs/harnesses.md): one canonical source with explicit per-host capability loss instead of silently diverging adapters.

## Combined recommendations

### Add

1. Two explicit Gauntlet modes: Delivery/Improvement and Bug Hunt. Generic bug-fixing requests must not implicitly activate either mode.
2. Strict role separation: Finder and Spec Verifier read only; Fixer is the single area writer; a fresh Fix Verifier performs post-fix review; no role approves itself.
3. One isolated worktree per area, sealed ownership, shared-interface contracts, and Combiner ownership of unassigned cross-area files.
4. Stable bug IDs and causal fingerprints based on mechanism, trigger/state, observable outcome, and affected contract. File/line is supporting evidence, not the deduplication key.
5. A three-decision Finder–Spec-Verifier loop. Every non-approval retains evidence; the third non-approval becomes `SPEC_REVIEW_LIMIT_REACHED`, never success.
6. Batched area implementation after specification review, followed by original reproduction, focused regression evidence, fresh Fix Verifier review, combined testing, adversarial integration review, merge, and Main Agent verification.
7. Operator-controlled `ADAPTIVE`, `CEILING(N)`, and `SUSTAINED(N)` concurrency. `SUSTAINED(N)` refills a useful slot in the same orchestration turn whenever compatible runnable work exists.
8. A single Main-owned ready queue, stable task attempts, atomic state transitions, backpressure, finite wave membership, first-completion refill, and truthful `CONCURRENCY_UNDERFILLED` evidence.
9. Per-role and per-task model/effort routing with requested-versus-actual records. Model strength never substitutes for independence or proof.
10. Machine-readable bug and campaign schemas, human templates, deterministic `.skill` packaging, version parity checks, internal-reference validation, and bounded static package scanning.
11. Honest terminal states for clean scoped search, verified fixes, partial coverage, inconclusive evidence, blockers, review exhaustion, and failures.

### Improve

1. Keep `SKILL.md` below the Agent Skills progressive-disclosure guidance; load Bug Hunt, scheduler, templates, schemas, and host mappings only when needed.
2. Preserve raw reproduction evidence separately from agent summaries. Every state transition names the artifact and actor that justified it.
3. Allow zero Finder findings. Reject quotas, confidence-only confirmation, majority vote, and severity inflation by reviewer count.
4. Prefer red-on-baseline/green-on-fix proof where feasible. An unexpected baseline pass is `INCONCLUSIVE` or investigation, not a successful fix.
5. Distinguish transient/replay-safe retries from semantic review failures and unknown side effects. The latter route through roles or approval; they are not blind retries.
6. Track active, runnable, blocked, approval-waiting, and terminal tasks. Spawned, idle, parked, blocked, or waiting agents do not count toward sustained concurrency.
7. Keep adapters thin. Host tool names, model identifiers, hooks, handoff syntax, and config keys must not fork canonical semantics.
8. Add positive, near-negative, and negated activation evaluations plus behavioral scenarios for Finder non-mutation, verifier independence, deduplication, three-decision closure, continuous replenishment, dependency underfill, resume, and exact-scope cancellation.
9. Use one generated source for version and packaging metadata where host schemas permit it; validate every remaining declaration.

### Remove or reject

1. Giant always-loaded protocol files, duplicated adapter instructions, compatibility shims after clean migration, and hand-maintained counts/indexes.
2. Launch-all/await-all barriers when another dependency-ready task can run; static fan-out is not sustained concurrency.
3. Placeholder agents, duplicate investigations, mandatory findings, or artificial task splitting to display the requested `N`.
4. Finder self-confirmation, Fixer self-verification, speculative Fixers before approval, and verifier mutation.
5. File/line-only deduplication, vote-based truth, max-severity merge, arbitrary confidence/coverage/code-size thresholds, and unsupported benchmark percentages.
6. Broad inherited tool permissions, mutable remote installs, `curl | bash`, automatic external posting, production actions, and hidden telemetry.
7. Syntax/static validation presented as behavioral correctness or security certification.
8. The existing exact-commit-message release workflows that fetch an external archive, replace the repository tree, require missing `scripts/run_all.py`, and cannot validate ordinary changes. Replace them with one routine validation workflow and a separate manual, approval-gated release path.

## Decisions applied to Gauntlet Loop 1.1.0

- Kept one installable skill and added two explicit campaign modes rather than creating a second implicit skill.
- Added `references/bug-hunt-protocol.md` and `references/concurrency.md` instead of turning the canonical file into a monolith.
- Added owner intake, bug specification, campaign-state templates, and two JSON Schemas.
- Added `references/output-quality.md` and sealed prompts for Main Agent, Finder, Spec Verifier, Fixer, fresh Fix Verifier, Combiner, Final Tester, and Integration Verifier.
- Added evidence classification, three independent review lenses, assumption/falsifier audits, consequence-before-dedup triage, required output receipts, and pre-handoff self-checks.
- Added causal evidence, zero-finding honesty, three specification decisions, batched area fixes, fresh post-fix review, final testing, integration verification, and Main post-merge verification.
- Added continuous useful-work replenishment with truthful underfill, queue backpressure, failure classification, approval identity, and resume rules.
- Added deterministic local validation and `.skill` packaging as the single repository validation entry point.
- Preserved explicit activation, frozen permissions, non-compensating hard gates, no false success, and Apache-2.0 identity.

## Deferred or intentionally excluded

- Host-specific Finder/Verifier/Fixer agent files were not made canonical. They should be generated or maintained as thin adapters only when a host contract is selected and verified.
- A runtime scheduler, database, dashboard, telemetry service, or cloud orchestrator was not added. Gauntlet Loop remains a portable protocol skill; hosts supply execution primitives.
- Automatic pushes, releases, PRs, comments, issue mutations, installs, and production actions remain outside skill authority and require the applicable explicit approval.
- No skill can guarantee a perfect or universally bug-free system. The strongest defensible claim is bounded by the approved scope, searched frontier, tools, environments, and recorded evidence.
