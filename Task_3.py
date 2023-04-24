from random import randint

the_biggest = []

n = int(input('Введите n '))

N = [randint(-100, 100) for i in range(n)]
may_be_the_biggest = [N[0]]

for i in range(1, len(N)):
    if N[i-1] < N[i]:
        may_be_the_biggest.append(N[i])
    else:
        if len(may_be_the_biggest) > len(the_biggest):
            the_biggest = may_be_the_biggest
            may_be_the_biggest = [N[i]]

print(f'Исходный массив: {" ".join([str(i) for i in N])}')
print(f'Самая длинная восходящая последовательность: {" ".join([str(i) for i in the_biggest])}')

