import heapq

n = int(input())
commands = [input().split() for _ in range(n)]

min_heap = []
output = []

for command in commands:
    if command[0] == 'insert':
        value = int(command[1])
        heapq.heappush(min_heap, value)
        output.append(f"insert {value}")
    elif command[0] == 'getMin':
        value = int(command[1])
        while min_heap and min_heap[0] < value:
            output.append("removeMin")
            heapq.heappop(min_heap)
        if not min_heap or min_heap[0] != value:
            output.append(f"insert {value}")
            heapq.heappush(min_heap, value)
        output.append(f"getMin {value}")
    elif command[0] == 'removeMin':
        if not min_heap:
            output.append("insert 0")
            heapq.heappush(min_heap, 0)
        output.append("removeMin")
        heapq.heappop(min_heap)

print(len(output))
for op in output:
    print(op)
