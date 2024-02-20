#Write a Python program to subtract five days from current date.
#1
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(5)
print(current_date)
print(five_days_ago)

#Write a Python program to print yesterday, today, tomorrow.
#2
from datetime import datetime, timedelta
today = datetime.now()
tomorrow = today + timedelta(1)
yesterday = today - timedelta(1)

print(yesterday)
print(today)
print(tomorrow)

#Write a Python program to drop microseconds from datetime.
#3
from datetime import datetime, timedelta
today = datetime.now()
print(today)

#Write a Python program to calculate two date difference in seconds.
#4
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds
date_format = "%Y-%m-%d %H:%M:%S"
date1_str = "2023-02-06 12:12:15"
date2_str = "2024-02-20 15:15:15"

date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)
difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)


