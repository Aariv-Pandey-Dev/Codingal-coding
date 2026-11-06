a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
avg = (a + b + c) / 3
if avg > a:
    print("Valid input.")
elif avg > b:
    print("Valid input.")
elif avg > c:
    print("Valid input.")
else:
    print("Invalid input.")