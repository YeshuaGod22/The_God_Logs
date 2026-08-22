# Administration Protocol — EXP-001

**Status:** pre-data protocol; frozen before candidate task generation.

## Unit of run

One run is one fresh model context receiving exactly one task under exactly one experimental condition. No run may see outputs from another condition or another run.

## Conditions

- D — Direct
- G — Generic alternatives
- S — Minimal schema
- C — Cued ability probe, only where a cue was frozen in advance

Use the exact condition language recorded in `PREREGISTRATION.md` once sealed.

## Run isolation

For every experimental output:
- start a fresh context/session where technically possible;
- provide only the condition instruction, task text, common output-format requirement, and for C only the frozen cue;
- do not provide DAE background, family terminology, experiment hypotheses, outputs from other runs, task-selection notes, or grader information;
- record model/version and configurable sampling settings where available.

If a platform cannot guarantee a fresh context, record that limitation before running and do not describe the run as context-isolated.

## Order/randomization

Before generating outputs, create a run manifest listing every required task × condition pair and assign opaque run IDs. Randomize execution order within practical platform constraints.

Do not execute all D runs, then all G runs, then all S runs as a default convenience.

For uncued/open tasks, omit C rather than inventing a cue after seeing D/G/S outputs.

## Common final-answer requirement

Each run must end with:
- Recommendation
- Confidence: 0–100
- Main reason
- Condition most likely to change recommendation

Intermediate reasoning may differ by condition and must be preserved verbatim.

## Raw preservation

Preserve every raw model response before grading or editing. Do not normalize spelling, headings, verbosity, or wording in the raw artifact.

Each raw record should include:
- opaque run ID;
- task ID;
- model/version;
- condition key stored separately from blind-grading copies;
- timestamp/order where available;
- full prompt/instructions;
- full response;
- execution anomaly if any.

## Blinding boundary

Blind-grading copies must remove condition labels and any metadata that directly reveals D/G/S/C. Do not alter substantive response content to make conditions look more similar.

The condition key must be kept separately until view extraction, semantic matching, relevance selection, and FULL-vs-ABLATED output comparison are complete for the relevant stage.

## Failure handling

A failed/truncated/malformed run may be rerun only under the preregistered exclusion rules. Preserve the failed raw run and mark the replacement relationship explicitly.

Never rerun merely because an output is weak, surprising, negative, or unhelpful to the hypothesis.

## Contamination stop rule

If any run receives information from another condition, a cue not frozen in advance, experiment hypotheses, or grader judgments, stop administration for that task and log the contamination before deciding whether the preregistered exclusion rule applies.
