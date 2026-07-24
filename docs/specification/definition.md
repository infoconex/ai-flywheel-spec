# Infoconex AI Flywheel Formal Definition

## Definition

The **Infoconex AI Flywheel** is an evidence-driven operating model in which AI does not merely assist a human in performing work, but progressively builds, operates, observes, and improves the system by which the work is performed.

A human authorizes the Flywheel to operate and defines the limits of that authority. Once authorized, the AI operates on its own within those limits until it reaches a condition requiring human judgment or approval.

During execution, the system combines three operating mechanisms:

1. **Deterministic capability** for work that can be performed reliably and repeatably through code or other deterministic tools.
2. **Procedural guidance, expressed as a Standard Operating Procedure (SOP)**, for defining how work should be performed, how capabilities should be used, how known conditions should be handled, and when escalation is required.
3. **AI reasoning** for interpretation, orchestration, judgment, problem solving, ambiguity, and conditions that cannot yet be handled reliably through deterministic behavior.

These mechanisms are not sequential lifecycle stages. They work together during execution. After execution produces evidence, the Flywheel evaluates what happened, classifies what was learned, determines whether adaptation is justified, and determines where any resulting reusable learning should live.

The core cycle is:

**Execute → Observe → Evaluate → Classify → Adapt → Validate → Persist → Reuse**

Governance applies throughout that cycle. It determines whether an action is authorized, requires human approval, requires human judgment, or is prohibited.

Operational work must occur inside an authorized unit of work with enough active execution context to attribute evidence, decisions, validation, persisted learning, and reuse to the work that produced them. Before candidate adaptations are applied, activated, or persisted, applicable governance, procedural, human-defined, and validated-learning constraints must be checked.

The result is a compounding system in which evidence from repeated execution can improve the operating state, reinforce patterns that continue to work, prevent repeated failures, and challenge learning that is no longer valid. Later execution uses the current validated operating state rather than starting from the same place again.

## Human Authority and Governance

Human authority establishes the scope within which the Flywheel may operate. That authority should be expressed through a persistent **Governance Policy** defining:

- The actions the AI may perform on its own
- The changes the AI may make on its own
- Decisions requiring human approval
- Conditions requiring human judgment
- Prohibited actions
- Applicable risk or impact thresholds
- Escalation requirements

Human authority is not a fourth execution layer. It is the source of governance over the system.

The governing relationship is:

> **Human authority authorizes. Governance constrains. The SOP guides. AI reasoning orchestrates. Deterministic capability performs repeatable work.**

### Uncertainty Boundary

The AI should request human judgment when the available evidence is not enough, is contradictory, or is too unclear to support a responsible decision.

The **Uncertainty Boundary** is an evidence-based escalation boundary. Its purpose is to prevent the system from pretending to be certain when it does not know enough.

### Authority Boundary

The AI should request human approval when it can identify a preferred action or improvement but has not been given authority to make that decision or change on its own.

A core governance rule is:

> **The AI may recommend increased autonomy, but it may not grant itself increased autonomy.**

The Flywheel may become more conservative by escalating more often when unexpected risk is discovered. Expanding its authority requires human authorization.

## Runtime Responsibilities

### Governance Policy

The Governance Policy defines what the Flywheel is allowed to do and when human authority must be involved. The SOP may not override the Governance Policy.

### Standard Operating Procedure (SOP)

The SOP is the operational control plane. It defines the intended outcome, process, available capabilities, normal execution path, known exception handling, evidence expectations, validation requirements, and escalation conditions.

Where the implementation organizes work into missions, goals, tasks, or executions, the SOP must define how authorized work is selected and how execution context is established before governed operational changes begin.

### AI Reasoning

AI reasoning interprets the situation, follows and applies the SOP, orchestrates capabilities, handles ambiguity, interprets results, and determines when escalation conditions have been reached.

### Deterministic Capability

Deterministic code and tools perform stable, repeatable, testable operations when the problem is understood well enough.

For a visual explanation of these runtime relationships, see the [Core Operating Model](../architecture/operating-model.md) and [Runtime Architecture](../architecture/runtime-view.md).

## Learning and Adaptation Outcomes

After execution, observation, and evaluation, the Flywheel classifies what the evidence means and asks:

> **Is adaptation justified?**
>
> **If reusable learning should change the operating state, where should that learning live?**

When adaptation is justified, learning may become:

- A new or improved deterministic capability
- Procedural knowledge in the SOP
- Reasoning knowledge such as durable guidance, examples, heuristics, or memory
- Stronger validation
- A proposed Governance Policy change requiring human authority

Classification may also determine that no adaptation is justified. A successful or acceptable outcome may reinforce an existing validated operating pattern, or the evidence may justify no new persistent learning at all.

A failed or rejected adaptation may still produce separate reusable learning, such as a known-failure rule, applicability constraint, detection mechanism, validation check, or strategy-selection rule. The failed candidate itself does not become approved behavior merely because useful evidence was produced.

This distinction is important: deterministic capability, procedural guidance through the SOP, and AI reasoning are used **during execution**, while decisions about whether and where learning should change the persistent operating state occur **after execution produces evidence**.

Persisted learning is not permanently authoritative. Later evidence may challenge, narrow, revise, supersede, deprecate, invalidate, roll back, or retire earlier learning through the lifecycle again.

## The Moving Determinism Boundary

The boundary among deterministic capability, procedural guidance, and AI reasoning can move as the system learns.

A recurring judgment may become a procedural rule. A stable procedure may become deterministic code. A brittle deterministic rule may move back into procedure or AI reasoning when the environment is more variable than expected.

The **Moving Determinism Boundary** therefore asks:

> **Where should this responsibility live so that it is handled as reliably as possible without removing flexibility that is still needed?**

## The Two Core Structural Boundaries

The AI Flywheel manages two core structural boundaries that answer different questions. The Uncertainty Boundary described above is a separate evidence-based escalation condition.

### Moving Determinism Boundary

Determines **where work and learning belong** among deterministic capability, procedural knowledge, and AI reasoning.

### Authority Boundary

Determines **what the AI is allowed to decide, execute, change, or persist on its own**.

The determinism boundary can move as the system learns. The authority boundary is governed by humans. The uncertainty boundary determines when the available evidence is not enough for responsible AI judgment.

## Related Specification Documents

- [Specification Overview](README.md)
- [Terminology](terminology.md)
- [Principles](principles/README.md)
- [Lifecycle](lifecycle/README.md)
- [Validation Sufficiency Requirements](validation-sufficiency.md)
- [Persisted Learning Requirements](persisted-learning.md)
- [Reuse Evidence Requirements](reuse-evidence.md)
- [Learning Supersession Requirements](learning-supersession.md)
- [Conformance](conformance/README.md)
- [Architecture and Diagrams](../architecture/README.md)
- [Worked Example: Continuous Dependency Maintenance](../examples/software-maintenance/worked-example.md)

For comparative research, see the [research section](../research/README.md).
