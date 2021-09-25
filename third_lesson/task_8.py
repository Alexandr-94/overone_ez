s = str(input())
a = s.find(' ')
c = s[a + 1:]+ ' ' + s[0:a]
print(c)
b = c.replace('1','one')
print(b)