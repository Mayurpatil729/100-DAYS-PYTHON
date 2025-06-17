
## 🧠 **4 Main Types of Methods in Python Classes**

| Method Type             | What It Works On                                  | Uses `self` or `cls`? | Decorator       |
| ----------------------- | ------------------------------------------------- | --------------------- | --------------- |
| **Instance Method**     | Works on object (instance)                        | ✅ `self`              | None            |
| **Class Method**        | Works on class (not object)                       | ✅ `cls`               | `@classmethod`  |
| **Static Method**       | Works independently (utility)                     | ❌ No `self` or `cls`  | `@staticmethod` |
| **Magic/Dunder Method** | Built-in special behavior (`__init__`, `__str__`) | Varies                | Special syntax  |

---

## 1️⃣ **Instance Methods**

### ➤ Definition:

* Most common method
* Access or modify **instance variables**
* Requires `self` (the object itself)

### ✅ Example:

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):  # instance method
        return self.brand

c = Car("Tata")
print(c.show_brand())  # Output: Tata
```

---

## 2️⃣ **Class Methods**

### ➤ Definition:

* Works on the **class itself**, not on object
* Used to access or change **class variables**
* Use `@classmethod` decorator and `cls` parameter

### ✅ Example:

```python
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total(cls):  # class method
        return cls.total_cars

Car()
Car()
print(Car.show_total())  # Output: 2
```

---

## 3️⃣ **Static Methods**

### ➤ Definition:

* Doesn’t use `self` or `cls`
* Used for utility tasks related to class
* Use `@staticmethod` decorator

### ✅ Example:

```python
class Car:
    @staticmethod
    def general_info():
        return "Cars are a means of transport."

print(Car.general_info())  # Output: Cars are a means of transport.
```

---

## 4️⃣ **Magic Methods (a.k.a Dunder Methods)**

### ➤ Definition:

* Start and end with `__double_underscores__`
* Control **object behavior** like printing, adding, comparing
* Examples: `__init__()`, `__str__()`, `__len__()`, `__eq__()`, etc.

### ✅ Example:

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):  # Magic method for print()
        return f"Car brand: {self.brand}"

c = Car("Tesla")
print(c)  # Output: Car brand: Tesla
```

---

## 🧠 Summary Table

| Method Type     | Keyword Used      | Works On       | Use Case                                 |
| --------------- | ----------------- | -------------- | ---------------------------------------- |
| Instance Method | `def` with `self` | Object         | Access/modify object’s data              |
| Class Method    | `@classmethod`    | Class (`cls`)  | Access/modify class variables            |
| Static Method   | `@staticmethod`   | None           | Utility/helper functions                 |
| Magic Method    | `__method__`      | Special syntax | Controls object behavior (e.g., `print`) |
