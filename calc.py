from itertools import *

nameString = input("List all the friends you wish to split costs with (separated by a space): ")

namesList = nameString.split( ) # Splits input String into individual string and puts it in a list
amountList = []

number_of_lists = len(namesList)

userAmountLists = [[] for i in range(number_of_lists)]
userNamesLists = [[] for i in range(number_of_lists)]

for i in range(len(userAmountLists)):
    for x in range(len(userAmountLists)):
        userAmountLists[i].append(0)

for i in range(len(userNamesLists)):
    userNamesLists[i].append(namesList[i])
    for name in namesList:
        if name != namesList[i]:
            userNamesLists[i].append(name)

def printNames(listofnames):
    for name in listofnames:
        print(name)

def checkName(nameInput, listNames):
    check = False
    for name in listNames:
        if name == nameInput:
            check = True      
    if check == False:
        printNames(listNames)
        renter = input("This is not one of the names on the list. Re-enter a name from above: ")
        checkName(renter, listNames) 
    return nameInput


def splitCosts(namePaid, amountPaid):
    for i in range(len(userNamesLists)):
        if userNamesLists[i][0] != namePaid:
            for x in range(len(userNamesLists[i])):
                if userNamesLists[i][x] == namePaid:
                    userAmountLists[i][x] = userAmountLists[i][x] + amountPaid/len(namesList)





addCheck = input("Do you want to add a payment? (y/n) : ")
while(addCheck == "y"):
    printNames(namesList)
    namePaid = input("Enter name of friend who paid:  ")
    namePaid = checkName(namePaid, namesList)
    amountPaid = input("Enter amount paid: $ ")
    splitCosts(namePaid, float(amountPaid))
    
    print(userAmountLists)
    print(userNamesLists)
    addCheck = input("Do you want to add another a payment? (y/n) : ")
        










print(userAmountLists)
print(userNamesLists)





