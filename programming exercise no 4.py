def calc_new_height():
    x = eval(input("Enter the current width : ")) #the user inputs the current width
    y = eval(input("Enter the current height : ")) #the user inputs the current height
    z = eval(input("Enter the desired width : ")) #the user inputs the desired width
    
    while z > x:
        z = eval(input("The desired width must be smaller than the current width, please re-enter another number : ")) #this prompt will be used when the user possibly inputs a number lower than the current width 

    formula1 = x / z #formula to find the scale 
    formula2 = y / formula1 #formula to find the corresponding height
    print("The corresponding height is : ", formula2) #the results of the corresponding height should be 259.0

calc_new_height()