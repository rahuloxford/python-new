# def total(a, b, c):
#     return a + b + c

# result = total(16, 89, 25)
# print(result)


# def evenOrOdd(number):
#     if (number % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"

# print(evenOrOdd(12))


# search if the target element is available inside the list,
# if target found print the index of it, otherwise -1

def search(nums, target):
    for index in range(len(nums)):
        if target == nums[index]:
            return index
    
    return -1

nums = [46, 89, 47, 76, 28, 37, 73]
target = eval(input("enter your target element? "))

result = search(nums, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")