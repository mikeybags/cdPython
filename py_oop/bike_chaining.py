class Bike(object):
    def __init__(self, price=100, max_speed=10):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price: " +str(self.price) + ", Max Speed: " +str(self.max_speed) + ", Miles: " + str(self.miles)
        return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        if self.miles - 5 < 0:
            print "You reversed", self.miles, "miles back to 0 total miles. You can't reduce your miles any further!"
            self.miles = 0
        else:
            self.miles -= 5
        return self

road_bike = Bike(500, 40)
mountain_bike = Bike(400, 20)
tricycle = Bike(25, 5)

road_bike.ride().ride().ride().reverse().displayInfo()
mountain_bike.ride().ride().reverse().reverse().displayInfo()
tricycle.reverse().reverse().reverse().displayInfo()
