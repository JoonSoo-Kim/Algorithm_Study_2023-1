def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(m):
        for j in range(n):
            print(f'{d[i][j]:4d}', end=" ")
        print()


F = set()
inf = 1000
w = [[0, 1, 3, inf, inf],
     [1, 0, 3, 6, inf],
     [3, 3, 0, 4, 2],
     [inf, 6, 4, 0, 5],
     [inf, inf, 2, 5, 0]]
n = len(w)
nearest = n * [0]
distance = n * [0]
printMatrix(w)

for i in range(1, n):
    nearest[i] = 0
    distance[i] = w[0][i]

for _ in range(n - 1):
    min = inf
    for i in range(1, n):
        if 0 <= distance[i] < min:
            min = distance[i]
            vnear = i

    e = (vnear, nearest[vnear])
    F.add(e)

    distance[vnear] = -1
    for i in range(1, n):
        if w[i][vnear] < distance[i]:
            distance[i] = w[i][vnear]
            nearest[i] = vnear

print()
print(F)