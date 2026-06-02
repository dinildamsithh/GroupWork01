#make a empty set. Add 2,5,"Hi","Hello",Ture. remove (10),removie(2),discard(10),discard(2),get union of 2 sets.look if 5 in set

x = set()
x.add(2)
x.add(5)
x.add("Hello")
x.add(True)
print(x)

x.remove(2)
print(x)

x.discard(10)
print(x)

y = {1,2,3,4,5,True}
z = x.union(y)
print(z)

v = x.intersection(y)
print(v)

