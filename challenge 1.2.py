
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#This code defines a function `is_leap_year()` that takes a year as input and returns `True` if it's a leap year and `False` otherwise. It then takes user input for a year and checks if it's a leap year using this function.