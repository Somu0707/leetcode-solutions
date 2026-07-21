from scanner import RepositoryScanner
from file_handler import FileHandler
from ai_generator import AIGenerator
from generate_root_readme import RootReadmeGenerator

from metadata_service import MetadataService
from metadata_handler import MetadataHandler


def main():

    scanner = RepositoryScanner()
    ai = AIGenerator()

    problems = scanner.scan()

    print(f"\nFound {len(problems)} problems\n")

    for problem in problems:

        slug = problem.split("-", 1)[1]

        # Generate metadata only once
        if not MetadataHandler.exists(problem):

            print(f"Fetching metadata for {problem}")

            MetadataHandler.save(
                problem,
                MetadataService.get_metadata(slug)
            )

            print("✅ Metadata saved")

        # Always load metadata
        metadata = MetadataHandler.load(problem)

        # Skip README if already present
        if FileHandler.has_readme(problem):
            print(f"Skipping {problem}")
            continue

        code = FileHandler.read_code(problem)

        markdown = ai.generate(metadata, code)

        FileHandler.save_readme(problem, markdown)

        print(f"Generated {problem}")

    RootReadmeGenerator().generate()

    print("\n✅ Root README updated successfully.")


if __name__ == "__main__":
    main()