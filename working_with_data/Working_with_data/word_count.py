filename ='C:\\Users\\yedhu\\OneDrive\\Desktop\\Welcome.txt'
def charcount(filename):
    return len(open(filename).read())
def wordcount(filename):
    return len(open(filename).read().split())
def linecount(filename):
    return len(open(filename).readlines())

print(charcount(filename))
print(wordcount(filename))
print(linecount(filename))