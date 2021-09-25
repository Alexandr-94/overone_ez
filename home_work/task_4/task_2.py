arr = [1,2,3,4,5,6,7,8,3,4,5,6,]
b = []
print('Массив',arr)
for i in arr:
    if arr.count(i) >= 2:
        if  i not in b:
            b.append(i)

print('',b)
# and b.count(i) == 0