import os
import sys
def find_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(root, file)
def count_python_files(directory):
    return sum(1 for _ in directory)
 
directory = sys.argv[1]
files= find_python_files(directory)
print(count_python_files(files))
