# numbers = []
# x = int(input("Number of elements in array: "))

# for i in range(0, x):
#     numbers.append(int(input("Enter a number: ")))
    
# print(numbers)  


def recursividade(x):
    if x == 1:
        return 1
    else:
        return(x * recursividade(x-1))    

num = 6
print("The factorial of", num, "is", recursividade(num))