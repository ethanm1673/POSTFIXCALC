"""
PostFix Calculator
Ethan S McConnell
APCSP 2/14/20
Riverwood Int. HS.
"""

def mathOpps(int1, int2, str1):
    if str1 == "*":
        return int1 * int2
    if str1 == "+":
        return int1 + int2
    if str1 == "-":
        return int1 - int2
    if str1 == "/":
        return int1 / int2

inputList = []
numList = []
oppList = []

inputStr = input("Enter your Postfix expression then press enter. ")

for x in range(len(inputStr)):
    inputList.append(inputStr[x])

z = 0
while z < len(inputList):
    if inputList[z] == " ":
        inputList.remove(" ")
    z = z + 1

inputNums = int(len(inputList)/2 + .5)

for x in range(inputNums):
    numList.append(inputList[x])

for x in range(inputNums, len(inputList)):
    oppList.append(inputList[x])

print(numList)

for x in numList:
    numList.append(mathOpps(int(numList.pop(len(numList)-1)), int(numList.pop(len(numList)-2)), oppList.pop(-1)))
    print(numList)