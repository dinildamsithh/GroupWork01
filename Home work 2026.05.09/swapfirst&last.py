n = int(input("Enter The Number"))
digits = list(map(int, str(n)))

digits[0] ,digits[-1] = digits[-1] ,digits[0]

result = int("".join(map(str, digits)))
print(result)