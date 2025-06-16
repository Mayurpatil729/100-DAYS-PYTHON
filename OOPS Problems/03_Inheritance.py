# Create an Electricclass that inherits from the Car class 
# and has an additional attribute

class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand} and {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
        
tesla=ElectricCar("Tesla","T-72","90kWH")
print(tesla.brand)
print(tesla.model)
print(tesla.battery_size)
print(tesla.full_name())



# This class is a child class that inherits from the Car class.
# It means ElectricCar automatically gets all attributes and methods of the Car class (like brand, model, and full_name()), without rewriting them.

#  What is super()?
# super() is a built-in Python function that lets you call the parent class’s methods.
# super().__init__(brand, model) means:
# “Hey, go to the parent (Car) class and call its constructor to set brand and model.”



