x = input("Input The Numbers For The List(Type a comma to seperate between the characters)").split(",")
y = list(map(int,x))

prev = 0
next = 0

for i in y:
    next = i
    if(next>=prev):
        list_sort = True
    else:
        list_sort = False
        break
    prev = next
print(list_sort)

