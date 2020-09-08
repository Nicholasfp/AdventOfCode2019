#Receive comma seperated values in batches of 5 batches that start with
#different values will do different tasks depending on the primary character
#Starting with 1 adds numbers from positions 1 and 2 and stores them in position 3
#Starting with 2 multiplies two inputs and stores in position 3
#Starting with 99 indicates the program is finished and the program should stop
#Include an error code for unknown values
#When code processed move to next 4 positions

#Import libraries
import csv
import math

#Empty list to save numbers into
ListNum = []
#List pointer
ListPointer = 0
#Set stop flag to false
StopFlag = 0

#Open InputNum data
with open('InputNum.csv') as csv_file:
    #Store values into the list 
    ReadNum = csv.reader(csv_file, delimiter=',')
    for row in ReadNum:
        ListNum = row

#Convert list into integer
for i in range(0, len(ListNum)):
    ListNum[i] = int(ListNum[i])
#Add next two positions and store in position 3

while StopFlag == 0:
    #Read current position
    x = ListNum[ListPointer]
    if x == 1:
        Sum = ListNum[(ListPointer+1)] + ListNum[(ListPointer+2)]
        WritePosition = ListNum[(ListPointer+3)]
        ListNum[WritePosition] = Sum
        #Clear Sum
        Sum = 0;
        #Update pointer
        ListPointer += 4

    #Multiply next two position and store in position 3
    elif x == 2:
        Multiplication = ListNum[(ListPointer+1)] * ListNum[(ListPointer+2)]
        WritePosition = ListNum[(ListPointer+3)]
        ListNum[WritePosition] = Multiplication
        #Clear Multiplication
        Multiplication = 0;
        #Update pointer
        ListPointer += 4
    
    #Stop program
    elif x == 99:
        StopFlag = 1
    #Error code
    else:
        Print("Error no correct input value found")
print(ListNum)
