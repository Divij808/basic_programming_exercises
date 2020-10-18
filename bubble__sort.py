lists = [4, 22, 11, 36, 9, 14, 1]
for i in range(len(lists) - 1):
    for i in range(len(lists) - 1):
        if lists[i] > lists[i + 1]:
            p = lists[i + 1]
            lists[i + 1] = lists[i]
            lists[i] = p
print(lists)