# Problem: Use a property decorator in the Car class to make the model attribute read-only.


class Car():
    total_car=0   # ✅ Class variable
    
    def __init__(self,brand,__model):
        Car.total_car+=1
        self.brand=brand  # ✅ Instance variable
        self.__model=__model  # ✅ Instance variable
        
    def full_name(self):
        temp=5               # ✅ Local variable (only available inside this method)
        return f"{self.brand} and {self.__model}"
    
    def fuel_type(self):
        return f"Petrol and Diesel"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return f"Electric Charge"
        
# tesla=ElectricCar("Tesla","T-72","90kWH")
# print(tesla.fuel_type())


tata1=Car("TATA","T-99")

print(tata1.model)
tata1.model='T-729'
print(tata1.model)



# first make it private
# ADD Property Decorator
