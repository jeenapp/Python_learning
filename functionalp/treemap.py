def treemap(func, nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.append(treemap(func, item))  
        else:
            result.append(func(item))  
    return result

nested_list = [1, 2, [3, 4, [5]]]
print(treemap(lambda x: x * x, nested_list)) 
