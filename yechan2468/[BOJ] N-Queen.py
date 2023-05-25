#  with function version (first code written)
import copy
# import copy
# import sys
# from datetime import datetime
# t1 = datetime.now()
#
# def visit(row, col, graph, n):
#     vertical, diag_upper, diag_lower = graph
#     vertical[col] = diag_upper[row+col] = diag_lower[row-col+n-1] = True
#
#
# def visited(row, col, graph, n):
#     vertical, diag_upper, diag_lower = graph
#     return vertical[col] or diag_upper[row+col] or diag_lower[row-col+n-1]
#
#
# def dfs(graph, n, row=0):
#     global result
#     for col in range(n):
#         if not visited(row, col, graph, n):
#             if row == n-1:
#                 result += 1
#                 return
#             copied_graph = copy.deepcopy(graph)
#             visit(row, col, copied_graph, n)
#             dfs(copied_graph, n, row+1)
#
# # n = int(sys.stdin.readline())
# n= 10
#
# vertical = [False] * n
# diag_upper = [False] * (2*n - 1)
# diag_lower = [False] * (2*n - 1)
# graph = [vertical, diag_upper, diag_lower]
# result = 0
#
# dfs(graph, n)
#
# t2 = datetime.now()
# print(result)
# print(f'{(t2-t1).seconds}.{(t2 - t1).microseconds}')






# without func call

# from datetime import datetime
# import copy
# import sys
#
# t1 = datetime.now()
#
# def dfs(graph, n, row=0):
#     global result
#     for col in range(n):
#         if not (graph[0][col] or graph[1][row+col] or graph[2][row-col+n-1]):
#             if row == n-1:
#                 result += 1
#                 return
#             copied_graph = copy.deepcopy(graph)
#             copied_graph[0][col] = copied_graph[1][row+col] = copied_graph[2][row-col+n-1] = True
#             dfs(copied_graph, n, row+1)
#
# n = 12
# vertical = [False] * n
# diag_upper = [False] * (2*n - 1)
# diag_lower = [False] * (2*n - 1)
# graph = [vertical, diag_upper, diag_lower]
# result = 0
#
# dfs(graph, n)
#
# t2 = datetime.now()
# print(result)
# print(f'{(t2-t1).seconds}.{(t2 - t1).microseconds}')







# with manual deep copy

# from datetime import datetime
# import sys
#
# t1 = datetime.now()
#
# def dfs(graph, n, row=0):
#     global result
#     for col in range(n):
#         if not (graph[0][col] or graph[1][row+col] or graph[2][row-col+n-1]):
#             if row == n-1:
#                 result += 1
#                 return
#             copied_graph = [graph[0][:], graph[1][:], graph[2][:]]
#             copied_graph[0][col] = copied_graph[1][row+col] = copied_graph[2][row-col+n-1] = True
#             dfs(copied_graph, n, row+1)
#
# n = 14
# vertical = [False] * n
# diag_upper = [False] * (2*n - 1)
# diag_lower = [False] * (2*n - 1)
# graph = [vertical, diag_upper, diag_lower]
# result = 0
#
# dfs(graph, n)
#
# t2 = datetime.now()
# print(result)
# print(f'{(t2-t1).seconds}.{(t2 - t1).microseconds}')





import sys


def visit(row, col, graph, n):
    vertical, diag_upper, diag_lower = graph
    vertical[col] = diag_upper[row+col] = diag_lower[row-col+n-1] = True


def visited(row, col, graph, n):
    vertical, diag_upper, diag_lower = graph
    return vertical[col] or diag_upper[row+col] or diag_lower[row-col+n-1]


def dfs(graph, n, row=0):
    global result
    for col in range(n):
        if not visited(row, col, graph, n):
            if row == n-1:
                result += 1
                return
            copied_graph = [graph[0][:], graph[1][:], graph[2][:]]
            visit(row, col, copied_graph, n)
            dfs(copied_graph, n, row+1)


n = int(sys.stdin.readline())
vertical = [False] * n
diag_upper = [False] * (2*n - 1)
diag_lower = [False] * (2*n - 1)
graph = [vertical, diag_upper, diag_lower]
result = 0

dfs(graph, n)

print(result)
