import json

student = {
    "name": "Alice",
    "age": 21,
    "GPA": 3.8
}

student_json = json.dumps(student)
print(student_json)
