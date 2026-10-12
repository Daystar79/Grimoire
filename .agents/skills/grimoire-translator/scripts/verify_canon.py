#!/usr/bin/env python3
"""
verify_canon.py: Strict verification of all Gates, Keys, Remnant Keys, Whispers,
Elements, and quoted text against canon in Sources/Manuscript_Master.md.
"""

import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
MANUSCRIPT_PATH = REPO_ROOT / "Sources" / "Manuscript_Master.md"
CODEX_PATH = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "references" / "realms_codex.md"
CLI_PATH = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "scripts" / "grimoire_cli.py"
README_PATH = REPO_ROOT / "README.md"
CROSSMAP_PATH = REPO_ROOT / "Core" / "Symbology_Translator_Crossmap.md"
CYBERNETICS_PATH = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "references" / "cybernetics_ai.md"
SKILL_PATH = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "SKILL.md"
CONTRADICTION_PATH = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "references" / "contradiction_index.md"
REFERENCES_DIR = REPO_ROOT / ".agents" / "skills" / "grimoire-translator" / "references"

ROMAN_TO_INT = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}
INT_TO_ROMAN = {v: k for k, v in ROMAN_TO_INT.items()}

def normalize(text: str) -> str:
    """Normalize curly quotes, markdown formatting, and whitespace."""
    if not text:
        return ""
    t = text.strip()
    t = t.replace('“', '"').replace('”', '"').replace('„', '"').replace('″', '"')
    t = t.replace('’', "'").replace('‘', "'").replace('′', "'")
    t = re.sub(r'[\*_]', '', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = " ".join(t.split())
    t = t.strip("\"' ")
    return t

def norm_gate(g: str) -> str:
    n = normalize(g)
    if n.startswith("The "):
        n = n[4:].strip()
    return n

def parse_canon(ms_text: str):
    chap_matches = list(re.finditer(r"^Chapter ([IVX]+) — The Realm of (.+)$", ms_text, re.M))
    if len(chap_matches) != 10:
        print(f"FAIL: Expected exactly 10 chapters in manuscript, found {len(chap_matches)}")
        sys.exit(1)
        
    canon = {}
    for i, m in enumerate(chap_matches):
        num = m.group(1)
        name = m.group(2).strip()
        start = m.end()
        end = chap_matches[i+1].start() if i + 1 < len(chap_matches) else len(ms_text)
        chap_text = ms_text[start:end]
        elem_lines = [l.strip() for l in chap_text.splitlines() if l.strip()]
        elem = elem_lines[0] if elem_lines else ""
        gate_m = re.search(r"The Gate — (.+)", chap_text)
        gate = gate_m.group(1).strip() if gate_m else ""
        whisper_m = re.search(r"Gatekeeper[’\']s Whisper", chap_text)
        whisper = [l.strip() for l in chap_text[whisper_m.end():].splitlines() if l.strip()][0] if whisper_m else ""
        key_m = re.search(r"^The Key$", chap_text, re.M)
        key = [l.strip() for l in chap_text[key_m.end():].splitlines() if l.strip()][0] if key_m else ""
        rem_m = re.search(r"^The Remnant Key$", chap_text, re.M)
        rem_key = [l.strip() for l in chap_text[rem_m.end():].splitlines() if l.strip()][0] if rem_m else ""
        
        canon[num] = {
            "index": i + 1,
            "name": name,
            "element": elem,
            "gate": gate,
            "whisper": whisper,
            "key": key,
            "remnant_key": rem_key,
        }
    return canon

def verify_codex(canon, codex_path=CODEX_PATH):
    failures = 0
    content = codex_path.read_text(encoding="utf-8")
    sections = re.findall(r'###\s+([IVX]+)\s+—\s+The Realm of\s+([^\n]+)\n(.*?)(?=###|\Z)', content, re.S)
    if len(sections) != 10:
        print(f"FAIL {codex_path.name}: expected 10 sections, found {len(sections)}")
        return 1, len(sections)
    
    for num, name, sec in sections:
        expected = canon[num]
        elem_m = re.search(r'\-\s+\*\*Subtitle\s*/\s*Element:\*\*\s*(.+)', sec)
        gate_m = re.search(r'\-\s+\*\*Gate:\*\*\s*([^\(\n]+)', sec)
        whisper_m = re.search(r"\-\s+\*\*Gatekeeper's Whisper:\*\*\s*(.+)", sec)
        key_m = re.search(r'\-\s+\*\*The Key:\*\*\s*(.+)', sec)
        rem_m = re.search(r'\-\s+\*\*The Remnant Key:\*\*\s*(.+)', sec)
        
        if not elem_m or normalize(elem_m.group(1)) != normalize(expected["element"]):
            print(f"FAIL {codex_path.name} Realm {num} Element mismatch: expected='{expected['element']}', found='{elem_m.group(1) if elem_m else None}'")
            failures += 1
        if not gate_m or norm_gate(gate_m.group(1)) != norm_gate(expected["gate"]):
            print(f"FAIL {codex_path.name} Realm {num} Gate mismatch: expected='{expected['gate']}', found='{gate_m.group(1) if gate_m else None}'")
            failures += 1
        if not whisper_m or normalize(whisper_m.group(1)) != normalize(expected["whisper"]):
            print(f"FAIL {codex_path.name} Realm {num} Whisper mismatch: expected='{expected['whisper']}', found='{whisper_m.group(1) if whisper_m else None}'")
            failures += 1
        if not key_m or normalize(key_m.group(1)) != normalize(expected["key"]):
            print(f"FAIL {codex_path.name} Realm {num} Key mismatch: expected='{expected['key']}', found='{key_m.group(1) if key_m else None}'")
            failures += 1
        if not rem_m or normalize(rem_m.group(1)) != normalize(expected["remnant_key"]):
            print(f"FAIL {codex_path.name} Realm {num} Remnant Key mismatch: expected='{expected['remnant_key']}', found='{rem_m.group(1) if rem_m else None}'")
            failures += 1
    return failures, len(sections)

def verify_cli(canon, cli_path=CLI_PATH):
    failures = 0
    sys.path.insert(0, str(cli_path.parent))
    import grimoire_cli
    if len(grimoire_cli.REALMS) != 10:
        print(f"FAIL {cli_path.name}: expected 10 REALMS, found {len(grimoire_cli.REALMS)}")
        return 1, len(grimoire_cli.REALMS)
    
    for idx in range(1, 11):
        data = grimoire_cli.REALMS.get(idx)
        num = INT_TO_ROMAN[idx]
        expected = canon[num]
        if not data:
            print(f"FAIL {cli_path.name} missing Realm {idx}")
            failures += 1
            continue
        if normalize(data.get('element')) != normalize(expected['element']):
            print(f"FAIL {cli_path.name} Realm {idx} Element mismatch")
            failures += 1
        if norm_gate(data.get('gate')) != norm_gate(expected['gate']):
            print(f"FAIL {cli_path.name} Realm {idx} Gate mismatch")
            failures += 1
        if normalize(data.get('key')) != normalize(expected['key']):
            print(f"FAIL {cli_path.name} Realm {idx} Key mismatch")
            failures += 1
        if normalize(data.get('remnant_key')) != normalize(expected['remnant_key']):
            print(f"FAIL {cli_path.name} Realm {idx} Remnant Key mismatch")
            failures += 1
        if normalize(data.get('whisper')) != normalize(expected['whisper']):
            print(f"FAIL {cli_path.name} Realm {idx} Whisper mismatch")
            failures += 1
    return failures, len(grimoire_cli.REALMS)

def verify_readme(canon, readme_path=README_PATH):
    failures = 0
    content = readme_path.read_text(encoding="utf-8")
    rows = re.findall(r'\|\s*\*\*([IVX]+)\s*—\s*([^|\*]+)\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|', content)
    if len(rows) != 10:
        print(f"FAIL {readme_path.name}: expected 10 table rows, found {len(rows)}")
        return 1, len(rows)
    
    for num, name, elem, gate, key in rows:
        expected = canon[num]
        if normalize(name) != normalize(expected["name"]):
            print(f"FAIL {readme_path.name} Realm {num} Name mismatch")
            failures += 1
        if normalize(elem) != normalize(expected["element"]):
            print(f"FAIL {readme_path.name} Realm {num} Element mismatch")
            failures += 1
        if norm_gate(gate) != norm_gate(expected["gate"]):
            print(f"FAIL {readme_path.name} Realm {num} Gate mismatch")
            failures += 1
        if normalize(key) != normalize(expected["key"]):
            print(f"FAIL {readme_path.name} Realm {num} Key mismatch")
            failures += 1
    return failures, len(rows)

def verify_crossmap(canon, crossmap_path=CROSSMAP_PATH):
    failures = 0
    content = crossmap_path.read_text(encoding="utf-8")
    dossiers = re.findall(
        r'###\s+([IVX]+)\s+—\s+[^\(]+\(([^\)]+)\)\s*\n'
        r'\*\*Gate:\*\*\s*([^·\n]+)·\s*\*\*Key:\*\*\s*([^·\n]+)·\s*\*\*Remnant Key:\*\*\s*([^\n]+)\s*\n'
        r'\*\*Whisper:\*\*\s*([^\n]+)',
        content
    )
    if len(dossiers) != 10:
        print(f"FAIL {crossmap_path.name}: expected 10 dossier headers, found {len(dossiers)}")
        return 1, len(dossiers)
    
    for num, elem, gate_short, key, rem_key, whisper in dossiers:
        expected = canon[num]
        if normalize(elem) != normalize(expected["element"]):
            print(f"FAIL {crossmap_path.name} Realm {num} Element mismatch")
            failures += 1
        g_short = gate_short.strip()
        rec1 = norm_gate(f"The Gate of {g_short}")
        rec2 = norm_gate(f"The Gate of the {g_short}")
        exp_gate = norm_gate(expected["gate"])
        if exp_gate not in (rec1, rec2):
            print(f"FAIL {crossmap_path.name} Realm {num} Gate mismatch: expected='{exp_gate}', reconstructed='{rec1}'/'{rec2}'")
            failures += 1
        if normalize(key) != normalize(expected["key"]):
            print(f"FAIL {crossmap_path.name} Realm {num} Key mismatch")
            failures += 1
        if normalize(rem_key) != normalize(expected["remnant_key"]):
            print(f"FAIL {crossmap_path.name} Realm {num} Remnant Key mismatch")
            failures += 1
        if normalize(whisper) != normalize(expected["whisper"]):
            print(f"FAIL {crossmap_path.name} Realm {num} Whisper mismatch")
            failures += 1
    return failures, len(dossiers)

def verify_cybernetics(canon, cyber_path=CYBERNETICS_PATH):
    failures = 0
    content = cyber_path.read_text(encoding="utf-8")
    rows = re.findall(r'\|\s*\*\*([IVX]+)\s*—\s*([^|\*]+)\*\*\s*<br>\s*\*?\(([^\)]+)\)\*?\s*\|', content)
    if len(rows) != 10:
        print(f"FAIL {cyber_path.name}: expected 10 table rows, found {len(rows)}")
        return 1, len(rows)
    
    for num, name, elem in rows:
        expected = canon[num]
        if normalize(name) != normalize(expected["name"]):
            print(f"FAIL {cyber_path.name} Realm {num} Name mismatch")
            failures += 1
        if normalize(elem) != normalize(expected["element"]):
            print(f"FAIL {cyber_path.name} Realm {num} Element mismatch: expected='{expected['element']}', found='{elem}'")
            failures += 1
            
    all_canon_gates = {norm_gate(c["gate"]) for c in canon.values()}
    cyber_gates = re.findall(r'(?<!Remnant\s)\b((?:The\s+)?Gate of [A-Za-z\s]+?)(?=\s*\(|[\,\.\n]|$)', content)
    for cg in cyber_gates:
        if norm_gate(cg) not in all_canon_gates:
            print(f"FAIL {cyber_path.name} unknown Gate name: '{cg}'")
            failures += 1
            
    all_canon_keys = {normalize(c["key"]): c for c in canon.values()}
    cyber_quotes = re.findall(r'[\"\u201c]([^\u201d\"\n]+)[\"\u201d]', content)
    quoted_keys_checked = 0
    for q in cyber_quotes:
        nq = normalize(q)
        if nq in all_canon_keys:
            quoted_keys_checked += 1
    return failures, len(rows)

def verify_skill(canon, skill_path=SKILL_PATH):
    failures = 0
    content = skill_path.read_text(encoding="utf-8")
    
    # Step 2 Keys (10 Realms)
    step2_keys = re.findall(r'-\s+\*\*([IVX]+)\s+([A-Za-z\s]+):\*\*\s+([^,]+),\s+.*?Key:\s+\*?\"([^\"]+)\"\*?', content)
    if len(step2_keys) != 10:
        print(f"FAIL {skill_path.name}: expected 10 Step 2 Keys, found {len(step2_keys)}")
        failures += 1
    else:
        for num, name, elem, key in step2_keys:
            expected = canon[num]
            if normalize(name) != normalize(expected["name"]):
                print(f"FAIL {skill_path.name} Step 2 Realm {num} Name mismatch")
                failures += 1
            if normalize(elem) != normalize(expected["element"]):
                print(f"FAIL {skill_path.name} Step 2 Realm {num} Element mismatch")
                failures += 1
            if normalize(key) != normalize(expected["key"]):
                print(f"FAIL {skill_path.name} Step 2 Realm {num} Key mismatch")
                failures += 1

    # Part 4 Remnant Keys (10 Remnants)
    rem_keys = re.findall(r'-\s+\*[^\*]+\*\s+\(Realm\s+([IVX]+)\s+Remnant\)\s+—\s+Remnant Key:\s+\*?\"([^\"]+)\"\*?', content)
    if len(rem_keys) != 10:
        print(f"FAIL {skill_path.name}: expected 10 Remnant Keys in Part 4, found {len(rem_keys)}")
        failures += 1
    else:
        for num, rem_key in rem_keys:
            expected = canon[num]
            if normalize(rem_key) != normalize(expected["remnant_key"]):
                print(f"FAIL {skill_path.name} Realm {num} Remnant Key mismatch")
                failures += 1
    return failures, len(rem_keys)

def verify_contradiction(canon, contradiction_path=CONTRADICTION_PATH):
    failures = 0
    content = contradiction_path.read_text(encoding="utf-8")
    all_canon_keys = {normalize(c["key"]): c for c in canon.values()}
    all_canon_gates = {norm_gate(c["gate"]): c for c in canon.values()}
    all_canon_whispers = {normalize(c["whisper"]): c for c in canon.values()}
    all_canon_rem = {normalize(c["remnant_key"]): c for c in canon.values()}
    
    quotes = re.findall(r'[\"\u201c]([^\u201d\"\n]+)[\"\u201d]', content)
    canon_quotes_checked = 0
    for q in quotes:
        nq = normalize(q)
        ng = norm_gate(q)
        if nq in all_canon_keys or nq in all_canon_rem or nq in all_canon_whispers or ng in all_canon_gates:
            canon_quotes_checked += 1
    return failures, canon_quotes_checked

def verify_quoted_sweep(ms_text, sweep_files):
    failures = 0
    norm_ms = normalize(ms_text)
    
    EXTERNAL_PATTERNS = [
        re.compile(p, re.IGNORECASE) for p in [
            r"Chi-Rho",
            r"O\.T\.O\.",
            r"E\.G\.C\.",
            r"Fraternitas Saturni",
            r"Luciferian",
            r"Draconian",
            r"Qliphoth",
            r"Crowley",
            r"Dee",
            r"Mathers",
            r"Jesus Prayer",
            r"Hesychas",
            r"Thelem",
            r"Golden Dawn",
            r"Gnostic",
            r"civilization of love",
            r"Second-pass change log",
            r"Updated Status",
            r"Works cited",
            r"Sources added",
            r"living_traditions\.md",
        ]
    ]
    CANDIDATE_PAT = re.compile(r'(Realm|Key|Remnant|Whisper|Gate|\bI\s+)', re.IGNORECASE)

    sweep_checked = 0
    for fpath in sweep_files:
        content = fpath.read_text(encoding="utf-8")
        for line_no, line in enumerate(content.splitlines(), 1):
            if not CANDIDATE_PAT.search(line):
                continue
            quotes = re.findall(r'[\"\u201c]([^\u201d\"\n]{12,})[\"\u201d]', line)
            for q in quotes:
                check_q = q
                if '…' in check_q:
                    check_q = check_q.split('…')[0]
                elif '...' in check_q:
                    check_q = check_q.split('...')[0]
                nq = normalize(check_q)
                if len(nq) >= 12:
                    sweep_checked += 1
                    if nq not in norm_ms:
                        if not any(p.search(line) for p in EXTERNAL_PATTERNS):
                            print(f"FAIL {fpath.name}:{line_no} quoted text not in manuscript: '{q}'")
                            failures += 1
    return failures, sweep_checked

def main():
    if not MANUSCRIPT_PATH.exists():
        print(f"Error: Manuscript not found at {MANUSCRIPT_PATH}")
        sys.exit(1)
        
    ms_text = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    canon = parse_canon(ms_text)
    
    total_failures = 0
    counts = {}
    
    f, c = verify_codex(canon)
    total_failures += f
    counts["realms_codex.md sections"] = c
    
    f, c = verify_cli(canon)
    total_failures += f
    counts["grimoire_cli.py REALMS"] = c
    
    f, c = verify_readme(canon)
    total_failures += f
    counts["README.md table rows"] = c
    
    f, c = verify_crossmap(canon)
    total_failures += f
    counts["Symbology_Translator_Crossmap.md dossiers"] = c
    
    f, c = verify_cybernetics(canon)
    total_failures += f
    counts["cybernetics_ai.md table rows"] = c
    
    f, c = verify_skill(canon)
    total_failures += f
    counts["SKILL.md Remnant Keys"] = c
    
    f, c = verify_contradiction(canon)
    total_failures += f
    counts["contradiction_index.md canon quotes"] = c
    
    sweep_files = [
        CODEX_PATH,
        CROSSMAP_PATH,
        SKILL_PATH,
        README_PATH,
        CYBERNETICS_PATH,
        CONTRADICTION_PATH,
    ] + sorted([p for p in REFERENCES_DIR.glob("*.md") if p not in (CODEX_PATH, CYBERNETICS_PATH, CONTRADICTION_PATH)])
    
    f, c = verify_quoted_sweep(ms_text, sweep_files)
    total_failures += f
    counts["Quoted-text sweep (>=12 chars)"] = c
    
    print("\n--- Canon Verification Summary ---")
    for k, v in counts.items():
        print(f"  {k}: {v} checked")
    print(f"Total failures: {total_failures}")
    
    if total_failures == 0:
        print("\nSUCCESS: All strict per-Realm checks and quoted-text sweeps PASSED!")
        sys.exit(0)
    else:
        print(f"\nFAILURE: {total_failures} check(s) failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
