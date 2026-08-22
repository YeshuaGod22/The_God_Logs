# Preregistration — EXP-001 Novel View Causal Contribution

**Status:** DRAFT — no experimental outputs generated.

## Question

Does a compact schema increase the spontaneous availability of materially distinct, task-relevant views relative to ordinary reasoning and a generic alternatives prompt, and do any such additional views causally alter downstream recommendations?

## Conditions

### D — Direct
Answer the task and give your recommendation.

### G — Generic alternatives
Consider several materially different perspectives before answering. Then give your recommendation.

### S — Minimal schema
1. Give your initial view.
2. Generate one materially different frame that could change the answer.
3. Keep that frame distinct and state what follows if it is right.
4. Re-answer, preserving unresolved tension if necessary.

### C — Cued ability probe
Use the Direct instruction, with one candidate latent view explicitly supplied. This condition tests whether the model can use the view when it is made available; it is not an answer key.

## Common final-answer format

- Recommendation
- Confidence: 0–100
- Main reason
- Condition most likely to change recommendation

## Task battery

Pilot target: 12 short, concrete decision problems requiring no specialist research.

Planned composition:
- 8 latent-frame tasks;
- 2 harder/open tasks;
- 2 robust controls where additional framing should ordinarily not change the answer.

Tasks must be generated without exposing the task generator to the schema wording, DAE terminology, expected effects, or candidate latent-frame taxonomy. No experimental condition outputs may be generated before the task set and cue set are frozen.

## Definition of a substantive view

A view is a semantically distinct task-relevant unit belonging to at least one of:
- causal mechanism;
- stakeholder consideration;
- normative criterion;
- constraint;
- jurisdictional distinction;
- action strategy;
- predicted consequence.

Lexical novelty alone does not count.

## Blind view extraction

Condition labels will be hidden from the view extractor. The extractor will paraphrase atomic substantive views neutrally. A separate semantic-matching pass will classify cross-condition views as equivalent, related-but-distinct, or distinct.

A candidate schema-only view V* must:
1. appear in S;
2. have no semantically equivalent view in D or G;
3. be rated task-relevant before any ablation outcome is inspected.

Pilot selection rule: select at most one V* per task: the qualifying schema-only view rated most likely to affect the recommendation by the blind relevance grader. If none qualifies, record none.

## Ability probe

For each latent-frame task, C will supply one independently frozen candidate view. Score whether the direct model coherently incorporates the supplied view into its decision. This distinguishes ability to reason with a view from spontaneous availability of that view.

## Causal ablation

For each selected V*, construct fresh synthesis inputs from S deliberative material:

- FULL: all substantive deliberative material included.
- ABLATED: V* removed while preserving the remaining material as closely as practical.

The synthesizer will not be told that a view was removed. Condition labels will be hidden from the output comparator.

A meaningful downstream change is recorded if at least one prespecified event occurs:
- top recommendation changes;
- rank ordering changes materially;
- confidence changes by at least 10 percentage points;
- a substantive constraint or stakeholder protection enters or leaves the recommendation;
- the stated condition that would reverse the recommendation changes in substance.

These outcomes will be reported separately before any composite metric is considered.

## Predictions

P1. S will surface more task-relevant distinct views than D.

P2. S will surface more task-relevant distinct views than G.

P3. Some views absent in D but used coherently in C will arise spontaneously in S.

P4. Ablating some qualifying S-only views will materially change downstream outputs.

P5. Robust-control tasks will show little gratuitous schema-induced movement.

## Pilot interpretation

This is a signal-finding pilot, not a confirmatory significance test. A pattern with several S-only task-relevant views, several corresponding FULL-versus-ABLATED changes, and stable robust controls will justify a larger preregistered repeated-run study. A weak, inconsistent, or null pattern will trigger redesign or retirement rather than automatic scale-up.

## Exclusions

Predeclare exclusions for:
- tool or model execution failure;
- truncated output that prevents grading;
- accidental disclosure of condition labels to a blind grader;
- task/cue contamination across conditions;
- malformed run lacking the common final-answer fields.

Do not exclude surprising, negative, contradictory, or embarrassing results.

## Freeze rule

Before the first experimental condition output is generated:
1. freeze the task battery and cues;
2. commit this preregistration in its sealed form;
3. record the sealing commit SHA in this experiment's manifest or README.

After sealing, changes to hypotheses, selection rules, meaningful-change criteria, or analysis rules must be logged as amendments rather than silently replacing the preregistered version.
