n = input("enter a number:")
n = int(n)
total = 0
for i in range(1,n+1):
    total = total+i
sam = total / n
print("SUM of first {}  number's average is {}.".format(n, sam))
