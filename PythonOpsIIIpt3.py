math = int(input("Enter your maths marks:"))
english = int(input("Enter your english marks:"))
science = int(input("Enter your science marks:"))
ss = int(input("Enter your social science marks:"))
CompSc = int(input("Enter your computer science marks:"))
avg = (math + english + science + ss + CompSc) / 5
print(f'Average: {avg}')
validRange = range(0, 101)
if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91,101):
    print("Grade A")
elif avg in range(81,91):
    print("Grade B")
elif avg in range(66,81):
    print("Grade C")
elif avg in range(51,66):
    print("Grade D")
elif avg in range(21,51):
    print("Grade F")
elif avg in range(0,21):
    print("Grade F-")