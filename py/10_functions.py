
#Functions with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

#Functions with return values
def add_numbers(a, b):
    return a+ b 

result = add_number(5, 3)
print(result) # 8

# Default parameters
def gree_with_title(name, title = "Mr. "):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))  # "Hello, Mr.Smith!
print(greet_with_title("Johnson", "Dr ")) # "Hello, Dr. Johnson!" 







students = {
    "student_001": "John",
    "age": 19,
    "major": "Computer Science",
    "grade": ["85","92","78"],

}

print(f"Name is {student_001}:{students[student_001]}")

#2. Build a temperature converter (Celsius to Fehrenheit)
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32 
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#Test the functions
print(f"25C = {celsius_to_fahrenheit(25)}F")
print(f"25C = {fahrenheit_to_celsius(77)}F")