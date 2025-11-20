# Windows Setup Guide 🪟

**Quick start guide for Windows users setting up the SDD Agentic Framework**

## ⚠️ Critical Requirements

### 1. Install Claude Code FIRST
**Before anything else:**
1. Visit [claude.ai/code](https://claude.ai/code)
2. Install Claude Code for Windows
3. Verify: Open a terminal and run `claude --version`
4. Login: Run `claude login`

**Why?** Claude Code is your AI assistant throughout setup. If you encounter ANY errors, Claude Code can help you fix them instantly.

---

## 2. Install Git for Windows

Git for Windows includes **Git Bash**, which you MUST use to run this framework.

1. Download: [git-scm.com](https://git-scm.com/download/win)
2. Run installer (accept all defaults)
3. **Important**: Git Bash is automatically installed

### Finding Git Bash

After installation:
- **Search**: Type "Git Bash" in Windows search
- **Pin it**: Right-click → Pin to taskbar for easy access
- **Location**: Usually `C:\Program Files\Git\git-bash.exe`

---

## 3. Install Node.js

1. Download: [nodejs.org](https://nodejs.org/) (v18 or higher)
2. Run installer (accept all defaults)
3. Verify in Git Bash:
   ```bash
   node --version  # Should show v18.x.x or higher
   npm --version   # Should show v9.x.x or higher
   ```

---

## 🚀 Quick Setup

### Step 1: Open Git Bash
**DO NOT use PowerShell or CMD!**
- Click the Git Bash icon you pinned to taskbar
- Or search for "Git Bash" in Windows search

### Step 2: Clone the Repository
```bash
# Navigate to your projects folder (example)
cd /c/Users/YourUsername/projects

# Clone the framework
git clone https://github.com/kelleysd-apps/sdd-agentic-framework.git my-project
cd my-project
```

### Step 3: Run Setup
```bash
# Try this first
npm run setup

# If that fails, try this
npm run setup:windows

# If that fails, try this
bash .specify/scripts/setup.sh
```

### Step 4: If You Get Errors
**STOP! Don't troubleshoot alone.**

1. Open Claude Code in your project directory
2. Paste the error message
3. Ask: "I'm on Windows setting up the SDD framework and got this error. Can you help?"
4. Follow Claude's instructions

---

## ❌ Common Mistakes

### Mistake 1: Using PowerShell or CMD
**Wrong:**
```powershell
PS C:\Users\Brian> npm run setup
'.' is not recognized as an internal or external command
```

**Right:**
```bash
Brian@DESKTOP-XYZ MINGW64 ~/projects/my-project
$ npm run setup
```

**Fix**: Close PowerShell. Open Git Bash.

---

### Mistake 2: Running Commands Outside Git Bash
**Symptom**: Commands like `chmod`, `bash`, or `./script.sh` don't work

**Fix**: You're in the wrong terminal. Open Git Bash.

---

### Mistake 3: Not Installing Claude Code First
**Problem**: You try to setup without Claude Code, hit errors, and get stuck

**Fix**: Install Claude Code first. It's your lifeline.

---

## 🎯 Complete Setup Checklist

Work through this checklist in order:

- [ ] ✅ Claude Code installed and working (`claude --version`)
- [ ] ✅ Git for Windows installed (includes Git Bash)
- [ ] ✅ Node.js v18+ installed (`node --version` in Git Bash)
- [ ] ✅ Project cloned using Git Bash
- [ ] ✅ Opened Git Bash (not PowerShell/CMD)
- [ ] ✅ Navigated to project directory in Git Bash
- [ ] ✅ Ran `npm run setup` or `npm run setup:windows`
- [ ] ✅ Setup completed successfully (or asked Claude for help)
- [ ] ✅ Opened Claude Code in project directory
- [ ] ✅ Ready to run `/specify` and start developing!

---

## 💡 Pro Tips for Windows Users

### Tip 1: Create a Desktop Shortcut
Right-click Git Bash → Create Shortcut → Move to Desktop

### Tip 2: Set Starting Directory
Right-click Git Bash shortcut → Properties → Start in:
```
C:\Users\YourUsername\projects
```

### Tip 3: Always Use Git Bash for This Framework
- PowerShell ❌
- CMD ❌
- Git Bash ✅

### Tip 4: Use Claude Code for Everything
Got a question? Error? Confusion? Ask Claude Code!

Example questions:
```
"How do I navigate to my projects folder in Git Bash?"
"I got a permission denied error. What does this mean?"
"Can you explain how to customize the constitution?"
"What's the difference between /specify and /plan?"
```

---

## 🆘 Getting Help

### Primary Support: Claude Code
1. Open Claude Code in your project directory
2. Paste error messages or describe your issue
3. Ask specific questions
4. Claude has full context of the framework

### If Claude Can't Help
1. Check [START_HERE.md](./START_HERE.md) for detailed setup instructions
2. Review [FRAMEWORK_README.md](./README.md) for framework documentation
3. Create an issue: [GitHub Issues](https://github.com/kelleysd-apps/sdd-agentic-framework/issues)

---

## ✅ Verify Setup Worked

After setup completes, verify everything works:

```bash
# In Git Bash, from your project directory

# 1. Check Node.js
node --version
# Should show v18.x.x or higher

# 2. Check npm
npm --version
# Should show v9.x.x or higher

# 3. Check framework files exist
ls .specify/
# Should show: memory/ scripts/ templates/ config/

# 4. Check constitution exists
cat .specify/memory/constitution.md | head -n 5
# Should show constitution content

# 5. Open Claude Code
claude code .
# Should open Claude Code in your project
```

If all checks pass: **🎉 You're ready to develop!**

---

## 🚀 Next Steps

With setup complete, start using the framework:

### 1. Open Claude Code
```bash
# From Git Bash in your project directory
claude code .
```

### 2. Create Your First PRD (Optional but Recommended)
In Claude Code, type:
```
/create-prd
```

### 3. Create Your First Feature
In Claude Code, type:
```
/specify "user authentication"
```

### 4. Let Claude Code Guide You
Claude will:
- Ask clarifying questions
- Generate specifications
- Create implementation plans
- Coordinate agents to build features
- Help with any issues

---

**Remember**: You're not alone! Claude Code is your co-pilot throughout this journey. Use it! 🤖
