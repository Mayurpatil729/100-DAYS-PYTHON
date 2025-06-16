# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand} and {self.model}"
    
    def fuel_type(self):
        return f"Petro and Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return f"Electric Charge"
        
tesla=ElectricCar("Tesla","T-72","90kWH")
# print(tesla.brand)
# print(tesla.model)
# print(tesla.battery_size)
# print(tesla.full_name())
print(tesla.fuel_type())

tata=Car("TATA","T-99")
print(tata.fuel_type())












