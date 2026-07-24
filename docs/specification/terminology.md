# Infoconex AI Flywheel Terminology

This page defines the standard terms used throughout the Infoconex AI Flywheel Specification.

The definitions are intentionally short. Detailed behavior and requirements remain in the linked specification documents.

## Infoconex AI Flywheel

The **Infoconex AI Flywheel** is an evidence-driven operating model in which AI performs work, observes outcomes, evaluates evidence, classifies what was learned and whether adaptation is justified, resolves the Adapt responsibility by creating or proposing a candidate improvement when change is justified or explicitly determining that no adaptation is required, validates learning intended for persistent future use, persists supported learning or reinforcing evidence, and reuses the current validated operating state in later execution.

See the [Formal Definition](definition.md).

## Governance Policy

A **Governance Policy** is the persistent, human-authorized definition of what the AI may decide, execute, change, and persist on its own, what requires approval or human judgment, and what is prohibited.

The Governance Policy sits above the SOP and constrains both execution and persistent changes.

See [Principle 1: Autonomy Is Bounded by Human Authority](principles/01-human-authority.md).

## Standard Operating Procedure (SOP)

A **Standard Operating Procedure (SOP)** is persistent, machine-consumable guidance that describes how work should be performed, including intended outcomes, process flow, capability use, known exceptions, evidence requirements, validation, and escalation.

Within the AI Flywheel, the SOP acts as an operational control plane but remains subject to the Governance Policy.

See [Principle 4: The SOP Is an Operational Control Plane](principles/04-sop-control-plane.md).

## Deterministic Capability

A **deterministic capability** is code, a tool, script, service, rule, workflow, or other repeatable mechanism used when work can be handled more reliably through explicit implementation than through AI reasoning.

See [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](principles/03-moving-determinism-boundary.md).

## Procedural Guidance

**Procedural guidance** is persistent knowledge that describes how work should be performed without fully turning that behavior into deterministic implementation. The SOP is the main form of procedural guidance in the AI Flywheel.

See [Principle 4: The SOP Is an Operational Control Plane](principles/04-sop-control-plane.md).

## AI Reasoning

**AI reasoning** is the interpretation, judgment, orchestration, problem solving, and contextual decision-making performed by the AI when the correct action cannot or should not be fully predetermined by code or fixed procedure.

AI reasoning may adjust execution-time behavior as context and intermediate results change. This is distinct from **Stage 5: Adapt**, which resolves a supported classification into a candidate improvement or an explicit determination that no adaptation is required.

See [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](principles/03-moving-determinism-boundary.md) and [Stage 5: Adapt](lifecycle/05-adapt.md).

## Outcome Evidence

**Outcome evidence** is observable information that is sufficient to judge what actually happened during execution and whether the intended outcome was achieved. It may include tool outputs, state changes, logs, tests, external signals, user feedback, or human decisions.

Model confidence, task completion, or the absence of an exception is not enough by itself.

See [Principle 5: Execution Must Produce Outcome Evidence](principles/05-outcome-evidence.md).

## Authorized Unit of Work

An **authorized unit of work** is the mission, goal, task, ticket, trigger, runbook invocation, or equivalent durable work item that defines what the Flywheel is allowed and expected to perform.

It provides the scope needed to select governance, apply procedural guidance, attribute evidence, and determine whether later validation, persistence, and reuse belong to the same work.

See [Operational Scope and Constraint Gates](operational-scope-and-constraint-gates.md).

## Execution Context

**Execution context** is the active operational state that ties a specific execution attempt to its authorized unit of work, applicable governance, procedural guidance, evidence, decisions, validation results, and learning outputs.

It allows reviewers and future executions to determine which work produced which evidence.

See [Stage 1: Execute](lifecycle/01-execute.md).

## Constraint Gate

A **constraint gate** is an explicit check that determines whether a proposed action or adaptation is authorized, approval required, judgment required, or prohibited before the Flywheel applies, activates, or persists the result.

Constraint gates may enforce governance policy, human restrictions, SOP rules, protected assets, environment limits, or validated learning from prior execution.

See [Operational Scope and Constraint Gates](operational-scope-and-constraint-gates.md) and [Stage 5: Adapt](lifecycle/05-adapt.md).

## Persistent Operational Asset

A **persistent operational asset** is a durable operational form through which validated learning can affect future execution. Examples include deterministic capability, code, SOP guidance, validation rules, configuration, reasoning knowledge, reusable examples, constraints, structured knowledge, failure-derived rules, and approved governance changes.

Storage alone is not enough. The validated learning must be identifiable, appropriately scoped, and available for future relevant use. Reinforcing evidence may also be durably associated with an existing validated operating pattern without creating a new adaptation.

See [Principle 7: Learning Must Change a Persistent Operational Asset](principles/07-persistent-learning.md) and [Persisted Learning Requirements](persisted-learning.md).

## Persisted Learning

**Persisted learning** is validated learning that survives the current execution in a durable operational form that can influence later relevant operation. It may represent an operational improvement, validated knowledge derived from failure or rejection, or reinforcing evidence associated with an existing validated pattern.

Raw history, unvalidated observations, or storage of a failed candidate do not by themselves become persisted learning.

See [Persisted Learning Requirements](persisted-learning.md) and [Stage 7: Persist](lifecycle/07-persist.md).

## Moving Determinism Boundary

The **Moving Determinism Boundary** determines where work and learning should live among deterministic capability, procedural guidance, and AI reasoning.

The boundary can move in either direction. Responsibility may move toward more deterministic handling as behavior becomes stable, or back toward procedure or reasoning when code becomes too brittle or the situation depends on context.

See [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](principles/03-moving-determinism-boundary.md).

## Authority Boundary

The **Authority Boundary** separates actions, decisions, and persistent changes the AI may perform on its own from those that require human approval or are prohibited.

The AI may recommend more authority but may not grant itself more authority.

See [Principle 1: Autonomy Is Bounded by Human Authority](principles/01-human-authority.md).

## Uncertainty Boundary

The **Uncertainty Boundary** is reached when the available evidence is not enough for the AI to responsibly decide what should happen, even when the AI may otherwise be allowed to act.

Crossing the uncertainty boundary requires human judgment or more evidence.

See [Principle 1: Autonomy Is Bounded by Human Authority](principles/01-human-authority.md).

## Evolution Routing

**Evolution Routing** is the process of classifying what was learned from an outcome, determining whether adaptation is justified, and selecting the part of the operating system best suited to own any resulting persistent improvement or reusable learning.

The classification may also resolve that no adaptation is required, that a successful outcome reinforces an existing validated pattern, or that no new persistent learning is justified.

The AI Flywheel uses this routing rule when a correction is required:

> **Correct the weakness at the lowest layer capable of handling it reliably without unnecessarily removing adaptability.**

See [Principle 6: Failure Determines Where the System Evolves](principles/06-evolution-routing.md).

## Validation

**Validation** is the evidence-based process of determining whether a candidate improvement or other learning intended for persistent future use is sufficiently supported for a stated claim and scope. Validation must address the intended outcome rather than only technical execution success and remains distinct from authorization.

See [Stage 6: Validate](lifecycle/06-validate.md) and [Validation Sufficiency Requirements](validation-sufficiency.md).

## Conformance

**Conformance** means showing, with objective evidence from actual operation, that an implementation satisfies the complete Infoconex AI Flywheel Specification.

The eight canonical principles provide the top-level conformance structure. Lifecycle behavior and governance provide operational evidence used to assess those principles; they do not create a second set of conformance areas. Each principle-aligned assessment resolves to **Conforms**, **Does Not Conform**, or **Insufficient Evidence**, and a complete conformance result requires sufficient evidence for all eight principles.

A conformance assessment against the specification does not by itself constitute certification, endorsement, approval, or official status.

See [Infoconex AI Flywheel Conformance](conformance/README.md) and [Principle-Aligned Conformance Assessments](conformance/principle-assessments.md).

## Related Documents

- [Infoconex AI Flywheel Specification](README.md)
- [Formal Definition](definition.md)
- [Principles](principles/README.md)
- [Lifecycle](lifecycle/README.md)
- [Validation Sufficiency Requirements](validation-sufficiency.md)
- [Persisted Learning Requirements](persisted-learning.md)
- [Reuse Evidence Requirements](reuse-evidence.md)
- [Learning Supersession Requirements](learning-supersession.md)
- [Conformance](conformance/README.md)
- [Architecture and Diagrams](../architecture/README.md)
