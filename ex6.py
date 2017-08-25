# number (integer) inside f-string
types_of_people = 10
# f-string
x = f"There are {types_of_people} types of people"

# string inside f-string
binary = "binary"
do_not = "don't"
# f-string
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# f-string inside f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# boolean inside f-string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# .format() function
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

# string concatenation
print(w + e)
print(w, e)
