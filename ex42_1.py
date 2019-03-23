class Animal(object):
#   color_dict = {"1":"black", "2":"red", "3":"white", "4":"grey", "5":"tri-color"}
#    def __init__(self, color_choice):
    pass

class Dog(Animal):
    def __init__(self, name):
       self.name = name

class Cat(Animal):
    color_dict = {"1":"black", "2":"red", "3":"white", "4":"grey", "5":"tri-color"}
    def __init__(self, name, color_choice):
        self.name = name
#        self.color_dict = color_dict
        self.color_choice = color_choice
    def print_color(self):
        print(self.color_dict[self.color_choice])
    def print_name(self):
        print(self.name)

class Hybrid(Cat, Dog):
    pass

#name and color of cat can be choosen by the user
print("Please enter the cats name:")
cat_name = input("> ")
spc_cat = str(cat_name)
print("Choose color from the following list:", Cat("test", 0).color_dict)
#input for dict
cat_color = input("> ")
spc_cat = Cat(cat_name, cat_color)
print("Name is:")
spc_cat.print_name()
print("Color is:")
spc_cat.print_color()

hybrid = Hybrid("test", "3")
hybrid.print_name()
hybrid.print_color()
