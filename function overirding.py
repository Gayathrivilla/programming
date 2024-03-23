class car_showroom:
    def __init__(self):
        self.cgst=789
        self.sgst=234
        self.insurance=678

    def company(self):
        while True:
           print("kia,verna,toyoto")
           self.n=input("select your company")
        if self.n=="kia":
            print("welocme to kia")
            self.model()
        elif self.n=="verna":
            print("welcome to verna")
            self.model()
        elif self.n=="toyoto":
            print("welcome to toyoto")
            self.model()
        else:
            print("invalid company") 

    def model(self):
        while True:
            self.carmodel = input("enter a car model")
            if self.carcompany == "toyota" and self.carmodel == "innova":
                break
            elif self.carcompany == "toyota" and self.carmodel == "fortuner":
                break
            elif self.carcompany == "mahindra" and self.carmodel == "scorpio":
                break
            elif self.carcompany == "mahindra" and self.carmodel == "thar":
                break
            elif self.carcompany == "mercedes" and self.carmodel == "Gwagen":
                break
            elif self.carcompany == "mercedes" and self.carmodel == "AMG":
                break
            else:
                print("enter a valid car model")

    def price(self):
        while True:
            if self.carmodel == "innova":
                srp = 3000000
                break
            elif self.carmodel == "fortuner":
                srp = 3300000
                break
            elif self.carmodel == "scorpio":
                srp = 2450000
                break
            elif self.carmodel == "thar":
                srp = 1120000
                break
            elif self.carmodel == "Gwagen":
                srp = 30000000
                break
            elif self.carmodel == "AMG":
                srp = 7100000
                break
            else:
                print("invalid")

        onroadprice = (srp)+(srp*((self.cgst)/100)) + \
            (srp*((self.sgst)/100))+(self.insurance)
        print(onroadprice)


obj1 = car_showroom()
obj1.company()
obj1.model()
obj1.price()