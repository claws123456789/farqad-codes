word = input("enter any word")
char = input("enter anyb charecter")
i = 0
count = 0
while (i<len(word)):
      if (word[i]==char):
        count = count+1
      i=i+1
print(count)


lower = int(input("enter any num"))
upper= int(input("enter any num"))

for i in range(lower,upper+1):
   if i>1:
       for j in range(2,i):
           if(i%j)==0:
               break
       else:
           print(i)