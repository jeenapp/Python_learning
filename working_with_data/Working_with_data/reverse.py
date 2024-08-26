def reverse(list):
    length = len(list)
    for i in range(length//2):
        last_index = length - 1 - i
        list[i], list[last_index] = list[last_index], list[i]
    return list

print(reverse([1, 2, 3, 4]))
print(reverse(reverse([1, 2, 3, 4])))