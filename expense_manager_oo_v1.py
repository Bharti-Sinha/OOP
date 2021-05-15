# functions were created outside of the class
# as these functions were used from previous non OOP version of the same program
# In this code, only dealt with attributes 
import sys


class Expense:
    date = "YYYY-MM-DD"
    name = None
    amount = 0


# expenses list will contain all the objects of the class Expense
expenses = []


def add_expense(expense_date, expense_name, expense_amount):
    expense = Expense()
    expense.date = expense_date
    expense.name = expense_name
    expense.amount = expense_amount
    expenses.append(expense)


def save_data():
    try:
        file_object = open("expenses.csv", "w")
        num_expense = len(expenses)
        i = 0
        while i < num_expense:
            file_object.write(expenses[i].date + "," + expenses[i].name + "," + expenses[i].amount)
            i += 1
        file_object.close()
    except:
        sys.stdout.write("Could not save to file.")


def find_expenses():
    sys.stdout.write("-------------\n")
    sys.stdout.write("Find Expenses\n")
    sys.stdout.write("-------------\n")
    if (len(expenses)) <= 0:
        sys.stdout.write("No expenses to find. Try adding expenses first.")
        return

    sys.stdout.write("Enter partial expense name to find:")
    sys.stdout.flush()
    search_target = sys.stdin.readline().strip()
    sys.stdout.write("\n")

    dates_width = 11
    names_width = 20
    amounts_width = 10

    column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:<" + str(amounts_width) + "} \n"

    row_text = column_format.format("----", "----", "--------")
    sys.stdout.write(row_text)
    row_text = column_format.format("Date", "Name", "Amount $")
    sys.stdout.write(row_text)
    row_text = column_format.format("----", "----", "--------")
    sys.stdout.write(row_text)

    matches = 0
    total_amount = 0
    num_expenses = len(expenses)
    i = 0
    while i < num_expenses:
        if search_target in expenses[i].name:
            row_text = column_format.format(expenses[i].date, expenses[i].name, expenses[i].amount)
            total_amount += expenses[i].amount
            matches += 1
            sys.stdout.write(row_text)
        i += 1
    sys.stdout.write("\n You've spent $" + str(total_amount) + " on " + + str(total_amount) + " matches.\n")

# rest of the code below from last week remain same
