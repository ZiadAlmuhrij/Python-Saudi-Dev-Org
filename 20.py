thisset = {"apple", "banana", "cherry" , 1, 2, 2,1,3}
thisset.add(3)

for x in thisset:
    print(x)
print ("banana" in thisset)

thisset.update(["one", 4])
print(thisset)