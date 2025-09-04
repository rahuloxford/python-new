
try:
    l = [1, 2, 3]
    print(l[6])
except NameError:
    print("Variable you're using might not be initialized")
except ZeroDivisionError:
    print("Cannot divide by zero you idoit")
except:
    print("Something went wrong")
else: # runs if theres no error in 'try' block
    print("abc")
finally:
    print("will run regardless you get an error or not in try")

print('program ended')