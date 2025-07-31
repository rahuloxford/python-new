# why we need loops?

# Q. print "Hello World" 100 times

count = 1
while count <= 100:
    print("Hello World", count)
    count = count + 1

'''
count = 0
while count < 100:
    count = count + 1
    if count >= 90 and count <= 95:
        continue
    print("Hello World", count)

'''


# print numbers from 1 to n 

start = 1
end = int(input("Enter the end? "))

while start <= end:
    print(start)
    start += 1 # start = start + 1


# print all the even numbers from 1 to n 

start = 1
end = int(input("Enter the end? "))

while start <= end:
    if start % 2 == 0:
        print(start)
    start += 1


# print the table of a number?

number = int(input("Enter the number you want the table of? "))

i = 1
while i <= 10:
    print(number * i)
    i += 1
