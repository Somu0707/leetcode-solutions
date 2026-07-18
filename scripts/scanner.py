import os


class RepositoryScanner:

    def __init__(self):
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        self.ignore = {
            ".git",
            ".github",
            ".venv",
            "scripts",
            "__pycache__"
        }

    def scan(self):
        problems = []

        for item in os.listdir(self.root):

            path = os.path.join(self.root, item)

            if item in self.ignore:
                continue

            if not os.path.isdir(path):
                continue

            if item[0].isdigit():
                problems.append(item)

        return sorted(problems)