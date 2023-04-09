import math

def formula1(timeDivision, getHours, getMinutes):
    return timeDivision * getHours + getMinutes

restart = 'Y'

while restart == 'Y' :
    
    timeDivision = 60
    getHours = int(input("Enter the hours in 12-hr format (1-12): "))

    if getHours > 12 or getHours < 1:

        print ("Wrong hour input, please try again") 
        continue

    getMinutes = int(input("Enter the minutes (0-59): "))

    if getMinutes > 59 or getMinutes < 0:
        print ("Wrong minute input, please try again")
        continue

    hourAngle = 0.5 * formula1(timeDivision, getHours, getMinutes)
    minuteAngle = 6 * getMinutes

    getAngle = abs(hourAngle - minuteAngle)

    if getAngle > 180:
        getAngle = 360 - getAngle

    print("The lesser angle in degrees between hours arrow and minutes arrow is ", getAngle)

    restart = input("If you want to try again press 'Y': ")
