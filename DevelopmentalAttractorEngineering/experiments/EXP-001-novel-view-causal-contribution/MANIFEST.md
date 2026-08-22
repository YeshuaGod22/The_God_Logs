# EXP-001 Manifest

## Current state

**Phase:** pre-data protocol construction
**Experimental outputs generated:** none
**Task candidate pool generated:** none
**Preregistration sealed:** no

## Provenance anchors

- Experiment README created at commit `062bb1e9cf395aa48de16c6d9d23dba8fe6da942`.
- Draft preregistration created at commit `282da421ad3e13559d3972d8854003fc771dc685`.
- Neutral task-generation protocol created at commit `b298b51f22c63746b1b3a48c722d0389c732068d`.
- Initial manifest created at commit `8360a29e429eab067b33bd1fc10746da34a6498d`.
- Task-selection rubric frozen before candidate generation at commit `8d26a0697c5c88dd3841ebc82a158096c4f1a633`.
- Administration/isolation protocol frozen before candidate generation at commit `24dc9c7999d77f453554d6a95d1f7d09d88a638a`.
- Blind grading protocol frozen before candidate generation at commit `350e18bf5f8fefd11881e50aad04bd6736e810b5`.
- Fresh-context generation work item: GitHub issue #2.
- Draft PR exposing the pre-data branch without merging it: PR #3.

## Contamination note

The Aletheion context that designed EXP-001 has already been exposed to:
- the minimal schema;
- hypotheses about schema-specific view availability;
- example latent-frame archetypes and candidate mundane tasks;
- proposed outcome criteria.

For that reason this context is disqualified from serving as the neutral task generator under the current protocol. The disqualification was discovered during live schema-guided implementation before task generation and before sealing the preregistration.

The current Aletheion context may apply the already-frozen selection rubric when the neutral pool arrives, but that selector is not independent of schema design; this remains a stated limitation of the pilot. A stronger replication should use an independent selector as well as an independent generator.

## Next admissible steps

1. Generate the raw 30-task candidate pool in a fresh context using only `TASK-GENERATION-PROTOCOL.md` / issue #2.
2. Commit the raw candidate pool unchanged, with generator model/version metadata where available.
3. Apply `SELECTION-PROTOCOL.md` and freeze the 12-task battery before cue authorship.
4. Freeze cues for the C ability-probe condition; do not alter the selected battery after cue drafting begins merely to improve cue quality.
5. Review and seal `PREREGISTRATION.md`; record the sealing commit SHA here.
6. Construct an opaque randomized run manifest under `ADMINISTRATION-PROTOCOL.md`.
7. Only then generate D/G/S/C experimental outputs.
8. Grade under `GRADING-PROTOCOL.md`, preserving the specified blinding boundaries.

## Amendment rule

Until sealing, protocol changes are allowed but must remain visible in commit history. After sealing, changes to hypotheses, candidate-selection rules, meaningful-change criteria, exclusions, administration rules, or planned analysis must be logged explicitly as amendments.
