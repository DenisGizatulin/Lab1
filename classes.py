class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def info(self) -> None:
        print(f"Name: {self._name}, Capacity: {self._capacity} лет")
        

class Car(Vehicle):
    def __init__(self, name, capacity, fuel_type):
        super().__init__(name, capacity)
        self.fuel_type = fuel_type

class Truck(Vehicle):
    def __init__(self, name, capacity, payload_capacity):
        super().__init__(name, capacity)
        self.payload_capacity = payload_capacity

class Bus(Vehicle):
    def __init__(self, name, capacity, number_of_doors):
        super().__init__(name, capacity)
        self.number_of_doors = number_of_doors

class Bicycle(Vehicle):
    def __init__(self, name, capacity, gear_count):
        super().__init__(name, capacity)
        self.gear_count = gear_count

class Motorcycle(Vehicle):
    def __init__(self, name, capacity, engine_type):
        super().__init__(name, capacity)
        self.engine_type = engine_type

class Scooter(Vehicle):
    def __init__(self, name, capacity, battery_capacity):
        super().__init__(name, capacity)
        self.battery_capacity = battery_capacity

class Van(Vehicle):
    def __init__(self, name, capacity, cargo_space):
        super().__init__(name, capacity)
        self.cargo_space = cargo_space

class Train(Vehicle):
    def __init__(self, name, capacity, number_of_cars):
        super().__init__(name, capacity)
        self.number_of_cars = number_of_cars

class Submarine(Vehicle):
    def __init__(self, name, capacity, depth_rating):
        super().__init__(name, capacity)
        self.depth_rating = depth_rating
