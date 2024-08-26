def square(x): return x * x
def my_map(f,list):
    return [f(item) for item in list]

print(my_map(square, range(5)))