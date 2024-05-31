n=47
s=0
n1=n
while n>0:
    digit=n%10
    n=n//10
    s=s+digit
if n1%s==0:
    print("divisible")
else:
    print("not divisible")
