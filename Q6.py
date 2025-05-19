#The code takes 5 values from the user, populating them as an array then calculates the average of those values.
while True:
    try:
        print("Please input five values.")
        Val = [int(input(f"{i+1}: ")) for i in range(5)]
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue  
    print(f"Your array of values is: {Val}")
    average = sum(Val) / len(Val)
    print(f"Average of the Values is: {average}")
    break