# Task Generation Protocol — EXP-001

**Status:** protocol only; no task outputs generated yet.

## Purpose

Generate a candidate pool of mundane decision problems without exposing the generator to the experimental schema, DAE vocabulary, predicted effects, or specific latent-frame hypotheses.

## Generator brief

Generate 30 short, concrete decision problems for a general reasoning study.

Requirements:
- each problem should require a recommendation, ranking, allocation, or go/no-go decision;
- each should contain enough information for a reasonable answer without web research or specialist expertise;
- each should admit more than one plausible consideration;
- avoid philosophical dilemmas, AI consciousness/personhood, theology, metacognition, identity, and other topics strongly associated with the research programme;
- prefer ordinary domains such as operations, scheduling, procurement, community policy, product decisions, workplace process, software rollout, logistics, pricing, maintenance, event planning, and shared-resource allocation;
- vary difficulty: some decisions should be robust and straightforward, some moderately underdetermined, and some more open;
- do not label hidden issues, intended perspectives, traps, or correct answers;
- keep each task approximately 80–150 words;
- do not include instructions to consider multiple perspectives;
- output only numbered task prompts.

## Selection protocol

After generation and before any D/G/S/C experimental outputs:

1. Remove tasks requiring factual knowledge not supplied in the prompt.
2. Remove tasks with an obvious single trick or riddle-like hidden answer.
3. Remove near-duplicates.
4. Select 12 tasks spanning multiple mundane domains.
5. Designate 2 as robust controls based on a pre-output judgment that materially different framing should rarely alter the recommendation.
6. For 8 non-control tasks, independently specify one candidate latent view for the C ability-probe condition. These cues are probes, not answer keys, and will not be shown to D, G, or S.
7. Retain 2 harder/open tasks without requiring a predefined cue if useful for exploratory view generation.

## Contamination rule

The task generator must not receive:
- the minimal schema wording;
- the P1–P5 predictions;
- DAE operator names;
- examples of preferred latent frames such as hidden stakeholders, Goodhart effects, bottleneck migration, jurisdiction, or option value.

Any task generated after exposure to those materials must be marked contaminated and excluded from the frozen pilot battery.

## Provenance

Preserve:
- exact generator prompt;
- generator model/version if available;
- raw 30-task candidate output;
- exclusion/selection decisions;
- final 12-task battery;
- cue set;
- timestamps or commit order sufficient to establish that all were frozen before experimental outputs.
