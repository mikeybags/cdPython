class Car(object):
    def __init__(self, price = 15000, speed = 100, fuel = "Full", mileage = 20):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if price > 10000:
            self.tax = 0.15
        self.display_all()

    def display_all(self):
        print "Price:", self.price
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel:", self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax:", self.tax

civic = Car(7000, 30, "Full", 30)
corvette = Car(40000, 160, "Almost Empty", 15)
jeep = Car(20000, 60, "One-Quarter Full", 12)
yugo = Car(1000, 5, "Almost Full", 40)
enzo = Car(500000, 250, "Half-Full", 10)
tesla = Car(90000, 50, "Who needs fuel?", "300 miles per charge")
