def unique(lst):
    unq=[]
    for i in lst:
        if i not in unq:
            unq.append(i)
    return unq
print(unique([1, 2, 1, 3, 2, 5]))

def uniq(lst):
    return set(lst)

print(uniq([1, 2, 1, 3, 2, 5]))