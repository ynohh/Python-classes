def loop_test(list, value):
    countLoop = 0
    for i in list:
        if i > value:
            countLoop += 1
    return countLoop
    

def recursive_test(list, value):
    if not list:
        return 0
    else:
        return (list[0] > value) + recursive_test(list[1:], value)
    
    
value = int(input("Enter a number: "))
numbers = list(range(1, 501))

print("\nLOOP")
print("Amount of numbers greater than", value, "is", loop_test(numbers, value))
print("\nRECURSIVE")
print("Amount of numbers greater than", value, "is", recursive_test(numbers, value))

