#The code prints out the new value of x based on the corresponding new value of y
#The loop continues provided y is still greater or equal to 6   x = 0
x = 0
y = 20
while y >= 6:
    y = y-4
    x = (2/y) + x
    print(f"when y is {y}, x is {x:.4f} ") 
