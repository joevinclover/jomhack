

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}

print(student["name"])
print(student.get("age"))
student["age"] = 21
student["email"] = "alice@gmail.com"


keys =  student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)


for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")




