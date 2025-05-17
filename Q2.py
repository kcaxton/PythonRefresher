#Calculating volume of a sphere given the radius
while True:
    try:
        Radius = float(input("Please input the radius:"))
        if Radius <= 0:
            print("Invalid input!")
        else:
            pi = 22/7
            Volume = (4/3) * pi * (Radius ** 3)
            print(f"Given radius of {Radius}, the volume of the sphere is {Volume:.2f}")
            break
    except ValueError:
        print("Input Should be decimal!")
