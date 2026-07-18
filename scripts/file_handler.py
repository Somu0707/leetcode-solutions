import os


class FileHandler:

    @staticmethod
    def read_code(problem_folder):
        cpp_file = None

        for file in os.listdir(problem_folder):
            if file.endswith(".cpp"):
                cpp_file = file
                break

        if cpp_file is None:
            raise FileNotFoundError("No C++ solution found.")

        with open(os.path.join(problem_folder, cpp_file), "r") as f:
            return f.read()

    @staticmethod
    def save_readme(problem_folder, markdown):
        readme_path = os.path.join(problem_folder, "README.md")

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"✅ README generated at: {readme_path}")

    @staticmethod
    def has_readme(problem_folder):
        return os.path.exists(
            os.path.join(problem_folder, "README.md")
        )