n1 = int(input("Enter the First Number"))
n2 = int(input("Enter the Second Number"))

if(n1>n2):
    n3 = int(input("Enter the Third number"))
    if(n3>n1):
        print(n3,"Is The Largest Number")
    else:
        print(n1,"Is The Largest Number")
else:
    n3 = int(input("Enter the Third number"))
    if(n3>n2):
        print(n3,"Is The Largest Number")
    else:
        print(n2,"Is The Largest Number")

