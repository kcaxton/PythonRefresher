#Calculating the area and perimeter of a square given the side length
def area(Length):
    Area = Length * Length
    return Area

def perimeter(Length):
    Perimeter = 4 * Length
    return Perimeter

while True:
    try:
        Length = float(input("Please input the length of the square:"))
        if Length <= 0:
            print("Invalid input!")
        else:
            Area_of_Square = area(Length)
            Perimeter_of_Square = perimeter(Length)
            print(f"The area of the square is {Area_of_Square} square units.\nThe perimeter is {Perimeter_of_Square} units.")
            break
    except ValueError:
        print("Input should be decimal!")