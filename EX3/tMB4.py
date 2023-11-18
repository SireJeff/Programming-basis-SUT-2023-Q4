def find_receiver_house(nums, target_sum):
    seen = {}
    result = []

    for i, num in enumerate(nums):
        complement = target_sum - num
        if complement in seen:
            result.append(seen[complement] + i)
        seen[num] = i

    if result:
        result.sort()
        for r in result:
            print(r)
    else:
        print("Not Found!")

# Input: Postal codes as a list of integers
postal_codes = list(map(int, input().split()))

# Input: Target sum for pairs
target_sum = int(input())

find_receiver_house(postal_codes, target_sum)
