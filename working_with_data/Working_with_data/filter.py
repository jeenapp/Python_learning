def even(x): return x %2 == 0
def my_filter(f,list):
     fil=[]
     for item in list:
          if f(item):
               fil.append(item)
     return fil
print(my_filter(even, range(10)))
