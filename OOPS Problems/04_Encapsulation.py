# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

### Encapsulation 

class Car():
    def __init__(self,__brand,model):
        self.__brand=__brand   # 🔐 Private variable
        self.model=model
        
    def full_name(self):
        return f"{self.__brand} and {self.model}"
    
    def get_brand(self):       # ✅ Getter method
        return f"{self.__brand} !"

tesla=Car("Tesla","T-72")
# print(tesla.__brand)
print(tesla.get_brand())


# __brand -> Private variable (encapsulated)
# get_brand()-> Public method to access private data (getter)
# model	Public-> variable (can be accessed directly)
# self.__brand-> Encapsulation in action


# --------------------------------------------------

class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand      # private attribute
        self.model = model          # public attribute

    def full_name(self):
        return f"{self.__brand} and {self.model}"

    def get_brand(self):            # getter method
        return self.__brand

    def set_brand(self, new_brand): # setter method
        if isinstance(new_brand, str):   # basic validation
            self.__brand = new_brand
        else:
            print("Invalid brand name")

# Creating object
tesla = Car("Tesla", "T-72")

# Accessing private variable through getter
print("Before update:", tesla.get_brand())   # Output: Tesla

# Updating private variable through setter
tesla.set_brand("Tata")

# Checking the updated value
print("After update:", tesla.get_brand())    # Output: Tata

# Full name after update
print("Full name:", tesla.full_name())       # Output: Tata and T-72
