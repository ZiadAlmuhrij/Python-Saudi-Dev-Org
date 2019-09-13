thisdect = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}

if "model" in thisdect:
    print ("yes, Model is there")
print(len(thisdect))
thisdect["color"] = "red"
print(thisdect)
thisdect.pop("model")
thisdect.popitem()
del thisdect["year"]
print(thisdect)
thisdect.clear()
print(thisdect)
del thisdect
print(thisdect)