class dad():
    def __init__(self,eyes,aggresive):
         self.eyes = eyes
         self.aggresive = aggresive
    def display(self):
         print(self.eyes)
         print(self.aggresive)
class son(dad):
     def __init__(self,age,name,eyes,aggresive):
          self.age = age
          self.name = name
          dad.__init__(self,eyes,aggresive)

obj = son(11,"farqad","grey",True)
obj.display()



class vehicle():
     def __init__(self,name,max_speed,milage):
          self.max_speed = max_speed
          self.milage = milage
          self.name = name
class bus(vehicle):
     pass

o = bus("ayaan",20000000,70)
print(o.name)
print(o.max_speed)
print(o.milage)


class person():
     def __init__(self,name,id_number):
          self.name = name
          self.id_number = id_number
     def display(self):
          print(self.name)
          print(self.id_number)
class Employee(person):
     def __init__(self,salary,post,name,id_number):
          self.salary = salary
          self.post = post
          person.__init__(self,name,id_number)

ob = Employee(1000,"employee","izaan",123456789)
ob.display()

          