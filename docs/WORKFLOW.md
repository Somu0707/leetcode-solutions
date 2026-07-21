# ⚙️ Workflow

## Overview

This document describes the execution flow of the AI-Powered LeetCode Documentation Generator.

Starting from the repository scan, the workflow fetches problem metadata, generates AI explanations, builds problem documentation, and finally updates the repository homepage.

---

# Complete Execution Flow

```text
                Start
                  │
                  ▼
        Execute scripts/main.py
                  │
                  ▼
        RepositoryScanner.scan()
                  │
                  ▼
      Discover Problem Directories
                  │
                  ▼
      ┌─────────────────────────────┐
      │ For Each Problem Directory │
      └─────────────────────────────┘
                  │
                  ▼
      Check metadata.json exists?
           │                │
           │Yes             │No
           ▼                ▼
 Load Existing Metadata   Fetch Metadata
           │                │
           └────────┬───────┘
                    ▼
            Save metadata.json
                    │
                    ▼
          Read solution.cpp
                    │
                    ▼
         Generate AI Explanation
                    │
                    ▼
                Save ai.md
                    │
                    ▼
       Convert HTML → Markdown
                    │
                    ▼
      Extract Documentation Sections
                    │
                    ▼
      Build Problem README.md
                    │
                    ▼
     Repeat for Remaining Problems
                    │
                    ▼
       Compute Repository Statistics
                    │
                    ▼
        Build Root README.md
                    │
                    ▼
                  Finish
```

---

# Step 1 — Repository Discovery

The execution begins in:

```text
scripts/main.py
```

The RepositoryScanner scans the repository and identifies all valid LeetCode problem folders.

Example:

```text
0001-two-sum
0278-first-bad-version
0504-base-7
0875-koko-eating-bananas
```

Only directories following the repository naming convention are processed.

---

# Step 2 — Metadata Generation

For each problem, the application checks whether metadata already exists.

If metadata is missing (or refreshed), the MetadataService sends a GraphQL request to LeetCode.

The response includes:

- Problem ID
- Title
- Difficulty
- Acceptance Rate
- HTML Description
- Example Test Cases
- Hints
- Topics

The MetadataHandler stores the response as:

```text
metadata.json
```

---

# Step 3 — Read Solution

The corresponding C++ solution is loaded from:

```text
solution.cpp
```

This becomes the primary input for AI analysis.

---

# Step 4 — AI Analysis

The AI Generator combines:

- Problem description
- Metadata
- C++ solution

and sends them to Google Gemini AI.

Gemini produces:

- Solution Explanation
- Thought Process
- Intuition
- Approach
- Algorithm
- Dry Run
- Edge Cases
- Complexity Analysis
- Key Takeaways

The generated explanation is saved as:

```text
ai.md
```

---

# Step 5 — Problem Parsing

LeetCode provides problem descriptions as HTML.

TemplateRenderer converts HTML into Markdown and extracts structured sections.

Extracted sections include:

- Problem Statement
- Examples
- Constraints
- Follow-up

This keeps the generated README clean and readable.

---

# Step 6 — Problem README Generation

ProblemReadmeBuilder combines:

- metadata.json
- Parsed Markdown
- AI Explanation
- solution.cpp
- Markdown Template

to generate:

```text
README.md
```

for the current problem.

Each problem becomes a self-contained learning resource.

---

# Step 7 — Repository Statistics

After all problem READMEs are generated, ReadmeBuilder scans every solved problem.

It computes:

- Total Problems
- Difficulty Distribution
- Average Acceptance Rate
- Progress Percentage
- Top Topics
- Recent Problems
- Monthly Activity

These statistics populate the repository homepage.

---

# Step 8 — Root README Generation

RootReadmeGenerator loads:

```text
templates/README_TEMPLATE.md
```

Placeholder values are replaced with live repository statistics.

The generated file becomes:

```text
README.md
```

at the project root.

This serves as the dashboard for the repository.

---

# Data Flow

```text
solution.cpp
        │
        ▼
 metadata.json
        │
        ▼
 Google Gemini AI
        │
        ▼
      ai.md
        │
        ▼
Problem README.md
```

---

# Repository Flow

```text
All Problem READMEs
         │
         ▼
 Repository Statistics
         │
         ▼
README_TEMPLATE.md
         │
         ▼
 Root README.md
```

---

# Generated Files

For every solved problem:

```text
0001-two-sum/
│
├── solution.cpp
├── metadata.json
├── ai.md
└── README.md
```

Repository-wide:

```text
README.md
```

---

# Error Recovery

The workflow is designed so each stage is independent.

If one stage fails:

- Metadata can be regenerated.
- AI explanations can be regenerated.
- Problem READMEs can be rebuilt.
- Root README can be regenerated independently.

This modular approach simplifies debugging and maintenance.

---

# Benefits of the Workflow

- Automated documentation generation
- Minimal manual effort
- Consistent formatting
- AI-assisted educational explanations
- Live repository statistics
- Easily extensible architecture
- Suitable for GitHub Actions automation

---

# Future Workflow Enhancements

Potential improvements include:

- Incremental updates for changed solutions only
- AI response caching
- Parallel processing for multiple problems
- Automatic GitHub Actions execution
- Multi-language solution support
- Pluggable AI providers
- Unit and integration tests

---

# Summary

The workflow transforms a simple LeetCode solution into a fully documented educational resource through a sequence of automated steps.

Each stage has a single responsibility, making the system modular, maintainable, and easy to extend.