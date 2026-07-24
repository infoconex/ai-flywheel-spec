# Non-Conforming Patterns

The following patterns may contain useful elements of the Infoconex AI Flywheel but are not sufficient by themselves to satisfy the complete methodology.

## Design-Only Conformance Claims

An architecture diagram, implementation plan, configured capability, or statement that a system "supports" a required behavior does not demonstrate conformance unless observable operation shows that the behavior actually occurred as required.

## Retry-Only Loops

A loop that repeatedly retries until a task succeeds does not conform to the Infoconex AI Flywheel Specification unless it also evaluates evidence, classifies learning, changes persistent operational assets when lasting improvement is justified, and reuses those improvements.

## Memory-Only Agents

An agent that stores conversational memory does not conform unless useful learning becomes durable operational capability, procedure, reasoning guidance, validation, or governance that affects future execution.

## Source-Rewriting-Only Systems

A system that only rewrites source code does not conform if it has no intentional model for deciding whether learning belongs in code, procedure, reasoning, validation, or governance.

## Reflection Without Operational Change

An agent that reflects on failure but never changes a persistent operational asset when lasting improvement is justified does not satisfy [Principle 7: Learning Must Change a Persistent Operational Asset](../principles/07-persistent-learning.md) or [Principle 8: Improvement Must Compound Through Reuse](../principles/08-compounding-reuse.md).

## Fixed Automation Without Evolution

A deterministic automation system with no evidence-driven mechanism for learning and improving its operating model does not conform to the Infoconex AI Flywheel Specification.

## Lessons That Are Never Reused

A workflow that records lessons but does not make them available to later execution, or cannot show that relevant learning actually influenced later execution, does not satisfy [Principle 8: Improvement Must Compound Through Reuse](../principles/08-compounding-reuse.md).

## Configured Controls That Are Not Enforced

The existence of an approval mechanism, escalation path, prohibited-action list, validation step, or other control does not demonstrate conformance when observable operation shows that the control is bypassed, ignored, or not invoked when required.

## Work Outside Authorized Scope

A system that performs governed operational work, persistent operational asset changes, adaptation, validation, persistence, or closeout outside an authorized unit of work and active execution context does not satisfy the operational scope requirements. Attaching evidence to a goal, mission, or task after unrelated work has already occurred is not enough.

## Adaptation Without Constraint Checks

A system that applies, activates, or persists candidate adaptations without first checking applicable governance, human restrictions, SOP rules, protected assets, environment limits, and relevant validated learning does not satisfy the Adapt requirements.

## Unrestricted Self-Modification

A system with unrestricted self-modification and no human-defined authority boundary does not satisfy [Principle 1: Autonomy Is Bounded by Human Authority](../principles/01-human-authority.md).

## Approval for Every Action

A human-in-the-loop workflow that requires routine approval for every action does not satisfy the intended model of delegated autonomy unless those approvals are genuinely required by authority or uncertainty boundaries.

## AI as Advisor Only

A system in which AI primarily recommends actions that humans routinely execute does not satisfy [Principle 2: AI Is the Operator, Not Merely the Assistant](../principles/02-ai-as-operator.md).

## Single-Destination Learning

A system that assumes every lesson belongs in one fixed destination—such as memory, code, or prompt text—does not satisfy [Principle 6: Failure Determines Where the System Evolves](../principles/06-evolution-routing.md) unless it can intentionally determine where responsibility should reside.

## Historical Learning Treated as Current

A system that retains superseded, deprecated, invalidated, or retired learning but cannot distinguish it from current validated guidance does not satisfy the persistence and reuse requirements when that ambiguity can affect future operation.

## Related Documents

- [Conformance Index](README.md)
- [Principle-Aligned Conformance Assessments](principle-assessments.md)
- [Conformance Evaluation Checklist](evaluation-checklist.md)
