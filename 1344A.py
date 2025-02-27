def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        seen = set()
        for r in range(n):
            seen.add((r + a[r]) % n)
        print("YES" if len(seen) == n else "NO")

if __name__ == '__main__':
    solve()