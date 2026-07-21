from scanner import RepositoryScanner
from file_handler import FileHandler
from ai_generator import AIGenerator
from generate_root_readme import RootReadmeGenerator

from metadata_service import MetadataService
from metadata_handler import MetadataHandler
from problem_readme_builder import ProblemReadmeBuilder


def main():

    scanner = RepositoryScanner()
    ai = AIGenerator()
    builder = ProblemReadmeBuilder()

    problems = scanner.scan()

    print(f"\nFound {len(problems)} problems\n")

    for problem in problems:

        print(f"\n{'=' * 60}")
        print(f"Processing: {problem}")
        print(f"{'=' * 60}")

        slug = problem.split("-", 1)[1]

        # -----------------------------------------
        # Generate metadata only once
        # -----------------------------------------
        if not MetadataHandler.exists(problem):

            print("📥 Fetching metadata...")

            MetadataHandler.save(
                problem,
                MetadataService.get_metadata(slug)
            )

            print("✅ Metadata saved")

        # -----------------------------------------
        # Load metadata
        # -----------------------------------------
        metadata = MetadataHandler.load(problem)

        # -----------------------------------------
        # Read solution.cpp
        # -----------------------------------------
        code = FileHandler.read_code(problem)

        # -----------------------------------------
        # Generate AI explanation
        # -----------------------------------------
        print("🤖 Generating AI explanation...")

        ai_text = ai.generate(
            metadata,
            code
        )

        # -----------------------------------------
        # Save AI explanation
        # -----------------------------------------
        with open(
            f"{problem}/ai.md",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(ai_text)

        print("✅ AI explanation saved")

        # -----------------------------------------
        # Generate professional README
        # -----------------------------------------
        builder.build(
            problem,
            metadata,
            code,
            ai_text
        )

        print("✅ README generated")

    # -----------------------------------------
    # Generate Root README
    # -----------------------------------------
    print("\nUpdating repository README...")

    RootReadmeGenerator().generate()

    print("✅ Root README updated successfully.")

    print("\n🎉 Automation completed successfully!")


if __name__ == "__main__":
    main()