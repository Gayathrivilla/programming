n=12
s=0
for i in range(1,12):
    if n%i==0:
        s=s+i
print(s)
if s>n:
    print("greater")
else:
    print("lesser")