def solve():
    t = int(input())  
    results = []

    for _ in range(t):
        n = int(input())  
        daughter_list = []
        available_kingdoms = set(range(1, n + 1))  
        unmarried_daughters = set(range(1, n + 1))  

        for i in range(1, n + 1):
            data = list(map(int, input().split()))
            k, preferences = data[0], data[1:]
            found_match = False

            for kingdom in preferences:
                if kingdom in available_kingdoms:
                    available_kingdoms.remove(kingdom)
                    unmarried_daughters.remove(i)
                    found_match = True
                    break

            if not found_match:
                daughter_list.append((i, preferences))

        if unmarried_daughters:
            unmarried_daughter = unmarried_daughters.pop()
            available_kingdom = available_kingdoms.pop()
            results.append(f"IMPROVE\n{unmarried_daughter} {available_kingdom}")
        else:
            results.append("OPTIMAL")

    print("\n".join(results))

solve()