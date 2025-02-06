num1 = [1,2,3]
num2 = [4,5,6,]
result = map(lambda x,y:x+y,num1,num2)
print(list(result))


a = [1,2,3]
def square(n):
    return n*n
result = map(square,a)
print(list(result))


