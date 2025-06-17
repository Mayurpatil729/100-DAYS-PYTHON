## 🔄 **What is Overloading?**

# **Overloading** means using the **same function or operator** with **different behavior** based on the number/type of arguments.

# Python supports:

### ✅ 1. **Operator Overloading**

### ⚠️ 2. **Method Overloading** (limited / not built-in)


## ✅ 1. **Operator Overloading (Fully Supported)**

# Python allows you to **define how operators work for your custom objects** by using **magic methods** (`__add__`, `__mul__`, etc.).
### 🔧 Example: `+` Operator Overloading


class Car:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price

car1 = Car(500000)
car2 = Car(300000)

print(car1 + car2)  # Output: 800000


# ✅ `+` behaves differently for `Car` objects because we overloaded it with `__add__`.


## ⚠️ 2. **Method Overloading (Limited in Python)**

# In other languages, you can define multiple methods with the **same name but different parameters**.
# But in Python:

# **Only the last method definition will be used.**

### ❌ Won’t Work Like This:
class Demo:
    def show(self, a):
        print("1 argument")

    def show(self, a, b):
        print("2 arguments")

d = Demo()
d.show(10)  # ❌ Error: Missing 1 required argument

# Only the **last `show()`** is kept — the earlier one is **overwritten**.
### ✅ Workaround for Method Overloading: Use Default Arguments


class Demo:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print("Two arguments:", a, b)
        elif a is not None:
            print("One argument:", a)
        else:
            print("No arguments")

d = Demo()
d.show()           # No arguments
d.show(10)         # One argument
d.show(10, 20)     # Two arguments


# ✅ Works like overloading by using **optional/default parameters**.

## 🧠 Summary

# | Type                 | Supported in Python? | How?                                          |
# | -------------------- | -------------------- | --------------------------------------------- |
# | Operator Overloading | ✅ Yes                | Using magic methods like `__add__`, `__sub__` |
# | Method Overloading   | ❌ Not directly       | Use default arguments or `*args` workaround   |

