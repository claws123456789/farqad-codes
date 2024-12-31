a = input ("enter any letter")
for i in a:
    if i == "a":
        print("a is found")
        break
    else:
        print("a is not found")


s = 10
while s > 0:
    s = s - 1
    if s == 9:

      continue
    print(s)


for a in range (10):
    if a%20 == 0:
        print("twist")
    elif a%15 == 0:
        pass
    elif a%3 == 0:
        print("fizz") 
    elif a%5 == 0:
        print("buzz")
    else:
        print(a)
