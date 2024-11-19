a = 7
print("type a is:",type(a))

b = 7.7
print("type b is:",type(b))

c = "farqad"
print("type c is:",type(c))

d = True
print("type d is:",type(d))


name = "ronaldo"
age = 39
is_student = True
weight = 55.45

print("name:", name)
print("data type of name is", type(name))

print("age:", age)
print("data type of age is", type(age))

print("is_student:", is_student)
print("data type of name is", type(is_student))

print("weight:", weight)
print("data type of name is", type(weight))


age = str(age)
print(age)
print("data type of age is",type(age))
weight = int(weight)
print(weight)
print("data type of weight is",type(weight))

text = str(input("enter a string"))
revtext = text[::-1]
text = revtext

print( " reverse of  given string is:")
print(text)