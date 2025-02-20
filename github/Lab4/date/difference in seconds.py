from datetime import datetime

date1_str = "2023-03-01 22:45:30"
date2_str = "2023-03-05 14:45:30"

date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference: {difference_in_seconds}")