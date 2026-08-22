# Selection Protocol — EXP-001

**Status:** frozen before candidate task generation.

## Purpose

Select the 12-task pilot battery from the neutral 30-task pool without using any D/G/S/C experimental outputs and without preferentially choosing tasks because they appear especially favorable to the schema.

## Selection order

Apply these steps in order to the raw 30-task pool.

1. **Eligibility screen**
   - Exclude tasks that require factual knowledge not supplied in the prompt.
   - Exclude tasks with an obvious single trick/riddle answer.
   - Exclude malformed tasks that do not require a recommendation, ranking, allocation, or go/no-go decision.
   - Exclude near-duplicates, retaining the earlier-numbered item unless the later item is materially clearer.

2. **Domain grouping**
   Assign each eligible task one broad domain label using only the task text: operations/logistics; workplace/process; product/business; community/institutional; software/technical rollout; event/shared-resource; other.

3. **Difficulty rating**
   Before seeing any experimental outputs, rate each eligible task:
   - 1 = robust/straightforward;
   - 2 = moderately underdetermined;
   - 3 = open/highly underdetermined.

   Difficulty is about decision underdetermination, not whether a particular hidden perspective is noticeable.

4. **Battery selection**
   - Select 2 difficulty-1 tasks as robust controls.
   - Select 8 difficulty-2 tasks.
   - Select 2 difficulty-3 tasks.
   - Maximize domain spread subject to those counts.
   - Where several tasks are interchangeable under these criteria, select the lower-numbered raw task. Do not choose among ties based on anticipated schema performance.

## Cue-authoring boundary

The 12-task battery must be frozen before cues are written.

For 8 non-control tasks, one candidate cue may then be authored for the C ability-probe condition. Cue authorship is explicitly separate from task selection: no task may be added, removed, or exchanged after cues are drafted merely because a cue is easy or difficult to formulate.

Each cue must:
- state one task-relevant consideration in neutral language;
- avoid telling the model which final recommendation is correct;
- avoid DAE/schema terminology;
- be short enough to function as an ability probe rather than a second solution.

The 2 harder/open tasks may remain uncued and exploratory if no clean neutral cue is available.

## Selection provenance

Preserve:
- the raw 30-task pool unchanged;
- eligibility exclusions with a short reason;
- domain and difficulty labels for all eligible tasks;
- the deterministic/tie-break selection record;
- final selected task IDs;
- cue text and cue-author identity/context where available.

## Contamination rule

No selector may inspect D/G/S/C outputs before the battery is frozen. No cue author may inspect D/G/S/C outputs before the cue set is frozen.

The current Aletheion context is permitted to apply this frozen selection rubric after the neutral pool arrives, but its prior exposure to the schema and task-design discussion must remain recorded as a limitation. A stronger later replication should use an independent selector as well as an independent task generator.
