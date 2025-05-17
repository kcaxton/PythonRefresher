def upper_case(char):
    if char is upper_case:
        print("The character is in upper case.")
    else:
        print("The character is not in upper case.")
        
def lower_case(char):
    if char.islower(char):
        print("The character is in lower case.")
    else:
        print("The character is not in lower case.")
        
while True:
    try:
        char = str(input("Please input a character:"))
        if len(char) != 1:
            print("Invalid input! Please enter a single character.")
        else:
            upper_case(char)
            lower_case(char)
            break
    except ValueError:
        print("Input should be a single string character!")