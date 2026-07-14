

grades = [
    ("Alice","Math,85"),
    ("Bob","Science",92),
    ("Alice","Science",92),
    ("Charlie","Math",90),
    ("Bob","Math,85"),
    ("Alice","English",95),
]


name2 = set()
subject2 = set()
for name, subject, grade in grades:
    name2.add(name)
    subject2.add(subject)
print("Unique students (method 2):", name2)
print("Unique subjects (method 2):", subjects2)


