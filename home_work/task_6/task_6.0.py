list = [15,48,'hello',6,19,'world']
arr =  []
nechet = []
chet = []
for i in list:
    if type (i) is int:
        arr.append(i)

print(i)
for i in arr:
    if i % 2 == 0:
        chet.append(i)
    elif i % 5 == 0:
        list.index(i)
print(chet)
print(type(chet))
print(arr)

