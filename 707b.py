def minimumcost(n, m, k, roads, warehouses):
    if k == 0 or k == n:
        return -1
 
    warehouse_set = set(warehouses) 
    min_cost = float('inf')  
 
    for u, v, l in roads:
        if (u in warehouse_set and v not in warehouse_set) or (v in warehouse_set and u not in warehouse_set):
            min_cost = min(min_cost, l)
 
    return min_cost if min_cost != float('inf') else -1
 
 
n, m, k = map(int, input().split()) 
roads = [tuple(map(int, input().split())) for _ in range(m)]
warehouses = list(map(int, input().split())) if k > 0 else [] 
 
print(minimumcost(n, m, k, roads, warehouses))