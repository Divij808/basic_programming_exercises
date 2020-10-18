list1 = [3, 2, 0, 15, 4, 60, 1]
for i in range(len(list1)-1):
    if list1[i] > list1[i+1]:
        p = list1[i+1]
        list1[i + 1] = list1[i]
        list1[i] = p
print('Biggest number in my list is {}'.format(list1[len(list1)-1]))
print(list1)

