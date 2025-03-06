import math

def factorize(n):
    divisors = {}
    while n % 2 == 0:
        divisors[2] = divisors.get(2, 0) + 1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            divisors[i] = divisors.get(i, 0) + 1
            n //= i
        i += 2
    if n > 1:
        divisors[n] = 1
    return divisors

def find_max_divisor(pi, qi):
    if pi % qi != 0:
        return pi
    qi_factors = factorize(qi)
    x = 1
    for prime in qi_factors:
        temp = pi
        while temp % qi == 0:
            temp //= prime
        if temp % qi != 0:
            x = max(x, temp)
    return x

t = int(input())
for _ in range(t):
    pi, qi = map(int, input().split())
    print(find_max_divisor(pi, qi))







