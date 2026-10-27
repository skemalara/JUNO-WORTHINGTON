"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a string of words that says "Welcome to my Python exercises"
# 2. Process: The program takes the input and suggests a loop of 5 iterations that I can accept or ignore to print the string. 
# 3. Out: The string is printed once and suggested 5 times. Then to change printing from 5 times to 3 times, I tried to change the range from 1, 5 to 1, 3. 
# 4. My message, and why: This message reflects the class, what is happening and is simple. 


# Your code below

print("Welcome to my Python exercises.")
print("Welcome to my Python exercises.")
print("Welcome to my Python exercises.")
print("Welcome to my Python exercises.")
print("Welcome to my Python exercises.")

for number in range (1, 3):
    print(f"{number}. Welcome to my Python exercises."
)

print("Welcome to my Python exercises."
      )

print("Hello, world!")
print("1. Hello, world!")
print("3. Hello, world!")print("4. Hello, world!")  

for i in range (0,5): 
    print("Welcome, let's keep going")
