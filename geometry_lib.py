import numpy as np
class Point:
    def __init__(self, p):
        self.p = np.array(p)
    
    def __repr__(self):
        return f"Point ({self.p})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return  Point(self.p + other.p)
    
    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Vector(self.p - other.p)

class Vector:
    def __init__(self, p):
        self.p = np.array(p)
    
    def __repr__(self):
        return f"Vector ({self.p})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return  Point(self.p + other.p)
        return  Vector(self.p + other.p)
    
    def __sub__(self, other):
        return Vector(self.p - other.p)
