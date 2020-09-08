#Fuel is based on mass, to find the fuel required for a module is
#Mass/3 rounded down and subtract 2

#import libraries
import math

#Recieve input
InputValue = input ("Please input the mass of the module:")

#Divide by 3
InputValue = float(InputValue)/3
#Round down
InputValue = math.floor(InputValue)
#Subtract 2
InputValue = InputValue-2
#Output result
print("Required fuel:", InputValue)
