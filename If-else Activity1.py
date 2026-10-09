a = int(input("What is today's temperature (in Degrees Celcius)? "))
if a > 15:
    print("Wear a T-Shirt")
    e = "Wear a T-Shirt, "
else:
    print("Wear a jacket.")
    e = "Wear a jacket, "
b = bool(input("Is it raining? (If false, just click enter) "))
if b == True:
    print("Pack an umbrella.")
    f = "pack an umbrella, "
else:
    print("No need for an umbrella.")
    f = "no need for an umbrella, "
    
c = int(input("What is the wind speed (km/h)? "))
if c >= 12:
    print("Take a windbreaker with you.")
    g = "take a windbreaker with you, "
else:
    print("No need for a windbreaker.")
    g = "no need for a windbreaker, "
d = bool(input("Are there puddles? (If false, just click enter) "))
if d == True:
    print("Wear Boots.")
    h = "and wear boots."
else:
    print("Wear Sneakers. ")
    h = "and wear sneakers."
i = e+f+g+h
print ("Final statement: ", i)