from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

# Current Date time
current_date = date.today()
print(current_date)
print(current_date + timedelta(days=30 * 5))
print(current_date + relativedelta(months=5))
print(date(2024, 6, 1) + relativedelta(months=5))
