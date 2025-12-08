#вариант 1
import math

class figura():
  
  def area(self):
    pass
  
  def perimeter(self):
    pass
  
  def vertices(self):
    pass
  
class triangle(figura):
  
  def __init__(self, x1, y1, x2, y2, x3, y3):
    self.points = [(x1, y1), (x2, y2), (x3, y3)]
    
  def _distance(self, p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
  
  def area(self):
    x1, y1 = self.points[0]
    x2, y2 = self.points[1]
    x3, y3 = self.points[2]
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
  
  def perimeter(self):
    d = self._distance
    p = d(self.points[0], self.points[1]) + d(self.points[1], self.points[2]) + d(self.points[2], self.points[0])
    return p
    
  def vertices(self):
    return 3
    
class rectangle(figura):
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    
    def area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)
    
    def perimeter(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))
    
    def vertices(self):
        return 4

class circle(figura):
    def __init__(self, cx, cy, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def vertices(self):
        return 0

def parse_shape(line):
    parts = line.strip().split()
    if not parts:
        raise ValueError("Пустой ввод")
    shape_type = parts[0].lower()
    try:
        if shape_type == "triangle" and len(parts) == 7:
            coords = list(map(float, parts[1:7]))
            return triangle(*coords)
        elif shape_type == "rectangle" and len(parts) == 5:
            coords = list(map(float, parts[1:5]))
            return rectangle(*coords)
        elif shape_type == "circle" and len(parts) == 4:
            cx, cy, r = map(float, parts[1:4])
            if r <= 0:
                raise ValueError("Радиус должен быть положительным")
            return circle(cx, cy, r)
        else:
            raise ValueError("Неизвестная фигура или неверные параметры")
    except ValueError as e:
        raise ValueError(f"Неверные параметры для {shape_type}: {e}")


shapes = []
print("Введите фигуры:")
while True:
  line = input()
  if not line.strip():
      break
  try:
      shape = parse_shape(line)
      shapes.append(shape)
  except Exception as e:
      print("Error:", e)
    
if not shapes:
  print("Нет введенных фигур.")
  
print("Введите команду:")
cmd = input().strip().lower()
  
if cmd == "area":
    total = sum(s.area() for s in shapes)
    print(f"Total area: {total:.2f}")
elif cmd == "perimeter":
    total = sum(s.perimeter() for s in shapes)
    print(f"Total perimeter: {total:.2f}")
elif cmd == "vertices":
    total = sum(s.vertices() for s in shapes)
    print(f"Total vertices: {total}")
else:
    print("Неизвестная команда.")
