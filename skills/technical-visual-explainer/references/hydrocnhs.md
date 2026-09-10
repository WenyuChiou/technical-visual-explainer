# HydroCNHS domain knowledge

Migrated from the two previous visual skills. Treat repository code/configuration as authoritative for implementation-specific claims; recheck relevant sources when the project changes. This reference is conditional knowledge, not a universal figure template.

## Physical story and policy boundary

Explain the selected watershed through forcing, rainfall-runoff, tributaries/subbasins, routing, reservoir/storage, and downstream flow in the order the actual configuration supports. Do not imply that every watershed uses the same topology. Reservoir cascades require routing and possible local tributary inflow between upstream outputs and downstream inputs.

HydroCNHS is a research/educational modeling framework; a small synthetic feasibility case does not make the framework itself only a demo. Do not assert fully distributed routing, real-time operations or deployment without supporting configuration evidence.

An ABM agent observes, chooses and acts. Dam, river-diversion and urban-water agents are examples, not a required complete cast. A rule policy and an LLM policy are alternatives within the decision responsibility; neither an API nor a retriever is an agent. Not every agent is an LLM.

The described Dam integration uses an in-process callback, not automatically a REST service. In the prior integration, an observation such as routed upstream inflow enters the Dam policy; a scalar release is returned for the reservoir outlet and downstream routing. In the proposed LLM route: observation/context → LLM policy → structured release proposal → deterministic validation → accepted release or fallback.

HydroCNHS retains the applicable state transition, water balance, pseudo-outlet insertion and Lohmann routing. The LLM policy does not replace these calculations. Recheck exact callback order and storage responsibility before drawing implementation notation.

## Comparisons and knowledge support

Use sibling existing-rule and LLM-policy lanes supplied by the same observation. Show the shared accepted release/interface before downstream routing. Validation and fallback must occur before an LLM proposal is applied. Do not route a raw proposal around its validator.

Optional grounding: operating manual → retriever → policy context → intended LLM decision. Mark retrieval as proposed/future unless implementation evidence exists. Retrieval neither changes model weights nor guarantees operating-rule enforcement. Keep it outside the rule lane unless that lane actually uses it.

For general explanation use “Upstream inflow”, “Reservoir state”, “Release proposal”, “Operating checks”, and “Downstream flow”. Use exact identifiers such as `release_cms` or `Dam API` only when verified and needed for that audience. No hard-coded model name is a universal whitelist.

## Sources retained for rechecking

Historical integration reference commit: `d7484fadda609a314528f6d6ab8c5e4e9a4b0c73` in `WenyuChiou/HydroCNHS`.
Relevant files: `README.md`, `src/hydrocnhs/abm.py`, `src/hydrocnhs/hydrocnhs.py`, `src/hydrocnhs/model_builder.py`.
Historical `llm_integration_review` development branch material is mutable and not proof of the current release.

Check the agent/interface distinction, parallel alternatives, validation placement, physical order and status labels on the actual generated image. Domain expert review remains distinct from visual QA.
