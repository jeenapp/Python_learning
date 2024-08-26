def triplet(n):
    tripl=[]
    for a in range(n):
        for b in range(a + 1, n):
            c = a + b
            if c < n:
                tripl.append((a, b, c))
    return tripl


print(triplet(5))
