def dups(lst):
    dup=[]
    a=[]
    for i in lst:
        if i in a:
            if i not in dup:
                dup.append(i)
        else:
            a.append(i)
    return dup

print(dups([1, 2, 1, 3, 2, 5]))