def vertices():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        c = [a[i] - b[i] for i in range(n)]

        d = max(c)

        strong= [i + 1 for i in range(n) if c[i] == d]

        results.append(f"{len(strong)}")
        results.append(" ".join(map(str, strong)))

    print("\n".join(results))

vertices()



