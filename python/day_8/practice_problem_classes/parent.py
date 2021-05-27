class Parent():
    name = "parent_class"
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def print_info(self):
        print("%s %s is %d years old" %(self.f_name, self.l_name, self.age))

    def change_last_name(self, name):
        self.l_name = name
        print("last name changed")

parent_instance_1 = Parent("Saravana", "kumar", 22)
parent_instance_1.print_info()
parent_instance_1.change_last_name("Nagaraj")
parent_instance_1.print_info()
