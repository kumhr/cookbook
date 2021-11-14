list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
res_list = []

for i in list1:
    if i % 2 != 0:
        res_list.append(i)

for i in range(len(list2)):
    if list2[i] % 2 == 0:
        res_list.append(list2[i])

print(res_list)
