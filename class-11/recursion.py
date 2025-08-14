
# recursion - when a function calls itself.

# Q. print the factorial of n using recursion.

def factorial(number):
    if number > 0:
        return number * factorial(number - 1)
    
    return 1

def sumOf1ton(number):
    if number > 0:
        return number + sumOf1ton(number - 1)
    
    return 0

num = eval(input("enter number? "))
print(f"factorial of {num} is: {factorial(num)}")
print(f"sum of 1 to {num} is: {sumOf1ton(num)}")