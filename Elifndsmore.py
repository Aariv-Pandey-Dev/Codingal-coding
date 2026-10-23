print(" === SMART SCHOOL DAY PLANNER === ")
day = input("Enter the day of the week: ")
weather = input("Enter the weather: ")
homework = bool(input("Do you have homework? (True/False, if false just click enter"))
print(f"Day plan for {day}.")
if day in ("Saturday", "Sunday"):
    daytype = "Weekend"
    print("Enjoy your weekend")
elif day == "Monday":
    daytype = "First day of the week, "
    print(daytype)
elif day == "Friday":
    daytype = "Last day of the week, "
    print(daytype)
else:
    daytype = "Middle of the week, "
    print(daytype)
if weather == "Sunny" and homework == False:
    print("Go play football, great day for it and no homework.")
if weather == "rainy" or "sunny":
    print("Pack an umbrella, or you may get wet.")
if daytype == "Weekend" and homework == True:
    print("Finish your homework and get outside!")