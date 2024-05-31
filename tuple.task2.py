l=[42,36,28,96,4,-1,1]
min=999
max=-999
for i in range(0,len(list)):
    if l[i]<min:
        mini=l[i]
    if l[i]>max:
        maxi=l[i]
    print(mini+maxi)