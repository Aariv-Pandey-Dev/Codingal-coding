membername = input("Enter your name: ")
clubname = input("Enter your club name: ")

member_number = 8
points = 9.5
is_active = True
print("Member Number", member_number, "Datatype", type(member_number))
print("Points", points, "Datatype", type(points))
print("Active", is_active, "Datatype", type(is_active))

badge_code = membername[:3] + clubname[-1] + str(member_number)
print(badge_code)

print("===== CLUB BADGE =====")
print("Member: " + membername)
print("Club: " + clubname)
print("Code: " + badge_code)
print("Points: " + str(points) + " | Active: " + str(is_active))