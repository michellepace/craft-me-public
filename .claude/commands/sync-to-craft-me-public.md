---
description: Sync committed files to craft-me-public repo
allowed-tools: Bash(git:*), Bash(rm:*), Bash(tar:*), Bash(cd:*), Bash(echo:*)
disable-model-invocation: true
---

# Sync to Public Portfolio

Sync **git-committed versions** of selected files to `~/projects/craft-me-public`.

## What Gets Synced

- `.claude/` (recursive)
- `portfolio/` (recursive)
- `README.md`
- `ailearnlog.jpg`

## Pre-flight Check

Before running the sync, verify the committed README.md does not contain links to `craft-me-private`. Run:

```bash
git show HEAD:README.md | grep -i "craft-me-private" && echo "🚨 STOP: README contains private repo links!" || echo "✅ README clean"
```

If the check fails, **stop and notify the user** — do not proceed with the sync.

## Execute Sync

```bash
#!/bin/bash
set -e

SOURCE="/home/mp/projects/craft-me-private"
TARGET="/home/mp/projects/craft-me-public"

echo "================================"
echo "Sync: Private → Public Portfolio"
echo "================================"
echo ""

echo "[1/6] Validating repositories..."
if [ ! -d "$SOURCE/.git" ]; then
  echo "❌ Source is not a git repo: $SOURCE"
  exit 1
fi
if [ ! -d "$TARGET" ]; then
  echo "❌ Target directory missing: $TARGET"
  exit 1
fi
echo "✅ Source: $SOURCE"
echo "✅ Target: $TARGET"
echo ""

echo "[2/6] Cleaning target directories..."
rm -rf "$TARGET/.claude" "$TARGET/portfolio"
rm -f "$TARGET/README.md" "$TARGET/ailearnlog.jpg"
echo "✅ Target cleaned"
echo ""

echo "[3/6] Exporting committed files from HEAD..."
cd "$SOURCE"
git archive HEAD .claude/ portfolio/ README.md ailearnlog.jpg | tar -x -C "$TARGET"
echo "✅ Exported to $TARGET"
echo ""

echo "[4/6] Staging changes..."
cd "$TARGET"
git add -A
echo "✅ All changes staged"
echo ""

echo "[5/6] Staged changes in target repo:"
echo ""
git status --short
echo ""

echo "[6/6] Summary"
echo "================================"
echo "✅ Sync completed successfully"
echo "================================"
```

## Next Steps

Show the user the git status output above.

Be helpful and ask me if I want to run the target project slash command `/commit`. Files are already staged.

Be happy too, because I like emojis 🙂
