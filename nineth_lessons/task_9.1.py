# # d = {}
# # d = {'dict': 1, 'dictionary': 2}
# # print(d)
#
# # d = dict(short='dict', long='dictionary')
# # d_2 = dict([(1,1), (2,4)])
# # print(d, '\n', d_2)
#
# # d = dict.fromkeys(['a', 'b'])
# # d_2 = dict.fromkeys(['a', 'b'], 100)
# # print(d, '\n', d_2)
#
# # d = {a: a ** 2 for a in range(7)}
# # print(d)
#
# d = {1:2,2:4,3:9}
# d[4] = 4**2
# print(d[1])
# print(d)
# print(d.items())

d = {1:['hello', 2],'2':[95,'sun']}
for key,value in d.items():
    print(key,'_',value[0],'_', value[1] )
print(d.items())
print(d.keys())
print(d.values())