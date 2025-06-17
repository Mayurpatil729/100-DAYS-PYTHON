

## 🔁 **Method Overloading**

### 📘 **Definition:**

> **Method overloading** means defining **multiple methods with the same name but different parameters** (number or type) **within the same class**.

### ⚠️ **Note in Python:**

Python **does not support true method overloading** like Java or C++. Only the **last method** with the same name is used. However, overloading can be **simulated** using:

* Default arguments
* `*args` and `**kwargs`

### 🧩 **Types of Overloading (Conceptual in Python):**

1. **Function Overloading** – Same function name, different number of arguments.
2. **Operator Overloading** – Using special methods (`__add__`, `__sub__`, etc.) to define custom behavior for built-in operators like `+`, `-`, etc.

---

## 🔄 **Method Overriding**

### 📘 **Definition:**

> **Method overriding** means **redefining a method in a child class** that already exists in the parent class, **with the same name, same parameters**, to provide a different or extended behavior.

It is used to achieve **polymorphism** in object-oriented programming.

### 🧩 **Types of Overriding:**

1. **Simple Overriding** – Child class **completely replaces** the parent method.
2. **Extended Overriding** – Child class **enhances** the parent method by calling it using `super()` and then adding extra logic.

---

## 🧠 Key Difference Table

| Feature        | Overloading                            | Overriding                      |
| -------------- | -------------------------------------- | ------------------------------- |
| Definition     | Same method name, different parameters | Same method name and parameters |
| Class Scope    | Same class                             | Parent and child class          |
| Python Support | Partial (simulated)                    | Fully supported                 |
| Common Use     | Convenience, flexibility               | Polymorphism, custom behavior   |
| Types          | Function, Operator                     | Simple, Extended                |

---

### 🔄 **Method Overloading** (📚 Simple Definition):

> Defining **multiple methods with the same name** but with **different number or types of arguments** in the **same class**.

🟡 *Note:* Python does **not support it directly**, but it can be done using default arguments or `*args`.

---

### 🔁 **Method Overriding** (📚 Simple Definition):

> Defining a **method in a child class** that has the **same name and parameters** as a method in the **parent class**, to **change or extend its behavior**.

---
