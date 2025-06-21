# # Class Inheritance and Composition
# Inheritance

# Inheritance allows you to create new classes (subclasses) that inherit properties and behaviors from existing classes (parent classes). Think of inheritance as a parent-child relationship. The child inherits characteristics and behaviors from its parent. This promotes code re-usability and facilitates the creation of class hierarchies.
class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)  # Call parent class constructor
    self.breed = breed

  def make_sound(self):
    print("Woof!")

dog = Dog("Buddy", "Labrador")
dog.make_sound()  # Output: Woof!


# Composition as an Alternative

# Composition is another technique for code reuse that involves creating objects of one class within another class. This allows you to combine functionalities from different classes without directly inheriting from them.

class Car:
  def __init__(self, engine):
    self.engine = engine  # Engine object as an attribute

  def start(self):
    self.engine.start()

class Engine:
  def start(self):
    print("Engine starting...")

car = Car(Engine())
car.start()  # Output: Engine starting...

#  practice
# Constructors and Destructors Instructions
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name}, age {self.age}, has been created.")

    def __del__(self):
        print(f"Goodbye, {self.name}!")

# Example usage:
person1 = Person("Alice", 30)
del person1  # This will trigger the destructor and print the farewell message