print("Body Mass Index (Upto the Age of 20)")
print(" ")
height = float(input("Height(m) is: "))
weight = float(input("Weight(kg) is: "))
age = int(input("Age is: "))
body_mass_index = (weight/(height*height))
if age <= 20:
    print("Body Mass Index is: " + str(body_mass_index)+" cm^3")
else:
    print("Age is out of limit")
print(" ")
print(" ")
if body_mass_index <= 17.5:
    print("You are Under-weight")
if 17.5 < body_mass_index:
    if body_mass_index <= 22.99:
        print ("You are Normal-weight")
if 22.9 < body_mass_index:
    if body_mass_index <= 27.99:
        print("You are Over-weight")
if 27.99 < body_mass_index:
    print("You are Obese")