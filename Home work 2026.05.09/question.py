# x = (5,6,7,8) y=("Hi","Hello",10)
#1) Put a for loop and print each values
#2)Concatenite x and y - print concatenation tuple
#3)make a tuple which includes (6,7) from x 
#4)unpack X using two variables

print("(1)") 

x = (5,6,7,8) 
for i in range (0,4):
    print(x[i])
y=("Hi","Hello",10)
for i in range (0,3):
    print(y[i], )

print("(2)")

z = x+y
print(z)

print("(3)")

Z = x[1:3]
print(Z)

print("(4)")
a,*b= (5,6,7,8)
print ("a =",a,"b =",b)

































