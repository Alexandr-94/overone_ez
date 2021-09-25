# a = 45
# b = 49
# deltemp = 7
# counter = 0
# arrtemp = []
# for i in range (a,b):
#     for j in range(1,b):
#         if i % j == 0:
#             counter += 1
#             arrtemp.append(j)
#     if counter >= 7:
#         print(f'{i} количество решений - {counter}, все решения',arrtemp)
#     else:
#         counter = 0
#         arrtemp = []
#
a=45
b=49
counter=0
arrtemp=[]
delmin=7
for i in range(a,b):
    for j in range(1,b):
        if i%j==0:
            counter=counter+1
            arrtemp.append(j)
    if counter>=7:
        print(f'у {i} кол-во решений - {counter}, все решения -',arrtemp)
    else:
        arrtemp=[]
        counter=0