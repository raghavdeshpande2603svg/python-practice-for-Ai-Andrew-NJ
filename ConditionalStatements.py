number = 2

match number:
    case 1:
        print("Number is 1")
    case 2 | 3:
        print("Number is 2 or 3")
#it is basically like a switch case statement in other programming languages. It is used to match the value of a variable with different cases.
x = 0
while x < 100:
    x += 2
print(x)