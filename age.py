# defining function to calculate the current age
def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    return age

# prompting the user to enter the date of birth
year_of_birth = int(input("Enter the year of birth: "))

# setting the current year as a constant
current_year = 2024

# subtracting the current age and the year of birth
age = calculate_age(year_of_birth, current_year)

# The output to be displayed after getting the current age
print(f"You are {age} years old.")

# prompting the user to enter their height in meters
height = float(input("Kindly enter your height in meters: "))

# determining the data type of each input and displaying it
print(f"Year of birth: {type(year_of_birth)}")
print(f"Current year: {type(current_year)}")
print(f"Age: {type(age)}")
print(f"Height: {type(height)}")

# determining the size of each input and displaying it
print(f"Year of birth: {len(str(year_of_birth))} characters")
print(f"Current year: {len(str(current_year))} characters")
print(f"Age: {len(str(age))} characters")
print(f"Height: {len(str(height))} characters")
