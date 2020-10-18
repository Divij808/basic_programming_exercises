import math


Hello = "Hello"
print(Hello)
bord = input("Do u want binary to denery(b2d) or denery to binary(d2b):")
if bord.strip() == "b2d":
    ban = int(input("enter a binary number:"))
    i = 0
    sum = 0
    while ban > 0:
        s1 = ban % 10
        ban = ban / 10
        sum = int(sum) + int(s1) * math.pow(2,i)
        i = i + 1
    print(sum)
elif bord.strip() == "d2b":
    d = int(input("enter a denry number"))
    denry = ""
    while d > 0:
        r = int(d % 2)
        d  = int(d / 2)
        denry = denry +str(r)
    print(denry[::-1])
else:
    print("error")