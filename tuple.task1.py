tuple1=("A",1,4,3,"B")
print(tuple1)
print(type(tuple1))
tuple1=tuple1+("hello",)
tuple1=tuple1+(7,"c")
print(tuple1)
tuple1[3]="D"
print(tuple1)
for i in range(0,5):
    n=int(input("enter"))
    tuple1=tuple1+(n,)
print(tuple1)