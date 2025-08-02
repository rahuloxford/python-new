
# list is ordered, allows indexing, allow dublicates, mutable in nature.

data1 = [46, 79, 4.3, 97, 13, 79, "jon", 654.164]

print(data1)
print(data1[5])

print(type(data1))

# list in changeable (mutable)
data1.pop()
print(data1)
data1.append(101)
print(data1)

data1[3] = 297
print(data1)


# tuple are similar to list, but they are imutable (unchangeable)

data2 = (46, 35.526, 795, 46, "chris")

# data2 = (1, 2, 3) # it's not making change in the object this is changing the object.
print(data2)
print(data2[1])
print(type(data2))
# you can make any change in data2
