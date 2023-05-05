In computer programming, we use the if statement to run a block code only when a certain condition is met.

For example, assigning grades (A, B, C) based on marks obtained by a student.

if the percentage is above 90, assign grade A
if the percentage is above 75, assign grade B
if the percentage is above 65, assign grade C
In Python, there are three forms of the if...else statement.

if statement
if...else statement
if...elif...else statement
1. Python if statement
The syntax of if statement in Python is:

if condition:
    # body of if statement
The if statement evaluates condition.

If condition is evaluated to True, the code inside the body of if is executed.
If condition is evaluated to False, the code inside the body of if is skipped.
How if statement works in Python
Working of if Statement
Example 1: Python if Statement
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')
Run Code
Output

Number is positive.
The if statement is easy
In the above example, we have created a variable named number. Notice the test condition,

number > 0
Here, since number is greater than 0, the condition evaluates True.

If we change the value of variable to a negative integer. Let's say -5.

number = -5
Now, when we run the program, the output will be:

The if statement is easy
