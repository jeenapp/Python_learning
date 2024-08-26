import os
import sys
def find_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(root, file)
def strip_line(lines):
    count=0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            count=count+1
    return count
def readfiles(filenames):
    for f in filenames:
            for line in open(f):
                yield line
   
directory = sys.argv[1]
files= find_python_files(directory)
lines=readfiles(files)
s_lines=strip_line(lines)
print(s_lines)
