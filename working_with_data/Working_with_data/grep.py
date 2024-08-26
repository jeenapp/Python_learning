filename ='C:\\Users\\yedhu\\OneDrive\\Desktop\\Welcome.txt'
def grep(filename,word):
    lines=open(filename).readlines()
    for i in lines:
        if word in i:
            print(i)
grep(filename,'sure')
