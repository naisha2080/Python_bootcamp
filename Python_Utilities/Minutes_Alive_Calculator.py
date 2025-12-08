"""
Created a python script that calculates approximately how many minutes old a person is, based on their age in years.

"""


def calculate_minutes(age_years):
    days_in_years = 365.25
    hours_in_day = 24
    minutes_in_hour = 60

    total_days = age * days_in_years
    total_hours = total_days * hours_in_day
    total_minutes = total_hours * minutes_in_hour

    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try:
        age = float(input("Enter your age: "))
        days, hours, minutes = calculate_minutes(age)

        print("You are approximately: ")
        print(f" -{days} days old")
        print(f" -{hours} hours old")
        print(f" -{minutes} minutes old\n")

        again = input("Would you like to try again? (y/n): ").strip().lower()

        if again != "y":
            print("Goodbye for now!")
            break
    
    except:
        print("Enter a valid number for age")

