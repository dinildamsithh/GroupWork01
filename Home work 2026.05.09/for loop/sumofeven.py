n = int(input("Enter The Number"))
sum = 0
for i in range(0,n+1):
    if(i%2==0):
     sum = sum + i
     
    else:
       sum = sum+0
print(sum)