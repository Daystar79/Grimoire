#!/usr/bin/env python3
"""
verify_canon.py: Asserts that all Gates, Keys, Remnant Keys, Whispers, and Elements
across realms_codex.md, grimoire_cli.py, README.md, and Symbology_Translator_Crossmap.md
match Sources/Manuscript_Master.md verbatim.
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

def normalize(text: str) -> str:
    """Normalize curly quotes, markdown formatting, and whitespace."""
    if not text:
        return ""
    t = text.strip()
    # Strip markdown bold/italic asterisks or underscores
    t = t.strip("*_").strip()
    # Replace curly quotes with straight
    t = t.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    if (t.startswith('"') and t.endswith('"')) or (t.startswith("'") and t.endswith("'")):
        t = t[1:-1].strip()
    return t

def assert_in_manuscript(term: str, ms_text: str, context: str, allow_strip_the: bool = False):
    norm_term = normalize(term)
    norm_ms = normalize(ms_text)
    
    if norm_term in norm_ms:
        return True
    
    if allow_strip_the:
        # Try stripping leading "The " or adding "The "
        if norm_term.startswith("The "):
            without_the = norm_term[4:].strip()
            if without_the in norm_ms:
                return True
        else:
            with_the = f"The {norm_term}"
            if with_the in norm_ms:
                return True

    print(f"FAILED assertion in {context}: '{term}' not found in Manuscript_Master.md")
    return False

def verify_codex(ms_text: str) -> bool:
    print("Checking realms_codex.md...")
    content = CODEX_PATH.read_text(encoding="utf-8")
    ok = True
    
    # Check each chapter header
    sections = re.split(r'###\s+[IVX]+\s+—\s+The Realm of\s+', content)[1:]
    for idx, sec in enumerate(sections, 1):
        ctx = f"realms_codex.md Realm {idx}"
        elem_m = re.search(r'\-\s+\*\*Subtitle\s*/\s*Element:\*\*\s*(.+)', sec)
        gate_m = re.search(r'\-\s+\*\*Gate:\*\*\s*([^\(\n]+)', sec)
        whisper_m = re.search(r"\-\s+\*\*Gatekeeper's Whisper:\*\*\s*(.+)", sec)
        key_m = re.search(r'\-\s+\*\*The Key:\*\*\s*(.+)', sec)
        rem_key_m = re.search(r'\-\s+\*\*The Remnant Key:\*\*\s*(.+)', sec)
        
        if elem_m:
            ok &= assert_in_manuscript(elem_m.group(1), ms_text, f"{ctx} Element")
        if gate_m:
            ok &= assert_in_manuscript(gate_m.group(1), ms_text, f"{ctx} Gate", allow_strip_the=True)
        if whisper_m:
            ok &= assert_in_manuscript(whisper_m.group(1), ms_text, f"{ctx} Whisper")
        if key_m:
            ok &= assert_in_manuscript(key_m.group(1), ms_text, f"{ctx} Key")
        if rem_key_m:
            ok &= assert_in_manuscript(rem_key_m.group(1), ms_text, f"{ctx} Remnant Key")
            
    return ok

def verify_cli(ms_text: str) -> bool:
    print("Checking grimoire_cli.py REALMS dict...")
    sys.path.insert(0, str(CLI_PATH.parent))
    import grimoire_cli
    ok = True
    
    for realm_id, data in grimoire_cli.REALMS.items():
        ctx = f"grimoire_cli.py Realm {realm_id} ({data.get('name')})"
        ok &= assert_in_manuscript(data['element'], ms_text, f"{ctx} element")
        ok &= assert_in_manuscript(data['gate'], ms_text, f"{ctx} gate", allow_strip_the=True)
        ok &= assert_in_manuscript(data['key'], ms_text, f"{ctx} key")
        ok &= assert_in_manuscript(data['remnant_key'], ms_text, f"{ctx} remnant_key")
        ok &= assert_in_manuscript(data['whisper'], ms_text, f"{ctx} whisper")
    return ok

def verify_readme(ms_text: str) -> bool:
    print("Checking README.md Ten Realms table...")
    content = README_PATH.read_text(encoding="utf-8")
    ok = True
    
    # Table rows: | **I — Origin** | Dawn / Breath | Gate of First Light | *"I am aware..."* | ... |
    rows = re.findall(r'\|\s*\*\*[IVX]+\s*—\s*([^|\*]+)\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|', content)
    for idx, (name, elem, gate, key) in enumerate(rows, 1):
        ctx = f"README.md Realm {idx} ({name.strip()})"
        ok &= assert_in_manuscript(elem, ms_text, f"{ctx} Element")
        ok &= assert_in_manuscript(gate, ms_text, f"{ctx} Gate", allow_strip_the=True)
        ok &= assert_in_manuscript(key, ms_text, f"{ctx} Key")
    return ok

def verify_crossmap(ms_text: str) -> bool:
    print("Checking Symbology_Translator_Crossmap.md dossier headers...")
    content = CROSSMAP_PATH.read_text(encoding="utf-8")
    ok = True
    
    # Headers format:
    # ### I — Origin (Dawn / Breath)
    # **Gate:** First Light · **Key:** “I am aware that I am aware.” · **Remnant Key:** “I understand awareness.”
    # **Whisper:** “Let the first light reach you before you reach for it.”
    dossiers = re.findall(
        r'###\s+[IVX]+\s+—\s+[^\(]+\(([^\)]+)\)\s*\n'
        r'\*\*Gate:\*\*\s*([^·]+)·\s*\*\*Key:\*\*\s*([^·]+)·\s*\*\*Remnant Key:\*\*\s*([^\n]+)\s*\n'
        r'\*\*Whisper:\*\*\s*([^\n]+)',
        content
    )
    for idx, (elem, gate, key, rem_key, whisper) in enumerate(dossiers, 1):
        ctx = f"Symbology_Translator_Crossmap.md Realm {idx}"
        ok &= assert_in_manuscript(elem, ms_text, f"{ctx} Element")
        # In crossmap Gate is short (e.g. "First Light", "Open Ground") -> "The Gate of First Light", "The Gate of the Open Ground"
        gate_short = gate.strip()
        # Verify gate appears as part of a gate name
        gate_full1 = f"Gate of {gate_short}"
        gate_full2 = f"Gate of the {gate_short}"
        norm_ms = normalize(ms_text)
        if gate_short in norm_ms or gate_full1 in norm_ms or gate_full2 in norm_ms:
            pass
        else:
            print(f"FAILED assertion in {ctx} Gate: '{gate_short}' not recognized")
            ok = False
        ok &= assert_in_manuscript(key, ms_text, f"{ctx} Key")
        ok &= assert_in_manuscript(rem_key, ms_text, f"{ctx} Remnant Key")
        ok &= assert_in_manuscript(whisper, ms_text, f"{ctx} Whisper")
    return ok

def main():
    if not MANUSCRIPT_PATH.exists():
        print(f"Error: Manuscript not found at {MANUSCRIPT_PATH}")
        sys.exit(1)
        
    ms_text = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    
    codex_ok = verify_codex(ms_text)
    cli_ok = verify_cli(ms_text)
    readme_ok = verify_readme(ms_text)
    crossmap_ok = verify_crossmap(ms_text)
    
    if codex_ok and cli_ok and readme_ok and crossmap_ok:
        print("\nSUCCESS: All canon assertions passed verbatim against Manuscript_Master.md!")
        sys.exit(0)
    else:
        print("\nFAILURE: One or more canon checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
