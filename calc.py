nameString = input("List all the friends you wish to split costs with (separated by a space): ") # Collects user input of n people to split monetary values with (input separated by space for each name)

namesList = nameString.split( ) # Splits input String into individual string and puts it in a list

number_of_lists = len(namesList) # Number of lists to be created for each array

userAmountLists = [[] for i in range(number_of_lists)] # Stores the owe value for each person
userNamesLists = [[] for i in range(number_of_lists)] # Stores  the name of each person

for i in range(len(userAmountLists)):  # Sets all owe amounts in the beginning to $0
    for x in range(len(userAmountLists)): 
        userAmountLists[i].append(0)

for i in range(len(userNamesLists)): # Adds all the names to the list in the same order as the owe amount
    userNamesLists[i].append(namesList[i]) # Adds the name to the beginning of the list (this ensures unique ordered lists are made)
    for name in namesList:
        if name != namesList[i]: # adds the other names from nameList
            userNamesLists[i].append(name)

def printNames(listofnames): # Function that prints the full list of names entered by user in input statement
    for name in listofnames:
        print(name)


def checkName(nameInput, listNames): # Function that verifies whether a user has responded with a correct name from the initial list of names provided by the user
    check = False 
    for name in listNames: # If the name matches the input list from earlier, it's good to go!
        if name == nameInput:
            check = True      
    if check == False: # If it is false, prompt user to re input the correct name
        printNames(listNames)
        renter = input("This is not one of the names on the list. Re-enter a name from above: ")
        return checkName(renter, listNames) # Recursive Fuction: Calls itself until a proper name is provided by the user
    return nameInput # Once the name is correct, this while loop ends

def splitCosts(namePaid, amountPaid): # Function to split the cost between n amount of friends in the group
    for i in range(len(userNamesLists)): # Goes through 0 to amount of names
        if userNamesLists[i][0] != namePaid: # Checks If the name is not the person who paid, and if not then continues
            for x in range(len(userNamesLists[i])): # Loops through the owe amount lists
                if userNamesLists[i][x] == namePaid: # Check for the name in the owe amount lists of others 
                    userAmountLists[i][x] = userAmountLists[i][x] + round(amountPaid/len(namesList),2) # Splits the price amongst the friend group


def printResults(): # Function to print the results of who owes you in a semi-pretty way 
    for x in range(len(userNamesLists)):
        print(userNamesLists[x][0] + " owes ", end="", flush=True) # print on same line
        for i in range(len(userNamesLists[x]) -1): # -1 is there so the range doesnt exceed and give error (first element is printed above)
            print(str(userNamesLists[x][i + 1]) + " $" + str(userAmountLists[x][i + 1]) + " ", end="", flush=True)
        print()
            


addCheck = input("Do you want to add a payment? (y/n) : ") # Asks user if they want to add a payment (y/n input)
while(addCheck == "y"): # while loop only breaks when there are no more payments to input
    printNames(namesList) # Prints the name added for user to easily see
    namePaid = input("Enter name of friend who paid:  ") # Asks user for the name of the friend who paid
    namePaid = checkName(namePaid, namesList) # Checks if the name entered if correct
    amountPaid = input("Enter amount paid: $ ") # Asks user how much the person who paid had spent
    splitCosts(namePaid, float(amountPaid)) # Splits the costs between the friends in the list
    printResults() # Prints results to see current owe amounts for all users
    addCheck = input("Do you want to add another a payment? (y/n) : ") # Asks User if they want to input another payment, if input is "y" then the while loop starts over, otherwise it ends

print() # Print the Final Balance Neatly for summary
print("Here is the final balance:")
print("-----------------------------")
printResults()



