from human import Human
class Wizard(Human):
    def heal(self):
        self.health += 10

class Ninja(Human):
    def steal(self):
        self.stealth += 5

class Samurai(Human):
    def sacrifice(self):
        self.health -= 5

harry = Wizard()
rain = Ninja()
tom = Samurai()

print harry.health
print rain.health
print tom.health

harry.heal()
print harry.health

rain.steal()
print rain.stealth

tom.sacrifice()
print tom.health
print tom.stealth

A general skeleton for implicit inheritance:
