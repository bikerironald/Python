# Magic Methods
# Magic methods are special methods in Python that start and end with double underscores (also known as dunder methods). They allow you to define specific behaviors for your objects in various contexts, such as arithmetic operations, comparisons, string representations, and more. Here are some common examples:

# __str__: Defines how an object is represented as a string.
# __repr__: Defines the official string representation of an object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)  # Output: Name: Alice, Age: 30

