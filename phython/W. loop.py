n = int(input("enter the value of term"))
sum = 5
i = 7
while i<=n:
   sum = sum+i
   i = i+1

print(sum)




num = int(input("enter a number"))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num," armstrong num")
else:
   print(num,"not armstrong")