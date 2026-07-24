# Principle 4: The SOP Is an Operational Control Plane

The Standard Operating Procedure (SOP) is a persistent, machine-consumable guide that tells the Infoconex AI Flywheel how to perform its work.

## Purpose

The SOP is more than documentation written for a human reader. It provides durable guidance that the AI can use directly during execution and across future executions.

It gives known process behavior a stable place to live without forcing every recurring rule into code or requiring the AI to rediscover the same procedure each time.

## Requirements

A conforming implementation must satisfy these requirements:

- A persistent operational procedure or equivalent durable guidance exists.
- The procedure is directly available to the AI during operation and survives individual execution contexts.
- The procedure defines how work should be performed with enough detail to guide reliable execution.
- Where applicable, it defines intended outcomes, available capabilities, normal execution flow, known conditions and exceptions, failure handling, evidence expectations, validation requirements, and escalation conditions.
- Where applicable, it defines how authorized work is selected, how active execution context is established, and when work must stop because no authorized mission, goal, task, or equivalent unit of work is active.
- The SOP guides AI reasoning without trying to remove all judgment.
- The SOP remains subject to the Governance Policy and may not expand or override human-defined authority.
- Procedural learning can update the SOP so future executions inherit improved guidance.

## Operational Model

A useful AI Flywheel SOP may contain:

- Process objectives and success criteria
- Normal execution flow
- Available deterministic capabilities and how to use them
- Known conditions and exceptions
- Known failure-handling procedures
- Expected evidence and logging
- Work selection, execution-context, and scope rules
- Validation requirements
- Conditions requiring AI judgment
- Escalation conditions

### Relationship to AI Reasoning

The SOP guides AI reasoning but does not replace it. The AI interprets the procedure in the context of the current execution, invokes capabilities as needed, and handles situations that cannot be completely specified in advance.

A strong SOP reduces unnecessary reasoning about known behavior while preserving flexibility for situations that still require judgment.

### Relationship to Deterministic Capability

The SOP may tell the AI to invoke deterministic capabilities for work that should not be reasoned through repeatedly. As a procedure becomes stable enough for code, the SOP may shift from describing how to perform the work to describing when and why the capability should be used.

### The SOP Evolves

Execution evidence may show that the SOP is incomplete, unclear, incorrect, missing an exception or validation step, or causing unnecessary AI reasoning.

When the right correction is procedural, the SOP should be updated so future executions inherit the improved guidance.

## Lifecycle Relationship

- **Execute:** The SOP guides the process, capability use, known exception handling, evidence expectations, escalation, and any required active work context.
- **Observe and Evaluate:** Execution evidence may reveal weaknesses or unclear parts of the procedure.
- **Classify:** The Flywheel determines whether learning belongs in procedural guidance.
- **Adapt:** The SOP is changed when procedure is the right destination.
- **Validate:** Procedural changes are tested against representative scenarios or other appropriate evidence.
- **Persist and Reuse:** The improved SOP becomes durable guidance for future execution.

## Evidence of Implementation

Evidence supporting this principle may include:

- A persistent SOP, runbook, procedure, or equivalent machine-consumable operational asset
- Proof that the AI directly accesses that guidance during execution
- Documented normal paths, known exceptions, evidence expectations, validation, or escalation rules
- Execution records showing work and evidence scoped to the authorized unit of work
- Execution examples showing that known procedure is reused across separate contexts
- Examples of execution learning producing durable procedural updates

## Non-Conforming Patterns

This principle is not satisfied when:

- Process knowledge exists only in temporary conversation history
- The AI must rediscover the same known procedure on every execution
- Procedural guidance is unavailable to future operation
- The procedure is only human documentation that the operating AI does not use
- The procedure can override governance restrictions
- The operating process performs governed work outside an authorized active unit of work and attaches the evidence afterward

## Relationships to Other Principles

- [Principle 1: Autonomy Is Bounded by Human Authority](01-human-authority.md) places the Governance Policy above the SOP.
- [Principle 2: AI Is the Operator, Not Merely the Assistant](02-ai-as-operator.md) describes the AI directly using and applying the procedure.
- [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](03-moving-determinism-boundary.md) determines when responsibility should remain procedural or move elsewhere.
- [Principle 5: Execution Must Produce Outcome Evidence](05-outcome-evidence.md) supplies the evidence that can expose procedural weaknesses.
- [Principle 6: Failure Determines Where the System Evolves](06-evolution-routing.md) determines when a correction belongs in the SOP.
- [Principle 7: Learning Must Change a Persistent Operational Asset](07-persistent-learning.md) requires useful procedural learning to survive the current execution.

## Principle Navigation

- [Principles Index](README.md)
- **Previous Principle:** [Principle 3: Work Is Distributed Across a Moving Determinism Boundary](03-moving-determinism-boundary.md)
- **Next Principle:** [Principle 5: Execution Must Produce Outcome Evidence](05-outcome-evidence.md)

## Related Documents

- [Runtime Architecture](../../architecture/runtime-view.md)
- [Stage 1: Execute](../lifecycle/01-execute.md)
- [Conformance](../conformance/README.md)
