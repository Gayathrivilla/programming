a=int(input("enter a"))
if a%3==0 and a%5==0:
    print("great")
elif a%3==0 and a%9==0:
    print("good")
elif a%3==0 and a%7==0:
    print("okay")
else:
    print("not okay")