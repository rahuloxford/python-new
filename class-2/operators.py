
# operators : symbols that performs some operations
'''
# Arithemetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 2)

print(10 // 4) # int division
print(2 ** 8) # exponent
print(10 % 3) # modulas

# Comparison operators
print(5 > 5)
print(5 >= 5)
print(1 < 1)
print(4 <= 4)

print(8 == 8)
print(6 != 6)
'''

# Logical operators

# and - return True only if all operands are True

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or - return True even if any one operand is True
# In other words False only if all operands are False

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not - inverts the operand.  True -> False, False -> True

print(not True)
print(not False)


# REAL LIFE EXAMPLE
'''
age = int(input('what is your age? '))

if age >= 18 and age <= 100:
    print("You can vote")

'''

'''
num = int(input("enter a number? "))

if num % 3 == 0 or num % 5 == 0:
    print("number is divisible by either 3 or 5")
else:
    print("number is not divisible by either 3 or 5")

'''

a = int(input('enter a number? '))
b = int(input('enter a number? '))
c = int(input('enter a number? '))

if a >= b and a >= c:
    print(a, "greatest")
else:
    if b > c:
        print(b, "is greatest")
    else:
        print(c, "is greatest")

'''
if a > b:
    if a > c:
        print(a, "is greatest")
    else:
        print(c, "is greatest")
else:
    if b > c:
        print(b, "is greatest")
    else:
        print(c, "is greatest")
'''

'''
if condition:
    if condition:
        if condition:
            code1
        else:
            code2
    else:
        code3
else:
    code4
    if condition:
        code5
    else:
        code6
'''







