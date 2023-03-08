USER_TXT_FILE = 'userinfo.txt'


def printTerms():
    print("\nAGREEMENT TO TERMS")
    print("These Terms of Use constitute a legally binding agreement m concerning your access")
    print(" to and use of this application.\nYou agree that by using this software that the")
    print(" information provided on the application is not intended for distribution to or")
    print(" use by any person or entity in any jurisdiction or country where such distribution")
    print("  or use would be contrary to law or regulation or which would subject us to ")
    print(" any registration requirement within such jurisdiction or country. ")
    input("Press Enter to continue...")
 

def main_menu():
    print("========= Main Menu =========")
    print("[1] ===== Create User")
    print("[2] ===== Add Expenses")
    print("[3] ===== Generate Report")
    print("[4] ===== print Terms of use")
    print("[5] ===== End program")
    

def createFile(file_name):
    with open(file_name, 'a') as f:
        f.write('')


def readUsers():
    user_list = []
    createFile(USER_TXT_FILE)
    user_file = open(USER_TXT_FILE, 'r')
    for line in user_file:
        line = line.rstrip("\n")
        line = line.split(",")
        user_list.append({"firstname": line[0], "lastname": line[1], "r_no": line[2], "total_yearly_revenue": line[3]})
    user_file.close()
    return user_list


def saveUser(user_list):
    user_file = open(USER_TXT_FILE, 'w')
    for user in user_list:
        print(user["firstname"], user["lastname"], user["r_no"], user["total_yearly_revenue"], sep=",", file=user_file)
    user_file.close()


def findUser(r_no):
    user_list = readUsers()
    _user = []
    for user in user_list:
        if user["r_no"] == r_no:
            _user = user
    return _user


def createUser(firstname, lastname, r_no, total_yearly_revenue):
    user_list = readUsers()
    user = {"firstname": firstname, "lastname": lastname, "r_no": r_no, "total_yearly_revenue": total_yearly_revenue}
    user_list.append(user)
    saveUser(user_list) 
    return user_list


def userExists(r_no):
    user = findUser(r_no)
    if len(user) == 0:
        print("This User does not have an account yet, Please create an account first")
        return False
    else:
        return user

 
def readExpenses(r_no):  
    user = userExists(r_no)
    expense_file_name = user["r_no"] + "_expenses.txt"
    createFile(expense_file_name)
    expense_list = []
    expense_file = open(expense_file_name, 'r')
    for line in expense_file:
        line = line.rstrip("\n")
        line = line.split(",")
        expense_list.append({"source": line[0], "amount": line[1], "classification": line[2]})
    expense_file.close()
    return expense_list


def saveExpense(r_no, expense_list):
    user = userExists(r_no)
    expense_file_name = user["r_no"] + "_expenses.txt"
    expense_file_name = open(expense_file_name, 'w')
    for expense in expense_list:
        print(expense["source"], expense["amount"], expense["classification"], sep=",", file=expense_file_name)
    expense_file_name.close()


def createExpense(r_no, source, amount, classification):    
    expense_list = readExpenses(r_no)
    expense = {"source": source, "amount": amount, "classification": classification}
    expense_list.append(expense)
    saveExpense(r_no, expense_list) 
    return expense_list
 

def printExpenseList(expense_list):
    print("\n=============== Current Expenses List ===============")
    print("Source", "Amount", "classification", sep='\t')
    for expense in expense_list:
        print(f'{expense["source"]}\t', f'{expense["amount"]}\t', f'{expense["classification"]}\t', sep='\t')


def highestExpenseAmount(expense_list): 
    amount_list = []

    for expense in expense_list:
        amount_list.append(expense["amount"])
        
    return max(amount_list)


def format_number(val):
    return str("{:.2f}".format(float(val)))


def generateReport(r_no):
    print("[1]: Print to Screen:")
    print("[2]: Print to File")
    choice = int(input("Select output option: "))

    user = findUser(r_no)
    expense_list = readExpenses(r_no)
    highest_expense_amt = highestExpenseAmount(expense_list)
    preferred_expenses = 0.5 * float(user["total_yearly_revenue"])
    total_yearly_revenue = float(user["total_yearly_revenue"])
    if choice == 1:

        print("=============== Expense Report ===============")
        print("Name: ", f'{user["lastname"]}\t', f'{user["firstname"]}')
        print("R#: ", f'{user["r_no"]}')
        print("Total Income: ", format_number(total_yearly_revenue))
        print("Highest Expense Category: ", format_number(highest_expense_amt))
        print("Preferred Expenses: ", format_number(preferred_expenses))

        print("------------ statement of current budget ------------")
        for expense in expense_list:
            exp_percent = float(expense["amount"])/total_yearly_revenue * 100
            print(expense["source"], f'{format_number(exp_percent) + "%"}',  sep="\t")

        printExpenseList(expense_list)

        print("=============== End of Expense Report ===============")

    elif choice == 2:

        # open file for writing
        expense_file_name = user["r_no"] + "_expense_report.txt"
        createFile(expense_file_name)
        expense_file_name = open(expense_file_name, "w")

        print("=============== Expense Report ===============", file=expense_file_name)
        print("Name: ", f'{user["lastname"]}\t', f'{user["firstname"]}', file=expense_file_name)
        print("R#: ", f'{user["r_no"]}', file=expense_file_name)
        print("Total Income: ", format_number(total_yearly_revenue), file=expense_file_name)
        print("Highest Expense Category: ", format_number(highest_expense_amt), file=expense_file_name)
        print("Preferred Expenses: ", format_number(preferred_expenses), file=expense_file_name)

        print("------------ statement of current budget ------------", file=expense_file_name)
        for expense in expense_list:
            exp_percent = float(expense["amount"]) / total_yearly_revenue * 100
            print(expense["source"], f'{format_number(exp_percent) + "%"}', sep="\t", file=expense_file_name)

        print("------------ current expense list ------------", file=expense_file_name)
        for expense in expense_list:
            print(expense["source"], expense["amount"], expense["classification"], sep="\t", file=expense_file_name)
        expense_file_name.close()
        print(f'File hase been saved as {expense_file_name}')
        print("=============== End of Expense Report ===============")
    else:

        print("Invalid print option")
        return False
