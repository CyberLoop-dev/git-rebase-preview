<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=Git%20Rebase%20Preview&fontColor=ffffff&fontSize=36" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=Git%20Rebase%20Preview;Inspect%20before%20rewriting%20history" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/git-rebase-preview?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/git-rebase-preview)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/git-rebase-preview?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/git-rebase-preview)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Preview and validate interactive-rebase todo files without running Git or changing repository history.**

</div>

## ✨ Overview

A read-only parser for Git interactive-rebase plans. It summarizes actions and flags common formatting mistakes before you start a rebase.

## 🚀 Features

- 🧭 Lists commit actions in their planned order.
- 🔤 Understands common one-letter action aliases.
- ⚠️ Reports malformed commit IDs and missing arguments.
- 🛡️ Never invokes Git or edits repository history.

## 🧪 Demo

```text
pick a1b2c3d Add parser
squash d4e5f6a Combine tests

2 commit actions; valid
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/git-rebase-preview.git
cd git-rebase-preview
python main.py rebase-todo.txt
```

## 🧰 Tech Stack

Python 3.10+ · Standard library only.

## 🗂️ Folder Structure

```text
git-rebase-preview/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Core todo parsing and validation
- [x] Unit tests and CI
- [ ] More merge and autosquash syntax coverage
- [ ] Optional colored terminal timeline

## 🤝 Contributing

Share a minimal todo file for parser issues. Tests must confirm that new parsing remains read-only.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>
