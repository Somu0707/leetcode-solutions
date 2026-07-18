from scanner import RepositoryScanner


class RootReadmeGenerator:

    def generate(self):

        scanner = RepositoryScanner()

        problems = scanner.scan()

        total = len(problems)

        markdown = f"""# 🚀 LeetCode Solutions

Automatically maintained using:

- Python
- GitHub Actions
- Gemini AI
- LeetHub

---

## Problems Solved

**Total : {total}**

---

## Repository

"""

        for problem in problems:
            markdown += f"- {problem}\n"

        with open("README.md", "w") as f:
            f.write(markdown)
            