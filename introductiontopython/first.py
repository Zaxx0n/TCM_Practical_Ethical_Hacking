#!/bin/python3

# print string
print("Hello, world!")
print("""This string runs
multiple lines""") # triple quote for multiple lines
print("This string is "+"awesome!"), # we can also concatenate
print('\n') # new line
print("Test that new line out")


# Maths
print(50 + 50) # add
print(50 - 50) # subtract
print(50 * 50) # multiply
print(50 / 50) # divide
print(50 + 50 - 50 * 50 / 50) # PEMDAS
print(50 ** 2) # exponents
print(50 % 6) # modulo - takes what is left over
print(50 / 6) # division with remainder (or a float)
print(50 // 6) # no remainder

print('\n')
# Variables and Methods
quote = "All is fair in love and war."
print(quote)

print(quote.upper()) # uppercase
print(quote.lower()) # lowercase
print(quote.title()) # titlecase
print(len(quote)) # count characters

name = "Zak" # string
age = 43 # int
gpa = 4.20 # float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) # won't round

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

#Functions

def who_am_i(): # this is a function without parameters
	name = "Zak" # local variable
	age = 43
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y
	
multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl(): # new line
	print('\n')
	
nl()

# Boolean Expression (True or False)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
# Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7 
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) # False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True

test_not = not True # False

nl()
# Conditional Statements - if/then/else/etc

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()

# Lists - Have Brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) # returns the second item in the list
print(movies[0]) # returns the first item in the list
print(movies[1:3]) # returns the first index number given right until the last number, but not include the last number
print(movies[1:]) # prints everything from the second item in the list till the end
print(movies[:1]) # prints everything till the second item in the list, but not the sedond item
print(movies[-1]) # prints the last item in the list

print(len(movies)) # counts the items in the list
movies.append("Jaws") # appends to the end of the list

movies.insert(2, "Hustle")
print(movies)

movies.pop() # removes the last item
movies.pop(0) # removes the first item

amber_movies = ["Just Go with It", "50 First Dates"]
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

# 2D Lists
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)
alices_grade = grades[1][1]
print(alices_grade)
nl()
# Tuples - do not change, () not mutable
grades = ("a", "b", "c", "f")

print(grades[1])
nl()

# Looping

# For Loop - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	

# While Loop - execute as long as True
i = 1

while i < 10:
	print(i)
	i += 1
	
nl()

# Advanced Strings

my_name = "Zak"
print(my_name[0]) # first letter
print(my_name[-1]) # last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) # delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)

quote2 = "He said, \"give me all your money\""
print(quote2)

too_much_space = "                                hello     "
print(too_much_space.strip())

print("A" in "Apple") # True
print("a" in "Apple") # False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) # impoved 

movie = "The Hangover"
print("My favortie movie is %s." % movie)
print(f"My favorite movie is {movie}.")
print("My favorite movie is {}.".format(movie))


nl()
# Dictionaries - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8}
# drink is the key, price is the value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees["Legal"] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)
drinks["White Russian"] = 8
print(drinks)

print(drinks.get("White Russian"))
