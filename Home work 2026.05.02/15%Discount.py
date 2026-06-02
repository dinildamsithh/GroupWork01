a = int(input("Enter The Amount"))
if(a>=1000):
    discount = a*15/100
    print("To Pay",a-discount)
else:
    print("To Pay",a)