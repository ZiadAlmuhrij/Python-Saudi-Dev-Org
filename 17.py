thistuple=("a","b","c","d","e")

if "b" in thistuple:
    print("yes, b is in this list")

repeattuple = ("Zed",) * 4
print (repeattuple)

addtuple = thistuple + repeattuple
print (addtuple)

exampletuple = (3,4,5,6)
exampletuple = exampletuple + (1,2,3)
print (exampletuple)
print (len(exampletuple))

contuple = tuple(("one","two","three"))
print (contuple)

thislist = [1,2,3,"a","b"]
convtuple = tuple(thislist)
print(convtuple)