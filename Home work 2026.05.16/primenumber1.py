n = int(input("Enter the Number"))
is_Prime = True
for i in range (2,n):
    if(n%i==0):
        is_Prime = False
    break
if(is_Prime):
    print("IT IS A PRIME NUMBER")
else:
    print("IT IS NOT A PRIME NUMBER")