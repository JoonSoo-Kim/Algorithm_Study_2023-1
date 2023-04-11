def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(m):
        for j in range(n):
            print(f'{d[i][j]:4d}', end=" ")
        print()

a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']

m = len(a)
n = len(b)
table = [[0 for j in range(n+1)] for i in range(m+1)]
min_index = [[(0, 0) for j in range(n+1)] for i in range(m+1)]

for j in range(n-1, -1, -1):
    table[m][j] = table[m][j+1] + 2

for i in range(m-1, -1, -1):
    table[i][n] = table[i+1][n] + 2

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        panelty = 0 if a[i] == b[j] else 1
        current_num = table[i+1][j+1] + panelty
        min_index[i][j] = (i+1, j+1)
        if current_num > table[i+1][j] + 2:
            current_num = table[i+1][j] + 2
            min_index[i][j] = (i+1, j)
        if current_num > table[i][j+1] + 2:
            current_num = table[i][j+1] + 2
            min_index[i][j] = (i, j+1)
        table[i][j] = current_num

printMatrix(table)



x = 0
y = 0
while x < m and y < n:
    tx, ty = x, y
    print(min_index[x][y])
    (x, y) = min_index[x][y]

    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == tx + 1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " ", " -")
