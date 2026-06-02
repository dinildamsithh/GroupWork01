x = input("Input The Numbers For The List(Type a comma to seperate between the characters)").split(",")
y = list(map(int,x))

n = int(input("Enter The Number"))

for i in y:
    if(n==i):
        is_in = True
        break
    else:
        is_in = False
print(is_in)