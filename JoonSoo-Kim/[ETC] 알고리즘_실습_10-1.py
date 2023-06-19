def promising(i: int, weight: int, total: int):
    return (weight+total>=W) and (weight==W or weight+w[i+1]<=W)

def s_s(i: int, weight: int, total: int, include: list):
    global cnt
    cnt += 1

    if promising(i, weight, total):
        if weight == W:
            print(include)
        else:
            include[i+1] = 1
            s_s(i + 1, weight + w[i + 1], total - w[i + 1], include)
            include[i+1] = 0
            s_s(i + 1, weight, total - w[i + 1], include)


n = 5
w = [1, 4, 5, 6, 8]
W = 10
cnt = 0
print("items = ", w, "W =", W)
include = n * [0]
total = 0
for k in w:
    total += k
s_s(0, 0, total, include)
print(cnt)