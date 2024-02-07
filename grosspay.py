#defing the function to calculate the gross_pay
def calculate_gross_pay (hours_worked,rate_per_hour):
    # Calculate the gross pay by multiplying the hours worked by the rate per hour
    gross_pay=hours_worked*rate_per_hour
    return gross_pay
# Prompt the user to enter the number of hours worked and the hourly rate
hours_worked=int(input("Enter hours:"))
rate_per_hour=float(input("Entter rate:"))
# Calculate  the gross pay
print(f"The gross pay is:{ calculate_gross_pay(hours_worked,rate_per_hour)}")
