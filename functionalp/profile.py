import time

def profile(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs) 
        end_time = time.time() 
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.2f} sec")
        return result
    return wrapper

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

fib = profile(fib)
print(fib(20)) 
