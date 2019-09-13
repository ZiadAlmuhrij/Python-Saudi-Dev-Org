thislist = ["apple", "banana", "cherry", 1 ,2, 3]
mylist= thislist.copy()
print (thislist)
print (thislist[5])
thislist[1]= "burned banana"
del thislist[3]
print(mylist)
for x in thislist:
    print(x)
