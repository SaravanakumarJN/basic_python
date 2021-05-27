class Bike():
    condition = "new"
    def __init__(self, model, color, average):
        self.model = model
        self.color = color
        self.average = average

    def display_bike(self):
        print("This is a %s %s with %d average" %(self.color, self.model, self.average))
    
bike_instance_1 = Bike("CBR 250R", "Black", 30)
print(bike_instance_1.color)
bike_instance_1.display_bike()