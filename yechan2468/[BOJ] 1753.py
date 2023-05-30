# import heapq
# import math
# import sys
#
#
# def dijkstra(graph, start):
#     visited = [False] * len(graph)
#     pqueue = []
#     heapq.heappush(pqueue, [0, start])
#     while pqueue:
#         weight, src = heapq.heappop(pqueue)
#         if not visited[src]:
#             visited[src] = True
#             for dest, weight in enumerate(graph[src]):
#                 heapq.heappush(pqueue, [weight, dest])
#                 graph[start][dest] = min(graph[start][dest], graph[start][src] + weight)
#
#
# vertex_count, edge_count = map(int, sys.stdin.readline().split())
# graph = [[math.inf for _ in range(vertex_count+1)] for _ in range(vertex_count+1)]
# for i in range(vertex_count + 1):
#     graph[i][i] = 0
# start = int(sys.stdin.readline())
# for i in range(edge_count):
#     src, dest, weight = map(int, sys.stdin.readline().split())
#     graph[src][dest] = min(graph[src][dest], weight)
#
# dijkstra(graph, start)
#
# from pprint import pprint
# pprint(graph)
#
# for distance in graph[start][1:]:
#     print(distance)


# import math
# from collections import defaultdict
# import heapq
# import sys
#
#
# def dijkstra(graph, start, vertex_count):
#     distances = [math.inf] * (vertex_count+1)
#     distances[start] = 0
#     visited = [False] * (vertex_count+1)
#     pqueue = []
#     heapq.heappush(pqueue, [0, start])
#
#     while pqueue:
#         weight, src = heapq.heappop(pqueue)
#         if visited[src]:
#             continue
#         visited[src] = True
#         for dest in graph[src].keys():
#             heapq.heappush(pqueue, [weight := graph[src][dest], dest])
#             distances[dest] = min(distances[dest], distances[src] + weight)
#
#     return distances[1:]
#
#
# vertex_count, edge_count = map(int, sys.stdin.readline().split())
# graph = defaultdict(lambda: defaultdict(lambda: math.inf))
# start = int(sys.stdin.readline())
# for i in range(edge_count):
#     src, dest, weight = map(int, sys.stdin.readline().split())
#     graph[src][dest] = min(graph[src][dest], weight)
#
# for distance in dijkstra(graph, start, vertex_count):
#     print('INF') if distance is math.inf else print(distance)


# 10 9
# 1
# 1 2 9
# 2 8 9
# 7 3 10
# 5 6 6
# 3 4 7
# 4 5 2
# 6 10 8
# 8 5 4
# 2 3 10


import math
from collections import defaultdict
import heapq
import sys


def dijkstra(graph, start, vertex_count):
    distances = [math.inf] * (vertex_count+1)
    distances[start] = 0
    visited = [False] * (vertex_count+1)
    pqueue = []
    heapq.heappush(pqueue, [0, start])

    while pqueue:
        _, src = heapq.heappop(pqueue)
        if visited[src]:
            continue
        visited[src] = True
        for dest in graph[src].keys():
            weight = graph[src][dest]
            if distances[src] + weight < distances[dest]:
                distances[dest] = distances[src] + weight
                heapq.heappush(pqueue, [distances[dest], dest])

    return distances[1:]


vertex_count, edge_count = map(int, sys.stdin.readline().split())
graph = defaultdict(lambda: defaultdict(lambda: math.inf))
start = int(sys.stdin.readline())
for i in range(edge_count):
    src, dest, weight = map(int, sys.stdin.readline().split())
    graph[src][dest] = min(graph[src][dest], weight)

for distance in dijkstra(graph, start, vertex_count):
    print('INF') if distance is math.inf else print(distance)
