"""Assemble paper.md from draft sections, fill placeholders, merge bibliographies."""
import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
d = root / "coding"

# merged bibliography, first definition of a key wins
seen, entries = set(), []
for bib in ["refs_key.bib", "refs_part1.bib", "refs_part2.bib", "refs_extra.bib"]:
    text = (d / bib).read_text()
    for m in re.finditer(r"@\w+\{([^,]+),.*?\n\}", text, re.S):
        key = m.group(1).strip()
        if key not in seen:
            seen.add(key)
            entries.append(m.group(0))
(root / "paper" / "refs.bib").write_text("\n\n".join(entries) + "\n")

subprocess.run(["python3", "-I", str(root / "scripts" / "build_table.py")], check=True, capture_output=True)
rows = json.loads((d / "master.json").read_text())
n = len(rows)
partial = sum(1 for r in rows if r["R"][0] != "○" and r["R"][7] != "○")
cov = (d / "coverage_by_community.md").read_text()
master = (d / "master_table.md").read_text()

paper = "".join((root / "draft" / f).read_text() + "\n\n" for f in ["sec0.md", "sec1-5.md", "sec6-11.md"])
paper = (paper.replace("{{N}}", str(n)).replace("{{R1R8_PARTIAL}}", str(partial))
         .replace("{{COVERAGE_TABLE}}", cov).replace("{{MASTER_TABLE}}", master))
(root / "paper" / "paper.md").write_text(paper.replace("bibliography: refs.bib", "bibliography: refs.bib"))

used = set(re.findall(r"@([A-Za-z0-9_]+)", paper)) - {"misc", "inproceedings", "article"}
missing = sorted(k for k in used if k not in seen)
print(f"works coded: {n}; R1&R8 partial: {partial}; bib entries: {len(seen)}; cited keys: {len(used)}")
print("MISSING KEYS:", missing)
