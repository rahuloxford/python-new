list1 = ["tom", 78, 3.1415, "jim", 78]

print(list1)
list1.append(55)
list1.insert(2, 99)
list1.extend([10, 20, 30, 40])
list1.pop()
list1.pop(4)
list1.remove(55)
print(list1.index(78))
print(list1.count(78))
# list1.clear()
list2 = list1.copy()

list1[0] = 101

print(list1)
print(list2)


list3 = [45, 90, 53, 11, 38]
list3.sort()
list3.reverse()
print(list3)