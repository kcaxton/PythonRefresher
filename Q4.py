#checking if a character input by a user is upper or lower
def upper_case(char):
    if char.isupper():
        print("The character is in upper case.")
        
def lower_case(char):
    if char.islower():
        print("The character is in lower case.")
        
while True:
    
    char = input("Please input a character:")
    if len(char) != 1:
        print("Invalid input! Please enter a single character.")
    elif not char.isalpha():
        print(f"The character {char} is not alphabetic! Please enter an alphabetic character.")
    else:
        upper_case(char)
        lower_case(char)
        break

        
        
