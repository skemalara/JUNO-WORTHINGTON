"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Eight example monthly marketing campaign budgets, in euros.
# 2. Process: Store the budgets in a list, sort a copy, and calculate their average.
# 3. Out: The complete list, one chosen budget, the sorted budgets, and the average.
# 4. The list is about monthly campaign budgets. The average shows the typical
#    monthly spend across the example campaigns.


# Your code below
# Store eight example monthly campaign budgets as whole euros (int values).
monthly_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2200, 2000]

# Display the list and the third budget; list positions start at zero.
print("Monthly budgets (EUR):", monthly_budgets)
print("Third budget (EUR):", monthly_budgets[2])

# sorted() creates an ascending copy and leaves monthly_budgets unchanged.
sorted_budgets = sorted(monthly_budgets)
print("Budgets in ascending order (EUR):", sorted_budgets)

# Divide the total by the number of budgets to calculate their average.
average_budget = sum(monthly_budgets) / len(monthly_budgets)
print(f"Average monthly budget: {average_budget:.2f} EUR")

# Hand check: the first three budgets average (1200 + 2500 + 1800) / 3 = 1833.33 EUR.
