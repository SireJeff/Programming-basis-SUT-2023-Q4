a=int(input("num of the first patient:"))
b=int(input("num of the last person:"))

print("",a , "and", b, "are:")
number=0

if a>b :
  for num in range(b,a + 1):

    if num > 1:
        for i in range(2, num):
           if (num % i) == 0:
               break

        else:
            number=number+1
  print(f"reverse order - amount: {number}")

else :
    for (num in range(a,b + 1)):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break

            elif i%2=0:
                number=number+1
            else:
                hagv
    print(f"main order - amount: {number}")
x=0
while x<200:
    x=x+1
else: 
    aaiudhg
