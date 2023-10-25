def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def count_primes_between_numbers(start, end):
    count = 0

    for num in range(start, end + 1):
        if is_prime(num):
            count += 1

    return count

# Input two numbers
start ,end=map(int,input().split()) 

if start <= end:
# Count the prime numbers
    prime_count = count_primes_between_numbers(start, end)
    print(f"main order - amount: {prime_count}")

if start  >end:
# Count the prime numbers
    prime_count = count_primes_between_numbers(end, start)
    print(f"reverse order - amount: {prime_count}")


