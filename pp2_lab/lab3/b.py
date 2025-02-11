class cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def beep(self):
        return f"{self.brand} {self.model} beeps"
    
    def go(self):
        return f"{self.brand} {self.model} started going"
    
    def stop(self):
        return f"{self.brand} {self.model} has stopped"

class Car(cars):
    def __init__(self, brand, model, year, speed):
        super().__init__(brand, model, year)
        self.speed = speed
    
    def race(self):
        return f"{self.brand} {self.model}'s speed is {self.speed} km/h"
    
    def __str__(self):
        return f"{self.brand}'s information has been introduced"
    
car1 = Car("Koeningsegg", "1", 2019, 60)
print(car1.go())
print(car1.race())
    