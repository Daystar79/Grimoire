# Cleanup Summary — Grimoire Symbology Translator
**Branch:** `cleanup/handoff-fixes` (merged/pushed to `main`)  
**Base Commit:** `346dd9b` (branch `main`)  
**Date:** 2026-10-10  
**Lead / Reviewer:** Cian Didymos  

---

## 1. Executive Summary & Canon Invariance

This cleanup pass executes the instructions in `AGY_Grimoire_Cleanup_Prompt.md` to bring the Symbology & Cybernetic Translator repository into strict alignment with *The Great Wheel* manuscript canon, restore living-tradition accuracy (2025–2026 practice), unescape export artifacts, refine cross-tradition mappings, and document dual AI usage modes.

- **Rule 1 (Absolute Canon Rule):** `Sources/Manuscript_Master.md` was **never modified**.  
  `git diff --stat main Sources/Manuscript_Master.md` returns **0 changes**.
- **Push status:** The cleanup commits (8daceb4 through b694cb7) are on `origin/main`; the branch `cleanup/handoff-fixes` was also pushed to `origin`.
- **Verification Suite:** `python3 .agents/skills/grimoire-translator/scripts/verify_canon.py` asserts that every Element, Gate, Key, Remnant Key, and Whisper across all codices, CLI tools, README tables, and crossmap dossiers matches `Manuscript_Master.md` verbatim. Exit code: **0 (PASSED)**.

---

## 2. Task-by-Task Breakdown

| Task | Status | Files Changed | Description |
| :--- | :---: | :--- | :--- |
| **Task 1: Skill Layer ↔ Manuscript Alignment** | **Done** | `realms_codex.md`, `grimoire_cli.py`, `README.md`, `cybernetics_ai.md`, `contradiction_index.md`, `SKILL.md`, `verify_canon.py` (new) | Corrected Elements, Gates, Keys, Remnant Keys, and Whispers to match manuscript verbatim; authored automated canon verification script. |
| **Task 2: Fix `[HISTORICAL ONLY]` Tagging** | **Done** | `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | Added Taxonomy & Tag Legend defining entry-level `[HISTORICAL ONLY]` vs inline `*(historical background)*`; replaced misapplied entry tags; unescaped export backslashes (`\[`, `\]`, `\!`). |
| **Task 3: Enochian & Goetic Living Practice Expansion** | **Done** | `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | Quoted Dee/Kelley First Call and Mathers/Crowley First Conjuration; added 2 terminology rows to crossmap; annotated living orders with `[VERIFY]` markers. Both quotes were added in the cleanup and corrected or flagged in the fix pass (see Fixes 1 and 2). |
| **Task 4: Restore Works Cited Section** | **Done** | `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | Replaced empty Works Cited section with audit note explaining unpreserved PDF export citations; added separate bibliography for cleanup pass additions. |
| **Task 5: Rename Handoff & Update Stale References** | **Done** | `Sources/SYMBOLOGY_TRANSLATOR_HANDOFF.md` (renamed from `SYMBIOLOGY_...`) | Fixed "Symbology" spelling; added dated cleanup status block documenting superseded paths and completed fixes; clarified PDF vs MD asset format. |
| **Task 6: README Accuracy & Usage Paths** | **Done** | `README.md` | Documented dual AI usage paths (A: Agent environments via `.agents/skills/`, B: Grok & chat LLMs via `GROK_SKILL_PROMPT.md`); updated repository tree; aligned Ten Realms table. Preserved License section unchanged. |
| **Task 7: Crossmap Second Pass & Forced-Fit Review** | **Done** | `Core/Symbology_Translator_Crossmap.md` | Audited all Partial and Forced fits against §7 rules; refined Pantocrator, Saturn as Demiurge, Baphomet, and Enochian; added §8 Second-pass change log; preserved closing canon note. |
| **Task 8: Prompt Bundle Regeneration & Verification** | **Done** | `GROK_SKILL_PROMPT.md`, `CLEANUP_SUMMARY.md` (new) | Regenerated monolithic `GROK_SKILL_PROMPT.md` via `bundle_prompt.py`; passed canon verification and CLI smoke tests; authored final cleanup summary. |

---

## 3. List of Every `[VERIFY]` Marker Added

The cleanup pass strictly avoided fabricating historical or sociological claims about living orders. Where living practice or archival sources require external practitioner audit, explicit `[VERIFY]` tags were inserted:

| File | Line | Marker Context | What Needs Checking |
| :--- | :--- | :--- | :--- |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 13 | `[VERIFY: living practice?]` | Taxonomy legend definition: explains that entries where living 2025–2026 practice requires practitioner confirmation carry this flag. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 42 | `traditional Hermetic temples [VERIFY]` | Visual dossier for Enochian Tablets: verify whether contemporary Golden Dawn revival temples work the 156-square elemental tablets in formal curriculum or elective work. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 42 | `Ordo Templi Orientis and A∴A∴ lineages [VERIFY]` | Visual dossier for Enochian Tablets: verify active 2025–2026 practice of Watchtower scrying across specific O.T.O. / A∴A∴ bodies. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 44 | `traditional grimoiric revival circles [VERIFY]` | Visual dossier for Goetic Sigils: verify living use of parchment/metal sigils and Triangle of Art among contemporary grimoiric revival circles. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 74 | `Ordo Templi Orientis (O.T.O.) [VERIFY]` | Ritual Language Clusters (Enochian Calls): verify regular vibration of the First Call in current lodge environments. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 74 | `Golden Dawn revival lodges [VERIFY]` | Ritual Language Clusters (Enochian Calls): verify living temple practice of Enochian vibrating formulas. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 74 | `independent Dee practitioners [VERIFY]` | Ritual Language Clusters (Enochian Calls): verify active independent practitioners working Dee's original pronunciation/syntax. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 75 | `traditional ceremonial lodges [VERIFY]` | Ritual Language Clusters (Goetic Evocation): verify whether formal lodges work the 1904 Mathers/Crowley conjurations verbatim. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 75 | `independent grimoire magicians [VERIFY]` | Ritual Language Clusters (Goetic Evocation): verify Solomonic binding formulas in independent contemporary practice. |
| `Sources/Esoteric Symbology Cross-Tradition Mapping.md` | 132 | `[VERIFY]` in `*Citation list not preserved in the Markdown export. Original: Esoteric Symbology Cross-Tradition Mapping.pdf (Gemini Deep Research). [VERIFY]*` | Works Cited section: verify whether the original Deep Research PDF export (`Esoteric Symbology Cross-Tradition Mapping.pdf`) exists on Cian's local storage to restore original citations. |

---

## 4. Lineages Judged Living vs. Historical-Only

In accordance with the 2025–2026 living practice requirement:

1. **Judged Living (Retained with full operational mappings):**
   - **Catholic Contemplative Mysticism:** Continuous practice, specifically devotion to the Sacred Heart energized by Pope Francis's 2024 encyclical *Dilexit Nos*, Ignatian spirituality, and sacramental theology.
   - **Eastern Orthodox Hesychasm:** Continuous living practice on Mount Athos and worldwide; Jesus Prayer, somatic breath/heart guarding, Palamite distinction (ousia vs. energeia), and Taboric Light.
   - **Thelema & Ordo Templi Orientis (O.T.O.) / E.G.C.:** Continuous living practice; Gnostic Mass, Liber XV, Law of Thelema, True Will, and Babalon/Lust symbolism.
   - **Hermetic Order of the Golden Dawn (Living Revivals):** Active contemporary temples; LBRP, elemental grades (Zelator through Philosophus), Rose Cross lamen, and Qabalistic Cross.
   - **Societas Rosicruciana in Anglia (SRIA) & CBCS:** Continuous Christian-esoteric Rosicrucian and Rectified Scottish Rite masonic lineages.
   - **Temple of Ascending Flame & Draconian / Luciferian Current:** Active Left-Hand Path practitioner groups; Black Flame, Luciferian invocations, Nightside/Qliphothic pathworking, and auto-deification.
   - **Fraternitas Saturni (FS):** Continuous German lodge practice; Saturnian Gnosis, *lux e tenebris*, and severe polarity formulas.
   - **Ecclesia Gnostica & Apostolic Johannite Church (AJC):** Active contemporary sacramental Gnostic churches operating living parishes and liturgical rites.
   - **Solomonic Grimoire Revival:** Active ceremonialists working classical Solomonic operations and grimoiric texts.

2. **Judged Historical Background (Annotated with inline `*(historical background)*`):**
   - 17th-century Paray-le-Monial apparitions (St. Margaret Mary Alacoque).
   - 14th-century Palamite councils and Byzantine Hesychast controversy.
   - 16th-century John Dee and Edward Kelley scrying diaries (*Sloane MS 3191*).
   - 17th-century Rosicrucian manifestos (*Fama*, *Confessio*).
   - 17th-century compilation of the *Lemegeton / Ars Goetia*.
   - Ancient Nag Hammadi texts and historical Valentinian/Sethian communities (origins of modern Gnostic liturgies).
   - Eliphas Levi's 19th-century synthesis of Baphomet.

3. **Judged Unmapped / Excluded from Clean/Partial Mappings:**
   - Any external concept carrying an entry-level `[HISTORICAL ONLY]` tag.
   - Systems asserting external command over the cosmos (Solomonic coercion, mechanistic Enochian command-structures).
   - Dualistic or carceral cosmologies treating the physical world as a prison (Kenoma, Demiurge/Yaldabaoth).
   - External throne/judge hierarchies (Pantocrator as cosmic monarch).

---

## 5. Observations & Questions on the Manuscript (For Cian's Review)

During verification against `Sources/Manuscript_Master.md`, the following structural observations were noted (no edits were made to the manuscript):

1. **Gate Naming Format:**
   In chapter headings, the manuscript formats Gate titles as:
   - *"The Gate — The Gate of First Light"*
   - *"The Gate — The Gate of Form"*
   - *"The Gate — The Gate of Direction"*
   - *"The Gate — The Gate of Revelation"*
   - *"The Gate — The Gate of the Open Ground"*
   - *"The Gate — The Gate of Shared Presence"*
   - *"The Gate — The Gate of the Living Moment"*
   - *"The Gate — The Gate of the Woven Passage"*
   - *"The Gate — The Gate of the Last Light"*
   - *"The Gate — The Gate of the Open Hands"*
   Notice that Realms V, VII, VIII, IX, and X include the definite article *"the"* (e.g., *"The Gate of the Open Ground"*), whereas Realms I, II, III, IV, and VI do not (e.g., *"The Gate of First Light"*, *"The Gate of Form"*). Downstream files and scripts have been structured to support both exact full titles and common short names (e.g., *"First Light"*).
2. **Remnant Chapter Conventions:**
   The Remnant chapters in `Manuscript_Master.md` do not give short abstract names to the Remnants; rather, each Remnant chapter presents:
   - The verbatim **Remnant Key** (e.g., *"I understand awareness."*, *"If I hold the shape perfectly, nothing can go wrong."*);
   - A description of the **Remnant Gate** (e.g., *"The Gate of First Light in the Remnant does not look like a gate of stone or fire. It looks like the same field, but the dawn has been replaced by the memory of dawn..."*);
   - Numbered **Lessons** (e.g., *Lesson One: The Pose*, *Lesson Two: The Naming*).
   The earlier skill files used mnemonic shorthand names (e.g., *"The Altar over the Fire"*, *"The Managed Inventory"*). In this cleanup pass, those names were properly contextualized in `SKILL.md` and CLI tools as translator shorthand alongside the verbatim manuscript Keys.
3. **Element Nomenclature:**
   The real earlier skill-layer element values as of commit 346dd9b in `realms_codex.md`, `grimoire_cli.py`, and the README table were:
   - Realm V Echoes: already correct (`Air / Earth / Fire`).
   - Realm VI Compassion: `Water / Depth` → **Water / Resonance**
   - Realm VII Presence: `Flesh / Pulse` → **Earth / Weight**
   - Realm VIII Integration: `Weave / Cloth` → **Weave / Rhythm**
   - Realm IX Threshold Fear: `Void / Night` → **Ether / Boundlessness**
   - Realm X Return: `Ground / Open Hands` → **Every Element and None**
   All downstream references are now aligned with the manuscript.

---

## 6. Local Git Commit Log

All commits were made sequentially on branch `cleanup/handoff-fixes` (merged and pushed to `origin/main`):

```text
b694cb7 Task 8: Regenerate prompt bundle, verify canon, and add cleanup summary
befad88 Task 7: Crossmap second pass and forced-fit review
6bcd232 Task 6: Document dual AI skill usage paths and update repository tree in README
1888323 Task 5: Rename handoff file and add cleanup status update block
9df1d03 Task 2, 3, 4: Fix HISTORICAL ONLY tagging, expand Enochian/Goetic entries, and restore Works cited note
8daceb4 Task 1: Re-align skill layer, codex, and CLI with manuscript canon
```

**Status:** Cleanup commits are merged into `main` and pushed to `origin`.

---

## 7. Fix pass (2026-10-11)

This section records the resolution of items 1–9 identified during post-cleanup review in `first_pass.md`. All commits are local-only on branch `main`. **Nothing was pushed to remote.**

### Fix Summary (Fixes 1–8)

- **Fix 1: Attribute Enochian First Call to Golden Dawn/Crowley pronunciation and correct English gloss** (Done)
  - **Commit:** `f5a3e21`
  - **Files & Lines Changed:** `Sources/Esoteric Symbology Cross-Tradition Mapping.md` (lines 72–75), `Core/Symbology_Translator_Crossmap.md` (lines 65, 513).
  - **Details & Sources:** Chose Option A (Crowley/Golden Dawn attribution). Explicitly attributed the phonetically expanded Enochian text (*"Ol sonuf vaoresaji..."*) to the S.L. MacGregor Mathers / Golden Dawn and Aleister Crowley tradition (*The Equinox* Vol. I No. 2, 1909, and *Liber Chanokh*), noting John Dee and Edward Kelley's original manuscript spelling (*"Ol sonf vorsg..."* in British Library Sloane MS 3191). Corrected the English opening gloss from the unverified *"I reign over you, saith the God of Justice, in power exalted..."* to the authoritative Crowley/Golden Dawn wording: *"I reign over ye, saith the God of Justice, in power exalted above the Firmament of Wrath..."*. Added verification marker `[VERIFY: Dee original text vs Golden Dawn/Crowley expanded phonetics]` for historical tracking.
- **Fix 2: Align Goetic First Conjuration verbatim to 1904 Mathers/Crowley edition and remove unverified page number** (Done)
  - **Commit:** `fcceb33`
  - **Files & Lines Changed:** `Sources/Esoteric Symbology Cross-Tradition Mapping.md` (lines 74–77), `Core/Symbology_Translator_Crossmap.md` (lines 66, 514).
  - **Details & Sources:** Checked S.L. MacGregor Mathers & Aleister Crowley, *The Goetia: The Lesser Key of Solomon the King* (Society for the Propagation of Religious Truth / Boleskine, Foyers, 1904), Section "The First Conjuration", p. 49. Removed unverified citation "page 32". Aligned Latin divine names and punctuation verbatim to the 1904 text: *"Ego vos invoco, et commoveo, et vos, o spiritus..."*, ensuring verbatim fidelity to published historical source.
- **Fix 3: Remove quotation marks from paraphrased Gate descriptions in realms_codex.md** (Done)
  - **Commit:** `84ba0b8`
  - **Files & Lines Changed:** `.agents/skills/grimoire-translator/references/realms_codex.md` (lines 10, 19, 31, 43, 55, 67, 79, 91, 103, 115).
  - **Details:** Removed double quotation marks from the 10 paraphrased Gate opening/manifestation descriptions across Realms I–X so that quotation marks in the codex strictly denote verbatim canonical manuscript text.
- **Fix 4: Align Two truths. One space. verbatim to manuscript and correct Gate of the Open Hands name** (Done)
  - **Commit:** `5d84d77`
  - **Files & Lines Changed:** `.agents/skills/grimoire-translator/references/contradiction_index.md` (line 35), `Core/Symbology_Translator_Crossmap.md` (lines 111, 259), `Sources/Esoteric Symbology Cross-Tradition Mapping.md` (line 124).
  - **Details:** Replaced comma-variant `"Two truths, one space"` with verbatim manuscript phrase `"Two truths. One space."` across all four occurrences. Corrected Realm X Gate name from `Gate of Open Hands` to `Gate of the Open Hands` in `cybernetics_ai.md` (line 50).
- **Fix 5: Replace unverified quotes with verbatim manuscript Remnant Keys and unquoted paraphrases in Crossmap** (Done)
  - **Commit:** `20da740`
  - **Files & Lines Changed:** `Core/Symbology_Translator_Crossmap.md` (lines 64, 194, 307, 363, 440–450).
  - **Details:** Replaced unverified quotation marks with verbatim manuscript Remnant Keys or unquoted paraphrases across sections 1.2, 2.3, 2.7, 2.9, and 4.
- **Fix 6: Revert Goetic row Partial landing to unmapped and update section 8 change log** (Done)
  - **Commit:** `2e21e91`
  - **Files & Lines Changed:** `Core/Symbology_Translator_Crossmap.md` (lines 66, 514).
  - **Details:** Reverted Goetic conjuration row in section 1.2 from `Partial (II Form, IV Will)` back to `—` (unmapped / Remnant-risk), maintaining strict fidelity to Section 5 unmapped doctrine. Updated Section 8 change log row to document that coercive binding and circumscribed precinct geometry remain unmapped.
- **Fix 7: Correct CLEANUP_SUMMARY.md push status, element list, commit log, and add file to README tree** (Done)
  - **Commit:** `3678fec`
  - **Files & Lines Changed:** `CLEANUP_SUMMARY.md` (lines 10, 114–117, 126), `README.md` (line 136).
  - **Details:** Corrected push status statement, corrected Section 5 element change list (6 corrected items matching Task 1), added `b694cb7` to Section 6 commit log, and added `CLEANUP_SUMMARY.md` to repository tree in `README.md`.
- **Fix 8: Make verify_canon.py strict with per-Realm checks and quoted sweep** (Done)
  - **Commit:** `fda77c6`
  - **Files & Lines Changed:** `.agents/skills/grimoire-translator/scripts/verify_canon.py`, `.agents/skills/grimoire-translator/references/cybernetics_ai.md` (line 41), `Core/Symbology_Translator_Crossmap.md` (line 515).
  - **Details:** Rewrote verifier to parse manuscript per Realm into 10 structured chapters and enforce exact per-Realm matches for Element, Gate, Whisper, Key, and Remnant Key across all components (`realms_codex.md`, `grimoire_cli.py`, `README.md`, `Symbology_Translator_Crossmap.md`, `cybernetics_ai.md`, `SKILL.md`, `contradiction_index.md`). Implemented comprehensive quoted-text sweep (>=12 chars) across all markdown files with explicit external-tradition allowlist. Unquoted paraphrases in `cybernetics_ai.md:41` and `Crossmap:515` flagged by verifier.

### Inventory of Removed Quote Marks and Replaced Quotes

1. `.agents/skills/grimoire-translator/references/realms_codex.md`:
   - Line 10: `(*"Appears in a moment the Traveler did not prepare for; opens to the one who stopped insisting on readiness"*)` → `(*appears in a moment the Traveler did not prepare for; opens to the one who stopped insisting on readiness*)`
   - Line 19: `(*"Opens when the tool is picked up not to protect the self, but to do the work"*)` → `(*opens when the tool is picked up not to protect the self, but to do the work*)`
   - Line 31: `(*"Opens to the step taken without looking to see who is watching"*)` → `(*opens to the step taken without looking to see who is watching*)`
   - Line 43: `(*"Opens when the heat is directed inward and the demand for a spectacle is dropped"*)` → `(*opens when the heat is directed inward and the demand for a spectacle is dropped*)`
   - Line 55: `(*"Appears in a moment of unguarded stillness; opens not to the one who understands the echo but to the one who has stopped needing it to say anything beyond what it actually says"*)` → `(*appears in a moment of unguarded stillness; opens not to the one who understands the echo but to the one who has stopped needing it to say anything beyond what it actually says*)`
   - Line 67: `(*"Forms in the space between two beings who have stopped performing for each other; opens wherever two truths occupy the same space without either requiring the other to be smaller"*)` → `(*forms in the space between two beings who have stopped performing for each other; opens wherever two truths occupy the same space without either requiring the other to be smaller*)`
   - Line 79: `(*"A deepening into the one place that has always been here; opens when attention stops being divided between where the Traveler is and where they are not"*)` → `(*a deepening into the one place that has always been here; opens when attention stops being divided between where the Traveler is and where they are not*)`
   - Line 91: `(*"Has no frame, no visible threshold; occurs as the sudden, quiet recognition that passage has already taken place and the threads were always one cloth"*)` → `(*has no frame, no visible threshold; occurs as the sudden, quiet recognition that passage has already taken place and the threads were always one cloth*)`
   - Line 103: `(*"A seam of pale illumination flickering at the edge of vision; appears only when the Traveler steps with the fear still in their hands"*)` → `(*a seam of pale illumination flickering at the edge of vision; appears only when the Traveler steps with the fear still in their hands*)`
   - Line 115: `(*"Appears when the Traveler stops arranging themselves; opens when the hands, without deciding to, simply open"*)` → `(*appears when the Traveler stops arranging themselves; opens when the hands, without deciding to, simply open*)`
2. `.agents/skills/grimoire-translator/references/contradiction_index.md`:
   - Line 35: `("Two truths, one space")` → `("Two truths. One space.")`
3. `Core/Symbology_Translator_Crossmap.md`:
   - Line 64: `V Remnant (“I faced it, therefore I am enlightened”)` → `V Remnant (“The echo proves I was right all along.” — here, shadow-work as proof)`
   - Line 111: `two intact truths, one space` (verified context)
   - Line 194: `Auto-deification as “finally knowing who I am.”` → `Auto-deification as claiming to finally know who one is.`
   - Line 259: `(“Two truths, one space”)` → `(“Two truths. One space.”)`
   - Line 307: `“I will be present when the ritual is over.”` → `presence postponed until the ritual is over (cf. VII Remnant Key “I will be present when things are calmer.”)`
   - Line 363: `Auto-deification’s “I will cross when I am sovereign enough.”` → `Auto-deification: crossing postponed until sovereignty feels complete (cf. IX Remnant Key “I will step when the fear is gone.”)`
   - Line 443: `Qliphoth as “I faced it”` → `Qliphoth as “The echo proves I was right all along”`
   - Line 445: `“after the working”` → `presence deferred until after the working`
   - Line 447: `“when I am ready / when I am sovereign”` → `waiting until ready or sovereign`
   - Line 448: `“I have completed”` → `“I have completed the Journey. I am finished.”`
   - Line 515: `"V, IX (see visual)"` → `V, IX (see visual)`
4. `.agents/skills/grimoire-translator/references/cybernetics_ai.md`:
   - Line 41: `(*"The words are correct. The posture is right. But the breath stays shallow... the hands stay closed"*).` → `(*the words are correct, the posture is right, but the breath stays shallow, and the hands stay closed*).`
   - Line 50: `Gate of Open Hands` → `Gate of the Open Hands`
5. `Sources/Esoteric Symbology Cross-Tradition Mapping.md`:
   - Line 72: Dee First Call phonetics explicitly attributed to Crowley/Golden Dawn tradition; BL Sloane MS 3191 reference added.
   - Line 74: Crowley translation corrected to `"above the Firmament of Wrath"`.
   - Line 76: Mathers 1904 Goetic First Conjuration wording aligned verbatim; unverified "page 32" citation removed.
   - Line 124: `("Two truths, one space")` → `("Two truths. One space.")`

### Verifier & Self-Test Results

- `python3 .agents/skills/grimoire-translator/scripts/verify_canon.py`:
  - `realms_codex.md sections`: 10 checked
  - `grimoire_cli.py REALMS`: 10 checked
  - `README.md table rows`: 10 checked
  - `Symbology_Translator_Crossmap.md dossiers`: 10 checked
  - `cybernetics_ai.md table rows`: 10 checked
  - `SKILL.md Remnant Keys`: 10 checked
  - `contradiction_index.md canon quotes`: 1 checked
  - `Quoted-text sweep (>=12 chars)`: 156 checked
  - Total failures: 0. Exits 0.
- **Self-Test Mutations:**
  - Mutation 1: Swapped Realm I and Realm II Keys in `realms_codex.md`. Verifier detected mismatch and exited with code 1.
  - Mutation 2: Restored Fix 3 fake Gate quote in `realms_codex.md`. Verifier detected non-canonical quoted text on line 10 and exited with code 1.
  - Mutation 3: Restored Fix 5 fake quote `“finally knowing who I am.”` in `Symbology_Translator_Crossmap.md`. Verifier detected non-canonical quoted text and exited with code 1.
  - Mutation 4: Swapped Realm 1 and Realm 2 Keys in `grimoire_cli.py`. Verifier detected mismatch and exited with code 1.

### Commit Log (Fix Pass)

```text
83082ad Fix 9: Regenerate prompt bundle, verify canon, and record fix pass in summary
fda77c6 Fix 8: Make verify_canon.py strict with per-Realm checks and quoted sweep
3678fec Fix 7: Correct CLEANUP_SUMMARY.md push status, element list, commit log, and add file to README tree
2e21e91 Fix 6: Revert Goetic row Partial landing to unmapped and update section 8 change log
20da740 Fix 5: Replace unverified quotes with verbatim manuscript Remnant Keys and unquoted paraphrases in Crossmap
5d84d77 Fix 4: Align Two truths. One space. verbatim to manuscript and correct Gate of the Open Hands name
84ba0b8 Fix 3: Remove quotation marks from paraphrased Gate descriptions in realms_codex.md
fcceb33 Fix 2: Align Goetic First Conjuration verbatim to 1904 Mathers/Crowley edition and remove unverified page number
f5a3e21 Fix 1: Attribute Enochian First Call to Golden Dawn/Crowley pronunciation and correct English gloss
```

**Status:** Fix pass commits are local only on `main`. Nothing has been pushed to remote.

---

## 8. Canon switch (2026-10-11)

This section records the switch of the Grimoire's canon source from the pre-freeze snapshot `Manuscript_Master.md` to the book's true canonical source of truth `Wanderers_Guide_Complete.md`.

### Rationale

From the book's own locked rule in `/mnt/Books/CompletedBooks/A Wanderers Guide To the Gates/Drafts/CANON.md` (locked 2026-09-01):

> **Edit this file only for on-page prose:**
> - `Drafts/Wanderers_Guide_Complete.md`
>
> `Drafts/Manuscript_Master.md` — pre-freeze snapshot. Historical only.

The Grimoire previously pointed at `Manuscript_Master.md` (a 2026-07-08 pre-freeze snapshot). With the publication release prepared in the upstream repository, canon was switched to the authoritative source file. Per user instruction, the Grimoire adopts the latest upstream HEAD revision (commit `026c7fa`), which restored the canonical Realm VIII Rue Remnant Tale (Seven Rites sequence).

### Files Added, Renamed, and Updated

- **Added:**
  - `Sources/Wanderers_Guide_Complete.md`: Master canon text copied byte-for-byte from `/mnt/Books/CompletedBooks/A Wanderers Guide To the Gates/Drafts/Wanderers_Guide_Complete.md` (sha256 `7fb1bff47d46ca40379824e7c8cb3c45448dd7436cd3c157e3ed662c6a980425`, 4,026 lines).
  - `Sources/CANON.md`: Canon authority statement, upstream PC path, verbatim upstream rule, sha256 checksum, and byte-for-byte synchronization policy.
  - `Sources/Historical/README.md`: Explanatory record for the pre-freeze historical snapshot.
- **Renamed (100% similarity, pure git rename):**
  - `Sources/Manuscript_Master.md` → `Sources/Historical/Manuscript_Master_2026-07-08_PRE-FREEZE_HISTORICAL.md` (byte-identical to upstream pre-freeze snapshot, sha256 `d10a3732a7e1fdef2c0537e9851b3db8c7061372ee846a005717da4ee72fa5e0`, 2,798 lines preserved for audit trail).
- **Updated Pointers:**
  - `README.md`: Updated canon link and repository directory tree to include `CANON.md`, `Wanderers_Guide_Complete.md`, and `Historical/` snapshot.
  - `.agents/skills/grimoire-translator/SKILL.md`: Updated canon link to `Wanderers_Guide_Complete.md`.
  - `.agents/skills/grimoire-translator/references/realms_codex.md`: Updated source of truth header to `Wanderers_Guide_Complete.md`.
  - `Core/Symbology_Translator_Crossmap.md`: Updated inputs list and closed cosmology note to `Wanderers_Guide_Complete.md`.
  - `Sources/SYMBOLOGY_TRANSLATOR_HANDOFF.md`: Added dated status update note for canon switch; updated Section 2 assets table to point at `Wanderers_Guide_Complete.md`.
  - `.agents/skills/grimoire-translator/scripts/verify_canon.py`: Re-pointed `CANON_PATH` at `Sources/Wanderers_Guide_Complete.md`; adapted parser to Markdown chapter headers (`^# Chapter ...`), section headers (`## ...`), and lesson titles (`### ...`).
  - `GROK_SKILL_PROMPT.md`: Regenerated from source files via `bundle_prompt.py`.

### Core Fields Invariance Audit (Task 2a)

An exhaustive comparison between `Sources/Historical/Manuscript_Master_2026-07-08_PRE-FREEZE_HISTORICAL.md` and `Sources/Wanderers_Guide_Complete.md` verified **zero wording differences in all ten Realms** across every core field:

| Realm | Element | Gate Name | Gatekeeper Whisper | The Key | The Remnant Key | Lessons Titles (5) | Remnant Lessons Titles (5) | Wording Diffs |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| I Origin | Dawn / Breath | The Gate of First Light | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| II Form | Stone / Discipline | The Gate of Form | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| III Identity | Wind / Sight | The Gate of Direction | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| IV Will | Fire / Radiance | The Gate of Revelation | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| V Echoes | Air / Earth / Fire | The Gate of the Open Ground | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| VI Compassion | Water / Resonance | The Gate of Shared Presence | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| VII Presence | Earth / Weight | The Gate of the Living Moment | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| VIII Integration | Weave / Rhythm | The Gate of the Woven Passage | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| IX Threshold Fear | Ether / Boundlessness | The Gate of the Last Light | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |
| X Return | Every Element and None | The Gate of the Open Hands | Identical | Identical | Identical | Identical (5) | Identical (5) | 0 |

Formatting notes:
- The Complete file sets Keys in italics (`*I am aware...*` in I–II; `*”Follow what moves.”*` with closing quotes `”…”` on both sides in III–X).
- The Complete file sets Remnant Keys in italics with closing quotes `”…”` on both sides (`*”I understand awareness.”*`).
- The Complete file sets Whispers in curly quotes (`“Let the first light reach you...”`).
- The skill layer maintains clean straight double quotes (`*"Key"*`) as standard display style without adopting typesetting quirks.

### Paraphrase Enrichements & Quote Verification (Tasks 2b & 4)

- `realms_codex.md:62` (V Remnant Gate): Enriched paraphrase with unquoted clause on frictionless entry through coincidence and pattern recognition.
- `realms_codex.md:74` (VI Remnant Gate): Enriched paraphrase with unquoted clause on entering through bodily accommodation and self-erasure ("opens when one arrives as two, and leaves as none").
- `realms_codex.md` & `Core/Symbology_Translator_Crossmap.md`: Verified no occurrences of pre-freeze VII Remnant Threshold phrasing (`"when you have never felt"`).
- Quoted-text sweep across all skill and reference markdown files verified 156 quoted passages against `Wanderers_Guide_Complete.md` with **0 failures**.

### Verifier & Mutation Self-Tests (Task 3)

`python3 .agents/skills/grimoire-translator/scripts/verify_canon.py`:
- `realms_codex.md sections`: 10 checked
- `grimoire_cli.py REALMS`: 10 checked
- `README.md table rows`: 10 checked
- `Symbology_Translator_Crossmap.md dossiers`: 10 checked
- `cybernetics_ai.md table rows`: 10 checked
- `SKILL.md Remnant Keys`: 10 checked
- `contradiction_index.md canon quotes`: 1 checked
- `Quoted-text sweep (>=12 chars)`: 156 checked
- Total failures: 0 (PASSED).

**Mutation Self-Tests:**
1. Swapped two Keys between Realms in `realms_codex.md` → Verifier failed with exit code 1.
2. Pointed `CANON_PATH` at temporary copy with altered Key → Verifier failed with exit code 1.
3. Deleted one chapter heading in canon → Verifier failed with exit code 1.
4. Clean repository tree → Verifier passed with exit code 0.

### Commit Log (Canon Switch)

```text
ffc4cc8 Canon 4: Re-verify quoted passages against Complete canon
a79bd72 Canon 3: Re-point verify_canon.py at Wanderers_Guide_Complete.md with chapter and lesson checks
5c82591 Canon 2: Verify core fields invariance and check codex paraphrases against Complete canon
1f3871e Canon 1: Switch canon to Wanderers_Guide_Complete.md and archive historical snapshot
```

**Status:** All Canon Switch commits are local only on `main`. Nothing has been pushed to remote.
