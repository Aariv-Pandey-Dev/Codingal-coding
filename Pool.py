age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ")
adult_here = input("Is an adult with you? (yes / no): ")
if age < 4:
    group = "Toddler"
elif age < 12:
    group = "Child"
elif age < 18:
    group = "Teen"
else:
    group = "Adult"
print("Age group:", group)
if can_swim != "yes" and can_swim != "no":
    print("Input error: swimming answer must be yes or no")
    swim_ok = False
else:
    swim_ok = True
if adult_here != "yes" and adult_here != "no":
    print("Input error: adult answer must be yes or no")
    adult_ok = False
else:
    adult_ok = True
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool: allowed")
else:
    print("Deep pool: not allowed")
if age < 12 or can_swim == "no":
    print("Warning: stay in the shallow end")
if adult_ok and not adult_here == "yes":
    print("Reminder: no adult is present, ask a lifeguard for help")
if not swim_ok or not adult_ok:
    print("Cannot decide: please answer yes or no")
elif age < 4 and adult_here == "no":
    print("Not allowed: toddlers must be with an adult")
elif age < 4:
    print("Splash pool only")
elif age < 12 and adult_here == "no":
    print("Not allowed: children under 12 need an adult")
elif age < 12:
    print("Main pool with an adult")
elif age < 18 and can_swim == "yes":
    print("Main pool, alone")
elif age < 18:
    print("Not allowed alone: you must be able to swim")
else:
    print("All pools open to you")
print("")
print("Have a nice swim!")