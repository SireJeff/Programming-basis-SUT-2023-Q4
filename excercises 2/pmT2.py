import sys
from math import gcd

def custom_gcd(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

def calculate(operation, numbers):
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return round(sum(numbers) / len(numbers), 2)
    elif operation == "lcd":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = (result * numbers[i]) // gcd(result, numbers[i])
        return result
    elif operation == "gcd":
        return custom_gcd(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "max":
        return max(numbers)
    else:
        return "Invalid command"

operation = input().strip()
if operation not in ["sum", "average", "lcd", "gcd", "min", "max"]:
    print("Invalid command")
else:
    numbers = []
    while True:
        try:
            num = input().strip()
            if num == "end":
                break
            numbers.append(int(num))
        except ValueError:
            print("Invalid command")
            continue

    result = calculate(operation, numbers)
    print(result)

#def custom_sum(numbers):
#    return sum(numbers)

#def custom_average(numbers):
#    return round(sum(numbers) / len(numbers), 2)

#def custom_lcm(numbers):
 #   def lcm(a, b):
  #      return a * b // custom_gcd(a, b)

   # result = numbers[0]
    #for i in range(1, len(numbers)):
     #   result = lcm(result, numbers[i])
    #return result

#def custom_gcd(a, b):
 #   while b:
  #      a, b = b, a % b
   # return a

#def custom_min(numbers):
 #   return min(numbers)

#def custom_max(numbers):
 #   return max(numbers)

#def custom_calculate(operation, numbers):
 #   if operation == "sum":
  #      return custom_sum(numbers)
   # elif operation == "average":
    #    return custom_average(numbers)
   # elif operation == "lcm":
   #     return custom_lcm(numbers)
   # elif operation == "gcd":
    #    return custom_gcd(numbers[0], numbers[1])
    #elif operation == "min":
     #   return custom_min(numbers)
    #elif operation == "max":
     #   return custom_max(numbers)
    #else:
     #   return "Invalid command"

#operation = input().strip()

#if operation not in ["sum", "average", "lcm", "gcd", "min", "max"]:
#    print("Invalid command")
#else:
   # numbers = []
   # while True:
       # try:
        #    num = input().strip()
       #     if num == "end":
      #          break
     #       numbers.append(int(num))
    #    except ValueError:
   #         print("Invalid command")
  #          continue

 #   result = custom_calculate(operation, numbers)
#    print(result)
