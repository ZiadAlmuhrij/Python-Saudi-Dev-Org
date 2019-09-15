

odd = []
even = []

for x in range(2,18,2):
    even.append(x)

for y in  range(3,19,2):
    odd.append(y)
print(even)
print('')
print(odd)

for a in odd:
    for b in even:
        print(a ,b)