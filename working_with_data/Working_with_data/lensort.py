def lensort(list):
    list.sort(key=lambda x: len(x))
    return list

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
