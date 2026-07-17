from utils import find_cpp_file, read_file
import sys

folder = sys.argv[1]

cpp = find_cpp_file(folder)

if cpp is None:
    print("No C++ file found.")
    exit()

print("Problem Folder:", folder)
print("CPP File:", cpp)

code = read_file(cpp)

print(code[:300])
