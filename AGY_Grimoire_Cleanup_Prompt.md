# Prompt for AGY: Grimoire Repo Cleanup Pass

> Paste everything below this line into Antigravity (AGY), opened on your local clone of `Daystar79/Grimoire`.
> Audit basis: commit `346dd9b` ("Add GROK_SKILL_PROMPT.md consolidated prompt bundle and generation script"). If your local clone is newer, re-check the line numbers before editing.

---

## Who you are working for and what this repo is

You are working in Cian Didymos's **Grimoire** repository: a *Symbology & Cybernetic Translator*. It maps living mystical traditions (Hesychasm, Catholic Sacred Heart mysticism, Thelema/O.T.O., Golden Dawn/Rosicrucianism, modern Gnosticism, Left-Hand Path/Luciferianism, Fraternitas Saturni, Solomonic/Enochian magic) and frontier AI/cybernetics onto Cian's own cosmology, **The Great Wheel**, from his book *A Wanderer's Guide to the Gates* (Ten Realms, Gates, Keys, Remnants, Thresholds).

Repo layout:

- `Sources/Manuscript_Master.md`: the book itself. **Closed source of truth.**
- `Sources/Esoteric Symbology Cross-Tradition Mapping.md`: the external living-traditions research layer (originally a Gemini Deep Research export).
- `Sources/SYMBIOLOGY_TRANSLATOR_HANDOFF.md`: the project plan, including four cleanup fixes requested for the external layer.
- `Core/Symbology_Translator_Crossmap.md`: the first mapping pass (external layer → Realms/Gates/Keys/Remnants).
- `.agents/skills/grimoire-translator/`: the agent skill (`SKILL.md`, `references/*.md`, `scripts/grimoire_cli.py`, `scripts/bundle_prompt.py`).
- `GROK_SKILL_PROMPT.md`: a generated bundle (SKILL.md plus the four reference files). **Never hand-edit it.** Regenerate it with `scripts/bundle_prompt.py`.

## Non-negotiable rules

1. **Never edit `Sources/Manuscript_Master.md`.** It is closed. Do not rewrite, correct, improve, expand, or reformat anything in it, including whitespace. All other files must conform to it, never the other way round. If you think the manuscript itself has a problem, list it in your final summary as a question for Cian and change nothing.
2. **Quote the manuscript verbatim.** Any Key, Remnant Key, Gatekeeper's Whisper, Gate name, or Realm element/subtitle that appears in quotation marks or in a "Key:" or "Gate:" field anywhere in the repo must match the manuscript character for character (straight vs. curly quotes may differ). Interpretive labels you or earlier tools coined (e.g. AI pivots, Remnant-trap nicknames) are allowed, but must not be presented as manuscript text.
3. **Living traditions only.** The external layer covers traditions with continuous, active 2025–2026 practice. Extinct or purely historical material is flagged, not silently deleted.
4. **Do not synonymize teleologies.** Black Flame ≠ Taboric Light; auto-deification ≠ theosis; Sacred Heart reparation ≠ merging; Goetic binding ≠ Luciferian invocation.
5. **When unsure, leave it unmapped.** "A hole is truer than a forced fit." Prefer a flagged gap over a guessed correspondence.
6. **Do not invent historical or factual content.** Every new factual claim you add (dates, quotations, ritual text, names of living orders or practitioners) must be backed by a source you cite inline (author/title/URL), **or** be marked `[VERIFY]` so Cian can check it. Never fabricate citations. When you quote ritual or liturgical text, quote from a public-domain or cited source, and do not paraphrase while presenting it as a quotation.
7. **Do not expand the research scope.** Add no new traditions and no new symbols beyond what the files already discuss, except where a task below explicitly says so.
8. **Local only.** Work on a new local branch (e.g. `cleanup/handoff-fixes`). Commit in small logical commits. **Do not push, open PRs, or touch the remote.** Cian will review and push himself.

---

## Audit summary: the handoff's four fixes

From `Sources/SYMBIOLOGY_TRANSLATOR_HANDOFF.md` §4, checked against `Sources/Esoteric Symbology Cross-Tradition Mapping.md` (121 lines):

| # | Fix requested | Status | Evidence |
|---|---|---|---|
| 1 | Complete, unbroken Master Visual Correspondences table | **Done** | Lines 14–23: header, separator, and 8 rows (Sacred Heart, Lust Card, Rose Cross, Pentagram/LBRP, Leviathan Cross, Pantocrator, Enochian Tablets, Goetic Sigils). Every row has 5 filled cells; nothing is truncated. (Optional coverage gap: see Task 7.) |
| 2 | Historical origin paragraphs compressed to ≤ 2 sentences | **Done** | Each visual dossier (lines 28–41) opens with a one-sentence origin, then moves to current practice. |
| 3 | `HISTORICAL ONLY` tag on entries lacking continuous 2025–2026 practice | **Present but misapplied → open (Task 2)** | |
| 4 | Enochian & Goetic entries expanded to the depth of other primary symbols | **Partly done → open (Task 3)** | Visual dossiers are now comparable in length (L35 ≈ 1,170 chars, L37 ≈ 1,215 chars vs. 875–1,515 for others). The language layer is still thin. |

---

## Tasks (only items still open)

### Task 1: Re-align the skill layer with the manuscript (highest priority)

**Files:**
- `.agents/skills/grimoire-translator/references/realms_codex.md`
- `.agents/skills/grimoire-translator/scripts/grimoire_cli.py` (the hardcoded `REALMS` dict)
- `README.md` ("The Great Wheel: Ten Realms" table)
- `.agents/skills/grimoire-translator/references/cybernetics_ai.md` (Realm headers in its mapping table)
- `.agents/skills/grimoire-translator/references/contradiction_index.md` and `SKILL.md` §3 Step 2, wherever they quote Keys

**What's wrong:** For Realms VI–X, and for two Gate names in V and X, the skill layer carries elements, Gate names, Keys, Remnant Keys and Whispers that **do not appear in the manuscript**. They look like invented or paraphrased stand-ins. Realms I–IV and most of V match.

`Core/Symbology_Translator_Crossmap.md` already uses the correct manuscript values (see its dossier header lines 118, 148, 178, 204, 232, 259, 288, 316, 344, 371), so the crossmap is the good reference.

Manuscript values, to verify yourself against the cited lines in `Sources/Manuscript_Master.md`:

| Realm | Field | Currently in skill layer (wrong) | Manuscript (correct) | MS line |
|---|---|---|---|---|
| V Echoes | Gate | Gate of Open Ground | **The Gate of the Open Ground** | 1022 |
| VI Compassion | Element | Water / Depth | **Water / Resonance** | 1285 |
| VI | Whisper | "Room for another does not require the erasure of yourself." | **"You cannot meet another if you have left yourself at the door."** | 1298 |
| VI | Key | "Two truths, one space." | **"I can be with you without becoming you, and without requiring you to become me."** ("Two truths. One space." is the prose that follows, not the Key.) | 1422–1423 |
| VII Presence | Element | Flesh / Pulse | **Earth / Weight** | 1532 |
| VII | Whisper | "The moment does not wait for you to feel ready for it." | **"The moment is already here. Let it find you."** | 1545 |
| VII | Key | "Here, now, as it is." | **"I am here. This is enough."** | 1683 |
| VII | Remnant Key | "If I stay perfectly still, the world cannot hurt me." | **"I will be present when things are calmer."** | 1686 |
| VIII Integration | Element | Weave / Cloth | **Weave / Rhythm** | 1799 |
| VIII | Gate | Gate of the Whole | **The Gate of the Woven Passage** | 1813 |
| VIII | Whisper | "A thread is not the cloth, but the cloth is nothing without the thread." | **"You have gathered seven fires. Now let them become one."** | 1812 |
| VIII | Key | "All threads, one weave." | **"There is nothing left to add and nothing left to remove."** | 1960 |
| VIII | Remnant Key | "If I understand how everything connects, I am master of the whole." | **"I keep different parts of myself for different contexts."** | 1963 |
| IX Threshold Fear | Element | Void / Night | **Ether / Boundlessness** | 2161 |
| IX | Whisper | "Fear does not mean turn back. It means you have reached the edge of what you knew." | **"The door appears only when you move."** | 2174 |
| IX | Key | "Step into the dark with what you carry." | **"I step because the fear is mine."** | 2302 |
| IX | Remnant Key | "When I am fearless, I will take the step." | **"I will step when the fear is gone."** | 2305 |
| X Return | Element | Ground / Open Hands | **Every Element and None** | 2433 |
| X | Gate | Gate of Open Hands | **The Gate of the Open Hands** | 2455 |
| X | Whisper | "The end of the journey is the beginning seen with open eyes." | **"You can set it down."** | 2454 |
| X | Key | "Return with empty hands." | **"The end is the beginning seen from the other side."** | 2631 |
| X | Remnant Key | "I have arrived, and I have nothing left to learn." | **"I have completed the Journey. I am finished."** | 2635 |

Also re-check every **Remnant Gate**, **Remnant** and **Threshold/Movement** description in `realms_codex.md` (especially VI–X; e.g. "a gilded throne at the summit" for X) against the manuscript's "The Remnant Gate", "The Remnant" and "The Threshold" sections for each chapter. Where a codex description has no basis in the chapter, replace it with a short faithful summary, or a short verbatim excerpt, of what the manuscript says.

In `SKILL.md` §4 Part 4, the ten Remnant-trap names (e.g. "Guru Complex", "Pseudosafety Paralysis", "Perfect Empty Vessel", "Confirmatory Echo", "Disembodied Stillness") are translator-coined labels, not manuscript terms. Keep them, but add one line saying they are translator shorthand. Next to each, add the manuscript's own Remnant Key for that Realm.

**Acceptance criteria:**
- Write a small check script, e.g. `.agents/skills/grimoire-translator/scripts/verify_canon.py`. It extracts every Key, Remnant Key, Whisper, Gate name and element from `realms_codex.md`, `grimoire_cli.py` (`REALMS`) and the README table, then asserts each appears verbatim in `Sources/Manuscript_Master.md` (normalize curly/straight quotes and a leading "The "). It must exit 0.
- `python3 .agents/skills/grimoire-translator/scripts/grimoire_cli.py list` and `realm 1` … `realm 10` print manuscript-exact Gates and Keys.
- `realm Compassion`, `search alignment` and `contradictions` still work.
- The AI/cybernetic pivot columns are unchanged unless they quoted a now-corrected Key.
- `git diff --stat` shows **no** change to `Sources/Manuscript_Master.md`.

### Task 2: Fix the `HISTORICAL ONLY` tagging (handoff fix #3)

**File:** `Sources/Esoteric Symbology Cross-Tradition Mapping.md`

**What's wrong:** The handoff asked for the tag only on entries that *lack* continuous, active 2025–2026 practice. Instead, the tag was stuck onto almost every visual dossier, apparently to mark the one-sentence origin line, even though each entry's own text documents living practice:

- Entry-level tags: L28 Sacred Heart ("In current practice, energized by … *Dilexit Nos*"), L29 Lucifer Sigils/Black Flame ("continuous use by … Temple of Ascending Flame"), L30 Thoth/Lust, L31 Rose Cross (SRIA/Scottish Rite "worn continuously"), L32 LBRP ("In daily practice today"), L33 Tree of Life/Qliphoth, L35 Enochian ("In active 2025–2026 practice"), L37 Goetic ("utilized heavily by living Solomonic practitioners"), L39 Leviathan Cross/Baphomet.
- Inline tags on historical background clauses: L67 (Nag Hammadi / Middle Platonism), L83 (Gregory Palamas, 14th c.), L91 (classical Gnostic Sophia mythos).
- Untagged: L38 Chi-Rho/Pantocrator, L40–41 Venus/Morning Star. This is consistent with them being living, but it shows the tagging rule was never applied systematically.
- The tags are written with escaped brackets (`\[HISTORICAL ONLY\]`), an export artifact.

**Do:**
1. Use two distinct markers:
   - `[HISTORICAL ONLY]` at **entry level**, only for an entry whose text shows no continuous 2025–2026 practice or living lineage.
   - *(historical background)* as an inline note on origin/background clauses inside entries that are otherwise living.
2. Re-evaluate every visual dossier, every terminology-table row (L51–56), every ritual-language paragraph (L61–67) and every idea dossier paragraph (L83–106). Remove the entry-level tag where the entry's own text documents current practice. Keep or add it where it doesn't.
3. If you believe an entry is historical-only but the file claims living practice, do **not** decide silently. Keep the text, add `[VERIFY: living practice?]`, and list it in your summary.
4. Add a one-paragraph tag legend under the Introduction (after line 6) explaining both markers.
5. Unescape the export artifacts (`\[` → `[`, `\]` → `]`, `\!` → `!`): 13 + 13 + 2 occurrences.

**Acceptance criteria:**
- No entry carries `[HISTORICAL ONLY]` while its own text asserts 2025–2026 practice.
- The tag legend exists.
- `rg -F '\['` and `rg -F '\!'` return nothing in this file.
- No content sentences were deleted; changes are tags, legend and escapes only.

### Task 3: Finish the Enochian & Goetic expansion (handoff fix #4)

**File:** `Sources/Esoteric Symbology Cross-Tradition Mapping.md`

**What's wrong:** The handoff asked for Enochian and Goetic entries to reach the same depth as other primary symbols "in both the visual and language layers (current use, living practitioners, functional equivalents, false equivalencies)". It also set a design rule (§6): "Language layer must include actual spoken ritual/prayer phrases, not just dictionary terms."

- The visual dossiers (L34–35, L36–37) are now adequate in length, but name living practitioners only generically ("Golden Dawn lineages and Thelemic orders"; "living Solomonic practitioners and independent ceremonial magicians").
- The language-layer paragraphs (L65 Enochian Calls ≈ 750 chars; L66 Goetic evocation ≈ 700 chars) are shorter than their peers (L61 ≈ 1,070; L62 ≈ 1,130). They quote **no actual spoken phrase**: no line of an Enochian Call, and only bare divine names for Goetia. Compare L61 (Thelemic greeting quoted) and L63 (Temple of Ascending Flame invocation quoted).
- Neither tradition has a row in the Terminology Cross-Map table (L49–56).

**Do:**
1. In L65 and L66, add one short, accurately quoted spoken formula for each tradition from a public-domain primary source. For example: a line of one of Dee's Enochian Calls/Keys (with the source's English gloss), and a line of a Goetic conjuration formula from the *Lemegeton / Ars Goetia*. Cite the source inline (edition/translator or URL). If you can't verify the exact wording, insert a placeholder `[VERIFY: quote from <source>]` instead of writing one from memory.
2. Name specific living orders/practitioner communities for each, only where you can cite them. Otherwise write `[VERIFY]`.
3. Add exactly two rows to the Terminology Cross-Map table, one Enochian term and one Goetic term, drawn from vocabulary already used in the file (e.g. "Watchtower"/"Call", "Triangle of Art"/"binding"). Use the existing 4-column format.
4. Keep the functional-equivalent and false-equivalency points already in the text. Do not reverse their conclusions.

**Acceptance criteria:**
- L65 and L66 each contain at least one quoted spoken phrase with a citation or `[VERIFY]` marker, plus named living lineages (cited or `[VERIFY]`).
- Each paragraph is roughly comparable in length to L61–L63.
- Two new terminology rows exist.
- No new traditions were introduced.

### Task 4: Deal with the empty "Works cited"

**File:** `Sources/Esoteric Symbology Cross-Tradition Mapping.md`, line 121

**What's wrong:** The file ends with the heading `#### **Works cited**` and nothing under it. The citations were lost in the PDF/Docs → Markdown export.

**Do:**
- If the original export (`Esoteric Symbology Cross-Tradition Mapping.pdf`, referenced in the handoff) exists anywhere in the local workspace, restore the citation list from it verbatim.
- Otherwise, do **not** reconstruct citations from memory. Add the line: `*Citation list not preserved in the Markdown export. Original: Esoteric Symbology Cross-Tradition Mapping.pdf (Gemini Deep Research). [VERIFY]*`
- Append any sources you cited in Tasks 2–3 under a separate sub-heading, "Sources added in cleanup pass".

**Acceptance criteria:** The section is no longer empty, and no citation appears that you did not actually take from a document or URL.

### Task 5: Fix the handoff file's name and stale references

**Files:** `Sources/SYMBIOLOGY_TRANSLATOR_HANDOFF.md`, `README.md`

**What's wrong:**
- The filename misspells "Symbology" as "SYMBIOLOGY". Every title inside the repo uses "Symbology".
- The handoff still lists the asset as a `.pdf` (line 26), but the repo holds `Sources/Esoteric Symbology Cross-Tradition Mapping.md`.
- The status line (line 4: "Mapping phase next") and §8 "Next Concrete Actions" are out of date: the crossmap exists.
- §7 describes a workspace layout (`00_CONTEXT.md`, `01_external/`, …) that the repo doesn't use.

**Do:**
1. Run `git mv Sources/SYMBIOLOGY_TRANSLATOR_HANDOFF.md Sources/SYMBOLOGY_TRANSLATOR_HANDOFF.md` and update the README repo-structure entry (README line 130). Grep the repo for any other reference to the old name.
2. Do not rewrite the handoff's history. Add a dated **"Status update (cleanup pass)"** block directly under the header. It should state:
   - the MD file replaced the PDF in-repo;
   - fixes 1–2 were found done and fixes 3–4 were completed in this pass;
   - the first mapping pass exists at `Core/Symbology_Translator_Crossmap.md`;
   - the §7 layout was superseded by the actual repo layout;
   - step 4 of §8 (forced-fit review) is the remaining item (see Task 7).
3. In the §2 asset table, add a note that the `.pdf` is the original export and the `.md` is the in-repo copy.

**Acceptance criteria:**
- `rg -i symbiology` returns nothing, apart from at most the old name quoted inside the status-update note.
- README links resolve.
- The original handoff text below the status block is unchanged except for the §2 note.

### Task 6: README accuracy

**File:** `README.md`

**What's wrong:**
- Line 64 says the skill is used "in an AI agent environment (such as Google Antigravity / Gemini CLI)". That is true for the `.agents/skills/` folder, but the README never mentions the second path: `GROK_SKILL_PROMPT.md`, a paste-in bundle for Grok/other LLMs, generated by `scripts/bundle_prompt.py`.
- The Repository Structure tree (lines 112–131) omits `GROK_SKILL_PROMPT.md` and `scripts/bundle_prompt.py`.
- The Ten Realms table (lines 21–32) carries the wrong values fixed in Task 1.

**Do:**
1. Split "Using the AI Skill" into two short sub-sections: (a) agent environments that load `.agents/skills/` (Antigravity / Gemini CLI); (b) Grok and other chat LLMs, by pasting `GROK_SKILL_PROMPT.md`, with the regenerate command `python3 .agents/skills/grimoire-translator/scripts/bundle_prompt.py`.
2. Add both files, plus `verify_canon.py` from Task 1, to the structure tree.
3. Bring the Ten Realms table in line with the manuscript (Element / Gate / Key) per Task 1. Keep the AI-pivot column.
4. Do **not** change the License section (see the note to Cian at the end).

**Acceptance criteria:**
- Both usage paths are documented.
- The tree matches `git ls-files`.
- `verify_canon.py` also covers the README table and passes.

### Task 7: Crossmap second pass after the source fixes (forced-fit review)

**File:** `Core/Symbology_Translator_Crossmap.md`

**What's wrong / pending:**
- The file is marked "**Status:** First mapping pass" (line 7).
- The handoff's §8 step 4 ("Review the resulting cross-maps for forced fits and refine") was never done.
- The crossmap's "Inputs" line already calls the external layer "cleaned", which was premature.
- Its Realm/Gate/Key language is already manuscript-accurate. **Do not "fix" it toward the old skill-layer values.**

**Do (after Tasks 2–3 are complete):**
1. For every crossmap row whose external item is now tagged `[HISTORICAL ONLY]` (Task 2), apply the living-only rule: either remove it from Clean/Partial and move it to §5 "What has no good match (leave unmapped)", or keep it with an explicit `HISTORICAL ONLY` flag. Use one approach consistently and say which in the "How to read this file" section.
2. Re-check the Enochian and Goetic rows and dossier mentions against the expanded Task 3 text. Map the two new terminology rows only if they land cleanly. Otherwise list them in §5 as unmapped.
3. Forced-fit review: go through every `Partial` and `Forced` tag and each §4 Remnant match. Apply the file's own §7 rules, especially "When unsure, leave it unmapped". Do not upgrade any fit to `Clean` without stating why in the row. For each change, add a short entry to a new "§8 Second-pass change log" at the bottom (row, old tag → new tag, reason).
4. Optional: the visual dossiers discuss five symbols that have no row in the Master Visual Correspondences table (Lucifer Sigils/Black Flame, Tree of Life/Qliphoth, Chi-Rho, Baphomet, Venus/Morning Star). You may add rows for them to the source table at L14–23, using **only** facts already in their dossiers (L29, L33, L38, L39, L41). If you do, confirm the crossmap already covers them; it does for most.
5. Update the header: "Status: Second mapping pass (post-cleanup)" with today's date. Leave the closing line "Target cosmology untouched." in place, and make sure it stays true.

**Acceptance criteria:**
- Every crossmap row that references a historical-only item is flagged or moved per the stated rule.
- The §8 change log exists, possibly listing "no changes" with reasons.
- No Realm/Gate/Key text in the crossmap differs from the manuscript (extend `verify_canon.py` to cover the crossmap's dossier header lines).

### Task 8 (final): Regenerate the bundle, verify, summarize

1. Run `python3 .agents/skills/grimoire-translator/scripts/bundle_prompt.py` to regenerate `GROK_SKILL_PROMPT.md`. Never hand-edit it.
2. Run `python3 .agents/skills/grimoire-translator/scripts/verify_canon.py` (must pass) and the CLI smoke tests: `list`, `realm 1`…`realm 10`, `realm Compassion`, `search alignment`, `contradictions`.
3. Confirm with `git diff --stat main` that `Sources/Manuscript_Master.md` is untouched.
4. Write a summary for Cian (in chat, and as `CLEANUP_SUMMARY.md` at the repo root) covering:
   - each task: done or partial, files changed, one-line description;
   - every `[VERIFY]` marker you added, with file:line and what needs checking;
   - entries you judged historical-only, or were unsure about;
   - any suspected issue in the manuscript itself (questions only, no edits);
   - commits made on the local branch (hashes). Confirm nothing was pushed.

---

## Order of operations

1. Create the local branch.
2. **Task 1** (skill layer ↔ manuscript, with `verify_canon.py`). This sets the canon every later step checks against.
3. **Task 2** (tagging), then **Task 3** (Enochian/Goetic), then **Task 4** (works cited), all in the external-layer file.
4. **Task 5** (rename and handoff status), then **Task 6** (README).
5. **Task 7** (crossmap second pass). It depends on 2 and 3.
6. **Task 8** (regenerate the bundle, verify, summarize). Always last, since any edit to `SKILL.md` or `references/` makes `GROK_SKILL_PROMPT.md` stale.

Commit after each task with a message naming the task number.

---

## Note to Cian (not a task for AGY; AGY must not act on this)

`README.md` says "This project is proprietary and confidential. All rights reserved.", and the manuscript carries a copyright notice. But `github.com/Daystar79/Grimoire` is currently a **public** repository, so the full manuscript is publicly readable. You may want to decide whether to make the repo private, or adjust the README wording. That's your call. Nothing in this prompt changes repo visibility or the License section.
