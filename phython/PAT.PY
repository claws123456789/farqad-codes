
n = int(input("enter any row"))
for i in range(n):
    for j in range(i+1):
        print("*",end = "")
    print()


n = int(input("enter any row"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end = "")
    print()



n = int(input("enter any row"))
number = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(number,end = "")
        number = number+1
    print()