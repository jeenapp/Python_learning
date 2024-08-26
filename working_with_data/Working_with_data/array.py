def array(rows, cols):
    result = []
    for i in range(rows):  
        row = [None] * cols
        result.append(row)
    return result

rows = 2
cols = 3
result = array(rows, cols)
result[0][0] = 5
print(result)