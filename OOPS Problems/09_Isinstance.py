# Demonstrate the use Of isinstanceO to check if my_tesla is an instance of Car and ElectricCar.

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
        
tesla=ElectricCar("Tesla","T-72","90kWH")
# print(tesla.battery_size)
print(isinstance(tesla,ElectricCar))       # isinstance method
print(isinstance(tesla,Car))

# tata1=Car("TATA","T-99")
# print(Car.total_car)









