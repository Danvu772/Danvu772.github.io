# dan-docs

Personal technical site + documentation system.  
Built on Quarto · Void Protocol theme · JetBrains Mono

---

## Setup

### 1. Install Quarto
```bash
# macOS
brew install quarto

# or download from https://quarto.org/docs/get-started/
```

### 2. Install Python deps
```bash
pip install jupyter matplotlib numpy scikit-learn fastapi bleak aiosqlite
```

### 3. Install fonts (optional but recommended)
Download **JetBrains Mono** from https://www.jetbrains.com/lp/mono/  
Install system-wide for matplotlib to pick it up.

### 4. Preview site locally
```bash
cd dan-docs
quarto preview
```
Opens at `http://localhost:4848`. Live-reloads on save.

### 5. Render full site
```bash
quarto render
# output goes to _site/
```

### 6. Deploy to GitHub Pages
```bash
quarto publish gh-pages
```

---

## Rendering a standalone PDF (homework)

From anywhere on your system:
```bash
quarto render path/to/hw3.ipynb --to pdf
```

Or with the alias (add to your `.zshrc`):
```bash
alias qpdf='quarto render --to pdf'
# then:
qpdf hw3.ipynb
```

For themed PDF from outside the project, point to the scss:
```yaml
# in your notebook's YAML frontmatter:
format:
  pdf:
    include-in-header: ~/dan-docs/pdf-overrides.scss
    geometry: "margin=1in"
```

---

## Project structure

```
dan-docs/
├── _quarto.yml              # site config & navbar
├── custom.scss              # Void Protocol — source of truth for all colors
├── pdf-overrides.scss       # print layer (white bg, adapted for paper)
├── index.qmd                # landing page
├── assets/
│   └── matplotlib_theme.py  # import this in every notebook
├── research/
│   ├── index.qmd            # auto-listing page
│   └── labsense.ipynb       # example portfolio piece
├── blog/
│   └── index.qmd
└── coursework/
    ├── index.qmd
    └── ee445-svm.ipynb      # example homework notebook
```

---

## Adding a new notebook to the site

1. Drop the `.ipynb` in the right folder (`research/`, `blog/`, `coursework/`)
2. Add this YAML frontmatter in a **Raw** cell at the top:

```yaml
---
title: "Your Title"
author: "Dan Nguyen"
date: "2025-XX-XX"
description: "One sentence. Shows up in listing cards."
categories: [tag1, tag2]
format:
  html:
    theme: [../custom.scss]
    toc: true
  pdf:
    include-in-header: ../pdf-overrides.scss
---
```

3. `quarto preview` — it appears in the listing automatically.

---

## Matplotlib theme usage

```python
import sys
sys.path.insert(0, '..')          # or use absolute path
from assets.matplotlib_theme import apply_void_theme, vc

apply_void_theme('dark')          # for website
# apply_void_theme('print')       # for PDF submission

# Color shortcuts:
plt.plot(x, y, color=vc.cyan)
plt.plot(x, z, color=vc.green)
```

---

## Switching between Void Protocol palettes

All colors are defined as CSS variables in `custom.scss`.  
Change `--vp-accent` at the top to instantly retheme everything.

Ghost Signal alt accent: `#80cbc4`  
Swap it in one line if you want to experiment.
