n=1223
sum=0
n1=n
while n>0:
    digit=n%10
    sum=sum*10+digit
    n=n/10
if sum==n1:
    print("palandrome")
else:
    print("not palandrome")