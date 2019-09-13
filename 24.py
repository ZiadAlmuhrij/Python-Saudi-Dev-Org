""" thisdect = {
    "brand" : {
    "model" : "Mustang",
    "year" : 1970
},

    "brand1" : {
    "model" : "ATS",
    "year" : 1999
},

    "brand2" : {
    "model" : "530",
    "year" : 2005
}} 
mydect = thisdect.copy()
mydict = dict(mydect)
print(mydect)
print(mydict)"""
child1 = {
    "name": "sarah",
    "year": 1999
}
child2 = {
    "name": "Ahmad",
    "year": 1998
}
child3 = {
    "name": "Ziad",
    "year": 2000
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3" : child3
}

print (myfamily)

thisdect = dict(brand="ford" , model = "must", year = 2014)
print(thisdect)
