def invertdict(d):
    inverted_dict = {value: key for key, value in d.items()}    
    return inverted_dict

inverted_dict = invertdict({'x': 1, 'y': 2, 'z': 3})
print(inverted_dict)
