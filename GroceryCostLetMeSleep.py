rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members
print("Cost per person:", cost_per_person)
total_items = int(input("Enter the total number of grocery items:"))
people = int(input("Enter the number of people sharing them (1 or more): "))
left_over = total_items % people
if left_over == 0:
    print(total_items, "items divide equally among", people, "people.")
else:
    print(total_items, "items do not divide equally among", people, "people -", left_over, "left over.")
weekly_average = 72.5
store_a_average = 70
store_b_average = 75
store_c_average = 80
if weekly_average < store_a_average and weekly_average < store_b_average and weekly_average < store_c_average:
    verdict = "cheaper than all three stores"
elif weekly_average > store_a_average and weekly_average > store_b_average and weekly_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"
print("\n=== SUMMARY ===")
print("Cost per person this week:", cost_per_person)
print("Weekly average:", weekly_average)
print("Verdict:", verdict)