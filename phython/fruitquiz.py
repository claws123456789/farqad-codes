#Write a Python class to convert an integer value to a Roman numeral and implement Object-Oriented Programming.
import random
class fruitquiz():
    def __init__(self):
        self.fruit={'1':'I',
                            '2':'II',
                             '3':'III',
                             '4':'IIII'}
    def quiz(self):
             while (True):
                      roman, number = random.choice(list(self.fruit.items()))
                      print("what is the number of{}".format(roman))
                      user_answer = input()
                      if(user_answer == number):
                           print("correct answer")
                      else:
                         print("wrong answer")
                      option = int(input("press 0 if you want to play again else press 1"))  
                      if  option:
                           break
    
print("welcome to number quiz")
obj = fruitquiz()
obj.quiz()


