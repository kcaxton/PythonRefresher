#Calculating seconds in the number of days given by the user
while True:
    
    try:
        Days = int(input("Please enter any number of days:"))
        Seconds_in_Days = Days * 24 * 60 * 60
        if Days <= 0:
            print("Invalid number of days!")
        elif Days == 1:
            print(f"Given {Days} day, there are {Seconds_in_Days} seconds.")
            break
        elif Days > 1:
            print(f"Given {Days} days, there are {Seconds_in_Days} seconds.")
            break
    except ValueError:
        print("Input should be numerical!")