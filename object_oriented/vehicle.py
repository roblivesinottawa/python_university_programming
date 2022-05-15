class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__secret = "This is a secret attribute"

    def setdiscount(self, amount):
        self._discount = amount

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def __repr__(self):
        return f"{self.year} {self.make} {self.model}"

vehicle1 = Vehicle("Ford", "Fiesta", 2019, 30000)
vehicle2 = Vehicle("Toyota", "Corolla",2017, 20000)
vehicle3 = Vehicle("Tesla", "Model S", 2019, 50000)

print(vehicle1)
print(vehicle1.getprice())


# set the discount
print(vehicle2.getprice())
vehicle2.setdiscount(0.25)
print(vehicle2.getprice())