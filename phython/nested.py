medical = input("Enter your medical cause yes or no")
attendance = int(input("Enter ypour attendance"))
if medical == "YES":
    print("YEs you are allowed")
else:
    if attendance > 75:
        
        print("yes you are allowed")
    else:
        print("you are not allwored")


print("select your choices")
print(" 1. is bike")
print("  2 is car")
choice = int(input("please select your choice"))
if choice == 1:
    print("what type of bike do you want")
    print("1. sports bike")
    print("2. reguler bike")
    choice2 = int(input("please select your bike"))
    if choice2 == 1:
        print("you selected sports bike")
    else:
        print("you selected reguler bike")
else:
    print("what type of car do you want")
    print("1. sports car")
    print("2. reguler car")
    choice2 = int(input("please select your car"))
    if choice2 == 1:
        print("you selected sports car")
    else:
        print("you selected reguler car")


unit = int(input("enter the unit"))
if unit<50:
    amount = unit*2.60
elif unit<=100:
    amount = unit*3.50
print(amount)

