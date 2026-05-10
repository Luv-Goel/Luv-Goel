# Contributing to Luv Goel's Projects

> *「一人では速く行けるが、共に行けば遠くまで行ける。」*
> *"Alone you go fast, together you go far."*

Thank you for taking the time to contribute. All my public projects follow the same ground rules — read this once and you're good across all repos.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Before You Start](#before-you-start)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting a Pull Request](#submitting-a-pull-request)
- [Commit Convention](#commit-convention)
- [Code Style](#code-style)
- [Getting Help](#getting-help)

---

## Code of Conduct

Be respectful, constructive, and professional. Harassment of any kind will not be tolerated. Simple.

---

## Before You Start

1. **Check existing issues** — your bug or feature idea might already be tracked.
2. **Open an issue first** before writing code for non-trivial changes. This avoids wasted effort if the direction isn't aligned.
3. **Fork the repository** and work off a feature branch — never off `main`.

---

## How to Contribute

### Reporting Bugs

Open an issue with the following:

```
**Summary:** One-line description of the bug
**Steps to reproduce:**
  1. ...
  2. ...
**Expected behaviour:** ...
**Actual behaviour:** ...
**Environment:** OS, language version, relevant deps
**Logs / Screenshots:** (if applicable)
```

### Suggesting Features

Open an issue tagged `enhancement` and describe:
- **The problem** you're solving (not just the solution)
- **Proposed approach** — high level is fine
- **Alternatives considered**

### Submitting a Pull Request

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/<repo>.git
cd <repo>

# 2. Create a branch
git checkout -b feat/your-feature-name

# 3. Make your changes, then stage and commit
git add .
git commit -m "feat: describe what you built"

# 4. Push and open a PR
git push origin feat/your-feature-name
```

**PR checklist:**
- [ ] Follows the commit convention below
- [ ] Tested locally — include test commands if applicable
- [ ] No unrelated changes (keep PRs focused)
- [ ] Linked to the relevant issue (`Closes #123`)

---

## Commit Convention

All commits must follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | When to use |
|---|---|
| `feat:` | New feature or capability |
| `fix:` | Bug fix |
| `docs:` | Documentation only changes |
| `refactor:` | Code restructure, no behaviour change |
| `perf:` | Performance improvement |
| `test:` | Adding or updating tests |
| `chore:` | Build process, tooling, deps |
| `ci:` | CI/CD changes |

**Examples:**
```
feat: add redis caching layer to inference endpoint
fix: resolve race condition in job scheduler
docs: update API reference for /infer route
```

---

## Code Style

- **Python** — follow [PEP 8](https://pep8.org/); use `black` for formatting
- **Go** — `gofmt` is non-negotiable
- **TypeScript / JavaScript** — ESLint + Prettier (config in repo)
- **General** — prefer clarity over cleverness; leave the code better than you found it

---

## Getting Help

If you're stuck, open a [Discussion](https://github.com/Luv-Goel) or drop a message at **luvgoelxyz1234@gmail.com**.

All contributions — big or small — are genuinely appreciated. 🚀
