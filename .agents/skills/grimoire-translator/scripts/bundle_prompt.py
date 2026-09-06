#!/usr/bin/env python3
"""
Bundle Script: Combines SKILL.md and all references into a single, self-contained
prompt file (GROK_SKILL_PROMPT.md) that can be pasted directly into Grok, Claude,
ChatGPT, or any LLM as a System Prompt / Custom Instruction.
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent.parent
OUTPUT_FILE = REPO_ROOT / "GROK_SKILL_PROMPT.md"

FILES_TO_MERGE = [
    ("Master Skill Instructions", SKILL_DIR / "SKILL.md"),
    ("The Ten Realms Codex", SKILL_DIR / "references" / "realms_codex.md"),
    ("Contradiction Index & Boundary Rules", SKILL_DIR / "references" / "contradiction_index.md"),
    ("Cybernetics & Frontier AI Mapping", SKILL_DIR / "references" / "cybernetics_ai.md"),
    ("Living Traditions Reference", SKILL_DIR / "references" / "living_traditions.md"),
]

def bundle():
    content = []
    content.append("# Grimoire Translator: Complete System Prompt & Knowledge Bundle\n")
    content.append("> **How to use:** Copy and paste this entire document into Grok's Custom Instructions, System Prompt, Claude Project Knowledge, or a Custom GPT.\n")
    content.append("> Once loaded, the LLM will respond to `Grimoire translate <text> to <system>`, `Grimoire analyze <text>`, and conversational queries.\n\n")
    content.append("---\n\n")

    for title, filepath in FILES_TO_MERGE:
        if not filepath.exists():
            print(f"Warning: {filepath} not found.")
            continue
        
        file_text = filepath.read_text(encoding="utf-8").strip()
        # Strip frontmatter from SKILL.md if present
        if file_text.startswith("---"):
            parts = file_text.split("---", 2)
            if len(parts) >= 3:
                file_text = parts[2].strip()

        content.append(f"<!-- ============================================================ -->")
        content.append(f"<!-- SECTION: {title.upper()} -->")
        content.append(f"<!-- ============================================================ -->\n")
        content.append(file_text)
        content.append("\n\n---\n\n")

    OUTPUT_FILE.write_text("\n".join(content), encoding="utf-8")
    print(f"Successfully generated self-contained bundle at: {OUTPUT_FILE}")

if __name__ == "__main__":
    bundle()
