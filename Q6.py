# Q6. Write a Python program that takes 5 values from the user and calculates the average of those values.
while True:
    try:
        Val = int(input("Please input 5 values:"))
        if len(Val) != 5:
            print("Invalid input! Please enter 5 values.")
        else:
            average = sum(Val) / len(Val)
            print(average)
            break
    except ValueError:
        print("Input should be numerical!")
        continue   