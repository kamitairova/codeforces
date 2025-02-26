def check_number(n):
    max_value = n // 111
    for value in range(max_value + 1):
        remainder = n - 111 * value
        if remainder % 11 == 0:
            return True
    return 


test_cases = int(input())
for _ in range(test_cases):
    number = int(input())
    if check_number(number):
        print("YES")
    else:
        print("NO")
