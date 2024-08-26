def group(list, size):
    new_list=[]
    for i in range(0, len(list), size):
        new_list.append(list[i:i + size])    
    return new_list

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))