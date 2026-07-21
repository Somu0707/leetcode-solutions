# 🏗️ System Architecture

## Overview

The AI-Powered LeetCode Documentation Generator automates the creation of rich documentation for solved LeetCode problems.

Instead of manually writing explanations for every solution, the system fetches problem metadata from LeetCode, analyzes the C++ solution using Google Gemini AI, and generates professional Markdown documentation for both individual problems and the entire repository.

The project follows a modular architecture where each component has a single responsibility, making it easy to maintain, extend, and test.

---

# High-Level Architecture

```text
                   LeetCode Repository
                           │
                           ▼
                 Repository Scanner
                           │
                           ▼
                 Problem Directories
                           │
                           ▼
                  Metadata Service
               (LeetCode GraphQL API)
                           │
                           ▼
                     metadata.json
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
      Read solution.cpp         HTML Problem Statement
              │                         │
              ▼                         ▼
         Google Gemini AI       Template Renderer
              │                         │
              ▼                         ▼
            ai.md              Structured Markdown
              │                         │
              └────────────┬────────────┘
                           ▼
                Problem README Builder
                           │
                           ▼
          Individual Problem README.md
                           │
                           ▼
                Root README Builder
                           │
                           ▼
                   Repository README.md
```

---

# Project Structure

```text
leetcode-solutions/
│
├── templates/
│   ├── README_TEMPLATE.md
│   └── PROBLEM_README_TEMPLATE.md
│
├── scripts/
│   ├── main.py
│   ├── scanner.py
│   ├── metadata_service.py
│   ├── metadata_handler.py
│   ├── ai_generator.py
│   ├── prompt_template.py
│   ├── template_renderer.py
│   ├── problem_readme_builder.py
│   ├── readme_builder.py
│   └── generate_root_readme.py
│
├── docs/
│   └── ARCHITECTURE.md
│
├── 0001-two-sum/
│   ├── solution.cpp
│   ├── metadata.json
│   ├── ai.md
│   └── README.md
│
└── README.md
```

---

# Component Responsibilities

## 1. RepositoryScanner

The RepositoryScanner is the entry point of the pipeline.

### Responsibilities

- Scan the repository
- Discover solved LeetCode problems
- Ignore unrelated directories
- Return a sorted list of problem folders

Example output:

```python
[
    "0001-two-sum",
    "0278-first-bad-version",
    "0504-base-7"
]
```

---

## 2. MetadataService

MetadataService communicates with the LeetCode GraphQL API.

It downloads all information required to document a problem.

### Retrieved Information

- Problem ID
- Title
- Difficulty
- Acceptance Rate
- HTML Problem Description
- Example Test Cases
- Hints
- Topics

The service only communicates with LeetCode and does not write any files.

---

## 3. MetadataHandler

MetadataHandler manages local storage of problem metadata.

### Responsibilities

- Save metadata.json
- Load metadata.json
- Check whether metadata already exists

Example

```json
{
    "id": "1",
    "title": "Two Sum",
    "difficulty": "Easy",
    "content": "...",
    "topics": [
        "Array",
        "Hash Table"
    ]
}
```

Separating metadata retrieval from metadata storage makes the system easier to maintain.

---

## 4. TemplateRenderer

LeetCode provides problem statements as HTML.

TemplateRenderer converts that HTML into structured Markdown.

### Responsibilities

- HTML → Markdown conversion
- Extract Problem Statement
- Extract Examples
- Extract Constraints
- Extract Follow-up

This class is responsible only for parsing problem content.

---

## 5. AIGenerator

AIGenerator uses Google Gemini AI to analyze the submitted solution.

### Inputs

- Problem metadata
- Problem description
- C++ solution

### Outputs

- Solution Explanation
- Thought Process
- Intuition
- Approach
- Algorithm
- Dry Run
- Edge Cases
- Complexity Analysis
- Key Takeaways

The generated explanation is stored in:

```
ai.md
```

---

## 6. ProblemReadmeBuilder

ProblemReadmeBuilder combines all generated information into a professional README.

### Inputs

- metadata.json
- Parsed Markdown
- AI Explanation
- solution.cpp
- Markdown Template

### Output

```
0001-two-sum/
    README.md
```

This class is responsible only for formatting documentation.

---

## 7. ReadmeBuilder

ReadmeBuilder generates repository-wide statistics.

### Statistics Generated

- Total Solved Problems
- Difficulty Distribution
- Average Acceptance Rate
- Progress Bar
- Most Solved Topic
- Top Topics
- Monthly Activity
- Recently Solved Problems

The builder prepares placeholder values used by the root README template.

---

## 8. RootReadmeGenerator

RootReadmeGenerator creates the repository homepage.

It combines

- README_TEMPLATE.md
- Repository statistics

to generate

```
README.md
```

This acts as the dashboard for the repository.

---

# End-to-End Execution Flow

```text
main.py
   │
   ▼
RepositoryScanner
   │
   ▼
Discover Problem Folders
   │
   ▼
MetadataService
   │
   ▼
metadata.json
   │
   ▼
Read solution.cpp
   │
   ▼
Google Gemini AI
   │
   ▼
ai.md
   │
   ▼
TemplateRenderer
   │
   ▼
ProblemReadmeBuilder
   │
   ▼
Problem README.md
   │
   ▼
ReadmeBuilder
   │
   ▼
RootReadmeGenerator
   │
   ▼
Repository README.md
```

---

# Design Principles

The project follows the **Single Responsibility Principle (SRP)**.

Each module performs one specific task.

| Component | Responsibility |
|-----------|----------------|
| RepositoryScanner | Discover problem folders |
| MetadataService | Fetch problem metadata |
| MetadataHandler | Store and retrieve metadata |
| TemplateRenderer | Parse HTML into Markdown |
| AIGenerator | Generate AI explanations |
| ProblemReadmeBuilder | Generate problem documentation |
| ReadmeBuilder | Compute repository statistics |
| RootReadmeGenerator | Generate repository homepage |

This modular design makes the project easier to maintain, test, and extend.

---

# Scalability

The architecture allows several future enhancements without major refactoring.

Possible improvements include:

- Incremental documentation generation
- AI response caching
- Parallel processing
- GitHub Actions automation
- Multiple programming language support
- Unit testing
- Plugin-based architecture
- Multiple AI provider support

---

# Summary

The project combines:

- LeetCode GraphQL API
- Google Gemini AI
- Python Automation
- Markdown Generation
- Template-Based Documentation
- Repository Analytics

to automatically transform solved LeetCode problems into well-structured educational documentation with minimal manual effort.