import sys

from pathlib import Path

from file_handler import FileHandler
from ai_generator import AIGenerator


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py <problem-folder>")
        return

    folder = sys.argv[1]

    cpp = FileHandler.get_cpp_file(folder)

    if cpp is None:
        print("No cpp file found.")
        return

    code = FileHandler.read(cpp)

    problem_name = Path(folder).name

    AIGenerator.generate(problem_name, code)


if __name__ == "__main__":
    main()
