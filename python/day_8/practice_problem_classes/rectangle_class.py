class Rectangle():
    no_of_sides = 4
    def __init__(self, angle1, angle2, angle3, angle4):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.angle4 = angle4

    def check_angles(self):
        if self.angle4 + self.angle3 + self.angle2 + self.angle1 == 360:
            return True
        else:
            return False

rectangle_instance_1 = Rectangle(90, 30, 60, 90)
print(rectangle_instance_1.check_angles())

class Square(Rectangle):
    angle = 90
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
        self.angle4 = self.angle

 
    