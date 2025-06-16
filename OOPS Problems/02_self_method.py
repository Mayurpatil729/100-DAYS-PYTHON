
# Add a Method to Display Full Name(brand,model)
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand} and {self.model}"

    
car1=Car("Tesla","101")
print(car1.brand)
print(car1.model)
print(car1.full_name())



