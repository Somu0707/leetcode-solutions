from pathlib import Path

def find_cpp_file(folder):
    folder = Path(folder)

    cpp_files = list(folder.glob("*.cpp"))

    if not cpp_files:
        return None

    return cpp_files[0]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
