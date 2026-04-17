# 🐍 Complete Object-Oriented Programming in Python (A to Z)

**A structured guide to mastering OOP, from foundational blueprints to advanced memory management and design patterns.**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/LunarLumos)

---

## 📖 The Four Pillars of OOP
Before diving into the code, remember the core principles:
1. **Encapsulation:** Bundling data and methods that work on that data within a single unit (Class).
2. **Inheritance:** Enabling a new class to take on the properties and methods of an existing class.
3. **Polymorphism:** Allowing different classes to be treated as instances of the same general class through the same interface.
4. **Abstraction:** Hiding complex implementation details and showing only the necessary features of an object.

---

## 📂 Curriculum & Roadmap

| ID | Topic | Theoretical Concept | Code |
| :--- | :--- | :--- | :---: |
| 1 | **Class & Object Creation** | A **Class** is a blueprint; an **Object** is a concrete instance of that blueprint. | [ [01] ](./1.py) |
| 2 | **Instance Methods** | Functions defined inside a class that can access and modify the object's state via `self`. | [ [02] ](./2.py) |
| 3 | **Class Attribute** | Variables defined at the class level; they are shared by all instances, saving memory. | [ [03] ](./3.py) |
| 4 | **Class Method** | Methods bound to the class, not the object. Used to factory-create objects or modify class state via `cls`. | [ [04] ](./4.py) |
| 5 | **Static Method** | Utility functions that belong to the class namespace but do not require access to `self` or `cls`. | [ [05] ](./5.py) |
| 6 | **Property Getter & Setter** | Encapsulation technique to protect attributes while allowing them to be accessed like variables. | [ [06] ](./6.py) |
| 7 | **Private Attributes** | Using `__` (double underscore) triggers **Name Mangling** to prevent direct external access. | [ [07] ](./7.py) |
| 8 | **Inheritance** | Promoting code reusability by allowing a child class to derive attributes/methods from a parent. | [ [08] ](./8.py) |
| 9 | **Multiple Inheritance** | A class inheriting from more than one parent. Managed via **MRO** (Method Resolution Order). | [ [09] ](./9.py) |
| 10 | **Method Overriding** | Providing a specific implementation of a method that is already provided by its parent class. | [ [10] ](./10.py) |
| 11 | **`super()` Usage** | A proxy object that allows you to call methods of the parent class (especially useful in `__init__`). | [ [11] ](./11.py) |
| 12 | **Magic Methods** | Special "Dunder" methods (like `__str__`) that allow custom objects to interact with Python's built-in functions. | [ [12] ](./12.py) |
| 13 | **Operator Overloading** | Customizing how objects respond to mathematical operators (`+`, `-`, `*`, etc.) via magic methods. | [ [13] ](./13.py) |
| 14 | **Abstract Base Class** | A blueprint for other classes. It cannot be instantiated and forces subclasses to implement specific methods. | [ [14] ](./14.py) |
| 15 | **Composition** | Building complex objects by combining simpler ones ("Has-a" relationship) rather than inheriting ("Is-a"). | [ [15] ](./15.py) |
| 16 | **Polymorphism** | The ability of different objects to respond to the same method call in their own specific way. | [ [16] ](./16.py) |
| 17 | **Encapsulation Example** | A practical look at hiding internal state and requiring all interaction to go through public methods. | [ [17] ](./17.py) |
| 18 | **Property Deleter** | Using `@name.deleter` to perform clean-up actions when an attribute is deleted via `del`. | [ [18] ](./18.py) |
| 19 | **`@dataclass`** | A decorator that automatically generates `__init__`, `__repr__`, and `__eq__` for data-heavy classes. | [ [19] ](./19.py) |
| 20 | **Singleton Pattern** | A design pattern that restricts the instantiation of a class to one single "global" instance. | [ [20] ](./20.py) |
| 21 | **Factory Method** | A creational pattern that uses a method to handle object creation without specifying exact classes. | [ [21] ](./21.py) |
| 22 | **Method Chaining** | Returning `self` at the end of a method to allow multiple methods to be called in a single line. | [ [22] ](./22.py) |
| 23 | **`__slots__`** | Explicitly declaring allowed attributes to prevent the creation of `__dict__`, significantly reducing memory usage. | [ [23] ](./23.py) |
| 24 | **Custom Exceptions** | Creating user-defined error types by inheriting from the built-in `Exception` class. | [ [24] ](./24.py) |
| 25 | **Descriptor** | A low-level mechanism for managing attribute access, used internally by properties and methods. | [ [25] ](./25.py) |
| 26 | **Context Manager** | Implementing `__enter__` and `__exit__` to manage resources (like files) safely using the `with` statement. | [ [26] ](./26.py) |
| 27 | **Callable Objects** | Allowing an instance of a class to be called like a function by implementing the `__call__` method. | [ [27] ](./27.py) |

---

## How to Run
Each file is designed to be self-contained. To explore a concept:
1. Open your terminal.
2. Run: `python <filename>.py` (e.g., `python 12.py`)

---
*Maintained by [LunarLumos](https://github.com/LunarLumos) 🌙*
