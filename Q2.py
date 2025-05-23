#Calculating volume of a sphere using radius given by the user
import math
while True:
    try:
        Radius = float(input("Please input the radius:"))
        if Radius <= 0:
            print("Invalid input! Radius should be a positive number.")
        else:
            Volume = (4/3) * math.pi * (Radius ** 3)
            print(f"Given radius of {Radius}, the volume of the sphere is {Volume:.2f}")
            break
    except ValueError:
        print("Input Should be a number!")
        continue