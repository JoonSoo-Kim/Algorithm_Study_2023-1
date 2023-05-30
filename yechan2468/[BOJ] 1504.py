import math
from collections import defaultdict
import heapq
import sys


def dijkstra(graph, start, n):
    distances = [math.inf] * (n+1)
    distances[start] = 0
    visited = [False] * (n+1)
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

    return distances


n, edge_count = map(int, sys.stdin.readline().split())
graph = defaultdict(lambda: defaultdict(lambda: math.inf))
for i in range(edge_count):
    src, dest, weight = map(int, sys.stdin.readline().split())
    graph[src][dest] = graph[dest][src] = weight
via1, via2 = map(int, sys.stdin.readline().split())

dist_vector_1 = dijkstra(graph, via1, n)
dist_vector_2 = dijkstra(graph, via2, n)
answer = min(dist_vector_1[1] + dist_vector_1[via2] + dist_vector_2[n],
             dist_vector_2[1] + dist_vector_2[via1] + dist_vector_1[n])
print(answer if math.isfinite(answer) else -1)
