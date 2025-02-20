from abc import ABC,abstractmethod
class animal():
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class cat(animal):
    def move(self):
        print("i can meow")
class dog(animal):
    def move(self):
        print("i can bark")
class lion(animal):
    def move(self):
        print("i can roar")
class horse(animal):
    def move(self):
        print("i can neigh")

r = human()
r.move()
c = cat()
c.move()
d = dog()
d.move()
l = lion()
l.move()
h = horse()
h.move()



#
#Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class india():
    def capital(self):
        print("new delhi is the capital of india")
    def language(self):
        print("hindi is the common language in india")
    def type(self):
        print("india is a developing country")

class japan():
    def capital(self):
        print("tokyo is the capital of japan")
    def language(self):
        print("japenise is the common langueage")
    def type(self):
        print("it is a developing country")
obj = india()
o = japan()
for i in(obj,o):
 i.capital()
 i.language()
 i.type()

from abc import ABC,abstractmethod
class hr(ABC):
    def print(self,a):
        print(a)
    def task(self):
        print("we are inside task")
class olo(hr):
    def task(self):
        print("we are inside olo task")
olo.obj = olo()
olo.obj.task()
olo.obj.print(100)

