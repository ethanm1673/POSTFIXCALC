"""
PostFix Calculator
Ethan S McConnell
APCSP 2/14/20
Riverwood Int. HS.
"""


#A function that translates the string opperations passed from the user input, to actual math opperations
def mathOpps(int1, int2, str1):
    if str1 == "*":
        return int1 * int2
    if str1 == "+":
        return int1 + int2
    if str1 == "-":
        return int1 - int2
    if str1 == "/":
        return int1 / int2


# Input list contains each char of the inputStr string
inputList = []
# Num list contains the the numbers passed from the inputList[]
numList = []
#opp list contains the opperations passed from the inputList[]
oppList = []

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

print(numList)

#Calls the mathOpps() function and passes the last two values of numList[] and the last value of oppList[] to be computed for the legnth of numList[]
for x in numList:
    numList.append(
        mathOpps(
            int(numList.pop(len(numList) - 1)),
            int(numList.pop(len(numList) - 2)), oppList.pop(-1)))
    print(numList)
