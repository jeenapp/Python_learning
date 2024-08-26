def cumulative_sum(lst):
    sum=0
    cum=[]
    for i in lst:
        sum=sum+i
        cum.append(sum)
    return cum

print(cumulative_sum([1, 2, 3, 4]))


