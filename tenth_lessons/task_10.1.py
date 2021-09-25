# string_set = {'Коля','Миша','Женя','Саша'}
# print(string_set)
#
# num_set = set([1,2,3,4,5,6])
# num_set.discard(3)
# num_set.discard(7)
# #num_set.remove(7)
# num_set.remove(4)
# #num_set.clear()
# print(num_set)
#
# months = {'Jan','Feb','March','Apr'}
# months_b = {'July','Sep','Oct'}
#
# months.add('Aug')
# all_months = months.union(months_b)
# print(all_months)
# print('Apr' in months)
# print(months)
#
# x = {1,2,3}
# y = {4,5,6}
# z = {7,4,9}
# # print(x|y|z)
# print(x & y)
# print(x - y)
# print(y - x)
#
#
num = [1,2,3,4,5,6,7,3,2,1,5]
st = set(num)
vf = frozenset([1,2,3,4,6,7,8,9,7,44,8,6,6,6])
print(st & vf)
print(st|vf)