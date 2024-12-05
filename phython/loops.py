n = int(input("enter a number whose sum you want"))
sum = 0

for i in range(1,n+1):
  sum = sum+i  
  print(sum)


string = input("enter any word")
string2 = ('')
for i in string:
   string2 = i + string2
   print("oringinal string",string)
   print("reversed string",string2)


n = int(input("enter any number"))
for i in range(n,0,-1):
   print(i)

