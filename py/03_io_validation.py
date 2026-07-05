

name = str(input("Enter your name: "))
height = float(input("Enter your height: ")) 

#Input validation 
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age < 500:
            break
        else:
            print("Age must be postitve!")
    except ValueError:
        print("Please enter a valid number")


#Output validation 
print(f"Hello, {name}!")
print(f"Your are {age} years old and {height} feet tall.")

