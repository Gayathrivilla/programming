def login():
    while n!=0:
        user=input("enter username")
        pwd=input("enter password")
        if user==pwd:
            print("login successfully")
            n=0
    else:
        print("invalid enter again")