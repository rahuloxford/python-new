
class Car:
    engine = ""
    color = ""
    price = 0

    def move(self):
        print("Car is moving...")

bmw = Car()
audi = Car()

bmw.engine = "v12 petrol engine"
bmw.color = "black"
bmw.price = 10000000

audi.engine = "v16 petrol engine"
audi.color = "red"
audi.price = 25000000

print(bmw.engine)
print(bmw.color)
print(bmw.price)
bmw.move()

print(audi.engine)
print(audi.color)
print(audi.price)
audi.move()