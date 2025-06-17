
## 🔄 **Method Overriding – 2 Conceptual Types**

# | Type                        | Description                                           | Example                                 |
# | --------------------------- | ----------------------------------------------------- | --------------------------------------- |
# | 1️⃣ **Simple Overriding**   | Child class **completely replaces** the parent method | No use of `super()`                     |
# | 2️⃣ **Extended Overriding** | Child class **extends or enhances** parent method     | Uses `super()` to call parent’s version |

# ---

## ✅ 1. **Simple Overriding**

# Child class defines a method with the **same name** as the parent and **completely replaces** its behavior.


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Simple override
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks



## ✅ 2. **Extended Overriding (With `super()`)**

# Child class **adds extra logic** but still wants to use the parent method using `super()`.


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Extended override
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()


# 🧾 **Output:**
# Animal speaks
# Dog barks


# So you’ve extended the functionality — not fully replaced it.

# ---

## 🧠 Summary

# | Type                | Uses `super()`? | Purpose                           |
# | ------------------- | --------------- | --------------------------------- |
# | Simple Overriding   | ❌ No            | Completely replaces parent method |
# | Extended Overriding | ✅ Yes           | Uses parent method + adds more    |

