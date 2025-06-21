# Deep Dive into Python Classes
# Constructors (__init__):

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Create a Point object
point = Point(3, 5)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (3, 5)