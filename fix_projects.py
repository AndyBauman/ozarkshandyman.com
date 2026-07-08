import re
from pathlib import Path

p = Path(__file__).parent / "site_content.py"
lines = p.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith("((") and stripped.endswith(")),"):
        inner = stripped[1:-2]
        tuples = re.findall(r"\(([^)]+)\)", inner)
        titles: list[str] = []
        for t in tuples:
            titles.extend(x.strip().strip('"') for x in t.split(","))
        projects = []
        for title in titles[:4]:
            projects.append((title, f"Premium {title.lower()} for Ozarks homes."))
        indent = line[: len(line) - len(line.lstrip())]
        items = ", ".join(f'("{t}", "{d}")' for t, d in projects)
        out.append(f"{indent}({items}),")
    else:
        out.append(line)
p.write_text("\n".join(out), encoding="utf-8")
print("fixed projects")
