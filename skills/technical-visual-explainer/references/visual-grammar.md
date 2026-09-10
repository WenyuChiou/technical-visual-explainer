# Visual grammar and style profiles

## Default: white technical explanation

White background; navy text (#12233F); simple icons with visible flat filled color areas; thin restrained boundaries; generous whitespace. Prefer one main composition. Boxes encode actual module boundaries, not decorative dashboard widgets. No mascot robots, 3D scenes, decorative glows or decorative gradients. Outline-only styling is an explicit reference choice, not a substitute for requested filled colored icons.

| Role | Color | Additional cue |
|---|---|---|
| Agent or method skill | Purple #7652B5 | role/function label |
| Tool operation | Blue #2876C7 | tool/function label |
| Input, source, saved result | Teal #168B8A | specific information name |
| Check and passing route | Green #298550 | question and PASS |
| Correction | Orange #D86B28 | REVISE and explicit destination |
| Human actor / decision maker | Gold #B18316 | context-specific person/decision label; HUMAN only for an escalation branch |
| Platform/boundary | Navy/neutral | Existing/Proposed status text |

This is a default role palette, not a demand to use every color. For physical diagrams reserve blue for water if useful, and explicitly record the adjusted role map for the whole family. Keep critical roles stable within that family. Status and focus use labels/boundaries separately from role color.

## Meaningful color inside each module

- Apply role color to substantial visible areas of the functional icon itself, with white/neutral negative details. A colored card or thin colored outline around a white interior is insufficient for a filled-color brief. Flat solid fills do not require gradients or lighting effects. Keep labels navy for readability.
- Assign color by the represented object's function, not its stage or column. A stage can include multiple roles. Use a neutral stage boundary and a small composite icon when useful: teal papers plus blue search, or green review shield plus orange revision pen. Every colored subpart must have an identifiable meaning; a palette is not a requirement to make every icon multicolored.
- Decide whether a legend is needed. If names, recognizable icons, branch labels and local keys already explain the necessary distinctions, omit it, including on a standalone image. Functional color consistency still applies. If an otherwise unexplained color, symbol, scale or line type changes interpretation, retain the smallest local key or legend that explains it; a detached image must not depend on a previous page. Keep meanings and ordering stable when keys recur, without forcing unused entries onto every view.
- Minimize the legend's visual weight: short labels, tiny color/icon samples, no prominent heading, large enclosing card or competing full-width band. A single quiet line or local key is preferable. For a landscape diagram, about 5% of canvas height is a starting upper allocation to try, not space to fill or a universal limit. First remove redundant entries or shorten labels; never make essential text unreadable. Judge area, contrast and hierarchy at delivery size, not just height. A scientific scale or substantive feedback mapping is not expendable legend decoration.
- Preserve a requested colored-icon vocabulary in key concepts of scientific diagrams. For example, assets can use an orange house, flood hazard blue water, vulnerability a teal house/waterline, household behavior purple people, and insurance a plum policy document. Register each icon's meaning for that figure; these are examples, not a fixed domain palette. Icons sit with the concepts they identify and do not replace decision diamonds, equations or necessary labels. Avoid adding an icon to every minor predictor merely to fill space.
- Register important icon silhouettes and semantic parts, including their overview and detail instances. A document stays teal when attached to a tool; a plotting operation is blue while its saved results are teal. A correction is orange even on the main route. Distinguish a tool that inspects a file from the acceptance check that judges its findings. Do not substitute a database symbol for an execution platform.
- Record the meaning of every visual effect. A pale fill and its darker stroke may express the same category with a subordinate background. A focus outline means “this view”; status words mean Existing/Proposed/Future. Neither implies success without an actual verdict.
- Use a gradient only for a real ordered/continuous quantity or transition, with its direction and endpoints explained. For discrete module classes, use flat colors. Remove an effect if its meaning cannot be stated.
- Color must be redundant with names, shapes or labels; do not require color perception to identify an important branch. Do not add decorative colored objects unrelated to a node or connection.

For the AutoResearchAgent example, stage containers are neutral. Literature combines teal papers and blue search; topic debate uses purple reasoning bubbles; planning combines a teal plan and purple design checklist; execution/validation combines blue execution tools, teal results and a green check; plotting/writing combines blue plot and purple writing; review/revision combines green check and orange correction; records combine teal package and green completeness check. Number, name, silhouette and position identify each stage. Existing Codex uses a neutral terminal/platform symbol as the shared execution foundation. The proposed research layer specifies how that foundation is used for research, not a second runtime. This is an example registry, not a universal seven-stage template.

## Optional: dark technical explanation

Use deep navy #0C1428, light text #F1F4FA, and brighter versions of the same role colors. Preserve the graph, reading order and relative emphasis. Avoid glowing borders that obscure arrow endpoints. Do not inherit a dark reference's technical statements or promotional wording.

## Structure and lines

Choose one primary reading direction. Use direct orthogonal routes with room around arrowheads. Distinguish flow from dependency/containment/zoom using line style and a short label when needed. Within a figure, one line style must not silently carry incompatible meanings.

Prefer solid directed lines for work/data flow and clearly labeled dashed returns for correction. A dependency link such as “Uses Codex execution and tools” must land on a boundary or component it actually supports, not resemble an alternative step in the main process. Do not draw a broad horizontal bus unless a shared bus genuinely exists.

Sibling alternatives must join at a common recipient, not travel through each other. Never let an arrow terminate on text, a random panel edge, or the middle of an unrelated chain. A source-supported dependency into a named panel boundary is valid; do not invent edges into all internal nodes to make it look more explicit. If a connection would crowd the figure, change the layout while preserving its meaning.

## Text allocation: labels in the diagram, explanation outside

Use short verb/object module labels and noun output labels. Start with roughly 2–5 words for a label, adjusted for language and necessary technical meaning; this is not a rigid word cap. A node gets one primary label and only a necessary qualifier. Check questions such as “Claims supported?” and branch conditions are functional labels, not narrative prose. Preserve exact equations, units and scientific conditions when needed.

Before generation, separate exact **visible labels** from **notes/caption only**. A heading names the subject. Put takeaway sentences, teaching commentary, transition sentences and repeated architecture/scope explanations outside the diagram by default. This also applies to detail views: added detail belongs in nodes, relationships and checks. User-requested annotated teaching graphics can use concise callouts when those callouts are the intended content.

For example, “Stage 3 decides how to study the selected direction” belongs in the speaker notes; the diagram already shows the planning operations. Replace “Future extension — current case ends before execution” with a small “Future work” label on the relevant stage boundary, and explain the case limit in notes. Keep a necessary endpoint such as “Case ends at Stage 3” once, rather than repeating it across the title, output and footer. “Existing Codex harness” on the actual foundation boundary conveys the relationship without an extra explanatory footer sentence.

After rendering, inspect every visible text block: does it name an object, relation, condition, status or necessary quantity? If it merely narrates what the arrows already show, move it outside. Inspect legend salience separately: if it attracts attention before the main process, remove redundancy or simplify its treatment. Whitespace recovered by deleting prose need not be refilled.

## Reference use

When supplied, the user's AI Research Skills reference illustrates stage organization and cross-stage support. The AI Agent learning project illustrates modular boundaries, parallel branches and convergence. Preserve those design principles, not their exact counts, identifiers or claims. These historical examples are optional, not prerequisites for another user's diagram.

For each reference record: source, image role (style, topology evidence, edit target), features adopted, and features intentionally not adopted. A local path is provenance, not a required runtime dependency of this skill. The prose profiles above remain usable without the original machine.

## Prompt outline

Use case / audience / aspect ratio / one message.
Reference image roles, retained regions and accepted master.
Exact short labels and their placement.
Directed edges and branch conditions; allowed return targets and terminal waits.
Role colors, reading order, whitespace and fixed family anchors.
Scientific/software non-claims and forbidden layout implications.
Change only the identified defect when editing.
