nameString = input("List all the friends you wish to split costs with (separated by a space): ")

namesList = nameString.split( ) # Splits input String into individual string and puts it in a list
amountList = []

for x in range(len(namesList)):
    amountList.append(0)

def printNames(listofnames):
    for name in listofnames:
        print(name)

def splitPrice(friendPaid, paidAmount, listNames, listAmounts):
    for i in range(len(listNames)):
        if listNames[i] != friendPaid:
            listAmounts[i] = listAmounts[i] + paidAmount/len(listNames)
    
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


addCheck = input("Do you want to add a payment? (y/n) : ")
while(addCheck == "y"):
    printNames(namesList)
    namePaid = input("Enter name of friend who paid:  ")
    namePaid = checkName(namePaid, namesList)
    amountPaid = input("Enter amount paid: $ ")
    splitPrice(namePaid, int(amountPaid), namesList, amountList)
    print(amountList)
    addCheck = input("Do you want to add another a payment? (y/n) : ")













print(namesList)
