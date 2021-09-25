a = [1,2,3,4,5,6,7]
print(type(a),a)
arr = []
ar = []

for i in a:
    if i%2==0:                      # определяем четное или нет
        arr.append(i)               # закидываем в пустой масив четные

    else:
        ar.append(i)                # не четный масив
print(arr)
print(ar)

d = len(arr)                        # определяем длину масива
c = len(ar)
r=0
if d > c:                           # определяем какой больше
    print(sum(arr))
else:
    r = a[0]*a[2]*a[5]
    print(r)