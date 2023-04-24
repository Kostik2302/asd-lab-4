from random import randint

def min_multiplication(i, j):
    global f
    global m
    if f[i][j] == None:
        if j - i == 1:
            f[i][j] = 0
        else:
            f[i][j] = 10000000
            for k in range(i + 1, j):
                f[i][j] = min(f[i][j], m[i] * m[k] * m[j] +  min_multiplication(i, k) + min_multiplication(k, j))
    return f[i][j]

n = 26
m = [randint(1, 10) for i in range(n)]
f = [[None for i in range(n)] for i in range(n)]

print(min_multiplication(0, n-1))