class shopping:
    def dresstype(self,typeofdress):
        self.a=typeofdress
    def price(self,cost):
        self.b=cost
    def size(self,size):
        self.c=size
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)
objectname=shopping()
objectname.dresstype("kurthi")
objectname.price(900)
objectname.size("l")
objectname.display()