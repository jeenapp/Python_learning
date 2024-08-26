def valuesort(d):
    sorted_items = sorted(d.items())
    sorted_values = [value for key, value in sorted_items]    
    return sorted_values

sorted_values = valuesort({'x': 1, 'y': 2, 'a': 3})
print(sorted_values)
