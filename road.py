import math

def road(zero_v, visited):
    amin = -1
    infinity = math.inf
    for i, next_v in enumarate(zero_v):
        if next_v < infinity and not in visited:
            infinity = next_v
            amin = i

    return amin

graph = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

amount_of_vertices = len(graph)

weigh = [math.inf]*N 

start_v = 0
visited = {v}
weigh(start_v) = 0
best = [0] * amount_of_vertices

while v != -1:
    for i, J in enumarate(graph[v]):
        if i not in visited:
            w = weigh[i] + j
            if w < weigh[i]:
                weigh[i] = w
                best[i] = v
    v = road(zero_v, visited)
    if v>=0
    visited.add(v)

start = 0
end = 4
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print(P)