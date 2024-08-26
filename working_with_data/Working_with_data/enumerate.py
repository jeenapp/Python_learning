def enumerate(list):
    enum = []
    for i, item in zip(range(len(list)), list):
        enum.append((i, item))    
    return enum

list = ['a', 'b', 'c']
print(enumerate(list))