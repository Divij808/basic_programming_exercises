import re
import math
calculator = input("enter math equation")

match = re.search(r'(\d+)(.+?)(\d+)', calculator.strip())
if match is None:
    print("Do not know the maths equation")
else:

    first = int(match.group(1))
    second = match.group(2).strip()
    third = int(match.group(3))
    if second.strip() == "*":
        answer = first * third
        print(answer)
    elif second.strip() == "/":
        answer = first / third
        print(answer)
    elif second == "+":
        answer = first + third
        print(answer)
    elif second == "-":
        answer = first - third
        print(answer)
    elif second.strip() == "%":
        answer = first % third
        print(answer)
    elif second.strip() == "^":
        answer = math.pow(first, third)
        print(answer)
    else:
        error = "Do not know the maths equation"
        print(error)
