a = [4,6,'py','tell',78]
b = [44,'hello',54,'exept',3]
b.extend(a)
print(a)
#c = a+b
b.insert(3,6)
print(b)
for i in b:
    if type(i) is str:
        b.remove(i)

print(b)
