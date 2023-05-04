# 연쇄행렬 최소곱셈
def mult_matrix_chain(d: list):
    n = len(d)
    min_mult = [[0 for _ in range(n)] for _ in range(n)]
    positions = [[0 for _ in range(n)] for _ in range(n)]

    for diagonal in range(1, n):
        for i in range(1, n-diagonal):
            j = i + diagonal

            # k = i 일때의 상태로 min_mult를 초기화
            min_mult[i][j] = min_mult[i][i] + min_mult[i+1][j] \
                            + d[i-1] * d[i] * d[j]
            positions[i][j] = i

            for k in range(i+1, j):
                temp = min_mult[i][k] + min_mult[k+1][j] \
                            + d[i-1] * d[k] * d[j]
                if temp < min_mult[i][j]:
                    min_mult[i][j] = temp
                    positions[i][j] = k

    print_matrix(min_mult)
    print()
    print_matrix(positions)
    print()
    print_order(positions, 1, n-1)

def print_order(positions:list, i: int, j: int):
    if i == j:
        print("A" + str(i), end="")
    else:
        k = positions[i][j]
        print("(", end="")
        print_order(positions, i, k)
        print_order(positions, k+1, j)
        print(")", end="")

def print_matrix(matrix: list):
    m = len(matrix)
    n = len(matrix[0])

    for i in range (m):
        for j in range(n):
            print(f'{matrix[i][j]:4d}', end=" ")
        print()


d = [5, 2, 3, 4, 6, 7, 8]
mult_matrix_chain(d)