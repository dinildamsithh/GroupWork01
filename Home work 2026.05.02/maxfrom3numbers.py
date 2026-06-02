n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))

if(n1>n2>n3):
    print("Largest is",n1)
else:
    if(n2>n1>n3):
         print("Largest is",n2)
    else:
        if(n3>n2>n1):
            print("Largest is",n3)
        else:
            if(n1>n3>n2):
                print("Largest is",n1)
            else:
                if(n2>n3>n1):
                    print("Largest is",n2)
                else:
                    if(n3>n1>n2):
                        print("Largest is",n3)

