# Prompt the user to enter a number
num = int(input("Enter a Number: "))

# Check divisibility by 5, 7, 11, and 2
if num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 2 == 0:
    # Check divisibility by 5
    if num % 5 == 0:
        print("The number is divisible by 5")
    else:
        print("Not divisible by 5")

    # Check divisibility by 7
    if num % 7 == 0:
        print("The number is divisible by 7")
    else:
        print("Not divisible by 7")

    # Check divisibility by 11
    if num % 11 == 0:
        print("The number is divisible by 11")
    else:
        print("Not divisible by 11")

    # Check divisibility by 2
    if num % 2 == 0:
        print("The number is divisible by 2")
    else:
        print("Not divisible by 2")
else:
    print("Not divisible by either 5, 7, 11, or 2")
