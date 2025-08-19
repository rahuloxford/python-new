# check if a user can vote or not?

age = int(input("what is your age? "))

if age >= 18:
    print("user can vote")
else:
    print("user cannot vote")


# check if the number given by user is even or odd?

number = int(input("enter a number? "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")






# build a grading system

marks = float(input("what is your marks? "))

if marks > 100 or marks < 0:
    print("wrong input provided")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 50:
    print("E")
else:
    print("Fail")











