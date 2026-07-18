from scanner import RepositoryScanner


class RootReadmeGenerator:

    def __init__(self):
        self.scanner = RepositoryScanner()

    def generate(self):

        problems = self.scanner.scan()

        total = len(problems)

        table = [
            "| # | Problem | Documentation |",
            "|---|---------|---------------|"
        ]

        for problem in problems:

            number, name = problem.split("-", 1)

            title = name.replace("-", " ").title()

            table.append(
                f"| {number} | [{title}](./{problem}/README.md) | ✅ |"
            )

        with open("templates/README_TEMPLATE.md", "r", encoding="utf-8") as f:
            readme = f.read()

        readme = readme.replace(
            "{{TOTAL_PROBLEMS}}",
            str(total)
        )

        readme = readme.replace(
            "{{PROBLEM_TABLE}}",
            "\n".join(table)
        )

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)