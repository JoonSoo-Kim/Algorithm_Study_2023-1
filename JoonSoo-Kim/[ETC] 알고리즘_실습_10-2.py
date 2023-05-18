def color(i: int, vcolor: list):
    global cnt
    global n
    cnt += 1

    if promising(i, vcolor):
        if i == n-1:

            print(vcolor)
        else:
            for clr in range(1, m+1):
                vcolor[i+1] = clr
                color(i+1, vcolor)

def promising(i: int, vcolor: list):
    switch = True
    j = 0

    while j < i and switch:
        if W[i][j] and vcolor[i] == vcolor[j]:
            switch = False
        j += 1
    return switch

cnt = 0
n = 7
W = [[0, 1, 1, 0, 0, 0, 1],
     [1, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 1, 1],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 1, 0],
     [0, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 1, 0],]

vcolor = (n) * [0]
m = 3
color(-1, vcolor)
print(cnt)

