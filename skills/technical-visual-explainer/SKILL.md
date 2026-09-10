---
name: technical-visual-explainer
description: Create clear research and technical explanation diagrams, including workflows, architectures, agent loops, mechanisms, comparisons, coupled systems, and progressive overview-to-detail slide sequences. Use for a diagram, README system map, or visual explanation; empirical data charts require standard plotting tools.
---

# Technical Visual Explainer

Make the relationships correct before making the picture attractive. A viewer should be able to trace what enters a component, what it does, and what happens next. Match the user's audience, purpose, references, and requested level of detail.

## Establish the brief

Inspect supplied images and relevant source material. Reuse facts and choices already given. Ask only consequential missing questions, grouped into at most three questions per exchange:

1. **Use and audience:** slide, README, paper, or teaching; prior knowledge; the one understanding the picture should produce.
2. **Structure:** process, layered architecture, mechanism, comparison, coupling, or concept relationships; single picture or progressive family; necessary detail.
3. **Appearance and constraints:** reference images, light/dark, language, aspect ratio, must-keep objects, scope and claims to avoid.

Do not re-ask known answers, impose a routine approval gate, or add a diagram family when one picture suffices. If enough is known, state the working brief and proceed. See [intake-and-patterns](references/intake-and-patterns.md) when the request is ambiguous.

## Plan the relationships

Before generation, record a compact content-and-relationship map. Use ordinary tables or prose; no mandatory API or deep schema is needed.

- For each object: stable name, actual job, input/output, parent boundary, role, and implementation status.
- For each connection: exact source, destination, relation, and condition where relevant.
- For each view: question answered, focus, visible objects, and intended reading order.

Keep conceptual roles separate: agent, method skill, tool, information source, interface, check, human actor or decision maker, physical model, and output. Name people for the actual context: researcher, applicant, reviewer, operator, or another supported role. An interface is not a decision maker. A skill name does not establish an implemented agent or orchestrator. Keep **Existing**, **Proposed**, and **Future** distinct from the visual emphasis of the current slide.

Inspect current evidence before making implementation claims. Style references are not factual sources. Do not copy their model names, counts, dates, or architecture claims into a new subject. For HydroCNHS work, read [hydrocnhs](references/hydrocnhs.md); otherwise leave its vocabulary unloaded.

## Choose the view and style

Read [visual-grammar](references/visual-grammar.md). Default to clean white with navy text, functional colors and simple filled icons, with space between connected objects. Match an explicit outline or dark reference when requested. Change appearance without changing the graph.

Color the meaningful internal icons/elements by function, not only their surrounding cards. When colored icons are requested, retain recognizable filled icons for key concepts even in a precise scientific workflow; density alone is not permission to replace them with colored boxes. Allocate space or separate overview and detail. Keep the in-image legend subordinate to the main explanation, and preserve its semantics across independently usable views. Stage identity, component role, current focus and implementation status are separate encodings. Every color, fill, fade, gradient, and emphasis must encode a recorded meaning; omit effects that carry no information. Keep overview text to short names and essential relationships, then expose operations and checks in the detail view. When extending an existing harness, preserve that foundation relationship explicitly rather than implying a second independent execution system.

- **Overview:** major boundaries, stages, handoffs, and essential dependencies. Represent all required stages without exposing every internal operation.
- **Detail:** actual inputs, work, tools, important check, branch conditions, return targets, and named output.
- **Comparison:** equal sibling alternatives, shared input and convergence only where the domain supports them.
- **Mechanism/coupling:** show the relevant physical or operational causal sequence; do not force a generic agent loop onto it.

Use concrete labels such as “Search papers”, “Compare methods”, “Research plan”, or “Source records”. Avoid generic “artifact” labels. Explain unfamiliar terms through their function. Do not shrink text to rescue a crowded layout; simplify, allocate more space, or split views while preserving necessary relationships.

## Make connected progressive views

For a sequence, read [progressive-views](references/progressive-views.md). Establish and inspect the master before producing dependent detail images. Show the master first; wait only if the user requested a review pause or a material ambiguity requires a decision.

Keep the same map, labels, stage order, icons, and reading positions. Highlight the current stage and expand it in a stable detail region. Focus fading must not mean “unimplemented”; future status needs its own explicit label. Use consecutive static slides by default.

For applicable checked loops:

- **PASS:** connect the check to the named accepted output or next operation.
- **REVISE:** connect the check through a specific correction back to the operation that must change; show the subsequent recheck.
- **HUMAN:** show the question/choice and its resume destination, or label it explicitly as waiting/stopped.

Never join all outcomes to a record/checkpoint line that appears to advance the workflow. Do not add pass/revise/human to concepts that lack those outcomes. A future stage may be explained in detail without being claimed as implemented.

## Generate and inspect

Use built-in imagegen for complete explanatory diagram images by default, following the current user preference. Use one request per distinct image, with exact short labels, edges, layout, palette, reference roles, and forbidden implications. For an image edit, inspect the target first and provide it as an edit reference. Preserve the accepted master and unchanged regions explicitly. When the user requests an editable companion while retaining imagegen, keep the generated master and add post-generation editing support; that request does not authorize replacing the main image with native drawing. An explicit request for native-only output takes precedence. Scientific data charts use plotting tools, not imagegen.

Record the tool used and only model/version information actually exposed by that tool. Do not assert a requested model was used without evidence. Save selected images in the project, not only the image cache. Keep original generated files as provenance. Do not silently fall back to another provider, CLI, or drawing method.

Inspect actual output at full resolution and intended display size. Verify every important edge against the map, all exact labels, branch order, color roles, boundaries, spacing, and legibility. Full-image generation cannot guarantee identical pixels between views; require stable meaning and recognizable layout instead.

Correct the observed defect with a targeted edit. If the desired symbol/style already exists inside the target, prefer that single target reference over adding another full page that could be mistaken for the edit target. After any local edit, verify the whole page's title, active stage, labels and branches; a correct replacement icon does not prove the correct page was edited. If the same defect persists, simplify/restructure the affected layout before another attempt. Preserve failure history; use the active environment's retry limits rather than inventing an unbounded regeneration loop. Do not accept a wrong arrow because the figure looks polished.

## Verify and hand off

For editable delivery, read [editable-companions](references/editable-companions.md). State which text, icons, modules and connectors can be edited, then test a representative modification in the target editor. A whole-page PNG in a PPTX is a reference image, not an editable workflow. Preserve the generated master and disclose reconstruction differences.

Use [acceptance-and-failures](references/acceptance-and-failures.md). Separate graph/spec checks, actual-image review, and audience feedback. Text matching and package validation cannot prove arrow correctness or comprehension.

Deliver the requested images and, when requested, a slideshow, reading cues, prompt/reference records, and concise QA findings. Use the presentation skill for file mechanics and research-talk-coach for requested talk/script work; their absence should not block a standalone diagram. Each view should have a clear pointing order and a transition to the next.

Preserve unaffected decks and project code. Keep proposals, examples, and generated figures distinguishable from empirical results. A successful example demonstrates that example, not general reliability. Do not claim listener understanding, scientific peer review, or precise timing without corresponding evidence.
