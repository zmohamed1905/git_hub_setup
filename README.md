# Python Intro


## Why Python:
- Python is a popular, in demand programming langauge.
- Easy to use for beginners
- Supported by large libraries


# Python use cases 
- Internet of things
- Game Development
- Artificial Intelligence
- Data Science


# Python Variables
- Variables help to store data values
- To store user data- hard code the data- any other type

# Here are some examples:
- first_name = "" - String
- last_name = ""
- DOB = 99- Int
- UK_resident= yes or no - Boolean
- salary = 40000 - Int
- travel = 15.4 - float
- gross_salary = salary + travel

# Below is an example of some code and variables in practice:

```python

first_name = "Zakariya"
last_name = "Mohamed"
salary = 50
travel = 3.5

#print("Zakariya")
print(first_name)
# display the value of var first_name
print(last_name)
print(salary)
print(travel)

#how to find out the type of data stored in the var
# type()
print(type(travel))
# interact with users by taking user data in - input

print("Good Morning, Please enter your name ")
name = input() # took user input and stored in the var called name
print("Hello dear")
print(name)

print("What is your first name?")
first_name = input()
print("What is your last name?")
last_name = input()
print("What is your DOB")
DOB = input()
print("What is your course name?")
course_name = input()
print("Are you a UK resident?")
UK_resident = input()
```
# Generating a new SSH key
Step 1. Open Bash terminal

Step 2. Open .ssh directory bu using this command
- cd ~/.ssh
- if it does not exist use mkdir ~/.ssh

Step 3. ssh-keygen -t rsa -b 4096 -C "your@email.com"
- Substitue the email with your GitHub email


# How to setup github using SSH key:
- Open GitBash
- enter $ ssh-keygen -t ed25519 -C "your_email@example.com"
-  This creates a new SSH key, using the provided email as a label.
> Generating public/private ALGORITHM key pair.

# Adding your SSH key to the ssh-agent
step 1: # start the ssh-agent in the background
$ eval "$(ssh-agent -s)" > Agent pid 59566

Step 2: $ ssh-add ~/.ssh/id_ed25519

Step 3: Replace id with your id_rsa

Checking Status:
- $ ssh -T git@github.com
- if you see : Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
- You have been successful



![image](https://user-images.githubusercontent.com/115154775/194919569-191530e1-6f4e-4ff7-8999-259b2c113dfa.png)


# Git & Github
add changes to our Github repo- the changes that we made on local host

- `git add filename` or `git add .`. means push everything from current location.
- `git commit -m "new markdown guide added"`
- now lets send this new data to Github
- `git push -u origin main`
- `git status`

# Git Cheat Sheet
```bash
These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```

# Intro to Data types & Operators
- `+ - * /`

# Comparison Operators
- `>` greater than
- `>` less than
- `==` True or False
- `>=` Greater than or equal to
- `<=` Less than or equal to


```python
a = 24
b = 16

print(a + b) # outcome added value of a & b
print(a - b) # outcome -a from b
# comparison
print(a > b) # True
print(a < b) # False
print(a == b)
```



# Using Built in Booleans:

```python
greeting = "Hello World!"
print(greeting)
print(greeting.isalpha()) # checks if it is in the alphabet
print(greeting.islower()) # checks if it is lower case
print(greeting.startswith("H")) # checks if it starts with a capital H
print(greeting.endswith("!")) # checks if it ends with specific letter/symbol
print(greeting.isdigit()) # checks if it is a digit

```

# String Slicing:
```python
greeting = "Hello World"
print(greeting)
# we have builtin method that checks the len of string
print(len(greeting))
print(greeting[-1])
print(greeting[0:5]) #prints 0-5
print(greeting[-6:]) # prints the remaining char
```




# String Methods are available:

```python

# use var= string "assddfffdgdfdf"
white_space = "lots of spaces at the end                "
print(len(white_space))
# strip() removes the white spaces
print(len(white_space.strip)) # this calculates the len and removes all white spaces at the end

Example_text = "here is some text with lot's of text"
print(Example_text.count("text")) # tells you how many times "text" is mentioned
print(Example_text.lower()) # allows you to convert everything into lower case
print(Example_text.upper()) # allows you to convert everything into upper case
print(Example_text.capitalize()) # allows you to convert the first char into a capital letter
print(Example_text.replace("with", ",")) # allows you to replace something (case_sensitive)

```
 
# Concatenation & Casting
- adding strings together
- casting/converting data types

```python
# user data input
first_name = "Shahrukh"
last_name = "Khan"
salary = 40
print(first_name)
print(last_name)
print(first_name + last_name)
print(first_name + " " + last_name + " " + str(salary))
# F-string
print(f" Hello {first_name} {last_name}") # Python 3.5/6 or above
```

# User Input Ask:
```python
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

```


# Data Collections

# Lists:
```python

# syntaxt ["sssss", "prpkrrkrk", "zmzmzmmz"]

shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
shopping_list.append("chicken")
print(shopping_list)
shopping_list[2] = "icecream"
print(shopping_list)
shopping_list.remove("fanta")
print(shopping_list)
#pop removes last item from list

#Lists allows multiple data types within the list
multiple_type = [1, 2, 3, "one", "five", "ten"]
print(multiple_type)
print(multiple_type[2])

```
# Tuples:
```python
# # Imutable - cant be changed - edited- added
# # user_details = DOB - country name - city name -
# syntax ("")
essentials = ("milk", "paracetamol", "drinks")
print(essentials)
# what is the diff between lists and tuples
essentials [0] = "coffee"
```


# Dictonaries:
```python
# # What is a Dictionary? - Data Collection Type
# # How to manage it - managing the data using dict
# # It works as a key value pair
# # Key value pair = value
# # Syntax {"Key" : "value"       }
# # store student's data - name, course_name, progress, completed_lessons
student_1 = {
    "key": "values",
    "name": "Zakariya",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["Lists", "tuples", "OOP"]
}
print(student_1)
print(type(student_1))
print(student_1["stream"]) #this will display the value saved inside stream
print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])

# Changing Data
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

#deleting item from list of completed_lessons_names
student_1["completed_lessons_names"].remove("OOP")
print(student_1["completed_lessons_names"])

# Dict Builtin Methods
# display keys only or values
# keys() values ()
print(student_1.keys())
print(student_1.values())

```

