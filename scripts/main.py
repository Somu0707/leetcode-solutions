from pathlib import Path
import sys

from ai_generator import AIGenerator
from file_handler import FileHandler


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python scripts/main.py <problem-folder>")
        return

    folder = sys.argv[1]

    cpp = FileHandler.get_cpp_file(folder)

    if cpp is None:
        print("No cpp file found.")
        return

    code = FileHandler.read(cpp)

    problem_name = Path(folder).name

    ai = AIGenerator()

    markdown = ai.generate(problem_name, code)

    print(markdown)


if __name__ == "__main__":
    main()