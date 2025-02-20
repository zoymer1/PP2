from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Today:", current_date)
print("Five days ago:", five_days_ago)