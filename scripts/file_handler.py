from pathlib import Path


class FileHandler:

    @staticmethod
    def get_cpp_file(problem_folder: str):
        folder = Path(problem_folder)

        cpp_files = list(folder.glob("*.cpp"))

        if not cpp_files:
            return None

        return cpp_files[0]


    @staticmethod
    def read(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


    @staticmethod
    def write(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
