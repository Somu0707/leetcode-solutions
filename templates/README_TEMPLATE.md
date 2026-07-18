# 🚀 LeetCode AI Automation

<div align="center">

### 🤖 Automatically generate professional AI-powered documentation for every accepted LeetCode solution.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-success?style=for-the-badge&logo=githubactions)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-orange?style=for-the-badge&logo=leetcode)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 About

Most LeetCode repositories contain only source code, making them difficult to revisit and understand later.

This project solves that problem by automatically generating a **well-structured AI-powered README** for every accepted LeetCode solution using **Google Gemini AI**.

Every time a new problem is pushed to GitHub, the workflow automatically:

- Detects newly added problems
- Generates an AI explanation
- Creates a professional README
- Updates the repository homepage
- Commits and pushes the changes

No manual documentation is required.

---

# ✨ Features

- 🤖 AI-generated explanation for every LeetCode problem
- ⚡ Fully automated using GitHub Actions
- 📁 Organized folder structure
- 📚 Dynamic repository homepage
- 🔄 Automatically skips existing README files
- 🚀 Zero manual documentation effort
- 💻 Clean and modular Python architecture

---

# 📊 Repository Statistics

| Metric | Value |
|---------|------:|
| 📚 Total Problems Solved | **{{TOTAL_PROBLEMS}}** |
| 🤖 AI Generated READMEs | **{{TOTAL_PROBLEMS}}** |
| ⚡ Automation Status | ✅ Active |
| 🔄 Last Updated | Automatically by GitHub Actions |

---

# 🏗️ Project Architecture

```text
                 LeetCode
                     │
                     ▼
               Accepted Solution
                     │
                     ▼
               LeetHub Extension
                     │
                     ▼
             GitHub Repository
                     │
                     ▼
             GitHub Actions CI
                     │
                     ▼
            Repository Scanner
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
 README Exists?               No README
         │                       │
      Skip Folder               ▼
                           Google Gemini AI
                                 │
                                 ▼
                       Generate README.md
                                 │
                                 ▼
                     Update Repository README
                                 │
                                 ▼
                       Commit & Push Changes
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Automation Scripts |
| Google Gemini API | AI README Generation |
| GitHub Actions | CI/CD Automation |
| Git | Version Control |
| Markdown | Documentation |
| LeetHub | Automatic Solution Upload |

---

# 📂 Repository Structure

```text
leetcode-solutions/
│
├── .github/
│   └── workflows/
│       └── leetcode-ai.yml
│
├── scripts/
│   ├── ai_generator.py
│   ├── scanner.py
│   ├── file_handler.py
│   ├── generate_root_readme.py
│   ├── main.py
│   └── ...
│
├── templates/
│   └── README_TEMPLATE.md
│
├── 0001-two-sum/
├── 0278-first-bad-version/
├── 0504-base-7/
├── 0557-reverse-words-in-a-string-iii/
│
└── README.md
```

---

# 📚 Solved Problems

{{PROBLEM_TABLE}}

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Somu0707/leetcode-solutions.git

cd leetcode-solutions
```

---

## Install Dependencies

```bash
pip install -r scripts/requirements.txt
```

---

## Configure Environment

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Locally

```bash
python scripts/main.py
```

---

# 🔄 Automation Workflow

```text
LeetCode
      │
      ▼
LeetHub Push
      │
      ▼
GitHub Actions Trigger
      │
      ▼
Repository Scanner
      │
      ▼
Gemini AI
      │
      ▼
Generate README
      │
      ▼
Update Root README
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
```

---

# 🎯 Future Improvements

- 📈 Easy / Medium / Hard Statistics
- 📊 Progress Dashboard
- 🔥 Recently Solved Problems
- 🏷️ Dynamic GitHub Badges
- 🤖 AI-generated LinkedIn Posts
- 📅 Daily Coding Streak Tracker
- 🌙 Interactive Dashboard

---

# 👨‍💻 Author

## Soma Sekhara Chari Mulugu

Computer Science Engineering Student

### Interests

- Data Structures & Algorithms
- Artificial Intelligence
- Cloud Computing
- Backend Development
- Automation

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

Made with ❤️ using Python, Google Gemini AI & GitHub Actions.

</div>