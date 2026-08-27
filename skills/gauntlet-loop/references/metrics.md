# Universal quality rubric

Every task classifies every metric as APPLICABLE, NOT_APPLICABLE, DEFERRED_TO_INTEGRATION, DEFERRED_TO_LATER_WAVE, or OWNER_EXCLUDED, with justification for non-applicable/deferred/excluded metrics.

1. Requirements fidelity
2. Functional correctness
3. Hidden edge cases
4. Regression risk
5. Code quality
6. Architecture
7. Maintainability
8. Extensibility
9. Scalability
10. Performance
11. Security
12. Privacy
13. Error handling
14. Reliability
15. Test quality and coverage
16. Visual quality
17. UX consistency
18. Accessibility
19. Asset quality
20. Originality and licensing
21. Platform compatibility
22. Deployment readiness
23. Documentation
24. Comparison against supplied references
25. Future-proofness
26. Integration readiness

Hard gates are non-compensating. A finding that blocks closure must identify the metric, observable gap, evidence/reproduction, why it matters, a concrete correction, expected benefit/trade-offs, and a verification method.

In Bug Hunt mode, map every candidate to one or more metrics. The enclosing
area task and integration review still classify all 26; candidate-level mapping
does not replace complete area/system coverage.
