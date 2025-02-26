def process_string():
    n = int(input())
    s = list(input().strip())
    deleted_count = 0

    for letter_idx in range(25, 0, -1):
        current_letter = chr(letter_idx + ord('a'))
        previous_letter = chr(letter_idx + ord('a') - 1)
        idx = 0

        while idx < len(s):
            if s[idx] == current_letter and (
                    (idx > 0 and s[idx - 1] == previous_letter) or
                    (idx < len(s) - 1 and s[idx + 1] == previous_letter)
            ):
                del s[idx]
                deleted_count += 1
                idx = max(idx - 1, 0)
            else:
                idx += 1

    print(deleted_count)


if __name__ == "__main__":
    test_cases = 1
    for _ in range(test_cases):
        process_string()
