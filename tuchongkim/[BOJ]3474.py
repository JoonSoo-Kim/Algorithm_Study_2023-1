# boj 3474
import sys

t = int(sys.stdin.readline().rstrip()) # 테스트 케이스 개수
for _ in range(t):
    number = int(sys.stdin.readline().rstrip()) 
    num5 = 0 # number! 에 5가 몇 개 존재하는지 저장
    exp5 = 5 # 5의 거듭제곱수
    while exp5 <= number:
        num5 += number // exp5
        exp5 *= 5
    print(num5)
    