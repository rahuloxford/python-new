'''
# print all the even numbers from 1 to n

num = 1
n = int(input("enter the end? "))
while num <= n:
    if num % 2 == 0:
        print(num)
    num = num + 1 # increment


# print the table of a number? given by user

number = int(input("enter a number to get table? "))

counter = 1
while counter <= 10:
    print(f"{number} x {counter} = {number * counter}")
    counter += 1

'''


# take a number from the user and print that number in reverse?
'''
number = int(input("enter a number? "))
original = number

reverse = 0

while number > 0:
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10

print(f"{original} is now reversed to {reverse}")

# check if a number is palindrom
if original == reverse:
    print("number is palindrom")
else:
    print("number is not palindrom")
'''


# count the number of digits in a number

number = int(input("enter a number? "))
original = number

count = 0

while number > 0:
    count += 1
    number = number // 10

print(f"{original} has {count} digits")


# what are f strings
name = "tim"
age = 35

#print(name, "is", age, "years old")
#print(f"{name} is {age} years old")
