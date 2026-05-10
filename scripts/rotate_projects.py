#!/usr/bin/env python3
"""
rotate_projects.py
Randomly selects 4 repos from the full list and patches the
<!-- PROJECTS_START --> ... <!-- PROJECTS_END --> block in README.md.
Add or remove repos from the REPOS list below to control what's eligible.
"""

import random
import re

# ── Edit this list to add/remove eligible repos ──────────────────────────────
REPOS = [
    "contextflow",
    "flowBeat",
    "CodeVista",
    "onnx-model-surgery",
    "Auto-Storyboard-Video-Creator",
    "vtuber-schedule-api",
]
# ─────────────────────────────────────────────────────────────────────────────

BASE = "https://github-readme-stats-sigma-five.vercel.app/api/pin/"
PARAMS = (
    "?username=Luv-Goel"
    "&theme=tokyonight"
    "&bg_color=0d1117"
    "&title_color=7aa2f7"
    "&icon_color=7dcfff"
    "&text_color=c0caf5"
    "&border_color=1a1b2e"
    "&border_radius=12"
)

selected = random.sample(REPOS, min(4, len(REPOS)))

# Build pairs of cards on each line for a 2-column layout
rows = []
for i in range(0, len(selected), 2):
    pair = selected[i : i + 2]
    line_parts = []
    for repo in pair:
        line_parts.append(
            f'<a href="https://github.com/Luv-Goel/{repo}">'
            f'<img src="{BASE}&repo={repo}{PARAMS}" /></a>'
        )
    rows.append("\n".join(line_parts))

cards_block = "\n\n".join(rows)

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- PROJECTS_START -->.*?<!-- PROJECTS_END -->",
    f"<!-- PROJECTS_START -->\n{cards_block}\n<!-- PROJECTS_END -->",
    content,
    flags=re.DOTALL,
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✓ Rotated featured projects: {', '.join(selected)}")
