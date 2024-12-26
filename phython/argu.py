def bill(total,tip):
    a = total+tip
    print("tip of the hotel is",a)
bill(430,30)


def cube(number):
    s = number*number*number
    print("cube answer is",s)
cube(2)

p = int(input("enter any number"))
flag = False
for i in range(2,p):
    if (p%i)==0:
        flag=True
        break
if flag:
    print("it is not a priem number")
else:
    print("it is a prime number")


def factorial(x):
   if x ==0 or x ==1:
    return 1
   else: 
    return x * factorial(x-1)
print(factorial(8))