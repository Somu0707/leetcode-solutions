# 🔄 Sequence Diagram

## Overview

This document describes how different components of the AI-Powered LeetCode Documentation Generator interact during execution.

GitHub supports **Mermaid**, so the diagrams below render automatically in the repository.

---

# Complete System Sequence

```mermaid
sequenceDiagram
    autonumber

    participant User
    participant Main as main.py
    participant Scanner as RepositoryScanner
    participant Metadata as MetadataService
    participant Handler as MetadataHandler
    participant AI as Gemini AI
    participant Renderer as TemplateRenderer
    participant Problem as ProblemReadmeBuilder
    participant Root as RootReadmeGenerator

    User->>Main: Execute automation

    Main->>Scanner: Scan repository
    Scanner-->>Main: List of problem folders

    loop For every problem

        Main->>Handler: metadata exists?

        alt Metadata Missing

            Main->>Metadata: Fetch metadata
            Metadata-->>Main: Problem metadata
            Main->>Handler: Save metadata.json

        else Metadata Exists

            Handler-->>Main: Load metadata.json

        end

        Main->>Main: Read solution.cpp

        Main->>AI: Generate explanation
        AI-->>Main: AI explanation

        Main->>Main: Save ai.md

        Main->>Renderer: Parse HTML
        Renderer-->>Main: Markdown sections

        Main->>Problem: Generate README.md
        Problem-->>Main: README created

    end

    Main->>Root: Generate repository README
    Root-->>Main: README.md updated

    Main-->>User: Automation completed
```

---

# Metadata Generation

```mermaid
sequenceDiagram
    autonumber

    participant Main
    participant MetadataService
    participant LeetCode
    participant MetadataHandler

    Main->>MetadataService: Fetch metadata

    MetadataService->>LeetCode: GraphQL Request

    LeetCode-->>MetadataService: Problem Details

    MetadataService-->>Main: Metadata Dictionary

    Main->>MetadataHandler: Save metadata.json
```

---

# AI Documentation Generation

```mermaid
sequenceDiagram
    autonumber

    participant Main
    participant GeminiAI
    participant ProblemReadmeBuilder

    Main->>GeminiAI: Metadata + Solution.cpp

    GeminiAI-->>Main: Explanation

    Main->>ProblemReadmeBuilder: metadata + ai.md + solution.cpp

    ProblemReadmeBuilder-->>Main: README.md
```

---

# Repository README Generation

```mermaid
sequenceDiagram
    autonumber

    participant Main
    participant ReadmeBuilder
    participant RootReadmeGenerator

    Main->>ReadmeBuilder: Scan repository

    ReadmeBuilder-->>Main: Statistics

    Main->>RootReadmeGenerator: Generate README

    RootReadmeGenerator-->>Main: README.md updated
```

---

# Component Interaction

```mermaid
flowchart TD

    A[main.py]

    B[RepositoryScanner]

    C[MetadataService]

    D[MetadataHandler]

    E[Gemini AI]

    F[TemplateRenderer]

    G[ProblemReadmeBuilder]

    H[ReadmeBuilder]

    I[RootReadmeGenerator]

    J[Repository README]

    A --> B

    B --> C

    C --> D

    D --> E

    E --> F

    F --> G

    G --> H

    H --> I

    I --> J
```

---

# File Generation Flow

```mermaid
flowchart LR

    A[solution.cpp]

    B[metadata.json]

    C[ai.md]

    D[Problem README.md]

    E[Repository README.md]

    A --> C

    B --> C

    B --> D

    C --> D

    D --> E
```

---

# Folder Lifecycle

```mermaid
flowchart TD

    A[Problem Folder]

    B[solution.cpp]

    C[Fetch Metadata]

    D[metadata.json]

    E[Gemini AI]

    F[ai.md]

    G[Problem README]

    A --> B

    A --> C

    C --> D

    B --> E

    D --> E

    E --> F

    D --> G

    F --> G
```

---

# Overall Pipeline

```mermaid
flowchart LR

    A[Repository]

    B[Scanner]

    C[Metadata]

    D[AI]

    E[Markdown Parser]

    F[Problem README]

    G[Statistics]

    H[Root README]

    A --> B

    B --> C

    C --> D

    D --> E

    E --> F

    F --> G

    G --> H
```

---

# Summary

The documentation pipeline consists of three major stages:

### Stage 1 — Data Collection

- Repository scanning
- Metadata retrieval
- Solution loading

### Stage 2 — Documentation Generation

- AI explanation generation
- HTML parsing
- README generation

### Stage 3 — Repository Dashboard

- Statistics computation
- Progress tracking
- Repository homepage generation

Each component performs a single responsibility, allowing the workflow to remain modular, maintainable, and easily extensible.