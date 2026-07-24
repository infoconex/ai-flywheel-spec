# Stage 1: Execute

The Infoconex AI Flywheel performs operational work using the current combination of procedural guidance, AI reasoning, and deterministic capability.

## Purpose

Execution applies the current operating model of the Flywheel to real work.

The AI is the operator of the process. It follows persistent procedural guidance, invokes deterministic capabilities, reasons about context and ambiguity, and carries authorized work forward without requiring a human to perform routine operational steps.

## Required Inputs and Preconditions

Execute requires:

- An authorized goal, trigger, request, event, or unit of work
- Active execution context sufficient to attribute evidence and decisions to that unit of work
- The applicable Governance Policy
- The current Standard Operating Procedure (SOP) or other persistent procedural guidance
- Available deterministic capabilities
- Relevant reasoning knowledge and context
- The current validated operating state inherited from prior Flywheel cycles, including relevant persisted learning and validated operating patterns

The execution must begin within the authority granted by the applicable Governance Policy.

When an implementation uses explicit missions, goals, tasks, or similar work containers, the required container and execution context must be selected before governed operational changes begin.

## Required Responsibilities

Execute must:

- Perform meaningful operational work rather than only generate instructions for a human operator
- Apply deterministic capability, procedural guidance, and AI reasoning in intentional and distinguishable roles
- Follow applicable procedural guidance while retaining enough reasoning ability to handle context, ambiguity, and exceptions
- Use deterministic capabilities where reliable repeatable behavior is already available and appropriate
- Apply relevant current persisted learning and validated operating patterns when they are applicable to the execution
- Keep actions within the current Governance Policy
- Keep actions within the selected authorized unit of work and avoid representing unrelated work as part of the execution
- Produce enough operational information for later observation of what actually occurred

The three operating mechanisms are not separate lifecycle stages. A single execution may move between AI reasoning and deterministic capabilities many times while following the same procedure.

## Required Outputs and Evidence

Execute must produce or preserve an operational record that may include:

- Operational results and outputs
- State changes
- Tool and capability results
- Errors and exceptions
- Decisions and escalation events
- Validation signals generated during operation
- The active unit of work and execution context for the evidence
- Other raw events needed to determine what actually occurred

## Completion Conditions

Execute is complete when the current execution attempt has reached an observable point and enough operational information exists for Observe to determine what actually happened.

Task completion, failure, or the absence of an exception does not by itself determine whether the lifecycle is complete.

## Relationship to Adjacent Stages

Execute begins from the current validated operating state, including relevant persisted learning and validated operating patterns made available through [Stage 8: Reuse](08-reuse.md).

Its operational record becomes the primary input to [Stage 2: Observe](02-observe.md).

## Governance Considerations

Every action remains subject to the Governance Policy.

Work that has no authorized unit of work, no applicable governance, or no active execution context must not proceed as governed Flywheel execution except for limited discovery required to establish that context.

When execution reaches the Authority Boundary, the affected action must be handled according to its governance outcome: Authorized, Approval Required, or Prohibited.

When execution reaches the Uncertainty Boundary because evidence is insufficient for responsible autonomous judgment, the affected decision requires additional evidence or human judgment.

Where practical, unrelated authorized work should continue rather than stopping the entire process.

## Relationships to Principles

- [Principle 1: Autonomy Is Bounded by Human Authority](../principles/01-human-authority.md) constrains every operational action.
- [Principle 2: AI Is the Operator, Not Merely the Assistant](../principles/02-ai-as-operator.md) establishes that the AI owns execution continuity.
- [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](../principles/03-moving-determinism-boundary.md) defines how runtime responsibility is divided.
- [Principle 4: The SOP Is an Operational Control Plane](../principles/04-sop-control-plane.md) defines the persistent procedural guidance used during execution.
- [Principle 5: Execution Must Produce Outcome Evidence](../principles/05-outcome-evidence.md) requires execution to produce enough observable information for later assessment.
- [Principle 8: Improvement Must Compound Through Reuse](../principles/08-compounding-reuse.md) requires relevant current learning to influence later execution when applicable.

## Stage Navigation

- [Lifecycle Index](README.md)
- **Next Stage:** [Stage 2: Observe](02-observe.md)

## Related Documents

- [Runtime Architecture](../../architecture/runtime-view.md)
- [Core Operating Model](../../architecture/operating-model.md)
- [Operational Scope and Constraint Gates](../operational-scope-and-constraint-gates.md)
- [Reuse Evidence Requirements](../reuse-evidence.md)
