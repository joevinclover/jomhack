
#Basic exceptions handling 
try: 
    number = int(input("Enter a number: "))
    result = 10 / number 
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
