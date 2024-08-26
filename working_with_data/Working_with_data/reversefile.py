filename ='C:\\Users\\yedhu\\OneDrive\\Desktop\\Welcome.txt'
def reverse(filename):    
    lines=open(filename).readlines()
    revers=lines[::-1]
    for i in revers:
        print(i,end='')
reverse(filename)
def reverseline(filename):    
    lines=open(filename).readlines()
    for i in lines:
        revers=i[::-1]
        print(revers,end='')
reverseline(filename)