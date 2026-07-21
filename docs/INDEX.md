# 📚 Documentation Index

Welcome to the documentation for the **AI-Powered LeetCode Documentation Generator**.

This directory contains detailed documentation describing the system architecture, execution workflow, engineering decisions, and internal implementation.

Whether you're a contributor, reviewer, or recruiter, these documents provide a complete understanding of how the project is designed and why it was built this way.

---

# Documentation Roadmap

| Document | Description |
|----------|-------------|
| 📖 **ARCHITECTURE.md** | High-level architecture, project structure, and responsibilities of each module. |
| ⚙️ **WORKFLOW.md** | Step-by-step execution flow from scanning the repository to generating documentation. |
| 🔄 **SEQUENCE_DIAGRAM.md** | Mermaid sequence diagrams and component interaction diagrams. |
| 🧠 **DESIGN_DECISIONS.md** | Engineering decisions, architectural trade-offs, and rationale behind the implementation. |

---

# Documentation Structure

```text
docs/
│
├── INDEX.md
├── ARCHITECTURE.md
├── WORKFLOW.md
├── SEQUENCE_DIAGRAM.md
└── DESIGN_DECISIONS.md
```

---

# Reading Guide

Depending on your interest, you can start with different documents.

## 👋 New to the project?

Start here:

```
README.md
        │
        ▼
ARCHITECTURE.md
        │
        ▼
WORKFLOW.md
```

This provides a high-level understanding of the project.

---

## 👨‍💻 Planning to contribute?

Read in this order:

```
ARCHITECTURE.md
        │
        ▼
WORKFLOW.md
        │
        ▼
DESIGN_DECISIONS.md
```

This explains how the system is organized, how it executes, and the reasoning behind key implementation choices.

---

## 🔍 Interested in the implementation?

Read:

```
SEQUENCE_DIAGRAM.md
        │
        ▼
WORKFLOW.md
```

These documents illustrate how components communicate and how data flows through the application.

---

## 🎯 Evaluating the engineering approach?

Start with:

```
DESIGN_DECISIONS.md
```

This document discusses:

- Architectural principles
- Trade-offs
- Technology choices
- Scalability
- Maintainability

---

# System Overview

The project automates the generation of documentation for solved LeetCode problems.

Its responsibilities include:

- Discovering solved problems
- Fetching problem metadata from LeetCode
- Parsing HTML into Markdown
- Generating AI-powered explanations
- Creating individual problem READMEs
- Building repository statistics
- Generating the repository homepage

---

# Documentation Philosophy

The documentation follows the same design principles as the codebase.

- Modular
- Easy to navigate
- Easy to maintain
- Focused on clarity
- Separated by responsibility

Each document focuses on one specific aspect of the project rather than trying to explain everything in a single file.

---

# Recommended Reading Order

```text
README.md
      │
      ▼
ARCHITECTURE.md
      │
      ▼
WORKFLOW.md
      │
      ▼
SEQUENCE_DIAGRAM.md
      │
      ▼
DESIGN_DECISIONS.md
```

Following this order provides a gradual understanding of the project—from high-level concepts to implementation details and engineering rationale.

---

# Future Documentation

As the project evolves, additional documentation may be added, such as:

- API Reference
- Configuration Guide
- Development Guide
- Testing Guide
- GitHub Actions Workflow
- Performance Optimizations
- Plugin Development Guide
- Changelog

---

# Final Notes

This documentation aims to make the project approachable for developers of all experience levels.

By documenting the architecture, workflow, and design decisions, the project becomes easier to understand, contribute to, and extend over time.

Thank you for taking the time to explore the project!