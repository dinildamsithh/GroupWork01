n = int(input("Input The Number: "))

prev = 0
next = 1
i = 0

if n <= 0:
    print("Please enter a number")
else:
    print("Fibonacci Sequence:")

    while i < n:
        print(prev, end=" ")

        temp = prev + next
        prev = next
        next = temp

        i = i + 1