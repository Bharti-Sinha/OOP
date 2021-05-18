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

    expense_manager = ExpenseManager()

    # expense_manager - is not a list but a single object
    # If we decide to maintain various expense categories,
    # we can create a list of ExpenseManager objects named expense_managers

    def run_expenses_manager(self):
        data_file_name = 'expenses.csv'
        if self.expense_manager.load_data(data_file_name) is None:
            sys.stdout.write("Could not open file " + data_file_name)
        choice = self.get_menu_choice()
        while choice != "x":
            sys.stdout.write("\n")
            if choice == 'a':
                self.add_expense_via_menu()
            elif choice == 'r':
                self.remove_expense_via_menu()
            elif choice == 'f':
                self.find_expenses_via_menu()
            choice = self.get_menu_choice()

        if self.expense_manager.load_data(data_file_name) is None:
            sys.stdout.write("Could not open file " + data_file_name)

    def get_menu_choice(self):
        menu = "\n====================== \n"
        menu = menu + "Expense Manager v1.0 \n"
        menu = menu + "====================== \n"
        menu = menu + '[A]dd an expense \n'
        menu = menu + '[R]emove an expense \n'
        menu = menu + '[F]ind expenses \n'
        menu = menu + 'E[x]it\n'

        sys.stdout.write(menu)
        menu = menu.lower()
        # print(menu)
        choice = self.get_str("Enter Choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = self.get_str(choice + " was an invalid choice! Re-enter:  ").lower()
        return choice

    def get_str(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
        while len(value) == 0:
            sys.stdout.write("Input cannot be blank. Renter: ")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()
        return value

    def get_float(self, prompt):
        value = None
        while value is None:
            try:
                value = float(self.get_str(prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
            return value

    def get_positive_float(self, prompt):
        value = self.get_float(prompt)
        while value < 0:
            value = self.get_float("Input must be positive. Re-enter: ")
        return value

    def add_expense_via_menu(self, ):
        sys.stdout.write("--------------\n")
        sys.stdout.write("Add an expense")
        sys.stdout.write("--------------\n")
        expense_date = self.get_str("Enter date as YYYY-MM-DD: ")
        sys.stdout.write("\n")
        expense_name = self.get_str("Enter name: ")
        sys.stdout.write("\n")
        expense_amount = self.get_positive_float("Enter amount ")
        sys.stdout.write("\n")

        self.expense_manager.add_expense(expense_date, expense_name, expense_amount)

    def find_expenses_via_menu(self):
        sys.stdout.write("--------------\n")
        sys.stdout.write("Find expenses")
        sys.stdout.write("--------------\n")
        matching_expenses = self.search_and_display_matching_expenses()

    def remove_expense_via_menu(self):
        sys.stdout.write("--------------\n")
        sys.stdout.write("Remove an expense")
        sys.stdout.write("--------------\n")
        matching_expenses = self.search_and_display_matching_expenses()
        if matching_expenses is None:
            return
        num_matching_expenses = len(matching_expenses)
        i = 0
        while i < num_matching_expenses:
            self.expense_manager.remove_expense(matching_expenses)
            i += 1
        sys.stdout.write("Above matches were removed \n")

    def search_and_display_matching_expenses(self):
        if (len(self.expense_manager.expenses)) <= 0:
            sys.stdout.write("No expenses to find. Try adding expenses first.")
            return

        sys.stdout.write("Enter partial expense name to find:")
        sys.stdout.flush()
        search_target = sys.stdin.readline().strip()

        matching_expenses = self.expense_manager.get_matching_expenses(search_target)
        num_matching_expenses = len(matching_expenses)
        i = 0
        if num_matching_expenses < 0:
            sys.stdout.write("There were no expenses that matched: " + search_target + "\n")
            return

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

        total_amount = 0

        i = 0
        while i < num_matching_expenses:
            row_text = column_format.format(matching_expenses[i].date, matching_expenses[i].name,
                                            matching_expenses[i].amount)
            total_amount += matching_expenses[i].amount
            sys.stdout.write(row_text)
            i += 1

        sys.stdout.write("\n You've spent $" + str(total_amount) + " on " + str(num_matching_expenses) + " matches.\n")

        return matching_expenses


# starts our program:

home_expense_manager = ExpenseManagerUI()
home_expense_manager.run_expenses_manager()

# remove_expenses method is only a single line and this could have been done in the front end ExpenseManagerUI
# however, if we change the data structure from a list to something else,
# we might need to add more code here.
# At that time, we wouldn’t want to have to change the front end code to match;
# this small implementation detail therefore promotes looser coupling, which is desirable.

