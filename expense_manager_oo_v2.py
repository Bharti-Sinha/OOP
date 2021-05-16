# In this task, you’ll learn how to apply functions inside classes
# in object-oriented programming, it is better to have functions defined inside a class
# Functions that are defined inside a class are called methods.
# we can then manipulate the attributes of objects inside that class by calling the methods of the class.
import sys


# ---------------------------------------------------------------------------------------------------------------------
# simple class that will serve the purpose of creating a data type for holding the information of an expense record.
class Expense:
    date = "YYYY-MM-DD"
    name = None
    amount = 0


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# class to store and retrieve Expense data
# This class will contain the expense list and
# all code relating to manipulating this list, such as adding, searching, removing, loading and saving expenses.
# main class of the “back end” of the application.
# The methods here will not display any outputs to the user and will not take any inputs directly from the user.
class ExpenseManager:
    # expenses list will contain all the objects of the class Expense
    expenses = []

    def add_expense(self, expense_date, expense_name, expense_amount):
        expense = Expense()
        expense.date = expense_date
        expense.name = expense_name
        expense.amount = expense_amount
        self.expenses.append(expense)

    def get_matching_expenses(self, expense_name_partial):
        matching_expenses = []
        for e in self.expenses:
            if expense_name_partial in e.name:
                matching_expenses.append(e)
        return matching_expenses

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def load_data(self, file_name):
        try:
            file_object = open(file_name, "r")
            i = 0
            line = file_object.readline()
            while line != "":
                fields = line.split(',')
                expense_date = fields[0]
                expense_name = fields[1]
                expense_amount = float(fields[2])
                self.add_expense(expense_date, expense_name, expense_amount)
                line = file_object.readline()
                i += 1
            file_object.close()
            return i
        except:
            pass

    def save_data(self, file_name):
        try:
            file_object = open(file_name, "w")  # open("expenses.csv", "w")
            num_expense = len(self.expenses)
            i = 0
            while i < num_expense:
                file_object.write(self.expenses[i].date + "," + self.expenses[i].name + "," + self.expenses[i].amount)
                i += 1
            file_object.close()
            return i
        except:
            sys.stdout.write("Could not save to file.")

# ---------------------------------------------------------------------------------------------------------------------




    def find_expenses(self):
        sys.stdout.write("-------------\n")
        sys.stdout.write("Find Expenses\n")
        sys.stdout.write("-------------\n")
        if (len(self.expenses)) <= 0:
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
        num_expenses = len(self.expenses)
        i = 0
        while i < num_expenses:
            if search_target in self.expenses[i].name:
                row_text = column_format.format(self.expenses[i].date, self.expenses[i].name, self.expenses[i].amount)
                total_amount += self.expenses[i].amount
                matches += 1
                sys.stdout.write(row_text)
            i += 1
        sys.stdout.write("\n You've spent $" + str(total_amount) + " on " + str(total_amount) + " matches.\n")

    def get_str(self, prompt):
        pass

    def run_expenses_manager_oo(self):
        # self.load_data()
        # choice = self.get_menu_choice()
        pass

    # rest of the code below from last week remain same and indented at this level





# Communication between ExpenseManagerUI and ExpenseManager
# will be performed using standard data types available in Python (strings, numbers, etc.)

# class will be the entry-point into the application, and will contain all user interaction code
# “front end” of the application and contains methods relating to displaying the user interface (menus),
# taking inputs as well as methods that invoke methods from the back end
class ExpenseManagerUI:
    # expense_manager
    # run_expense_manager, get_menu_choice,
    # get_str, get_float, get_positive_float, add_expense_via_menu,
    # search_and_display_matching_expenses, find_expenses_via_menu, remove_expenses_via_menu
    pass


home_expenses_manager = ExpenseManager()
home_expenses_manager.run_expenses_manager_oo()
