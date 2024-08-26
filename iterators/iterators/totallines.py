import os
import sys

def find_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(root, file)
def count_lines(lines):
    return sum(1 for _ in lines)
def readfiles(filenames):
    for f in filenames:
            for line in open(f):
                yield line
    
directory = sys.argv[1]
files= find_python_files(directory)
lines=readfiles(files)
print(count_lines(lines))
