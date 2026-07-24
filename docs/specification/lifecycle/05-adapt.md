# Stage 5: Adapt

The Infoconex AI Flywheel creates or proposes a candidate improvement when change is justified and explicitly resolves when no adaptation is required.

## Purpose

Adaptation turns a supported classification into a concrete response.

The goal is not continuous change or maximum automation. The goal is to correct an identified weakness when change is justified while preserving stable operating behavior when the evidence does not support change.

## Required Inputs and Preconditions

Adapt requires:

- The classification produced by [Stage 4: Classify](04-classify.md)
- The selected improvement destination when adaptation is justified
- The evidence supporting the classification
- The current persistent operational assets
- The current placement of responsibility across the Moving Determinism Boundary
- The applicable Governance Policy
- Applicable constraints from human instructions, SOP rules, current validated learning, protected assets, and the authorized unit of work

Adaptation requires a supported classification. An unsupported preference for a tool, technology, prompt, code change, or other mechanism is not enough.

## Required Responsibilities

When adaptation is justified, Adapt must:

- Create or propose a concrete candidate improvement that addresses the classified weakness or learning opportunity
- Place the candidate in the improvement destination selected by classification unless new evidence shows that destination is unsuitable
- Preserve the reason and evidence supporting the candidate change
- State the expected improvement the candidate is intended to produce
- Identify enough validation intent to allow the candidate itself to be evaluated
- Keep the proposed or applied change within the applicable Governance Policy
- Check applicable constraints before applying, activating, or persisting the candidate change

When classification determines that no adaptation is justified, Adapt must explicitly record that no candidate change is required and preserve the evidence supporting continuation of the current operating pattern.

Possible adaptations include:

- Code changes
- New deterministic tools
- Changes to existing capabilities
- SOP changes
- Stronger validation
- New reusable reasoning guidance
- Movement of responsibility across the Moving Determinism Boundary
- A proposed Governance Policy change

The Flywheel should follow the Evolution Routing Rule:

> **Correct the weakness at the lowest layer capable of handling it reliably without unnecessarily removing adaptability.**

Adaptation produces a candidate change only when change is justified. It does not by itself prove that the change is correct or authorize that change for persistent use.

A no-change resolution is not a skipped Adapt stage. It is an explicit determination that no candidate adaptation is warranted by the supported classification.

## Required Outputs and Evidence

Adapt must produce one of the following:

- A concrete candidate change or proposed governance decision
- An explicit `no adaptation required` resolution identifying the operating pattern being preserved

The result must preserve:

- The reason and evidence supporting the result
- The persistent asset or responsibility placement that would be affected when a candidate change exists
- The expected improvement when a candidate change exists
- The information needed for [Stage 6: Validate](06-validate.md) to resolve the next lifecycle responsibility

## Completion Conditions

Adapt is complete when the classification has been resolved into an explicit adaptation result.

When change is justified, a concrete candidate improvement, its intended effect, and enough validation intent must be explicit.

When no change is justified, the no-change resolution and supporting evidence must be explicit. Silently doing nothing does not satisfy the stage contract.

Generating or applying a change does not by itself satisfy the lifecycle requirement for validation or persistence.

## Relationship to Adjacent Stages

Adapt consumes the classification and supporting evidence produced by [Stage 4: Classify](04-classify.md).

Its candidate improvement or explicit no-change resolution becomes the primary input to [Stage 6: Validate](06-validate.md).

## Governance Considerations

Not every adaptation may be applied autonomously.

The Governance Policy and applicable constraint gate determine whether a proposed change is:

- Authorized
- Approval Required
- Judgment Required
- Prohibited

The constraint gate must be evaluated before a candidate adaptation is applied, activated, or persisted for future use. It should account for human restrictions, protected assets, current validated learning, SOP rules, environment limits, and any other constraints applicable to the authorized unit of work.

A prohibited candidate must not be applied or persisted as approved behavior. A candidate requiring approval or judgment must stop at the applicable boundary until the required human decision is obtained and preserved as evidence.

The AI may recommend an expansion of its authority but may not grant itself additional authority.

Where approval is required before a candidate can be tested or applied in an isolated environment, the Flywheel must obtain that approval before proceeding.

## Relationships to Principles

- [Principle 6: Failure Determines Where the System Evolves](../principles/06-evolution-routing.md) defines how learning is routed to an appropriate improvement destination.
- [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](../principles/03-moving-determinism-boundary.md) allows adaptations to change where responsibility lives.
- [Principle 1: Autonomy Is Bounded by Human Authority](../principles/01-human-authority.md) constrains what the AI may change or propose on its own.
- [Principle 7: Learning Must Change a Persistent Operational Asset](../principles/07-persistent-learning.md) becomes relevant once a candidate improvement has been validated and authorized for persistence.

## Stage Navigation

- [Lifecycle Index](README.md)
- **Previous Stage:** [Stage 4: Classify](04-classify.md)
- **Next Stage:** [Stage 6: Validate](06-validate.md)

## Related Documents

- [Learning Architecture](../../architecture/learning-view.md)
- [Core Operating Model](../../architecture/operating-model.md)
- [Operational Scope and Constraint Gates](../operational-scope-and-constraint-gates.md)
