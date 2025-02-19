INF = 1e9 + 7

def floyd_warshall(n, m, edges):
    dp = [[INF] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for u, v, length in edges:
        dp[u][v] = dp[v][u] = length

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, length = map(int, input().split())
    edges.append((u - 1, v - 1, length))

dp = floyd_warshall(n, m, edges)

for i in range(n):
    for j in range(n):
        if dp[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dp[i][j], end=" ")
    print()

# INF = -(1e9 + 7)
#
# def floyd_warshall_longest(n, m, edges):
#     dp = [[INF] * n for _ in range(n)]
#
#     for i in range(n):
#         dp[i][i] = 0
#
#     for u, v, length in edges:
#         dp[u][v] = dp[v][u] = length
#
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])
#
#     return dp

# n, m = map(int, input().split())
# edges = []
#
# for _ in range(m):
#     u, v, length = map(int, input().split())
#     edges.append((u - 1, v - 1, length))
#
# dp = floyd_warshall_longest(n, m, edges)
#
# for i in range(n):
#     for j in range(n):
#         if dp[i][j] == INF:
#             print("INF", end=" ")
#         else:
#             print(dp[i][j], end=" ")
#     print()

