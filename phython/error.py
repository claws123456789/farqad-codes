try:

    num = int(input("enter any number"))
    print (num)

except ValueError as ex:
       print ("expectation",ex )
       
       
try:

     num1 = int(input("enter any number"))  
     num2 = int(input("enter any number")) 
     result = num1/num2
     print("result is:",result)
except ZeroDivisionError:
      print("zero is not allowed")
 
except ValueError:
      print("enter a numrical number")

except NameError as ex:
      print("the expectation is:",ex)

except:
      print("some error accured")

finally:
      print("i will excute no matter what happens")





valid = False
while not valid:

 try:

    n = int(input("Enter a number: "))
 while n%2 == 0:
    print("bye")
valid = True
 except ValueError:
 print("Invalid"):