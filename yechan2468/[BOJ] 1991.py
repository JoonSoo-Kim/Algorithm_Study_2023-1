from collections import defaultdict
import sys


def preorder_traversal(graph, start='A'):
    left, right = graph[start]
    print(start, end='')
    if left is not None:
        preorder_traversal(graph, left)
    if right is not None:
        preorder_traversal(graph, right)
    return


def inorder_traversal(graph, start='A'):
    left, right = graph[start]
    if left is not None:
        inorder_traversal(graph, left)
    print(start, end='')
    if right is not None:
        inorder_traversal(graph, right)
    return


def postorder_traversal(graph, start='A'):
    left, right = graph[start]
    if left is not None:
        postorder_traversal(graph, left)
    if right is not None:
        postorder_traversal(graph, right)
    print(start, end='')
    return


input = sys.stdin.readline
graph = defaultdict(lambda: (None, None))
for _ in range(int(input())):
    root, left, right = map(lambda x: None if x == '.' else x, input().split())
    graph[root] = (left, right)

preorder_traversal(graph)
print()
inorder_traversal(graph)
print()
postorder_traversal(graph)
