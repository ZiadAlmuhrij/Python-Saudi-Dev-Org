thisdect = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdect)

x = thisdect ["model"]
print(x)
z = thisdect.get("model")
print(z)

thisdect ["model"] = "Chev"
x = thisdect ["model"]
print(x)

for x in thisdect:
    print (x)
    print(thisdect[x])

for x in thisdect.values():
    print (x)

thisdict = {"brand" : "BMW", "model" : "730", "year": 1996}
print(thisdict.values())

for x, y in thisdict.items():
    print(x,y)
