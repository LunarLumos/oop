
---

### **Abstraction (OOP)**

**1. What is abstraction in object-oriented programming, and why is it useful?**
**Answer:**
Abstraction in Python (and OOP in general) means hiding internal implementation details and showing only the necessary functionality to the user.
**Why it is useful:** It helps to reduce complexity, improve code readability, and enforce a clean interface between components.

---

**2. How do abstract classes differ from interfaces in Python?**
**Answer:**
Python does not have "interfaces" like Java but uses **abstract base classes (ABCs)** from the `abc` module to achieve similar functionality.

| Feature     | Abstract Class                                   | Interface-like (via ABCs)                |
| ----------- | ------------------------------------------------ | ---------------------------------------- |
| Methods     | Can have both abstract and concrete methods      | Can be used to enforce method signatures |
| Inheritance | Can be inherited to implement abstract methods   | Achieves interface-like behavior         |
| Use         | Use `@abstractmethod` to define required methods | No separate "interface" keyword          |

**Example:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")
```

---

### **Threads (Multithreading)**

**3. What is a thread in Python, and how is it different from a process?**
**Answer:**
A **thread** is a smaller unit of a process that can run concurrently with other threads within the same process.

| Thread                           | Process                                 |
| -------------------------------- | --------------------------------------- |
| Lightweight                      | Heavyweight                             |
| Share memory                     | Have separate memory                    |
| Created using `threading.Thread` | Created using `multiprocessing.Process` |

---

**4. Explain the two ways to create a thread in Python.**
**Answer:**

1. **Using a function:**

```python
import threading

def print_msg():
    print("Thread running")

t = threading.Thread(target=print_msg)
t.start()
```

2. **Using a class:**

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread running")

t = MyThread()
t.start()
```

---

### **Exceptions (Error Handling)**

**5. What is an exception in Python? Explain the difference between checked and unchecked exceptions.**
**Answer:**
An **exception** is an error that occurs during program execution.

* **Python does not have checked exceptions** like Java.
* All exceptions in Python are **unchecked**—they are handled at runtime.

Example:

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

---

**6. What is the purpose of the try-except-finally block? What is the `raise` keyword, and how does it differ from `throws` in Java?**
**Answer:**

* `try-except-finally` in Python is used to handle exceptions:

  * `try`: Code that might throw an exception.
  * `except`: Code that handles exceptions.
  * `finally`: Code that always runs (cleanup code).

**Example:**

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid integer")
finally:
    print("Done")
```

* `raise` in Python is like `throw` in Java: it is used to manually throw exceptions.

```python
raise ValueError("Custom error message")
```

* Python **does not use `throws`** like Java. Exceptions are not declared in method definitions.

---

