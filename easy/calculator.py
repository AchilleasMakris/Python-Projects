n1 = int(input("Give me the 1rst number: "))
n2 = int(input("Give me the 2nd number: "))

case = input("What calculation you want to perform? Reply with: +, -, *, or / :")

match case:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case "*":
        print(n1*n2)
    case "/":
        print(n1/n2)
    case _:
        print("Please provide a valid input")


