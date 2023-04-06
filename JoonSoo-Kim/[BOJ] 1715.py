import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
result = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    current_result = heapq.heappop(cards)
    current_result += heapq.heappop(cards)
    result += current_result
    heapq.heappush(cards, current_result)

print(result)