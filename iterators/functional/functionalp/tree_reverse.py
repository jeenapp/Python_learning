def tree_reverse(nested_list):
    reversed_list = []
    for item in reversed(nested_list):
        if isinstance(item, list):
            reversed_list.append(tree_reverse(item))  
        else:
            reversed_list.append(item)  
    return reversed_list

nested_list = [1, 2, [3, 4, [5]]]
print(tree_reverse(nested_list)) 
