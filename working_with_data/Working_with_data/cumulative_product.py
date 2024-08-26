def cumulative_product(lst):
    prod=1
    cum=[]
    for i in lst:
        prod=prod*i
        cum.append(prod)
    return cum

print(cumulative_product([1, 2, 3, 4]))