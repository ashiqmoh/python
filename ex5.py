my_name = "Ashiq Mohamed"
my_age = 27
my_height = 178
my_weight = 65
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg hevay.")
print(f"Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# to insert a variable into a string in print function, there is 3 ways:
#    - either concatenated through ','
#    - through string-f by using {}
#    - by using '+'
