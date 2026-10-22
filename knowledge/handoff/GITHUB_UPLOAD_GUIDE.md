# Add handoff package to GitHub
Target: https://github.com/Kogulanathan69/BuildMind-Knowledge-.git

This package is **not yet pushed**. Keep existing repository files, work on a new branch or review changes before committing.

Windows PowerShell (Git installed):
```powershell
git clone https://github.com/Kogulanathan69/BuildMind-Knowledge-.git
cd BuildMind-Knowledge-
git checkout -b docs/ai-handoff-2026-10-22
New-Item -ItemType Directory -Force knowledge/handoff | Out-Null
# Copy the four included handoff files into knowledge/handoff using File Explorer.
git add knowledge/handoff
git status
git commit -m "docs: add BuildMind AI knowledge handoff and source inventory"
git push -u origin docs/ai-handoff-2026-10-22
```
Open a PR on GitHub to review/merge. If branch already exists, choose a distinct name.

## Source documents
Do not bulk-upload raw 2+GB ZIP collection to ordinary Git. GitHub blocks files >100MB and large binaries make history unwieldy. Keep originals in backed-up storage, and upload only verified, permitted datasets (e.g., selected CSV/JSON and openly redistributable PDFs) using **Git LFS** when appropriate. Record stable source links, filename, version and hash in the source inventory. Exclude confidential or third-party restricted materials.
