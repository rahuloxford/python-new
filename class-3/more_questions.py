
response = input("Have you completed your homework? ")

if response in ("Yes", "yes", "y", "Y", "YES"):
    print("You will get the chocolate")
elif response in ("No", "no", "NO", "n", "N"):
    print("You will not get the chocolate")
else:
    print("Wrong answer provided!")
