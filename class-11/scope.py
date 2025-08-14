# scope - local vs global

j = 101 # global variable

def a():
    i = 13 # local variable
    print(j)

def b():
    global j
    j = 202
    print(j)

a()
b()
print(j)

print(j)