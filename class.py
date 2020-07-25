"""The concept of class inside another class aka Inner class 
is tried"""

"""We first try creating an object inside the outer class"""
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() 
        #object of class Laptop() created by self.lap !!! Don't forget the self.Laptop()!!!

    class Laptop:
        def __init__(self):
            self.brand = 'Lenovo'
            self.ram = 8
        
        def get_laptop_config(self):
            print (self.brand, self.ram)

s1 = Student('KK', 2)
s2 = Student('AM', 3)

s1.lap.get_laptop_config()

"""We now try creating an object outside the outer class"""
class Students:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        

    class Laptops:
        def __init__(self):
            self.brand = 'Lenovo'
            self.ram = 8
        
        def get_laptop_config(self):
            print (self.brand, self.ram)

s1 = Students('KK', 2)
s2 = Students('AM', 3)

# We create an object of type Laptops() which is inside class Students
# Hence we have to access the laptop class through Students class as follows-

lappy1 = Students.Laptops()
lappy1.get_laptop_config()