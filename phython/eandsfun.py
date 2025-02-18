#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class far():
    privatevariable = 8
    def privatemethod(self):
       print("my name is farqad")

obj = far()
obj.privatemethod()



class computer():
    def __init__(self,model,price):
        self.model = model
        self.price = price
        def display(self):
         print("the model name is",self.model)
         print("the price name is",self.price)

ob = computer("bmw",1000)
ob.display()










class StringReverser:

def __init__(self, text):

self.text = text

def reverse_words(self):

return ' '.join(self.text.split()[::-1])

# Example usage

string = "Hello World! This is Python."

reverser = StringReverser(string)

print(reverser.reverse_words())


