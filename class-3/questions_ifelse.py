# Q. print if the number is POSITIVE, NEGATIVE, ZERO
number = float(input("enter a number here? "))

if number > 0:
    print("POSITIVE")
elif number < 0:
    print("NEGATIVE")
else:
    print("ZERO")


# grade calculator
marks = float(input("enter your marks? "))

if marks >= 90:
    print("Your marks is:", marks)
    print("Your grade is: A")
elif marks >= 80:
    print("Your marks is:", marks)
    print("Your grade is: B")
elif marks >= 70:
    print("Your marks is:", marks)
    print("Your grade is: C")
elif marks >= 60:
    print("Your marks is:", marks)
    print("Your grade is: D")
elif marks >= 50:
    print("Your marks is:", marks)
    print("Your grade is: E")
else:
    print("Your marks is:", marks)
    print("You failed the exam")


# Q. discount calculator
amount = float(input("What is your total bill amount? "))

if amount >= 10000:
    print("Your total bill is:", amount)
    print("After discount:", amount - (amount / 100 * 30))
elif amount >= 5000:
    print("Your total bill is:", amount)
    print("After discount:", amount - (amount / 100 * 20))
elif amount >= 1000:
    print("Your total bill is:", amount)
    print("After discount:", amount - (amount / 100 * 10))
else:
    print("Your total bill is:", amount)
    print("Please pay your billl")


# Q. bus fair calculator (calculate the bus fair)
# $5 for first 3km then $2 for every next km
distance = float(input("enter the distance traveled in (km)? "))

if distance <= 3:
    print("Your fair is $ 5")
else:
    fair = 5 + (distance - 3) * 2
    print("Your fair is: $", fair)


