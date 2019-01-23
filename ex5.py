name = "Laurence M. Schmalzl"
age = 25
height = 175.0 #cm
height_inch = height * 0.39
weight = 70.0 #kg
weight_lbs = weight * 2.2
eyes = "Brown"
teeth = 'White'
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {height_inch} inches tall.")
print(f"He's {weight} kg heavy.")
print(f"He's {weight_lbs} lbs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I'd add {age}, {height}, and {weight} I get {total}.")
