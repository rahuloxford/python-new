
# operators -> symbols that performs some operations

# ------ Arithemetic Operators ------

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)

print(10 / 4)
print(10 // 4) # int division

print(2 ** 5) # exponent
print(17 % 3) # modulas


# ------ Comparison Operators ------

print(5 > 5)
print(5 >= 5)

print(1 < 5)
print(2 <= 5)

print(18 == 19)
print(5 != 8)


# ------ Logical Operators ------
# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not
print(not True or not False)
print(not False)

print("=----------")

#age = 12
#print(age >= 18 and age <= 100)

num = 30
print(num % 5 == 0 or num % 15 == 0)



# membership operators

show = "prison break"

print("prison" in show)
print("peter" not in show)


# identity operators
a = "hello"
b = "hello"
c = "".join(["he", "llo"])  # creates a new string at runtime

print(a == b)   # True - values are the same
print(a is b)   # True - both point to the same interned string object

print(a == c)   # True - values are still the same
print(a is c)   # False - c is a new object with the same content


print(a is not c)




