class Animal(object):
    def __init__(self, name=None):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name, "Health:", self.health
        return self

animal = Animal("animal1")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

harvey = Dog("Harvey")
harvey.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()

    def fly(self):
        self.health -= 10
        return self

dragon = Dragon("Puff the magic dragon")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
