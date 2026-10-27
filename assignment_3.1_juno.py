"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A whole number N entered by the user.
# 2. Process: Count from 1 to N and use the remainder after division by 2 to
#    determine whether each number is odd or even.
# 3. Out: Each number from 1 to N, labelled odd or even.
# 4. If N is 0 or negative, display a message that N must be at least 1.
#    If N is greater than 100 (including 5000), display a message instead of
#    printing too many lines.


# Your code below
number_limit = int(input("Enter a whole number from 1 to 100: "))

if number_limit < 1:
    print("Please enter a number that is at least 1.")
elif number_limit > 100:
    print("Please enter a number no greater than 100.")
else:
    for number in range(1, number_limit + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
