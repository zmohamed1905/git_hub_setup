# # lets see the operators in action
# - `>` greater than
# - `>` less than
# - `==` True or False
# - `>=` Greater than or equal to
# - `<=` Less than or equal to

# a = 24
# b = 16
#
# print(a + b) # outcome added value of a & b
# print(a - b) # outcome -a from b
# # comparison
# print(a > b) # True
# print(a < b) # False
# print(a == b)
#
# # % operator
# # This operator is called modulo
# # This operator is used to give the remainder of dividing the two operands.
#
# # Boolean Builtin methods in Python- Boolean Methods
#
# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha()) # checks if it is in the alphabet
# print(greeting.islower()) # checks if it is lower case
# print(greeting.startswith("H")) # checks if it starts with a capital H
# print(greeting.endswith("!")) # checks if it ends with specific letter/symbol
# print(greeting.isdigit()) # checks if it is a digit


# String Slicing
# string indexing - starts from 0
# Hello World!
# 01234567891011
#          -2 -1

# greeting = "Hello World"
# print(greeting)
# # we have builtin method that checks the len of string
# print(len(greeting))
# print(greeting[-1])
#
#String Methods are availabble

# # use var= string "assddfffdgdfdf"
# white_space = "lots of spaces at the end                "
# print(len(white_space))
# # strip() removes the white spaces
# print(len(white_space.strip)) # this calculates the len and removes all white spaces at the end
#
# Example_text = "here is some text with lot's of text"
# print(Example_text.count("text")) # tells you how many times "text" is mentioned
# print(Example_text.lower()) # allows you to convert everything into lower case
# print(Example_text.upper()) # allows you to convert everything into upper case
# print(Example_text.capitalize()) # allows you to convert the first char into a capital letter
# print(Example_text.replace("with", ",")) # allows you to replace something (case_sensitive)


# # user data input
# first_name = "Shahrukh"
# last_name = "Khan"
# salary = 40
# print(first_name)
# print(last_name)
# print(first_name + last_name)
# print(first_name + " " + last_name + " " + str(salary))
# # F-string
# print(f" Hello {first_name} {last_name}") # Python 3.5/6 or above

print("Good Morning, Please enter your First Name")
first_name = input()

print("Enter Last Name")
last_name = input()

print("Enter DOB")
DOB = input()

print("Are you a UK resident? Yes or No")
uk_resdient= input()

print("What is your house number?")
house_number = input()

print("Please state one hobby of yours")
user_hobbies = input()


print(f"Hello {first_name} {last_name} {DOB} {uk_resdient} {house_number} {user_hobbies}")
