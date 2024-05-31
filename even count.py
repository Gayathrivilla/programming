s=0
n=12467
while n>0:
    digit=n%10
    if digit%2==0:
        s=s+1
    n=n//10
print(s)