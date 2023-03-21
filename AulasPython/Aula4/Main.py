print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Potentiation")
print("6 - Exit")
option = int(input("Chose an operation:"))



def operations(op, a, b):
    if op == 1:
        return lambda a, b: a + b
    elif op == 2:
        return lambda a, b: a - b
    elif op == 3:
        return lambda a, b: a * b
    elif op == 4:
        return lambda a, b: a / b
    else:
        return lambda a, b: a **b
    

while option != 6:

    if option == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add_result = operations(option, num1, num2)
        print(add_result)
    elif option == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(sub_calc(num1, num2))
    elif option == 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(mult_calc(num1, num2))
    elif option == 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(div_calc(num1, num2))
    else:
        num1 = int(input("Enter the number that will be potentiated: "))
        num2 = int(input("Enter the number to potentiate: "))
        print(pot_calc(num1, num2))

    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Potentiation")
    print("6 - Exit")
    option = int(input("Chose an operation:"))




