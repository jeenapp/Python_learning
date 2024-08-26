def my_zip(list1, list2):
    lists = [list1, list2]
    length = len(list1)
    return [[list[i] for list in lists] for i in range(length)]
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = my_zip(list1, list2)
print(zipped) 
