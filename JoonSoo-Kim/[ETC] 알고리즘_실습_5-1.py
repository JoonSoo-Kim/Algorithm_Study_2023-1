# 이항계수 계산
def get_bin_recursion(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    else:
        return get_bin_recursion(n-1, k-1) + get_bin_recursion(n-1, k)

def get_bin(n: int, k: int) -> int:
    bin_list = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i+1, k+1)):
            if j == 0 or j == i:
                bin_list[i][j] = 1;
            else:
                bin_list[i][j] = bin_list[i-1][j-1] + bin_list[i-1][j]

    return bin_list[n][k]


print(get_bin_recursion(10, 5), get_bin(10, 5))