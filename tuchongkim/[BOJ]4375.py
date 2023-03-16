while True:
    try:
        n = int(input())
    except:
        break
    cnt, dgt = 1, 1 #cnt : 배수, dgt : 자릿수
    while True:
        if cnt % n == 0:
            print(dgt)
            break
        else:
            cnt = cnt * 10 + 1
            cnt %= n
            dgt += 1
