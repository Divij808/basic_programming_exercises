# Selection sort
list2 = [1,6,9]
list3 = []
for j in range(len(list2)):
    for i in range(len(list2) - 1):
        if len(list2) == 1:
            break
        if list2[i] < list2[i + 1]:
            p = list2[i + 1]
            list2[i + 1] = list2[i]
            list2[i] = p
    list3.append(list2[len(list2) - 1])
    list2.remove(list2[len(list2) - 1])
len(list3)
print(list3)
start = 1
end = len(list3)
run = True
target = int(input('enter a number'))
while run:
    middle = int((start + end) / 2)
    if list3[middle - 1] == target:
        print('found the number')
        run = False
    elif start == end:
        print('I do not have the number {}'.format(target))
        run = False
    elif list3[middle - 1] > target:
        end = middle - 1
    elif list3[middle - 1] < target:
        start = middle + 1
