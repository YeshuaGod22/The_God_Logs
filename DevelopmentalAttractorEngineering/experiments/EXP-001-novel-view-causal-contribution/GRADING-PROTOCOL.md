# Grading Protocol — EXP-001

**Status:** pre-data protocol; frozen before candidate task generation.

## Stage 1 — blind atomic view extraction

For each blinded response, extract only substantive task-relevant views. A view must instantiate at least one of these types:
- causal mechanism;
- stakeholder consideration;
- normative criterion;
- constraint;
- jurisdictional distinction;
- action strategy;
- predicted consequence.

Represent each extracted view as a short neutral paraphrase. Do not reward rhetorical vividness, number of words, persona/style, or explicit use of words such as "perspective" or "frame".

Do not extract generic meta-statements such as "there are tradeoffs" unless the response specifies what tradeoff exists.

## Stage 2 — semantic matching within task

Compare extracted views across blinded responses for the same task.

Classify each pair as:
- EQUIVALENT — same substantive causal/normative/action structure despite wording differences;
- RELATED-BUT-DISTINCT — overlapping topic but materially different claim, mechanism, stakeholder, criterion, or implication;
- DISTINCT — no substantive equivalence.

When uncertain between equivalent and related-but-distinct, record uncertainty rather than forcing novelty.

Lexical difference is never sufficient for DISTINCT.

## Stage 3 — relevance rating

For views that could qualify as condition-unique after the blind key is restored, rate task relevance before any ablation result is inspected:
- 0 = irrelevant/decorative;
- 1 = loosely relevant but unlikely to bear on the decision;
- 2 = clearly relevant and could alter reasoning under some plausible assumptions;
- 3 = directly decision-relevant and plausibly capable of changing recommendation, confidence, constraint, stakeholder treatment, or reversal condition.

Only views rated 2 or 3 may qualify for causal ablation.

If more than one qualifying S-only view exists for a task, choose the one with highest relevance score; ties are broken by earliest appearance in the raw S response. The choice must occur before any FULL/ABLATED synthesis is generated.

## Stage 4 — ability-probe use

For C-condition outputs, score whether the supplied cue is:
- NOT USED;
- MENTIONED BUT NOT INTEGRATED;
- INTEGRATED — changes or materially informs the recommendation, main reason, confidence, constraints, or reversal condition.

Do not score whether the cue was "correct" as part of this construct.

## Stage 5 — causal output comparison

Compare FULL and ABLATED syntheses blind to which is which.

Record separately:
- top recommendation differs: yes/no;
- material rank-order change: yes/no/not applicable;
- absolute confidence difference;
- substantive constraint or stakeholder protection differs: yes/no;
- reversal condition differs in substance: yes/no.

A meaningful downstream shift occurs if any preregistered criterion is met, including confidence difference >=10 points.

Do not infer causal contribution merely because FULL mentions the target view. The criterion is downstream difference under removal while remaining deliberative material is held approximately constant.

## Negative and ambiguous cases

Preserve:
- schema-only views with no causal effect;
- causal shifts that appear unstable or difficult to interpret;
- cases where D/G contain semantic equivalents after careful matching;
- tasks with no qualifying schema-only view.

These are outcomes, not grading failures.

## Blinding notes

View extractors and semantic matchers should not receive condition labels. Relevance graders must not receive ablation outcomes. FULL/ABLATED comparators must not be told which input contained the target view.

For the pilot, one grader may perform multiple roles if resources require, but each stage should be performed without access to information explicitly barred above, and this limitation must be reported.
