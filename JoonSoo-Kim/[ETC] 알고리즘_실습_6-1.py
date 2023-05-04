class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data

def make_tree(key: int, r_matrix: int, start: int, end: int):
    k = r_matrix[start][end]

    if k == 0:
        return
    else:
        p = Node(key[k])
        p.left_child = make_tree(key, r_matrix, start, k-1)
        p.right_child = make_tree(key, r_matrix, k+1, end)
        return p

def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(m):
        for j in range(n):
            print(f'{d[i][j]:4d}', end=" ")
        print()

def printMatrixF(d):
    n = len(d[0])
    for i in range(n):
        for j in range(n):
            print(f'{d[i][j]:5.2f}', end=" ")
        print()

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.left_child)
    print(root.data)
    print_inOrder(root.right_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.left_child)
    print_preOrder(root.right_child)

key = [" ", "A", "B", "C", "D"]
p = [0, 0.375, 0.375, 0.125, 0.125]
n = len(p) - 1

a_matrix = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
r_matrix = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

for i in range(1, n+1):
    a_matrix[i][i-1] = 0
    a_matrix[i][i] = p[i]
    r_matrix[i][i] = i
    r_matrix[i][i-1] = 0
a_matrix[n+1][n] = 0
r_matrix[n+1][n] = 0

for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j = i + diagonal

        p_sum = 0
        for m in range(i, j+1):
            p_sum += p[m]

        a_matrix[i][j] = a_matrix[i][i-1] + a_matrix[i+1][j] + p_sum
        r_matrix[i][j] = i
        for k in range(i+1, j+1):
            current_num = a_matrix[i][k-1] + a_matrix[k+1][j] + p_sum
            if a_matrix[i][j] > current_num:
                a_matrix[i][j] = current_num
                r_matrix[i][j] = k

printMatrixF(a_matrix)
print()
printMatrix(r_matrix)

root = make_tree(key, r_matrix, 1, n)
print_inOrder(root)
print()
print_preOrder(root)


