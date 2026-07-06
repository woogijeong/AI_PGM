class Car:
    def __init__(self,make, model, color , price):
        self.make = make
        self.price = price
        self.color = color
        self.model = model
        
    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed
    def __str__(self):
        return f"Car ( speed = {self.speed} , color = { self.color } , model = { self.model})"


class ElectricCar(Car):
    def __init__(self, make, model, color, price, battery_capacity):
        super().__init__(make, model, color, price)
        self.battery_capacity = battery_capacity
    def set_battery_capacity(self, battery_capacity):
        self.battery_capacity = battery_capacity
    def get_battety_capacity(self):
        return self.battery_capacity
    def __str__(self):
        return f"ElectricCar ( make = {self.make}, model = {self.model}, color = {self.color}, price = {self.price}, battery_capacity = {self.battery_capacity})"

myCar = ElectricCar("Telsa", "model X", "red", 50000 , 100)
print(myCar)