tuplex =("farqad",3.5,6,)
print(tuplex)

tuplex = (1,7,10,8,6,4,)
print("tuplex")


tuplex = tuplex+(9,)
print(tuplex)


tuplex = (1,9,7,8,10,4)
print("tuplex.count(9,7,10)")


tuplex = (5,3,7,9,10,4,8,2,0)
a = tuplex[3:5]
print(a)







def palind(r):
    a = len(r)-1
    s = 0
    while(a<s):
             if(r[s]!=r[a]):
                     return False
             a+=1
             s-=1
             return True
r = (1,2,3,3,2,1)
if(palind(r)):
           print("The tuple is a flip-flop!")

else:

      print("The tuple is not a flip flop")



weather =  (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in range(0,7):
        if(weather[i]==0):
                rainy+=1
        else :
                sunny+=1
if(sunny>rainy):
                print("good weather")
else:
                print("bad weather")

           
        
    