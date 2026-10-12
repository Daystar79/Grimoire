#!/usr/bin/env bash
# Pull latest changes from GitHub for current branch with canon verification.
# Usage: ./pull.sh
set -e

# Always run from repository root
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

BRANCH="$(git branch --show-current)"
if [ -z "$BRANCH" ]; then
  echo "Error: HEAD is detached. Please checkout a branch before pulling." >&2
  exit 1
fi

echo "==> Pulling latest changes for branch '$BRANCH' from origin..."

if ! git diff-index --quiet HEAD -- 2>/dev/null; then
  echo "Notice: You have uncommitted changes in your working tree."
fi

git pull origin "$BRANCH" "$@"

# Run canon verification if script exists
if [ -f ".agents/skills/grimoire-translator/scripts/verify_canon.py" ]; then
  echo "==> Verifying canon integrity..."
  python3 .agents/skills/grimoire-translator/scripts/verify_canon.py
fi

echo "==> Successfully pulled latest changes."
echo "Current commit: $(git log -1 --oneline)"
