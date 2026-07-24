# Operational Scope and Constraint Gates

The Infoconex AI Flywheel must keep operational work inside an authorized scope and must check applicable constraints before adapting persistent operational assets.

## Purpose

The Flywheel improves by acting, observing, learning, and reusing validated operating state. That improvement loop depends on knowing which authorized work produced the evidence and which constraints governed the work.

Without explicit scope and constraint gates, an implementation can appear to learn while actually performing unrelated work, bypassing human restrictions, or applying changes that were never authorized for the current context.

## Authorized Operational Scope

Each execution must be tied to an authorized unit of work. The form of that unit of work may vary by implementation. Examples include:

- A mission
- A goal
- A task
- A ticket
- A runbook invocation
- A scheduled or event-triggered operation
- Another durable work item with equivalent authority and traceability

The authorized unit of work must identify the intended outcome, applicable governance, relevant procedural guidance, and enough execution context for later evidence to be attributed to the work actually performed.

When an implementation uses nested units such as missions, goals, and executions, operational work must not proceed unless the required current unit and execution context are selected and active.

## Scope Requirements

A conforming implementation must:

- Identify the authorized unit of work before operational execution begins.
- Make the applicable Governance Policy and SOP available before action is taken.
- Attribute execution evidence, validation evidence, human decisions, and persisted learning to the relevant unit of work.
- Prevent unrelated mission work, repository changes, adaptation, validation, persistence, or closeout from being represented as part of a different unit of work.
- Preserve enough context to determine which execution produced which learning or reinforcing evidence.

An implementation may perform preparatory discovery needed to identify the applicable unit of work, but it must not perform governed operational changes until the work is inside an authorized scope.

## Pre-Adaptation Constraint Gate

Before a candidate adaptation is applied, activated, or persisted for future use, the Flywheel must evaluate applicable constraints.

Constraints may come from:

- The Governance Policy
- Human instructions or restrictions
- The SOP
- Validated learning and current operating state
- Protected assets or paths
- Risk, security, compliance, cost, or execution-environment limits
- Explicit prohibitions discovered during earlier execution

The constraint gate must determine whether the candidate change is authorized, requires approval, requires human judgment, or is prohibited. A prohibited candidate must not be applied or persisted as approved behavior.

## Evidence Requirements

Evidence for operational scope and constraint gates should show:

- Which authorized unit of work was active.
- Which execution produced the evidence.
- Which constraints were checked before adaptation.
- Whether the candidate change was allowed, approval required, judgment required, or prohibited.
- Which evidence supported the constraint decision.
- Whether any human decision was required and preserved.

For a no-change path, the record should still preserve the operating pattern being continued and the evidence supporting that continuation when the result is intended to reinforce future reuse.

## Relationship to Lifecycle

- **Execute:** Work begins from an authorized unit of work and active execution context.
- **Observe and Evaluate:** Evidence remains attributable to the work that produced it.
- **Classify:** Learning is classified within the scope and constraints of the work.
- **Adapt:** Candidate changes pass through the applicable constraint gate before being applied, activated, or persisted.
- **Validate:** Validation evidence is attributed to the candidate, scope, and constraints being evaluated.
- **Persist:** Only validated and authorized learning becomes current operating state.
- **Reuse:** Later execution uses current learning only where its scope and constraints apply.

## Non-Conforming Patterns

This requirement is not satisfied when:

- Work is performed outside any authorized unit of work and later attached to a goal or mission after the fact.
- A candidate adaptation bypasses applicable human restrictions or governance constraints.
- Evidence cannot show which execution produced the learning.
- A prohibited or unvalidated change becomes current operating behavior.
- Logs or evidence are only global and cannot support review of the specific work that produced the result.

## Related Documents

- [Formal Definition](definition.md)
- [Stage 1: Execute](lifecycle/01-execute.md)
- [Stage 5: Adapt](lifecycle/05-adapt.md)
- [Principle 1: Autonomy Is Bounded by Human Authority](principles/01-human-authority.md)
- [Principle 4: The SOP Is an Operational Control Plane](principles/04-sop-control-plane.md)
- [Conformance Evaluation Checklist](conformance/evaluation-checklist.md)
