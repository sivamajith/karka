a=-5
if (a<0):
     print("postive")
else:
     print("negative")

a=4
if(a%2==0):
     print("even")
else:
     print("odd")

a=5
b=2
print(a*a)


a=10
b=5
if(a>b):
    print("greater")
else:
    print("equal")

year=2004
if year %4==0 or year %100==0:
    print("leap year")
else:
    print("not leap year")

age=int(input("enter your age"))
if age<16:
    print("you cant drive")
elif 16<= age >=17:
    print("you can drive but not vote")
elif 18<= age >=24:
    print("you can vote but not rent a car")
else:
    print("you can do preety much anything")
    
total=100
if(total>=90 and total<=100):
    print("a")
elif(total>=80 and total<=89):
    print("b")
elif(total>=70 and total<=79):
    print("c")
elif(total>=60 and toatl<=69):
    print("d")
else:
    print("fail")

year=2004
if(year %4==0 or year %100==0):
    print("leap year")
else:
    ("not leap year")

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
