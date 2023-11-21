def is_valid_base(b):
    return 2 <= b <= 9

def decimal_to_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])

total_sum = 0
invalid_base = False

while True:
        n, b = map(int, input().split())
        if n == -1 and b == -1:
            break
        if not is_valid_base(b):
            invalid_base = True
            continue
        divisors_sum = sum(i for i in range(1, n + 1) if n % i == 0)
        total_sum += int(decimal_to_base(divisors_sum, b))


if invalid_base:
    print("Invalid base!")
else:
    print(total_sum)
