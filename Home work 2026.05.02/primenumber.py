number = int(input("Enter The Number"))
X=1
for i in range(2,number):  
      X=X*(number%i)
if(X>0):
       print("IT IS A PRIME NUMBER")
else:
       print("IT IS NOT A PRIME NUMBER")

            