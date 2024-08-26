class ReverseIter:
    def __init__(self, n):
        self.n = n
        self.i = len(n)  
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == 0:
            raise StopIteration  
        self.i -= 1
        return self.n[self.i]

list = [1, 2, 3, 4, 5]
rev = ReverseIter(list)
for item in rev:
    print(item)
