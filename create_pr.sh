#!/usr/bin/env bash
set -euo pipefail
REPO_URL="${1:-}"
if [ -z "$REPO_URL" ]; then
  echo "Usage: ./create_pr.sh <your-github-repo-ssh-or-https-url>"
  exit 1
fi

git init
git remote add origin "$REPO_URL"
git checkout -b feat/cac-2024-analysis
git add .
git commit -m "CAC 2024 analysis: code, figures, and data story (contains 23f1001029@ds.study.iitm.ac.in)"
git push -u origin feat/cac-2024-analysis

if command -v gh >/dev/null 2>&1; then
  gh pr create --fill --title "CAC 2024: analysis, visualizations, and data story" --body-file README.md
else
  echo "Now open a PR on GitHub using your browser."
fi