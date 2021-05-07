#Aileen Morales, Maura Blazek, Matt Uriegas
#Group 3, Final Project

import os.path

DIRECTORY = 'C:\\Users\\murie\\PycharmProjects\\pythonProject\\'
FILENAME = "userinfo"

def display_menu(): # Function to display menu
   print('-----Main Menu-----')
   print('1)  Create new user')
   print('2)  Add User Expenses')
   print('3)  Generate Report')
   print('4)  Print Terms of Use')
   print('5)  Exit\n')

def create_user(): # Function to create a new user
    rNum = input('Input your R Number:  ')

    while isUser(str(rNum)):
        print('*****File found!  User already exists!.*****\n')
        rNum = input('Input your rNumber again:  ')

    print('File name for this user\'s expenses is: ', rNum + '_expenses'+'.txt\n')

    userList = []
    fname = input('Enter first name:  ')
    lname = input('Enter last name:  ')
    totalYearly = input("Enter your Total Yearly Revenue: ")
    userList.append([fname, lname, rNum, totalYearly])
    saveUser(FILENAME + '.txt', userList)

def is_valid_file(f):
    return os.path.exists(DIRECTORY + f)

def isUser(rNum): # Checks if user exists in userinfo file
    try:
        with open(DIRECTORY + FILENAME + ".txt", 'r') as fileread:
            for lines in fileread:
                linesplit = lines.rstrip().split(',')
                for i in linesplit:
                    if i == rNum:
                        return True
        return False
    except:
        return False



def addUserExpenses(): # Function to add expenses to users personal file
    uNum = input("Enter your RNumber: ")
    uNumF = uNum + "_expenses.txt"
    expArr = []
    if(isUser(uNum)): #Checks if user exists
        numofItems = int(input('Enter number of items:  '))
        for i in range(numofItems):
            source = input('Enter the source:  ')
            amount = input('Enter the amount spent:  ')
            print("Enter the classification.")
            classification = input('(Must be grocery, utility, recreational, gas, travel, healthcare): ')
            expArr.append([source, amount, classification])

        saveUExpenses(uNumF, expArr)
    else:
        print("Your file does not exist.")
        print("Add your file using option 1")
        print("Returning to menu\n")

def saveUser(f, user):
    with open(DIRECTORY + f, 'a') as filein:
        for s in user:
            filein.write(s[0] + ',' + s[1] + ',' + s[2] + ',' + s[3] + '\n')


def read_in_file(f): #Function for reading userinfo file and returning a list
    itemlist = []

    with open(DIRECTORY + f, 'r') as fileread:
        for lines in fileread:
            linesplit = lines.rstrip().split(',')
            itemlist.append([linesplit[0], linesplit[1], linesplit[2], linesplit[3]])

    return itemlist

def read_user_expenses(f): # Function for reading user expenses file and returning a list
    expenses = []

    with open(DIRECTORY + f, 'r') as fileread:
        for lines in fileread:
            linesplit = lines.rstrip().split(',')
            expenses.append([linesplit[0], linesplit[1], linesplit[2]])

    return expenses

def saveUExpenses(f, arr):
    with open(DIRECTORY + f, 'a') as filein:
        for s in arr:
            filein.write(s[0] + ',' + s[1] + ',' + str(s[2]) + '\n')

def generate_report(): # Function to generate users report from expenses
    uNum = input("Enter your RNumber: ")
    uNumF = uNum + "_expenses.txt"
    if not is_valid_file(uNumF): #Checks if user exists
        print("Your expenses file does not exist.")
        print("Add your expenses file using option 2")
        print("Returning to menu\n")
        return

    uRead = read_in_file(FILENAME + ".txt")
    temp = []

    for i in uRead: # Saves user info to temp list and is used to print
            if i[2] == uNum:
                temp = i

    print('Name: ' + temp[0])
    print('R#: ' + temp[1])
    print('Total Income(revenue): ' + temp[3])

    sum = 0
    explist = [0, 0, 0, 0, 0, 0]
    uExpenses= read_user_expenses(uNumF)

    for i in uExpenses:# For loop for adding up total expenses and based on category
        sum += int(i[1])
        if i[2].lower() == 'grocery':
            explist[0]+=int(i[1])
        elif i[2].lower() == 'utility':
            explist[1]+=int(i[1])
        elif i[2].lower() == 'recreational':
            explist[2]+=int(i[1])
        elif i[2].lower() == 'gas':
            explist[3]+=int(i[1])
        elif i[2].lower() == 'travel':
            explist[4]+=int(i[1])
        elif i[2].lower() == 'healthcare':
            explist[5]+=int(i[1])

    max = 0
    for i in range(1, len(explist)): # Loop used to check which category has the most expenses
        if explist[max] < explist[i]:
            max = i
    max+=1
    category = getCategory(max)

    print("Your preferred expenses would be: ", int(temp[3])/2)
    print('Total Expenses: ' +  str(sum))
    print ('Highest expenses category: ' + category)

    statIncome = (int(sum)/int(temp[3])) * 100
    print(classification(statIncome) + '\n')

    print('Source', '\t', 'Expense', '\t', 'Category')
    for i in uExpenses:
        print(i[0], '\t', i[1], '\t', i[2])
    print('\n')


def getCategory(x): # Gets category of max expenses
    if x == 1:
        return "Grocery"
    elif x == 2:
        return "Utility"
    elif x == 3:
        return "Recreational"
    elif x == 4:
        return "Gas"
    elif x == 5:
        return "Travel"
    elif x == 6:
        return "Healthcare"


def terms(): # Prints terms of use
    print("Terms of Service: Our Mission is to give our people financial knowledge. However, we will be using really complicated terms\n\
    so people that are using our service are not fully aware of what is going on. We strive to make it so complicated that users repel\n\
    from reading our terms of service. In addition, you own the content that you post. We also become owners of your content and you grant us\n\
    and other users certain rights and license to use it. The details of these licences are described in other areas of the contract that will be\n\
    extremely hard to locate. Yes, we did it on purpose. You can repost content from this report elsewhere provided that you attribute the content \n\
    back to the Quora platform and give us the right to attain your soul for future purposes.\n")

def classification(metric): # Function to determine where user falls based on expenses
    if metric <=20:
        return 'You an amazingly rich hooman'
    elif metric <= 40:
        return 'You in the upper class, hooman'
    elif metric <= 60:
        return 'You a middle class hooman'
    elif metric <= 80:
        return 'You a kinda broke hooman'
    elif metric <= 100:
        return 'You a broke hooman'
    else:
        return 'You should consider getting your stuff together, hooman'
