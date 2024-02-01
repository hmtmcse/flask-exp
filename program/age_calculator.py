# importing the date module from the datetime package
from datetime import date

# "30/01/2023"
# "23/03/1991"
# ------------
# 7 - 10 - 32

# defining a function calculate the age
def calculate_age(birthday):
    # using the today() to retrieve today's date and stored it in a variable
    today = date.today()
    today = date.today()

    # a bool representing if today's day, or month precedes the birth day, or month
    day_check = ((today.month, today.day) < (birthday.month, birthday.day))

    # calculating the difference between the current year and birth year
    year_diff = today.year - birthday.year

    # The difference in years is not enough.
    # We must subtract 0 or 1 based on if today precedes the
    # birthday's month/day from the year difference to get it correct.
    # we will subtract the 'day_check' boolean from 'year_diff'.
    # The boolean value will be converted from True to 1 and False to 0 under the hood.
    age_in_years = year_diff - day_check

    # calculating the remaining months
    remaining_months = abs(today.month - birthday.month)

    # calculating the remaining days
    remaining_days = abs(today.day - birthday.day)

    # printing the age for the users
    print("Age:", age_in_years, "Years", remaining_months, "Months and", remaining_days, "days")


def calculate_age2(birth_date, current_date):
    # Calculation
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def get_days_in_month(month, year):
    # Returns the number of days in a given month and year
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31


def calculate_my_age(day, month, year, today=None):
    date_of_birth = date(day=day, month=month, year=year)
    if not today:
        today = date.today()

    year = today.year - date_of_birth.year
    month = today.month - date_of_birth.month
    day = today.day - date_of_birth.day

    print(f"Raw Day: {day}, Month: {month}, Year: {year}")

    if day < 0:
        month -= 1
        day += 30

    if month < 0:
        year -= 1
        month += 12

    print(f"Age Day: {day}, Month: {month}, Year: {year}")


# main function
if __name__ == "__main__":
    calculate_my_age(31, 3, 2022, date(day=30, month=1, year=2024))
    calculate_my_age(26, 4, 2022, date(day=30, month=1, year=2024))
    print(calculate_age2(date(day=31, month=3, year=2022), date(day=30, month=1, year=2024)))
    print(calculate_age2(date(day=26, month=4, year=2022), date(day=30, month=1, year=2024)))
