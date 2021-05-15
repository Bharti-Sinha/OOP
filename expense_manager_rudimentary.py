# variables date, name and value are default or uninitialized values
# values that were declared when the variables were first created
# that all objects default to unless another value is given.


class Expense:
    date = "YYYY-MM-DD"
    name = None
    value = 0

e1 = Expense()
print("Expense e1 has: ")
print(e1.date)
print(e1.name)
print(e1.value)

print()

e2 = Expense()
print("Expense e2 has: ")
print(e2.date)
print(e2.name)
print(e2.value)
