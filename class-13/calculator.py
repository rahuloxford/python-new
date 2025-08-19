
def total(*numbers):
    total = 0
    for number in numbers:
        total += number
    
    return total


def product(*numbers):
    product = 1
    for number in numbers:
        product *= number
    
    return product



if __name__ == "__main__":
    print("I am Calculator")