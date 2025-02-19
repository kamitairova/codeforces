def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    n = int(input())

    if n % 2 != 0:
        print(-1)
        return

    adj_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [0] * (n + 1)
    parent = [-1] * (n + 1)
    even_count = 0
    subtree_size = [1] * (n + 1)

    stack = [(1, -1)]
    while stack:
        node, par = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            stack.append((node, par))
            for neighbor in adj_list[node]:
                if neighbor != par:
                    parent[neighbor] = node
                    stack.append((neighbor, node))
        elif visited[node] == 1:
            visited[node] = 2
            if par != -1:
                subtree_size[par] += subtree_size[node]
            if subtree_size[node] % 2 == 0:
                even_count += 1

    print(even_count - 1 if even_count > 0 else 0)


if __name__ == "__main__":
    solve()



# import sys

# sys.setrecursionlimit(10 ** 6)


# def dfs(u, parent):
#     subtree_size = 1
#     for v in tree[u]:
#         if v != parent:
#             subtree_size += dfs(v, u)
#     if subtree_size % 2 == 0:
#         global edges_to_remove
#         edges_to_remove += 1
#     return subtree_size


# n = int(input())

# edges = []
# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     edges.append((u, v))



# if n % 2 == 1:
#     print(-1)
# else:
#     tree = [[] for _ in range(n + 1)]
#     for u, v in edges:
#         tree[u].append(v)
#         tree[v].append(u)

#     edges_to_remove = 0
#     dfs(1, -1)

#     print(edges_to_remove - 1)
