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