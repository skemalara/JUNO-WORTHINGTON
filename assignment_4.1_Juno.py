"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The same eight example monthly campaign budgets from exercise 4.0.
# 2. Process: Display the original order, an ascending copy, a reversed copy, and
#    then sort the original list in place before restoring it from a saved copy.
# 3. Out: Four budget orders, followed by the unchanged original list.
# 4. I chose original order, ascending, reversed original order, and descending.
#    sorted() and slicing make copies; sort(reverse=True) changes the original list.
#    I restore the original order from a saved copy before the final display.


# Your code below
# Reuse the same eight example monthly campaign budgets from exercise 4.0.
monthly_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2200, 2000]

# Save a copy so the exact starting order can be restored after the in-place sort.
original_budgets = monthly_budgets.copy()

# Show the original order before making any changes.
print("Original order (EUR):", original_budgets)

# sorted() returns a new ascending list and leaves monthly_budgets untouched.
ascending_budgets = sorted(monthly_budgets)
print("Ascending order (EUR):", ascending_budgets)

# A reversed slice is another new list, so it does not reorder monthly_budgets.
reversed_budgets = monthly_budgets[::-1]
print("Reverse of original order (EUR):", reversed_budgets)

# sort() changes monthly_budgets itself, so this displays its descending order.
monthly_budgets.sort(reverse=True)
print("Descending order (in-place) (EUR):", monthly_budgets)

# Restore the exact starting order from the saved copy after demonstrating sort().
monthly_budgets[:] = original_budgets

# The final line displays the original list for comparison with exercise 4.0.
print("Original list, restored (EUR):", monthly_budgets)
