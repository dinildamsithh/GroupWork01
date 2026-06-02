n = int(input("Enter The Number"))
digits = list(map(int, str(n)))
i=0
sum = 0
for i in range (digits[0],digits[-1]+1):
    sum = sum + i
    i = i+1
print(sum)

