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
