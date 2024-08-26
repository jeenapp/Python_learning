filename ='C:\\Users\\yedhu\\OneDrive\\Desktop\\new.txt'
def head(filename):
    lines=open(filename).readlines()
    heads=lines[:10]
    print(heads)
def tail(filename):
    lines=open(filename).readlines()
    length=len(lines)
    tails=lines[length-10:]
    print(tails)

head(filename)
tail(filename)