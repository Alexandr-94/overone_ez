with open('file.txt') as l:
    x =l.readlines()
    w,n =[],[]
    for i in x:
        i = i[:-1]
        if i.isalpha():
            print(i)
            w.append(i)
        elif i.isdigit():
            n.append(i)
print(sorted(n)+sorted(w))
