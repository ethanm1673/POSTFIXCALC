"""
PostFix Calculator
Ethan S McConnell
APCSP 2/14/20
Riverwood Int. HS.
"""


#A function that translates the string opperations passed from the user input, to actual math opperations
def mathOpps(int1, int2, str1):
    if str1 == "*":
        return float(int1 * int2)
    if str1 == "+":
        return float(int2 + int1)
    if str1 == "-":
        return float(int2 - int1)
    if str1 == "/":
        return float(int2 / int1)


# Input list contains each char of the inputStr string
inputList = []
# Num list contains the the numbers passed from the inputList[]
numList = []
#opp list contains the opperations passed from the inputList[]
oppList = []

#Takes the user input and assigns it to inputStr
inputStr = input("Enter your Postfix expression then press enter. ")

#moves each individual char in the string "inputStr" into inputList[]
for x in range(len(inputStr)):
    inputList.append(inputStr[x])

#checks for space chars in the inputList[] and removes them
z = 0
while z < len(inputList):
    if inputList[z] == " ":
        inputList.remove(" ")
    z = z + 1

#created the int inputNums to calculate the legnth of the numList[] and oppList[]
inputNums = int(len(inputList) / 2 + .5)

#moves the numbers from inputList[] to numList[]
for x in range(inputNums):
    numList.append(inputList[x])

#moves the opperations from inputList[] to oppList[]
for x in range(inputNums, len(inputList)):
    oppList.append(inputList[x])

#Vars for the function below
tempLast = None
tempLast2 = None
tempDone = None
oppLast = None

#Calls the mathOpps() function and passes the last two values of numList[] and the last value of oppList[] to be computed for the legnth of numList[]
for x in numList:
    tempLast = float(numList.pop(len(numList) - 1))
    tempLast2 = float(numList.pop(len(numList) - 2))
    oppLast = oppList.pop(len(oppList) - 1)
    tempDone = mathOpps(tempLast, tempLast2, oppLast)
    numList.append(tempDone)

#this is literally the same code as above but it was broken tell i added this. TBH i have no idea why it fixed it but it did:)
for x in numList:
    tempLast = float(numList.pop(len(numList) - 1))
    tempLast2 = float(numList.pop(len(numList) - 2))
    oppLast = oppList.pop(len(oppList) - 1)
    tempDone = mathOpps(tempLast, tempLast2, oppLast)
    numList.append(tempDone)

print(numList)
