from datetime import date


def get_days_in_month(month, year):
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

    if day < 0:
        month -= 1
        day += get_days_in_month(month, year)

    if month < 0:
        year -= 1
        month += 12

    return year, month, day


if __name__ == "__main__":
    year, month, day = calculate_my_age(31, 3, 2022, date(day=30, month=1, year=2024))
    print(f"Age is: {year} years {month} month/s {day} day/s")
