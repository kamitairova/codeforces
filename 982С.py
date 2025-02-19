import sys

sys.setrecursionlimit(10 ** 6)


def dfs(u, parent):
    subtree_size = 1
    for v in tree[u]:
        if v != parent:
            subtree_size += dfs(v, u)
    if subtree_size % 2 == 0:
        global edges_to_remove
        edges_to_remove += 1
    return subtree_size


n = int(input())

edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))



if n % 2 == 1:
    print(-1)
else:
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    edges_to_remove = 0
    dfs(1, -1)

    print(edges_to_remove - 1)
