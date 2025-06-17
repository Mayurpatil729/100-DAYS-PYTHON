
# Add a static method to the Car class that returns a general description Of a car.


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
    
    @staticmethod
    def general_description():
        return f"Cars are means of Transport"

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
print(tata1.general_description())
print(Car.general_description())

# 🧠 What is a @staticmethod?
# A method that doesn’t use self or cls
# It belongs to the class, not any specific object
# It's like a utility function related to the class


# -----------------------------------------------------------------------


## 🧠 What is a **Class Method**?

# > A **class method** is a method that is **bound to the class**, not the object.
# > It can access and modify **class variables**, but **not instance (object) variables**.


### ✅ Key Points:

# * Uses the **`@classmethod`** decorator
# * Takes **`cls`** as the first parameter (not `self`)
# * Can be called by **both class and object**
# * Often used for:

#   * Working with class-level data
#   * Creating alternative constructors

# ---

## 🔧 Example Code:


class Car:
    total_cars = 0  # 👈 Class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"

### 🛠️ Using the class method:


car1 = Car("TATA", "Nexon")
car2 = Car("Tesla", "Model 3")

# Call using class
print(Car.get_total_cars())   # ✅ Output: Total cars created: 2

# Call using object
print(car1.get_total_cars())  # ✅ Output: Total cars created: 2


# ---

# ### 🔍 What’s Happening?

# | Method Type    | First Parameter | Works On           | Accesses                          |
# | -------------- | --------------- | ------------------ | --------------------------------- |
# | `@classmethod` | `cls`           | Class (not object) | Class variables like `total_cars` |

# ---

## 🧪 Bonus: Class Method as Alternative Constructor


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, info):
        name, age = info.split('-')
        return cls(name, int(age))

# Create using class method
s1 = Student.from_string("Mayur-22")
print(s1.name, s1.age)  # Output: Mayur 22




# ## ✅ Summary

# | Feature        | Class Method                             |
# | -------------- | ---------------------------------------- |
# | Decorator      | `@classmethod`                           |
# | First Argument | `cls` (represents class)                 |
# | Can Access     | Class variables                          |
# | Common Use     | Track class data, alternate constructors |
# | Called by      | Class name or object                     |

# ---





















