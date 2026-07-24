# Conformance Evaluation Checklist

Use this checklist to evaluate whether a system satisfies the Infoconex AI Flywheel Specification.

A complete conformance review must be supported by observable evidence rather than architecture labels or stated intent alone. The checklist is organized around the eight canonical principles. Lifecycle stages and governance behavior provide the operational evidence used to evaluate those principles; they do not create a separate set of conformance requirements.

Use this checklist together with [Principle-Aligned Conformance Assessments](principle-assessments.md), which defines the normative basis, expected evidence, assessment condition, and contradictory evidence for each principle.

For each principle, record:

- **Result:** Conforms, Does Not Conform, or Insufficient Evidence.
- **Evidence basis:** The concrete operational evidence supporting the result.
- **Contradictory evidence:** Material evidence that conflicts with the claimed result.
- **Unresolved gaps:** Missing evidence or uncertainty that prevents a reliable conclusion.

A configured capability is not evidence that the capability operated as required. **Insufficient Evidence is not a passing result.**

## Principle 1: Autonomy Is Bounded by Human Authority

1. Who authorized the Flywheel to operate?
2. Where are its authority boundaries defined?
3. What actions may the AI perform autonomously?
4. What actions require human approval?
5. What conditions require human judgment because available evidence is insufficient?
6. What actions are prohibited?
7. Can the AI expand its own authority, or only recommend a governance change for human approval?
8. Does observable operation show governance constraining actions as they occur?
9. Does observable operation show governance constraining persistent changes and self-improvement?
10. Can the system distinguish approval required from judgment required?
11. Is there evidence that prohibited actions are actually blocked rather than merely documented as prohibited?
12. Before adaptation is applied, activated, or persisted, is there evidence that applicable constraints were checked and enforced?

Canonical sources: [Principle 1: Autonomy Is Bounded by Human Authority](../principles/01-human-authority.md), [Infoconex AI Flywheel Lifecycle](../lifecycle/README.md#governance-applies-throughout-the-lifecycle), [Operational Scope and Constraint Gates](../operational-scope-and-constraint-gates.md), and the normative governance requirements incorporated by the specification. Supporting explanation: [Governance and Escalation](../../architecture/governance-and-escalation.md).

## Principle 2: AI Is the Operator, Not Merely the Assistant

13. Does observable execution show the AI performing meaningful operational work itself?
14. Can it continue autonomously within its delegated authority?
15. Does routine execution avoid unnecessary human handoffs?
16. When humans intervene, can the implementation show that the intervention was required by authority, uncertainty, or judgment rather than because the AI is only advisory?

Canonical sources: [Principle 2: AI Is the Operator, Not Merely the Assistant](../principles/02-ai-as-operator.md) and [Stage 1: Execute](../lifecycle/01-execute.md).

## Principle 3: Work Is Distributed Across a Moving Determinism Boundary

17. Can the system distinguish deterministic capability, procedural guidance, and AI reasoning in actual operation?
18. Is each significant responsibility intentionally placed in the mechanism best suited to own it?
19. Can evidence cause those responsibilities to move when the current allocation is no longer appropriate?
20. Can responsibility move in either direction across the Moving Determinism Boundary rather than only toward more code or automation?
21. Is there operational evidence that classification and adaptation can change responsibility placement rather than the boundary existing only as a design concept?

Canonical source: [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](../principles/03-moving-determinism-boundary.md). Relevant lifecycle evidence: [Stage 1: Execute](../lifecycle/01-execute.md), [Stage 4: Classify](../lifecycle/04-classify.md), and [Stage 5: Adapt](../lifecycle/05-adapt.md). Supporting explanation: [Runtime Architecture](../../architecture/runtime-view.md).

## Principle 4: The SOP Is an Operational Control Plane

22. Does a persistent Standard Operating Procedure (SOP) or equivalent machine-consumable procedure exist?
23. Does it define how work should be performed and how known exceptions should be handled?
24. Does it identify available capabilities, evidence expectations, validation, and escalation conditions where appropriate?
25. Does it define work-selection and execution-context rules when the implementation uses missions, goals, tasks, or equivalent work containers?
26. Is the SOP subordinate to the Governance Policy?
27. Does observable execution show the operating process actually consulting or following the SOP where applicable?
28. Can validated procedural learning change the SOP or equivalent guidance for future execution?

Canonical source: [Principle 4: The SOP Is an Operational Control Plane](../principles/04-sop-control-plane.md). Relevant lifecycle evidence includes [Stage 1: Execute](../lifecycle/01-execute.md), [Stage 5: Adapt](../lifecycle/05-adapt.md), [Operational Scope and Constraint Gates](../operational-scope-and-constraint-gates.md), [Stage 7: Persist](../lifecycle/07-persist.md), and [Stage 8: Reuse](../lifecycle/08-reuse.md).

## Principle 5: Execution Must Produce Outcome Evidence

29. Does execution produce evidence sufficient to evaluate what actually occurred?
30. Can outcomes be evaluated against intended results and success criteria?
31. Can the system distinguish verified success, failure, partial success, and unresolved uncertainty?
32. Is success independently validated where practical?
33. Are failures and unexpected results retained as learning inputs?
34. Are material human judgments and approvals preserved as evidence?
35. Is the evidence attributable enough to explain what happened and why the system reached its conclusion?
36. Does the evidence identify the authorized unit of work and execution context that produced it?
37. When a candidate improvement is validated, does the evidence address the intended outcome rather than only technical execution or task completion?
38. Is the validation evidence appropriate to the claim, risk, and intended scope of future use?
39. Are representative conditions covered when materially different operating scenarios affect the validation claim?
40. Are material regressions and unacceptable side effects checked when they are reasonably relevant to the candidate?
41. Are contradictory, incomplete, or insufficient results kept failed, uncertain, or unresolved rather than represented as successful validation?
42. Is enough validation evidence preserved to determine what was validated, against what criteria, under what conditions, and with what limitations?

Canonical sources: [Principle 5: Execution Must Produce Outcome Evidence](../principles/05-outcome-evidence.md), [Stage 2: Observe](../lifecycle/02-observe.md), [Stage 3: Evaluate](../lifecycle/03-evaluate.md), [Stage 6: Validate](../lifecycle/06-validate.md), and [Validation Sufficiency Requirements](../validation-sufficiency.md).

## Principle 6: Failure Determines Where the System Evolves

43. Can the system identify the type of weakness, uncertainty, or learning opportunity revealed by an outcome?
44. Are successful outcomes also classified when they provide evidence that an existing pattern should be reinforced or reused?
45. Can the system determine whether adaptation is justified rather than assuming every lifecycle execution must create a change?
46. Can the system determine where resulting learning should live?
47. Can learning be routed to deterministic capability, procedure, reasoning knowledge, validation, or governance as appropriate?
48. Can responsibility move across the Moving Determinism Boundary when classification shows that a different mechanism should own the behavior?
49. Does the system avoid forcing every lesson into one fixed adaptation mechanism?
50. Does observable evidence show that classification and routing decisions actually occurred rather than being inferred from the resulting artifact alone?

Canonical sources: [Principle 6: Failure Determines Where the System Evolves](../principles/06-evolution-routing.md), [Stage 3: Evaluate](../lifecycle/03-evaluate.md), [Stage 4: Classify](../lifecycle/04-classify.md), and [Stage 5: Adapt](../lifecycle/05-adapt.md).

## Principle 7: Learning Must Change a Persistent Operational Asset

51. Do validated and authorized improvements survive the current execution?
52. Can persisted learning take the operational form appropriate to what was learned rather than being limited to memory or a knowledge store?
53. Does the implementation distinguish persisted learning from raw logs, transcripts, unvalidated observations, and historical records?
54. Before an improvement is persisted for future use, can the implementation show that the applicable validation sufficiency requirements were satisfied?
55. Are validation and authorization represented as separate decisions so approval cannot substitute for evidence and validation cannot grant authority?
56. Can validated learning derived from a failed or rejected attempt persist without the failed candidate itself being represented as approved behavior?
57. On a no-change path, can reinforcing evidence be associated with an existing validated operating pattern without manufacturing a candidate adaptation?
58. Are persisted learning items identifiable and scoped to the conditions supported by their evidence and validation?
59. Is persisted learning available to the later operating process that needs it rather than merely stored somewhere?
60. Can later evidence challenge previously persisted learning through the existing lifecycle?
61. Can persisted learning be revised, superseded, deprecated, invalidated, rolled back, retired, or moved when evidence requires it?
62. Can the implementation distinguish current validated guidance from superseded, deprecated, invalidated, retired, or historical learning?
63. Does observable operation show known-invalid or superseded learning being prevented from continuing as current guidance within the affected scope?
64. Can a reviewer trace what learning was challenged, what evidence triggered the change, and what resulting state became current where that traceability is required?
65. Can a reviewer identify the specific persistent asset changed, learning item retained, operating pattern reinforced, or prior learning superseded by a learning event?

Canonical sources: [Principle 7: Learning Must Change a Persistent Operational Asset](../principles/07-persistent-learning.md), [Stage 6: Validate](../lifecycle/06-validate.md), [Validation Sufficiency Requirements](../validation-sufficiency.md), [Persisted Learning Requirements](../persisted-learning.md), [Learning Supersession Requirements](../learning-supersession.md), and [Stage 7: Persist](../lifecycle/07-persist.md).

## Principle 8: Improvement Must Compound Through Reuse

66. Do later relevant executions have access to validated and authorized persisted learning from earlier cycles?
67. Can the implementation distinguish learning that was available from learning that was actually selected, applied, invoked, or enforced?
68. When reuse is claimed, can a reviewer identify the persisted learning or validated operating pattern involved and why it was applicable?
69. Is there observable evidence showing how earlier learning influenced the later execution rather than merely existing in storage?
70. Can validated failure-derived learning cause later execution to avoid a known failure, apply a constraint, select a different strategy, or otherwise improve without promoting the failed adaptation itself?
71. Can repeated successful operation demonstrate continued reuse of an existing validated operating pattern even when no new adaptation is created?
72. Does the implementation avoid requiring irrelevant, invalid, superseded, or unauthorized learning to be applied merely to claim reuse?
73. Does reuse avoid selecting deprecated, superseded, invalidated, retired, or otherwise non-current learning as current guidance where it should no longer apply?
74. Does repeated execution reduce unnecessary repeated reasoning, repeated failure, tool exploration, or human escalation where relevant validated learning applies?
75. Does reused behavior continue to produce outcome evidence so earlier learning can be reevaluated?
76. Can a reviewer point to later behavior that changed or remained reliably improved because of learning from earlier execution?

Canonical sources: [Principle 8: Improvement Must Compound Through Reuse](../principles/08-compounding-reuse.md), [Stage 8: Reuse](../lifecycle/08-reuse.md), [Reuse Evidence Requirements](../reuse-evidence.md), and [Learning Supersession Requirements](../learning-supersession.md).

## Conformance Decision

A system conforms to this version of the Infoconex AI Flywheel Specification only when all eight principle-aligned assessments are **Conforms**, supported by objective evidence from actual operation, and the complete lifecycle behavior required by the specification is present.

A result of **Does Not Conform** or **Insufficient Evidence** for any principle prevents a complete conformance result for this version.

The checklist supports assessment against the specification. It does not create certification, endorsement, approval, or official status.

This version does not define partial or maturity-based conformance levels.

## Related Documents

- [Conformance Overview](README.md)
- [Principle-Aligned Conformance Assessments](principle-assessments.md)
- [Non-Conforming Patterns](non-conforming-patterns.md)
- [Validation Sufficiency Requirements](../validation-sufficiency.md)
- [Persisted Learning Requirements](../persisted-learning.md)
- [Reuse Evidence Requirements](../reuse-evidence.md)
- [Learning Supersession Requirements](../learning-supersession.md)
- [Formal Definition](../definition.md)
- [Principles](../principles/README.md)
- [Lifecycle](../lifecycle/README.md)
