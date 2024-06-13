fruits=["apple","mango","orange"]
fruits.insert(1,"cherry")
print(fruits)

a=["roti","dosa"]
b=["tea","coffee"]
a.extend(a)
a.remove("dosa")
b.pop(1)
print(a)
print(b)

a=["orange","apple"]
a.sort()
print(a)

b=[55,100,10,20]
b.sort()
print(b)

a=[1,2,3,4]
b=a.copy()
print(b)