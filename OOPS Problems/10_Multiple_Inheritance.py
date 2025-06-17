# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating
# multiple inheritance.


class Battery:
    def battery_info(self):
        return "Battery capacity is 90kWh"

class Engine:
    def engine_info(self):
        return "Dual motor system"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"{self.brand} {self.model}"

# 🧬 Multiple Inheritance: ElectricCar gets everything from Battery, Engine, and Car
class ElectricCar(Battery, Engine, Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)  # explicitly call Car's constructor

    def full_info(self):
        return f"{self.car_info()} | {self.engine_info()} | {self.battery_info()}"


tesla = ElectricCar("Tesla", "Model S")
print(tesla.full_info())

# print(Car.__mro__)
# print(help(Car))

# -------------------------------------------------------------------

# 🧬 What is Multiple Inheritance?
# In Python, a class can inherit from more than one parent class. This is known as multiple inheritance.
# It means a child class can get:
# Attributes
# Methods
# from two or more parent classes.


# 🔁 Method Resolution Order (MRO)
# When multiple parents have a method with the same name, Python uses MRO (left to right) to decide which one to call.
# MRO (Method Resolution Order) tells Python in what order to look for a method or attribute when multiple classes are involved.
# It’s especially important when:
# A class inherits from multiple parent classes
# More than one parent has methods with the same name

# ✅ Rule:
# Python follows the order from left to right as defined in the class declaration.
# It uses something called the C3 Linearization algorithm (but you don’t need to memorize that — understanding the order is more important).



# ----------------------------------------------------------------------





