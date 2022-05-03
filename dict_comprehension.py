days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
weekly_temp = {day: temp for (day, temp) in zip(days, temp_C)}

print(weekly_temp)