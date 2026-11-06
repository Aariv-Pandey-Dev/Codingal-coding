numn = int(input("Enter a numerator (integer):"))
numd = int(input("Enter a denominator (integer):"))
if numn % numd == 0:
    print(f"{numn} is divisible by {numd}")
else:
    print(f"{numn} is not divisible by {numd}")