"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers entered by the user.
# 2. Process: Convert the inputs to numbers, then add, subtract, multiply, and divide.
# 3. Out: Display the results of those four operations.
# 4. If the second number is zero, display a message instead of dividing by zero.
#    Addition, subtraction, and multiplication are still displayed.
#
# Python's / operator performs true division, so 7 / 2 is 3.5. The // operator
# would perform floor division and give 3 for these positive numbers.


# Your code below
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number == 0:
    print("Division: cannot divide by zero.")
else:
    print("Division:", first_number / second_number)
