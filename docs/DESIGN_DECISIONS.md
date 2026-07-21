# 🧠 Design Decisions

## Purpose

This document explains the architectural and technical decisions behind the AI-Powered LeetCode Documentation Generator.

Rather than only describing *how* the system works, it explains *why* each major design choice was made.

Understanding these decisions makes the project easier to maintain, extend, and evaluate.

---

# 1. Why a Modular Architecture?

## Decision

The project is divided into small, independent components instead of one large automation script.

```
RepositoryScanner

MetadataService

MetadataHandler

TemplateRenderer

AIGenerator

ProblemReadmeBuilder

ReadmeBuilder

RootReadmeGenerator
```

---

## Why?

A single file handling scanning, API requests, AI generation, HTML parsing, and README creation would quickly become difficult to understand and maintain.

By separating responsibilities:

- each module performs one task
- components are easier to debug
- features can be added without affecting unrelated code
- individual modules can be tested independently

This follows the **Single Responsibility Principle (SRP)**.

---

## Trade-offs

### Advantages

- Easier maintenance
- Better readability
- Easier debugging
- Better scalability

### Disadvantages

- More files
- Slightly more boilerplate

The maintainability benefits outweigh the additional project structure.

---

# 2. Why Use LeetCode GraphQL API?

## Decision

Metadata is fetched directly from LeetCode's GraphQL API.

---

## Why?

Using the official API provides structured information such as:

- title
- difficulty
- acceptance rate
- HTML description
- examples
- hints
- topics

This avoids fragile HTML scraping and reduces the chance of breakage if the website layout changes.

---

## Alternatives Considered

### HTML Scraping

Pros

- Simple for small projects

Cons

- Fragile
- Breaks with UI changes
- Hard to maintain

### GraphQL API ✅

Pros

- Structured responses
- Reliable
- Easier parsing
- Faster development

---

# 3. Why Store metadata.json?

## Decision

Problem metadata is stored locally.

---

## Why?

Without caching, every execution would repeatedly call the LeetCode API.

Local storage provides:

- faster execution
- reduced network usage
- offline access after initial generation
- easier debugging

Example

```text
metadata.json
```

acts as a cache between executions.

---

## Alternatives

Always fetch metadata.

Pros

- Always latest data

Cons

- Slower
- More API requests
- Difficult to debug

Caching offers a better balance.

---

# 4. Why Separate MetadataService and MetadataHandler?

## Decision

Fetching data and storing data are handled by different modules.

---

## Why?

Fetching and storage are independent concerns.

MetadataService knows:

- how to talk to LeetCode

MetadataHandler knows:

- how to read/write JSON

This separation allows storage formats to change without modifying API logic.

---

# 5. Why Google Gemini AI?

## Decision

Gemini is used to generate explanations.

---

## Why?

The project requires:

- reasoning over algorithms
- code understanding
- Markdown generation
- educational explanations

Gemini performs these tasks effectively while providing accessible APIs suitable for automation.

---

## Alternatives Considered

Manual explanations

Pros

- Full control

Cons

- Time consuming
- Difficult to maintain

Other LLM providers

Pros

- Similar capabilities

Cons

- Different pricing, APIs, or limits

The implementation is modular enough that another AI provider can replace Gemini in the future.

---

# 6. Why Generate ai.md?

## Decision

AI output is stored separately before README generation.

---

## Why?

Separating AI output provides several benefits.

- Easier debugging
- Reusable content
- Simpler regeneration
- Better separation of concerns

The README builder focuses only on assembling documentation rather than generating it.

---

# 7. Why Template-Based README Generation?

## Decision

README files are generated using Markdown templates.

---

## Why?

Templates ensure consistency across all problems.

Benefits include:

- consistent formatting
- easy customization
- centralized updates
- cleaner implementation

Changing one template automatically updates every generated README.

---

## Alternative

Building Markdown manually inside Python.

Cons

- difficult to maintain
- repetitive string formatting
- harder to extend

Templates provide a cleaner solution.

---

# 8. Why Convert HTML to Markdown?

## Decision

Problem statements are converted before insertion into README files.

---

## Why?

LeetCode returns HTML.

GitHub renders Markdown much more cleanly.

Benefits

- improved readability
- cleaner repository
- easier editing
- portable documentation

---

# 9. Why Two README Builders?

## Decision

The project has:

```
ProblemReadmeBuilder

ReadmeBuilder
```

---

## Why?

These builders have different responsibilities.

ProblemReadmeBuilder

- generates documentation for one problem

ReadmeBuilder

- computes repository-wide statistics

Keeping them separate avoids unnecessary complexity.

---

# 10. Why Store Repository Statistics Separately?

Repository statistics are computed independently from README generation.

This makes it possible to:

- add new metrics
- reuse statistics elsewhere
- improve performance
- simplify testing

---

# 11. Why Placeholder-Based Templates?

Instead of concatenating strings, placeholders are used.

Example

```text
{{TOTAL_PROBLEMS}}

{{AVERAGE_ACCEPTANCE}}

{{PROBLEM_TABLE}}
```

Benefits

- easier to read
- easier to edit
- less error-prone
- resembles professional templating systems

---

# 12. Why Use Markdown Documentation?

The project documentation itself is written in Markdown.

Reasons

- GitHub native support
- searchable
- version controlled
- easy to maintain
- readable without special software

---

# 13. Why Generate Everything Automatically?

The repository is designed so that a single command updates the entire project.

```bash
python scripts/main.py
```

This ensures:

- consistency
- reproducibility
- reduced manual effort
- fewer human errors

Automation also prepares the project for GitHub Actions integration.

---

# 14. Why This Directory Structure?

```
scripts/
templates/
docs/
problem folders/
README.md
```

The structure separates:

- source code
- templates
- documentation
- generated content

This keeps the repository organized as it grows.

---

# Lessons Learned

Developing this project reinforced several software engineering principles.

- Design modules around responsibilities rather than features.
- Separate data retrieval from data storage.
- Prefer reusable templates over duplicated formatting logic.
- Cache expensive operations whenever possible.
- Generate derived files automatically instead of editing them manually.
- Keep the workflow deterministic so results are reproducible.

---

# Future Evolution

The architecture was intentionally designed to support future improvements without major refactoring.

Potential enhancements include:

- Incremental README generation
- AI response caching
- GitHub Actions integration
- Multiple programming language support
- Multiple AI providers
- Plugin architecture
- Parallel execution
- Unit and integration tests

---

# Conclusion

This project is more than a documentation generator.

It demonstrates practical software engineering concepts including:

- Modular architecture
- Separation of concerns
- Automation
- Template-based code generation
- API integration
- AI-assisted documentation
- Scalable project organization

Each design decision was made with the goals of maintainability, extensibility, and clarity. While the implementation can continue to evolve, the architectural principles provide a solid foundation for future development.