# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car():
    total_car=0   # ✅ Class variable
    
    def __init__(self,brand,model):
        Car.total_car+=1
        self.brand=brand  # ✅ Instance variable
        self.model=model  # ✅ Instance variable
        
    def full_name(self):
        temp=5               # ✅ Local variable (only available inside this method)
        return f"{self.brand} and {self.model}"
    
    def fuel_type(self):
        return f"Petro and Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return f"Electric Charge"
        
# tesla=ElectricCar("Tesla","T-72","90kWH")
# print(tesla.fuel_type())

tata1=Car("TATA","T-99")
tata2=Car("TATA","T-100")
tata3=Car("TATA","T-101")
# print(tata.fuel_type())

print(Car.total_car)

# ---------------------------------------------------------------


# | Variable Type     | Example                    | Belongs To      | Accessed By                |
# | ----------------- | -------------------------- | --------------- | -------------------------- |
# | Class Variable    | `total_car`                | Class itself    | `ClassName.var`            |
# | Instance Variable | `self.brand`, `self.model` | Specific object | `self.var` or `object.var` |
# | Local Variable    | `temp` (inside a method)   | Method only     | Cannot access outside      |












