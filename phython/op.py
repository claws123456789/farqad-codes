a = 7
b = 10
c = 77

 

if a == b and b == c:
    print("equal")
else :
     print("not equal")
    


x = 1
y = 10
z = 100



print(x != y)
print(y != z)


height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))


BMI = weight / (height/ 100)**2
print(BMI)

if BMI <=18.4:
    print("you are underweight")
elif BMI <=24.9:
    print("you are healthy")
elif BMI <=29.9:
    print("you are over weight")
elif BMI <=34.9:
    print("you are severely over weight")
elif BMI <=39.9:
    print("you are obese")

num = int(input("enter any number"))
if num%2==0:
 print("even")

else:
    print("odd")
