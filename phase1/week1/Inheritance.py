# Base class: Shape
# - __init__(color)
# - area() → returns 0
# - __str__ → "Shape | Color: red | Area: 0"

# Child: Rectangle(Shape)
# - __init__(color, width, height)
# - uses super().__init__(color)
# - area() → width * height
# - __str__ → "Rectangle | Color: blue | Area: 20"

# Child: Circle(Shape)
# - __init__(color, radius)
# - uses super().__init__(color)
# - area() → 3.14159 * radius * radius
# - rounds area to 2 decimal places in __str__
# - __str__ → "Circle | Color: red | Area: 78.54"

# Test every class. Test __str__, area(), 
# and make sure super() is used correctly.

class Shape:
  def __init__(self, color):
    self.color = color
  
  def area(self):
    return 0
    
  def __str__(self):
    return f"Shape | Color {self.color} | Area: {self.area()}"

class Rectangle(Shape):
  def __init__(self, color, width, height):
    super().__init__(color)
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
  
  def __str__(self):
    return f"Rectangle | Color: {self.color} | Area: {self.area()}"

class Circle(Shape):
  def __init__(self,color,  radius):
    super().__init__(color)
    self.radius = radius
    
  def area(self):
    return 3.14159 * self.radius * self.radius
  
  def __str__(self):
    return f"Circle | Color: {self.color} | Area: {self.area()}"
  

s = Shape("pink")
print(s)
print(s.area())
  
r = Rectangle("blue", 5, 4)
print(r) 
print(r.area())

c = Circle("red", 2)
print(c)
print(c.area())
  
  
  
  
  
  
  
  
  
  
  
  
  
  