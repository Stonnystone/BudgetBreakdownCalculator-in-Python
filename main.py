# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import mylib as bdc


def main():


    print("\n============ Budget Breakdown Calculator ============")
    while 1:
        bdc.main_menu()

        option = int(input("\n Select an option: "))

        if option == 1:
            print("=============== Create New User Account ===============")
            firstname = input(" What is your Firstname? ")
            lastname = input(" What is your Lastname? ")
            r_no = input(" What is your Reg. No.? ")
            total_yearly_revenue = float(input(" What is your Total Yearly Revenue? "))
            bdc.createUser(firstname, lastname, r_no, total_yearly_revenue)
            print("User account created successfully.")
            main()
        elif option == 2:
            r_no = input(" What is your Reg. No.? ")
            user = bdc.userExists(r_no)
            if not user:
                main()
            current_expenses = bdc.readExpenses(r_no)
            bdc.printExpenseList(current_expenses)

            print("=============== Create New Expense ===============")
            print('Enter expense sources. Type q as expense source to finish.')
            print('Expense Source', 'Amount', 'Classification', 'Total')

            # loop to create more expenses
            while 1:
                source = input(" Enter the Expense source: ")
                if source.lower() == 'q':
                    break
                amount = float(input(" Enter the Amount: "))
                classification = input(" Enter the Expense classification: ")
                bdc.createExpense(r_no, source, amount, classification)
                print("----------------------------------------------")
            main()

        elif option == 3:

            r_no = input("\n What is your Reg. No.? ")
            user = bdc.userExists(r_no)
            if not user:
                main()
            bdc.generateReport(r_no)
            main()
        elif option == 4:

            bdc.printTerms()
            main()

        elif option == 5:
            # confirm that the user wants to start again
            yes_list = ["yes", "y", "yeah"]
            restart = input("Are you sure you want to Quit [yes, yeah or y to quit]? ").lower()
            if restart not in yes_list:
                main()

            print("Thank you for using the application. Exiting the application...")
            break

        else:
            print("Please choose a correct option")
            main()
    exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


