'''
# creating a function
def greet(name):
    print(f"Welcome {name}")
    print("Hope you are having a nice day")


# calling the function
greet("Tim")
greet("Jon")
greet("Peter")
greet("Mark")
'''

def user_details(name, age, height, weight=0):
    print("--User Details--")
    print(f"User name is: {name}")
    print(f"User age is: {age}")
    print(f"User height is: {height}")
    print(f"User weight is: {weight}")

# positional arguments
user_details("Mark", 28, 5.9, 176.9)

# keyword arguments
user_details(age=34, name="Bruce", weight=176.25, height=5.11)

# default arguments
user_details("Peter", 17, 6.0, 183.5)


