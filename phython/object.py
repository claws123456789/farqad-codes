#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IO():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("enter your name")
    def print_string(self):
        print(self.str1.upper())
str1 = IO()
str1.get_string()
str1.print_string()




#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class em:
    def __init__(self):
        print(em created)
    def __del__(self) :  
        print(em created)
    
    def create_obj():
        print("making object")
        obj = em()
        print("function ends")
        return obj
    print('calling create_obj()function...')
    obj = create_obj
    print('programe end')