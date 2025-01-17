num1, num2 = 0, 1
count = 0

n = int(input("Give me an integer: "))

if n == 0:
    print("The fibonacci sequence of 0 is 0")
elif n == 1:
    print("The fibonacci sequence of 1 is 1")
else:
    print("Fibonacci sequence: ")
    while count <= n:
        print(num1, end = " ")
        temp = num1 + num2
        num1 = num2
        num2 = temp
        count += 1