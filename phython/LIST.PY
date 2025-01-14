a = []
print()
a = [7,10,13]
print(a)
a = [10,32]*5
print(a)
a = [4,2,9]
a = a[::-1]
print(a)


def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print(lst)
    return ctr
count = match_words(['aba','cfc','xyz','aba','1221'])
print (count)


l = (2,4,6,7,4,3)
count = 0
for i in l:
    count += i
print(count)
print(len(l))
