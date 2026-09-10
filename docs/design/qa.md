# Cover and package checks

Checked on 2026-09-10. These records describe this repository's development
examples, not a benchmark of general drawing reliability.

## Cover inspection

The three selected generated originals were inspected at full resolution.
The English and Traditional Chinese README covers were then displayed inside
locally rendered README pages at **900 x 450 CSS pixels**. The English size was
confirmed from the browser's image geometry; the Chinese page uses the same
900px article and 2:1 image. The Social preview was displayed at **640 x 320**
and **320 x 160**; browser geometry confirmed both dimensions plus their 1px
border. Both social images were fully loaded.

The actual browser screenshots were inspected during the authoring session.
These were local README previews, not a claim that GitHub had already been
published at inspection time. The originals and delivered JPEGs are retained
here for inspection; the private preview server is not part of the package.

| Check | Observation |
|---|---|
| Main relationship | Map leads to Draw, which leads to Check, with two separate navy arrowheads. |
| Correction | The orange arrow starts at Check, travels above the main path and returns to Draw. It does not enter Map or bypass checking. |
| Detail relationship | The navy Check outline connects to Labels/Links by a dashed leader without an arrowhead. The bracket groups two inspection aspects, not sequential steps. |
| Color meaning | Purple method, blue drawing tool, green checks and orange revision retain their meaning. Functional glyphs have colored filled areas. The four-entry legend is inside each cover. |
| Typography | Main title, short labels and Chinese text are readable at 900px. No clipped text or overlapping functional elements was observed. At 320px, the Social title and main composition remain recognizable; small legend text is not intended as a full explanation at that size. |
| Localization | Chinese title and tagline use Traditional Chinese. Diagram wording is localized, the English brand remains, and the main connections and icon shapes remain recognizable. |

The initial Chinese version gave the secondary English name too much visual
weight and crowded its spacing. One targeted image edit reduced this block;
the selected result was checked again for title, wording and connection drift.
The initial version remains in `originals/readme-zh-TW-initial.png`. Slight
raster shading and optical differences remain; the result is not claimed to
be pixel-identical, vector-native or manually drawn.

## Output provenance and format

- Four built-in `image_gen.imagegen` requests: English master, initial Chinese,
  English social, and a targeted Chinese correction. Three final covers selected.
- Exact prompts, original image hashes and edit-reference roles are in
  [generation.json](generation.json) and [prompts](prompts).
- Original covers are 1774 x 887 PNGs. README exports are 1800 x 900 JPEGs.
  Social export is 1280 x 640 JPEG, **176,902 bytes**.
- Export uses RGB conversion, Lanczos resizing and JPEG quality 93 with
  chroma subsampling disabled. No compositing, retouching or text replacement
  was performed outside imagegen.
- The tool did not expose a model identifier. No exact image-model version is asserted.

The Social size and file limit follow
[GitHub's Social preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

## Verification boundaries

The installable skill is a copy of the previously reviewed local skill, with
its ten source hashes retained in [skill-source-hashes.json](skill-source-hashes.json).
The installed copy and formal presentation were not edited for this publication.
This packaging pass checks independent installation and local links; it does
not rerun the unchanged prior behavioral study or research experiments.

`tests/test_package.py` checks local documentation links, the copied skill's
independence from this repo, the checker's behavior after relocation, and
personal-path leakage in installable text. Its three tests and the eleven
existing graph tests run in CI. Image semantics, actual screen readability,
and bilingual meaning require separate inspection; the tests cannot prove them.

Human comprehension, taste, grayscale/color-vision behavior and external-host
end-to-end compatibility remain unmeasured. The AutoResearchAgent pictures are
development examples of a proposed workflow. A saved picture or a passing
structural check is not scientific validation.
