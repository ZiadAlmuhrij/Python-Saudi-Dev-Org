thisset = {"apple", "banana", "cherry" , 1, 2, 2,1,3}
thisset.add(3)

for x in thisset:
    print(x)
print ("banana" in thisset)

thisset.update(["one", 4])
print(thisset)

print(len(thisset))

thisset.remove("banana")
thisset.discard("cherry")
thisset.discard("che4rry")
print(thisset)
x= thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset)
del thisset
"""print(thisset)"""

thisset = set(("apple", "banana","water"))
print(thisset)