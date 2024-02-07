# define functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    return x // y

# print menu
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Floor Division")

# take input from the user
 choice = input("Enter choice(1/2/3/4/5/6): ")
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

# get user's choice
while True:
    
    if choice in ('1', '2', '3', '4', '5', '6'):
        # perform the selected operation
        if choice == '1':
            print(f"{x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"{x} - {y} = {subtract(x, y)}")
        elif choice == '3':
            print(f"{x} * {y} = {multiply(x, y)}")
        elif choice == '4':
            print(f"{x} / {y} = {divide(x, y)}")
        elif choice == '5':
            print(f"{x} % {y} = {modulus(x, y)}")
        elif choice == '6':
            print(f"{x} // {y} = {floor_division(x, y)}")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
