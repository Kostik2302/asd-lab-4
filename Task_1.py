def grabbed(i, j):
    global a
    global ans
    global exhibit
    if a[i][j] == 0:
        return
    if i == 0:
        ans.append(i)
        return
    if a[i-1][j] == a[i][j]:
        grabbed(i-1, j)
    else:
        grabbed(i-1, j-exhibit[i][0])
        ans.append(i)
    

n = int(input('Введите количество экспонатов: '))
m = int(input('Введите количество заходов: '))
k = int(input('Введите количество киллограм: '))
exhibit = []
for i in range(n):
    w, c = map(int, input('Введедите вес и стоимость экспоната: ').split())
    exhibit.append([w, c])

for l in range(m):
    ans = []
    not_grabbed = []
    a = [[0 for i in range(k+1)] for i in range(n)]
    for i in range(n):
        for j in range(k+1):
            if j >= exhibit[i][0]:
                a[i][j] = max(a[i-1][j], a[i-1][j-exhibit[i][0]] + exhibit[i][1])
            else:
                a[i][j] = a[i-1][j]

    grabbed(n-1, k)
    print(a)
    for i in range(n):
        if i in ans:
            print(exhibit[i])
        else:
            not_grabbed.append(exhibit[i])
    exhibit = not_grabbed
    n = len(exhibit)




