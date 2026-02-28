# 📝 Git Commands Reference for CartoonifyAI

## Quick Reference for ArpitSingh8

---

## 🚀 Initial Push to GitHub

### Step 1: Create Repository on GitHub
Go to: https://github.com/new
- Name: `CartoonifyAI`
- Public repository
- Don't initialize with README

### Step 2: Run These Commands
```bash
git init
git add .
git commit -m "Initial commit: Complete CartoonifyAI project"
git remote add origin https://github.com/ArpitSingh8/CartoonifyAI.git
git branch -M main
git push -u origin main
```

**Or simply run:**
```bash
git_push.bat
```

---

## 📁 Basic Git Commands

### Check Status
```bash
git status
```
Shows which files have been modified

### Add Files
```bash
# Add all files
git add .

# Add specific file
git add home.py

# Add specific folder
git add backend/
```

### Commit Changes
```bash
# Commit with message
git commit -m "Your message here"

# Commit with detailed message
git commit -m "Title" -m "Detailed description"
```

### Push to GitHub
```bash
# First time
git push -u origin main

# After that
git push
```

### Pull from GitHub
```bash
git pull origin main
```

---

## 🌿 Branch Commands

### Create New Branch
```bash
git checkout -b feature-name
```

### Switch Branch
```bash
git checkout main
git checkout feature-name
```

### List Branches
```bash
git branch
```

### Merge Branch
```bash
# Switch to main first
git checkout main

# Merge feature branch
git merge feature-name
```

### Delete Branch
```bash
# Delete local branch
git branch -d feature-name

# Delete remote branch
git push origin --delete feature-name
```

---

## 📊 View History

### View Commit History
```bash
# Full history
git log

# Compact history
git log --oneline

# Last 5 commits
git log -5

# With graph
git log --graph --oneline
```

### View Changes
```bash
# See what changed
git diff

# See staged changes
git diff --staged
```

---

## ↩️ Undo Changes

### Undo Unstaged Changes
```bash
# Undo changes in specific file
git checkout -- home.py

# Undo all changes
git checkout -- .
```

### Unstage Files
```bash
# Unstage specific file
git reset home.py

# Unstage all
git reset
```

### Undo Last Commit (Keep Changes)
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (Discard Changes)
```bash
git reset --hard HEAD~1
```

---

## 🔗 Remote Commands

### View Remotes
```bash
git remote -v
```

### Add Remote
```bash
git remote add origin https://github.com/ArpitSingh8/CartoonifyAI.git
```

### Change Remote URL
```bash
git remote set-url origin https://github.com/ArpitSingh8/CartoonifyAI.git
```

### Remove Remote
```bash
git remote remove origin
```

---

## 🏷️ Tag Commands

### Create Tag
```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"
```

### Push Tags
```bash
# Push specific tag
git push origin v1.0.0

# Push all tags
git push --tags
```

### List Tags
```bash
git tag
```

### Delete Tag
```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## 🔍 Search Commands

### Search in Files
```bash
# Search for text
git grep "search term"

# Search in specific files
git grep "search term" -- "*.py"
```

### Search Commits
```bash
# Search commit messages
git log --grep="bug fix"

# Search by author
git log --author="ArpitSingh8"
```

---

## 🛠️ Configuration

### Set User Info
```bash
git config --global user.name "Arpit Singh"
git config --global user.email "your.email@example.com"
```

### View Configuration
```bash
# View all config
git config --list

# View specific config
git config user.name
```

### Set Default Editor
```bash
git config --global core.editor "code"
```

---

## 📦 Stash Commands

### Save Work Temporarily
```bash
# Stash changes
git stash

# Stash with message
git stash save "Work in progress"
```

### View Stashes
```bash
git stash list
```

### Apply Stash
```bash
# Apply latest stash
git stash apply

# Apply specific stash
git stash apply stash@{0}
```

### Delete Stash
```bash
# Delete latest stash
git stash drop

# Delete specific stash
git stash drop stash@{0}

# Delete all stashes
git stash clear
```

---

## 🔄 Update Commands

### Update from Remote
```bash
# Fetch changes
git fetch origin

# Pull and merge
git pull origin main

# Pull and rebase
git pull --rebase origin main
```

---

## 🎯 Common Workflows

### Workflow 1: Add New Feature
```bash
# Create feature branch
git checkout -b feature-email-verification

# Make changes...

# Add and commit
git add .
git commit -m "feat: Add email verification"

# Push to GitHub
git push -u origin feature-email-verification

# Create Pull Request on GitHub
# After merge, switch back to main
git checkout main
git pull origin main
```

### Workflow 2: Fix Bug
```bash
# Create fix branch
git checkout -b fix-login-error

# Make changes...

# Add and commit
git add .
git commit -m "fix: Resolve login redirect issue"

# Push to GitHub
git push -u origin fix-login-error
```

### Workflow 3: Update Documentation
```bash
# Make changes to README.md

# Add and commit
git add README.md
git commit -m "docs: Update installation instructions"

# Push
git push
```

---

## 🚨 Emergency Commands

### Discard All Local Changes
```bash
git reset --hard HEAD
git clean -fd
```

### Recover Deleted Commit
```bash
# Find commit hash
git reflog

# Recover commit
git checkout <commit-hash>
```

### Fix Wrong Commit Message
```bash
# Change last commit message
git commit --amend -m "New message"

# Push (force if already pushed)
git push --force
```

---

## 📝 Commit Message Templates

### Feature
```bash
git commit -m "feat: Add user profile page"
```

### Bug Fix
```bash
git commit -m "fix: Resolve password validation error"
```

### Documentation
```bash
git commit -m "docs: Update README with new features"
```

### Style
```bash
git commit -m "style: Improve dashboard layout"
```

### Refactor
```bash
git commit -m "refactor: Optimize image processing function"
```

### Test
```bash
git commit -m "test: Add unit tests for authentication"
```

### Performance
```bash
git commit -m "perf: Improve image loading speed"
```

---

## 🔐 Authentication

### Using Personal Access Token
```bash
# When prompted for password, use your token
git push
Username: ArpitSingh8
Password: <paste-your-token-here>
```

### Save Credentials
```bash
# Cache credentials for 1 hour
git config --global credential.helper cache

# Cache credentials for 24 hours
git config --global credential.helper 'cache --timeout=86400'

# Store credentials permanently (use with caution)
git config --global credential.helper store
```

---

## 📊 Useful Aliases

### Set Up Aliases
```bash
# Short status
git config --global alias.st status

# Short log
git config --global alias.lg "log --oneline --graph"

# Short commit
git config --global alias.cm commit

# Short checkout
git config --global alias.co checkout
```

### Use Aliases
```bash
git st          # Instead of git status
git lg          # Instead of git log --oneline --graph
git cm -m "msg" # Instead of git commit -m "msg"
git co main     # Instead of git checkout main
```

---

## 🎓 Best Practices

### 1. Commit Often
- Make small, focused commits
- Each commit should do one thing

### 2. Write Good Messages
- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Start with type: feat, fix, docs, etc.

### 3. Pull Before Push
```bash
git pull origin main
git push origin main
```

### 4. Use Branches
- Don't work directly on main
- Create feature branches
- Merge after review

### 5. Review Before Commit
```bash
git status
git diff
git add .
git commit -m "message"
```

---

## 🆘 Troubleshooting

### Problem: Merge Conflict
```bash
# Edit conflicted files
# Look for <<<<<<< HEAD markers
# Choose which changes to keep
# Remove conflict markers

git add .
git commit -m "Resolve merge conflict"
```

### Problem: Pushed Wrong Files
```bash
# Remove from Git but keep locally
git rm --cached filename

# Commit and push
git commit -m "Remove sensitive file"
git push
```

### Problem: Need to Undo Push
```bash
# Revert commit (creates new commit)
git revert HEAD
git push

# Or force push (dangerous!)
git reset --hard HEAD~1
git push --force
```

---

## 📚 Learn More

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Interactive Tutorial:** https://learngitbranching.js.org

---

## ✅ Quick Checklist

Before pushing:
- [ ] All files added
- [ ] Good commit message
- [ ] No sensitive data
- [ ] Code tested
- [ ] Documentation updated

After pushing:
- [ ] Verify on GitHub
- [ ] Check README displays
- [ ] Add topics/tags
- [ ] Set description

---

**Your GitHub:** https://github.com/ArpitSingh8
**Your Project:** https://github.com/ArpitSingh8/CartoonifyAI

---

*Keep this file handy for quick reference!*
