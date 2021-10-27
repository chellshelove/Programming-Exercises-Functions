print("convert_to_days()")
def convert_to_days(): #input the hours, minutes and seconds (1)
    hours = eval(input("Enter number of hours : "))
    minutes = eval(input("Enter number of minutes : "))
    seconds = eval(input("Enter number of seconds : "))
    print("The number of days is :", intoDays(hours, minutes, seconds)) #the results from intoDays function is printed (3)
        
def intoDays (h,m,s): #the data that has been inputed will then be calculated with this helper function (3)
    formula = ((h*3600)+(m*60)+(s))/86400 #formula to convert into days 
    return round(formula, 4) #the value will be rounded and returned 

convert_to_days()