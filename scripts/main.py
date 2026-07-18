from scanner import RepositoryScanner
from file_handler import FileHandler
from ai_generator import AIGenerator
from generate_root_readme import RootReadmeGenerator


def main():

    scanner = RepositoryScanner()
    ai = AIGenerator()

    problems = scanner.scan()

    print(f"\nFound {len(problems)} problems\n")

    for problem in problems:

        if FileHandler.has_readme(problem):
            print(f"Skipping {problem}")
            continue

        code = FileHandler.read_code(problem)

        problem_name = problem.split("-", 1)[1].replace("-", " ").title()

        markdown = ai.generate(problem_name, code)

        FileHandler.save_readme(problem, markdown)

        print(f"Generated {problem}")

    # Update the repository's main README
    RootReadmeGenerator().generate()

    print("\n✅ Root README updated successfully.")


if __name__ == "__main__":
    main()