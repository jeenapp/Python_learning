import sys

def readfiles(filenames):
    for f in filenames:
            for line in open(f):
                yield line
def filter_long_lines(lines):
    for line in lines:
        if len(line) > 40:
            yield line
def printlines(lines):

    for line in lines:
        print(line, end="")

filenames = sys.argv[1:]
lines = readfiles(filenames)
long_lines = filter_long_lines(lines)
printlines(long_lines)

