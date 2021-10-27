def convert_tempC():
    tempF = eval(input("Enter a temperature in Fahrenheit : ")) #the user inputs the desired temperature in fahrenheit
    formulaC = (tempF-32) * (5/9) #formula to convert fahrenheit to celcius
    print("The temperature in Fahrenheit is : ", tempF) #the temperature in fahrenheit is printed 
    print("The temperature in Celsius is : ", formulaC) #the results from converting the temparature from fahrenheit to celcius
    return formulaC

def convert_tempK():
    celcius = convert_tempC()
    formulaK = celcius + 273.15 #formula to convert celcius to kelvin
    print("The temperature in Kelvin is : ", formulaK) #the results from converting the temparature from celcius to kelvin
    
convert_tempK() 