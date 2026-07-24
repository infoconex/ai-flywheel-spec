# Principle-Aligned Conformance Assessments

This document defines how to assess conformance against the eight canonical Infoconex AI Flywheel principles using observable evidence from actual operation.

It does not create a second set of specification requirements. Each assessment is derived from the corresponding normative principle together with the lifecycle and cross-cutting requirements that provide observable evidence of that principle in operation.

## Assessment Method

For each principle, an assessor must evaluate four things:

1. **Normative basis** — The specification requirements that define what must be true.
2. **Observable evidence** — Evidence from actual operation showing whether those requirements were exercised as required.
3. **Assessment condition** — The condition that must be satisfied for the principle to pass.
4. **Contradictory evidence** — Evidence showing that required behavior was absent, bypassed, or operated contrary to the specification.

A design document, architecture diagram, configured capability, or stated intention may support an assessment, but it does not by itself prove that required behavior occurred.

An assessor should record **Conforms**, **Does Not Conform**, or **Insufficient Evidence** for each principle. **Insufficient Evidence** is not a passing result. Complete conformance requires all eight principles to be supported by sufficient observable evidence.

The same lifecycle evidence may support multiple principles, and one principle may require evidence from multiple stages. The lifecycle is therefore evidence-producing behavior, not a second set of conformance categories.

## Principle 1: Autonomy Is Bounded by Human Authority

### Normative basis

The implementation must operate within persistent human-defined authority boundaries. The AI must not grant itself additional authority, prohibited actions must remain prohibited, required approvals must be enforced, and unresolved uncertainty requiring human judgment must be escalated appropriately.

### Observable evidence

Evidence should show, as applicable:

- The current Governance Policy or equivalent authority definition.
- Actual autonomous actions performed within delegated authority.
- Approval gates being enforced where required.
- Prohibited actions being blocked.
- Applicable constraints being checked before candidate adaptations are applied, activated, or persisted.
- Uncertainty or judgment boundaries causing escalation rather than unsupported autonomous action.
- Persistent changes being constrained by the same authority model.
- Any governance change that expands authority receiving human authorization.

### Assessment condition

This principle conforms when observable operation shows that authority boundaries actively constrain both execution and self-improvement, applicable constraints are enforced before adaptation changes the operating state, and the AI cannot bypass, redefine, or expand those boundaries on its own.

### Does not conform when

Examples include prohibited actions succeeding, required approvals being bypassed, candidate adaptations being applied without required constraint checks, unresolved judgment being treated as autonomous certainty, or the AI granting itself broader authority.

## Principle 2: AI Is the Operator, Not Merely the Assistant

### Normative basis

The AI must perform meaningful operational work and continue within delegated authority rather than merely advising a human who routinely performs the work instead.

### Observable evidence

Evidence should show:

- AI initiating or carrying out substantive operational actions.
- AI invoking capabilities, following procedure, and making permitted operational decisions.
- Routine work continuing without unnecessary human handoff.
- Human involvement occurring because governance, uncertainty, or judgment requires it rather than because the AI is only advisory.

### Assessment condition

This principle conforms when actual execution shows that the AI is the operating actor for meaningful portions of the process within its authority boundary.

### Does not conform when

The AI primarily recommends actions while humans routinely perform the operational work, or ordinary execution cannot proceed without unnecessary human intervention.

## Principle 3: Work Is Distributed Across a Moving Determinism Boundary

### Normative basis

Responsibilities must be intentionally placed among deterministic capability, procedural guidance, and AI reasoning, and evidence must be able to cause that placement to change in either direction when another mechanism becomes more appropriate.

### Observable evidence

Evidence should show:

- Distinguishable use of deterministic capability, procedural guidance, and AI reasoning.
- A reasoned basis for where significant responsibilities currently live.
- Classification and adaptation decisions that can move responsibility when evidence shows the current placement is weak or inappropriate.
- Evidence that the operating model can move responsibility toward or away from deterministic implementation when such movement is justified, without requiring that every assessment history contain an actual movement event.

### Assessment condition

This principle conforms when responsibility placement is intentional and evidence-responsive rather than fixed by architecture convention or a one-way assumption that all learning must eventually become code.

### Does not conform when

Every lesson is forced into one mechanism, the system cannot change responsibility placement when evidence requires it, or the three operating mechanisms are not meaningfully distinguishable.

## Principle 4: The SOP Is an Operational Control Plane

### Normative basis

A persistent machine-consumable Standard Operating Procedure (SOP), or equivalent procedural guidance, must direct how work is performed while remaining subordinate to the Governance Policy.

### Observable evidence

Evidence should show:

- A durable procedure available to the operating system.
- Execution actually consulting or following that procedure where applicable.
- Guidance for process flow, known conditions, capability use, evidence, validation, and escalation as appropriate to the process.
- Governance overriding or constraining procedural guidance when required.
- Work-selection and execution-context rules being followed when the implementation uses missions, goals, tasks, or equivalent work containers.
- Validated procedural learning being able to change the procedure for later execution.

### Assessment condition

This principle conforms when procedural guidance is both durable and operationally active in directing execution, including any required work-scope and execution-context rules, rather than merely existing as human documentation.

### Does not conform when

The SOP exists only as passive documentation, is not available to the operating process, is routinely ignored, allows governed work outside required active scope, or can override governance.

## Principle 5: Execution Must Produce Outcome Evidence

### Normative basis

Execution must produce observable evidence sufficient to determine what actually happened and whether the intended outcome was achieved. Validation conclusions must satisfy the applicable Validation Sufficiency Requirements.

### Observable evidence

Evidence should show:

- Observable execution results and relevant state changes.
- Evaluation against intended outcomes or success criteria.
- Distinction among verified success, failure, partial success, and unresolved uncertainty.
- Material human judgments and approvals preserved where they affect the outcome.
- Attribution of evidence to the authorized unit of work and execution context that produced it.
- Validation evidence addressing the intended claim rather than technical completion alone.
- Contradictory, incomplete, or insufficient evidence remaining unresolved rather than being represented as success.

### Assessment condition

This principle conforms when lifecycle decisions can be traced to attributable outcome evidence strong enough to support the claims being made.

### Does not conform when

Success is inferred only from model confidence, task completion, lack of an exception, or technical execution when the intended outcome is broader.

## Principle 6: Failure Determines Where the System Evolves

### Normative basis

Failures and other learning opportunities must be evaluated and classified so resulting learning is intentionally routed to the part of the operating system best suited to own it. Successful outcomes must also be classifiable when they reinforce existing validated patterns.

### Observable evidence

Evidence should show:

- Evaluation of failures, weaknesses, uncertainty, and meaningful successful outcomes.
- Explicit classification of what was learned.
- A decision about whether adaptation is justified.
- A reasoned destination for learning, such as deterministic capability, procedure, reasoning knowledge, validation, or governance.
- No-change outcomes being explicitly resolved when adaptation is not justified.
- Failure-derived learning being separated from the failed candidate itself.

### Assessment condition

This principle conforms when operational evidence shows that learning is intentionally classified and routed instead of being forced into a single improvement mechanism or discarded when no adaptation occurs.

### Does not conform when

Failures merely trigger retries, every lesson is routed to one fixed destination, successful reinforcing evidence is ignored, or the system cannot explain why learning belongs where it was persisted.

## Principle 7: Learning Must Change a Persistent Operational Asset

### Normative basis

Validated and authorized reusable learning must survive the current execution in an appropriate persistent operational form. Persisted learning must remain scoped, identifiable, available for future operation, and subject to later challenge and supersession.

### Observable evidence

Evidence should show:

- A specific durable operational asset or reinforced validated pattern associated with the learning event.
- Applicable validation and authorization before a governed improvement becomes active for future use.
- Failure-derived learning persisting separately from any failed or rejected candidate.
- Reinforcing evidence being retained without manufacturing an unnecessary adaptation.
- Applicability scope and enough traceability for later use and review.
- Current guidance being distinguishable from superseded, deprecated, invalidated, retired, or historical learning.
- Known-invalid or superseded learning no longer being treated as current guidance within the affected scope.

### Assessment condition

This principle conforms when reusable learning changes the durable operating state in a form future operation can use, and that state can later be corrected when new evidence requires it.

### Does not conform when

Learning exists only in logs or conversation history, a failed candidate is promoted as approved behavior, durable learning cannot be used later, or known-invalid learning remains active as current guidance.

## Principle 8: Improvement Must Compound Through Reuse

### Normative basis

Later relevant execution must actually use applicable current persisted learning, and observable evidence must demonstrate that the earlier learning influenced later operation.

### Observable evidence

Evidence should show:

- The persisted learning or validated operating pattern available to a later relevant execution.
- Why that learning was applicable and still current, valid, and authorized.
- How it was selected, invoked, applied, enforced, or otherwise incorporated.
- Observable influence on later behavior or continued use of an existing validated pattern.
- Failure-derived learning causing a later execution to avoid, constrain, detect, escalate, or select differently without reusing the failed candidate.
- Repeated successful operation reinforcing continued effective reuse when no new adaptation is required.
- New outcome evidence continuing to evaluate the reused operating state.

### Assessment condition

This principle conforms when later execution demonstrably benefits from relevant earlier learning instead of merely having that learning stored or retrievable.

### Does not conform when

Persisted learning is never used when relevant, availability or retrieval is treated as proof of reuse, known reusable failures are repeatedly rediscovered, or non-current learning continues to drive execution.

## Overall Conformance Decision

A complete Infoconex AI Flywheel conforms only when all eight principle-aligned assessments have sufficient evidence and the complete lifecycle behavior required by the specification is present.

A reviewer must not infer missing behavior from architecture labels, product claims, examples, or design intent. When evidence is insufficient to establish a required behavior, the assessment result is **Insufficient Evidence**, not **Conforms**.

A conformance claim is a self-assessment or independent assessment against the published specification. It is not certification, endorsement, approval, or official status granted by the specification author unless a separate certification program explicitly exists.

## Related Documents

- [Conformance Overview](README.md)
- [Conformance Evaluation Checklist](evaluation-checklist.md)
- [Non-Conforming Patterns](non-conforming-patterns.md)
- [Principles](../principles/README.md)
- [Lifecycle](../lifecycle/README.md)
- [Validation Sufficiency Requirements](../validation-sufficiency.md)
- [Persisted Learning Requirements](../persisted-learning.md)
- [Reuse Evidence Requirements](../reuse-evidence.md)
- [Learning Supersession Requirements](../learning-supersession.md)
