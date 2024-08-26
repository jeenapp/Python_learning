def mini(lst):
    minimum = lst[0]
    for x in lst[1:]:
        if x < minimum:
            minimum = x    
    return minimum
def maxi(lst):
    maximum = lst[0]
    for x in lst[1:]:
        if x > maximum:
            maximum = x    
    return maximum

lst = [4, 3, 1, 1, 5, 9, 2]
strings = ["apple","banana","orange","cherry","grape"]
print(mini(lst))
print(maxi(lst))
print(mini(strings))
print(maxi(strings))