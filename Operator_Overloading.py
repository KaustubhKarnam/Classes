class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __repr__(self):
        return f"Result 1 = {self.m1}, Result 2 = {self.m2}"
    
    def __add__(self, other):
        return Student(self.m1+other.m1, self.m2+other.m2)

s1 = Student(60, 70)
s2 = Student(50, 70)

s3 = s1 + s2
print(s3)

