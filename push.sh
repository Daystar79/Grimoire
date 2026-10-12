#!/usr/bin/env bash
# Push changes to GitHub with automated canon verification and bundle generation.
# Usage: ./push.sh ["commit message"]
set -e

# Always run from repository root
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

BRANCH="$(git branch --show-current)"
if [ -z "$BRANCH" ]; then
  echo "Error: HEAD is detached. Please checkout a branch before pushing." >&2
  exit 1
fi

COMMIT_MSG="$*"

# Optional prompt if running in an interactive terminal and no message was provided
if [ -z "$COMMIT_MSG" ]; then
  if [ -t 0 ]; then
    read -r -p "Enter commit message (press Enter for default): " input_msg
    COMMIT_MSG="$input_msg"
  fi
fi

# Fallback default message
if [ -z "$COMMIT_MSG" ]; then
  COMMIT_MSG="Update $(date +'%Y-%m-%d %H:%M:%S')"
fi

# If prompt bundle script exists, regenerate GROK_SKILL_PROMPT.md
if [ -f ".agents/skills/grimoire-translator/scripts/bundle_prompt.py" ]; then
  echo "==> Regenerating prompt bundle (GROK_SKILL_PROMPT.md)..."
  python3 .agents/skills/grimoire-translator/scripts/bundle_prompt.py
fi

# Run canon verification if script exists
if [ -f ".agents/skills/grimoire-translator/scripts/verify_canon.py" ]; then
  echo "==> Verifying canon integrity..."
  python3 .agents/skills/grimoire-translator/scripts/verify_canon.py
fi

# Check if there are any changes (modified, added, deleted, untracked)
HAS_CHANGES=false
if [ -n "$(git status --porcelain)" ]; then
  HAS_CHANGES=true
fi

# Check if there are unpushed commits
UNPUSHED=0
if git rev-parse --verify "origin/$BRANCH" >/dev/null 2>&1; then
  UNPUSHED=$(git rev-list --count "origin/$BRANCH..$BRANCH" 2>/dev/null || echo 0)
else
  UNPUSHED=1
fi

if [ "$HAS_CHANGES" = false ] && [ "$UNPUSHED" -eq 0 ]; then
  echo "Everything is clean and up to date. Nothing to commit or push."
  exit 0
fi

if [ "$HAS_CHANGES" = true ]; then
  echo "==> Staging changes..."
  git add -A

  echo "==> Committing: \"$COMMIT_MSG\"..."
  git commit -m "$COMMIT_MSG"
fi

echo "==> Pushing to origin/$BRANCH..."
git push -u origin "$BRANCH"

echo "==> Successfully pushed to origin/$BRANCH."
echo "Current commit: $(git log -1 --oneline)"
