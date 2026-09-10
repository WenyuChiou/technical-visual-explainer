# Acceptance and observed failure cases

## Three independent evidence layers

1. **Content graph:** required objects/relations, names, stages and statuses match the brief. Check conditions, unreachable objects, bypasses, false joins and exact return destinations.
2. **Actual image:** inspect every important arrow start, end and arrowhead; visible spelling; reading hierarchy; color/shape roles; cropping and overlap. Inspect at the requested destination's size. For slide-and-README delivery inspect both presentation size and the intended README width (about 900 px for the current user case); do not require unused destinations. A text file or PPT package pass proves none of these.
3. **Audience:** can a fresh listener state the input, main path, decisions and limit? Until observed, comprehension and style satisfaction remain unmeasured.

For a family, additionally compare stable navigation labels/order/positions, focus versus implementation status, recurring icons and boundary meaning. A contact sheet is useful for continuity but does not replace inspecting individual pages.

When filled colored icons are requested, inspect the actual internal color areas, not just card borders or a prompt saying “colorful”. Pick recurring objects and trace their category, silhouette and colored parts from overview to detail. Verify each standalone image includes the legend needed to decode it. Examine consecutive views at the intended screen size, including the least-emphasized stage and longest label. A screen test observes layout and navigation, not audience understanding.

## Failure record from AutoResearchAgent

| Observed problem | Prevention / acceptance question |
|---|---|
| User requested a precise workflow but received mascot/cartoon styling | Distinguish illustrative icons from narrative cartoons; inspect actual style references |
| Overview accumulated coordinator, state buses and internal decisions | Keep architecture level explicit; move operations to details without deleting stage coverage |
| Generic agent proposal obscured its Codex foundation | Show the actual existing/proposed boundary and dependency |
| Several pages behaved like unrelated diagrams | Use a stable stage registry and recurring map with one current focus |
| Literature revision line had an unclear origin | Trace from check to correction to the exact rework node |
| PASS, REVISE and HUMAN joined a checkpoint bus | Records are not a control-flow continuation; no bypass around acceptance |
| Stages 5–7 had outcome labels without clearly closed loops | Separate each detail stage and inspect each branch |
| “Accepted paper” could imply external publication | Use “Reviewed draft” or explicitly internal acceptance when intended |
| Color encoded roles, stages and future state inconsistently | Separate role, focus and implementation status |
| Removing gradients accidentally forced hollow single-color outlines | Keep flat filled color areas; remove only the unwanted lighting effect |
| Category colors were explained only in chat while exported images had no legend | Include a compact stable role legend in independently used images |
| An entire stage was assigned one color although its detail contained several roles | Neutral stage container; meaningful colored subparts and stable stage ID/name |
| A repeated module changed category because of its column or icon choice | Trace recurring semantic objects and distinguish operation, information and verdict |
| Repeated full generation changed stage names and layouts | Edit with accepted references and an exact shared registry |
| Token tests passed while arrows remained wrong | Keep text smoke checks separate from image evidence |

## Behavioral tests

Use realistic tasks with sufficient raw context, not the expected answer. Check: complete brief proceeds; missing purpose/audience triggers only relevant questions; consumer process contains no water assumptions; an empirical scatterplot uses real data/standard plotting; false branch joins are found; a future stage is not described as already implemented.

In a forward test, let an independent agent read the skill and task without the author's conclusions. Preserve the actual response and inspect its decisions. Do not replace this with hand-written “passing” fixtures. For a negative test, report the defect and why it breaks the graph, not merely a missing keyword.

Completion requires no unresolved critical semantic errors and no unreadable key labels. Record observations and remaining limitations, not unsupported self-scores. A test topic used to refine the skill is a development example, not an untouched held-out benchmark.

## Optional structural helper

`../scripts/check_graph.py` checks a small directed specification for unknown endpoints, acceptance bypasses, rework paths and unresolved human terminals. Its CLI describes the optional input fields. Use it for larger checked-loop families when a graph record already exists; it does not impose a schema on the research agent. `../evals/test_graph.py` exercises positive and deliberately broken graphs. A passing graph must still be traced against the actual image.
