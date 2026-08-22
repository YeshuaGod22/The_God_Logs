# EXP-001 — Novel View Causal Contribution

**Status:** protocol drafting; no experimental outputs generated.

## Core question

Can a compact schema surface a materially distinct, task-relevant view that ordinary reasoning and a generic alternatives prompt do not surface, and does that view causally alter the final output?

## Minimal causal chain

1. Direct and generic-diversity baselines do not surface view V.
2. A cued baseline demonstrates that the same base model can use V when V is supplied.
3. The minimal schema surfaces V without the cue.
4. Removing V from otherwise matched deliberative material changes a prespecified downstream output.

## Planned pilot

- 12 short decision tasks.
- 8 latent-frame tasks, 2 harder/open tasks, 2 robust controls.
- Conditions: Direct (D), Generic Alternatives (G), Minimal Schema (S), Cued Ability Probe (C).
- Blind view extraction and semantic matching.
- At most one schema-only candidate view selected per task before ablation outcomes are inspected.
- Fresh synthesis with FULL versus ABLATED deliberative material.

## Minimal schema under test

1. Give your initial view.
2. Generate one materially different frame that could change the answer.
3. Keep that frame distinct and state what follows if it is right.
4. Re-answer, preserving unresolved tension if necessary.

## Scope

This pilot does not test long-term development, identity, consciousness, cross-session persistence, or cross-model inheritance. It tests a narrow causal claim about view availability during deliberation.

See `PREREGISTRATION.md` for frozen pilot rules once sealed.
