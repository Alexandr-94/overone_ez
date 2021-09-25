# f = open('xyz.txt', 'w')
# f.write('Hello \nWorld')
# f.close()
# f = open('xyz.txt', 'r')
# print(*f)
# f.close()
# import os
#
# #os.rename('xyz.txt', 'abc.txt')
# print('Текущая деректория:',os.getcwd())
#
# #os.mkdir('folder')
# # os.chdir('folder')
# # print('Текущая дериктория изменилась на folder', os.getcwd())
# # os.chdir('..')
# # os.makedirs('nested1/nested2/nested3')
# #os.remove('C:/Users/sante/PycharmProjects/overone/twelveth_lesson/folder/2.txt')
# #os.rmdir('folder')
# os.removedirs('nested1/nested2/nested3')

with open('1.txt') as a:
    f = a.readline()
for i in f:
    i = i.replace('_',' ')
    j = i.split(' ')
print(j)

    print(type(f))