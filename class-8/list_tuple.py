# collection types

# list
# we use [] to create list
# list can store elements of different type.
# list is ordered, allows indexing, allows duplicates and is mutable.
driver1 = ["max", 27, "red bull", True, "red bull"]
print(driver1)
print(driver1[2])
print(type(driver1))

# i can make changes in driver1 cause it a list.
driver1.append(1400)
print(driver1)
driver1.pop()
driver1.pop()
print(driver1)
driver1[0] = "max verstappen"
print(driver1)


# tuple
# we use () to create tuple
# tuple can store elements of different type.
# tuple is ordered, allows indexing, allows duplicates and is imutable.
driver2 = ("Sebastian", 40, "red bull", False, "red bull")
print(driver2)
print(driver2[0])
print(type(driver2))




# set
# we use {} to create set
# set can store elements of different type.
# set is unordered, does not allows indexing, does not allows duplicates and is mutable.


driver3 = {"charles leclerc", 28, "ferrari", True, "ferrari", 28, 28}

print(driver3)
#print(driver3[3])
print(type(driver3))


driver3.add(1111)
print(driver3)









