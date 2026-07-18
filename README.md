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

# 📖 About

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

# 📊 Repository Dashboard

## 📈 Repository Statistics

| Metric | Value |
|--------|------:|
| Total Problems | **4** |
| Easy | 🟢 4 |
| Medium | 🟠 0 |
| Hard | 🔴 0 |
| Average Acceptance | **61.04%** |
| Unique Topics | **7** |

---

## 🎯 Progress to Next Milestone

```text
░░░░░░░░░░░░░░░░░░░░ 4 / 100 (4.0%)
```

**Next Milestone:** **100 Problems**

---

## 🏷️ Top Topics

- **String** : 2
- **Array** : 1
- **Hash Table** : 1
- **Binary Search** : 1
- **Interactive** : 1

---

## 🆕 Recently Solved

- 🆕 [Reverse Words in a String III](./0557-reverse-words-in-a-string-iii/README.md)
- 🆕 [Base 7](./0504-base-7/README.md)
- 🆕 [First Bad Version](./0278-first-bad-version/README.md)
- 🆕 [Two Sum](./0001-two-sum/README.md)

---

## 🟢 Repository Health

| Component | Status |
|----------|:------:|
| Metadata Cache | ✅ |
| AI README Generator | ✅ |
| GitHub Actions | ✅ |
| Root README Generator | ✅ |

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
│   ├── metadata_handler.py
│   ├── metadata_service.py
│   ├── readme_builder.py
│   ├── template_renderer.py
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

| # | Problem | Difficulty | Acceptance | Topics | README |
|---:|---------|------------|-----------:|--------|:------:|
| 0001 | [Two Sum](./0001-two-sum/README.md) | 🟢 Easy | 57.82% | Array, Hash Table | ✅ |
| 0278 | [First Bad Version](./0278-first-bad-version/README.md) | 🟢 Easy | 47.37% | Binary Search, Interactive | ✅ |
| 0504 | [Base 7](./0504-base-7/README.md) | 🟢 Easy | 54.89% | Math, String | ✅ |
| 0557 | [Reverse Words in a String III](./0557-reverse-words-in-a-string-iii/README.md) | 🟢 Easy | 84.08% | Two Pointers, String | ✅ |

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

# 🎯 Roadmap

- ✅ AI README Generation
- ✅ Metadata Caching
- ✅ Dynamic Repository Statistics
- ✅ Progress Dashboard
- ✅ Top Topics Analytics
- ✅ Recently Solved Section
- 🔜 Monthly Activity Dashboard
- 🔜 Coding Streak Tracker
- 🔜 Repository Analytics

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

Made with ❤️ using Python • Google Gemini AI • GitHub Actions

</div>