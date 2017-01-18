class Bike(object):
    def __init__(self, price=100, max_speed=10):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price: " +str(self.price) + ", Max Speed: " +str(self.max_speed) + ", Miles: " + str(self.miles)
    def ride(self):
        print "Riding..."
        self.miles += 10
    def reverse(self):
        print "Reversing..."
        if self.miles - 5 < 0:
            print "You reversed", self.miles, "miles back to 0 total miles. You can't reduce your miles any further!"
            self.miles = 0
        else:
            self.miles -= 5

road_bike = Bike(500, 40)
mountain_bike = Bike(400, 20)
tricycle = Bike(25, 5)

road_bike.ride()
road_bike.ride()
road_bike.ride()
road_bike.reverse()
road_bike.displayInfo()

mountain_bike.ride()
mountain_bike.ride()
mountain_bike.reverse()
mountain_bike.reverse()
mountain_bike.displayInfo()

tricycle.reverse()
tricycle.reverse()
tricycle.reverse()
tricycle.displayInfo()
