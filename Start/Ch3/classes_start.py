class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.engine = enginetype
        self.wheels = 4
        self.doors = 4

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Car at {self.speed} mph")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, has_side_car):
        super().__init__("Motorcycle")
        self.engine = enginetype
        if has_side_car:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Motorcycle at {self.speed} mph")

corolla = Car("gas")
tesla = Car("electric")
bike = Motorcycle("gas", True)

corolla.drive(100)
tesla.drive(120)
bike.drive(200)
