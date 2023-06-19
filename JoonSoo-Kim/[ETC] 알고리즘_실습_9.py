node_cnt = 0
sol_cnt = 0


def queens(n: int, index: int, col: list):
    global sol_cnt
    global node_cnt

    if promising(index, col):
        node_cnt += 1
        if index == n:
            print(col[1:n + 1])
            sol_cnt += 1
        else:
            for j in range(1, n+1):
                col[index+1] = j
                queens(n, index+1, col)


def promising(index: int, col: list):
    k = 1
    switch = True

    while k < index and switch:
        if col[index] == col[k] or abs(col[index]-col[k]) == index - k:
            switch = False
        k += 1
    return switch


n = 4
col = (n+1) * [0]
queens(n, 0, col)
print(sol_cnt)
print(node_cnt)