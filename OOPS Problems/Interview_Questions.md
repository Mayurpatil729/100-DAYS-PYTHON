Great choice, Mayur! These are core OOPs concepts in Python that are commonly asked in interviews. Here's a clean and concise set of **answers** to help you **revise and explain confidently**.

---

## 📘 **OOPs in Python – Interview Questions with Answers**

---

### **1. What is the difference between a class and an object?**

* **Class** is a **blueprint** or **template** for creating objects. It defines properties (variables) and behaviors (methods).
* **Object** is an **instance** of a class. It holds real values and uses the class structure.

🧠 *Example:*

```python
class Car:  # Class
    pass

my_car = Car()  # Object
```

---

### **2. What is `self` in Python?**

* `self` refers to the **current instance** of the class.
* It is used to **access instance variables and methods** inside a class.
* It must be the **first parameter** in instance methods (but passed automatically by Python).

---

### **3. Explain `__init__` method (constructor).**

* `__init__()` is a **special method** called when an object is created.
* It is used to **initialize object variables** (e.g., name, age, brand).

🧠 *Example:*

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
```

---

### **4. What is inheritance? Explain multiple inheritance.**

* **Inheritance** allows a class (child) to **reuse code** from another class (parent).
* The child gets access to parent’s attributes and methods.

🧠 *Types:*

* **Single Inheritance:** One parent, one child
* **Multiple Inheritance:** One child inherits from **more than one parent**

🧠 *Example:*

```python
class Battery:
    pass

class Engine:
    pass

class ElectricCar(Battery, Engine):  # Multiple inheritance
    pass
```

---

### **5. What is the difference between instance, class, and static methods?**

| Method Type     | Decorator       | First Argument | Usage                          |
| --------------- | --------------- | -------------- | ------------------------------ |
| Instance Method | *(none)*        | `self`         | Access/modify object variables |
| Class Method    | `@classmethod`  | `cls`          | Access/modify class variables  |
| Static Method   | `@staticmethod` | None           | Utility function, independent  |

---

### **6. What is encapsulation and abstraction?**

* **Encapsulation:** Hiding internal data and protecting it using methods (e.g., private variables).
* **Abstraction:** Hiding **complex implementation** and showing only **important features** to the user.

🧠 *Example of encapsulation:*

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        self.__balance += amount
```

---

### **7. What are magic methods (dunder methods) in Python?**

* Special methods with **double underscores** (dunder = "double underscore")
* Used to define **object behavior**, like:

  * `__init__()` → constructor
  * `__str__()` → string representation
  * `__add__()` → overloading +
  * `__len__()`, `__eq__()`, etc.

🧠 *Example:*

```python
class Car:
    def __str__(self):
        return "This is a car"
```

---

### **8. What is method overriding?**

* Method overriding occurs when a **child class defines a method** with the **same name as the parent class** method.
* The child’s version **replaces** the parent’s version when called by a child object.

🧠 *Example:*

```python
class Car:
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Car):
    def fuel_type(self):  # Overrides parent method
        return "Electric"

tesla=ElectricCar()
print(tesla.fuel_type())
```




