a = [5,[1,2],2,'r',4,'ee']
b = [4,'we','ee',3,[1,2]]
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)
