n = int(input("Enter The Number"))
digits = list(map(int, str(n)))
i=0
product = 1
for i in range (digits[0],digits[-1]+1):
    product = product*i
    i = i+1
print(product)