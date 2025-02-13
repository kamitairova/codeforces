import heapq

def best_way(N, M, roads, S, T):
    graph = [[] for _ in range(N + 1)]
    
    for a, b, w in roads:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    max_capacity = [0] * (N + 1)
    max_capacity[S] = float('inf') 
    
    pq = []
    heapq.heappush(pq, (-float('inf'), S)) 
    
    while pq:
        current_weight, u = heapq.heappop(pq)
        current_weight = -current_weight 
        
        if u == T:
            return current_weight  

        for v, weight in graph[u]:
            path_weight = min(current_weight, weight)
            
            if path_weight > max_capacity[v]:
                max_capacity[v] = path_weight
                heapq.heappush(pq, (-path_weight, v))
    
    return -1  

N, M = map(int, input().split()) 
roads = []
for _ in range(M):
    A, B, W = map(int, input().split())
    roads.append((A, B, W))
S, T = map(int, input().split())

print(best_way(N, M, roads, S, T))
