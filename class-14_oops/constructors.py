class Car:
    def __init__(self, engine, mileage, price):
        self.engine = engine
        self.mileage = mileage
        self.price = price

    def details(self):
        print(f"Car engine: {self.engine}")
        print(f"Car mileage: {self.mileage}")
        print(f"Car price: {self.price}")

    def distanceToEmpty(self, fuel):
        print(f"You can travel {fuel * self.mileage}km,")
        print("With the remaining fuel left.")

bmw = Car("v12 petrol", 13.5, 16000000)
audi = Car("v16 petrol", 11, 20000000)
honda = Car("3ltr petrol", 15, 3500000)

bmw.distanceToEmpty(20)

# audi.details()
# honda.details()