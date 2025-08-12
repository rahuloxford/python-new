# *args & **args


# *args

# def total(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# result = total(13, 96, 43, 10, 78)
# print(result)


def user(**details):
    for i, j in details.items():
        print(f"{i} --> {j}")

user(name="peter", age=28, height=5.9, weight=59)
user(name="jon walker", age=43, rno=46579, salary=46301)