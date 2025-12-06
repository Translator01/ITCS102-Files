# templates.py

# --- LESSON 1: PRINTING - BASIC ---
PRINTING_BASIC_CODE = """
# Lesson: Basic Printing
# Task: Write three print() statements to output:
#   "Hello World!"
#   "Welcome to ITCS 102!"
#   "Python is fun!"

# TODO: Write your print statements here
"""
PRINTING_BASIC_EXPECTED = "Hello World!\nWelcome to ITCS 102!\nPython is fun!\n"

# --- LESSON 2: PRINTING - STRING FORMATTING ---
PRINTING_FORMAT_CODE = """
# Lesson: String Formatting
# Task: Create variables for name and age, then use an f-string
# to print: "My name is {name} and I am {age} years old."
# Example name: 'Bob', age: 25

# TODO: Create variables and use f-string formatting
"""
PRINTING_FORMAT_EXPECTED = "My name is Bob and I am 25 years old.\n"

# --- LESSON 3: VARIABLES - STRING CONCATENATION ---
VAR_CONCAT_CODE = """
# Lesson: String Concatenation with Variables
# Task: Concatenate first_name and last_name with a space between them
# Example: first_name = 'Alice', last_name = 'Smith'
# Output should be: Alice Smith

# TODO: Create the variables and concatenate them
"""
VAR_CONCAT_EXPECTED = "Alice Smith\n"

# --- LESSON 4: VARIABLES - ASSIGNMENT ---
VAR_ASSIGN_CODE = """
# Lesson: Variables and Assignment
# Task: Create a variable 'answer' and assign it the result of 10 * 5
# Then print the answer

# TODO: Create the variable and assign the calculation
"""
VAR_ASSIGN_EXPECTED = "50\n"

# --- LESSON 5: DATA TYPES - TUPLE ---
TUPLE_CODE = """
# Lesson: Tuples
# Task: Create a tuple containing four fruit names: apple, orange, grapes, cherry
# Then print the tuple

# TODO: Create and print the tuple
"""
TUPLE_EXPECTED = "('apple', 'orange', 'grapes', 'cherry')\n"

# --- LESSON 6: LOOPS - FOR LOOP ---
FOR_LOOP_CODE = """
# Lesson: For Loops
# Task: Write a for loop using range() to print numbers from 0 to 4

# TODO: Write the for loop
"""
FOR_LOOP_EXPECTED = "0\n1\n2\n3\n4\n"

# --- LESSON 6b: LOOPS - WHILE LOOP ---
WHILE_LOOP_CODE = """
# Lesson: While Loops
# Task: Use a while loop to print the numbers 0, 1, 2 (one per line).

# TODO: Implement the while loop that prints 0 then 1 then 2
"""
WHILE_LOOP_EXPECTED = "0\n1\n2\n"

# --- LESSON 7: LOOPS - NESTED FOR LOOP ---
NESTED_FOR_CODE = """
# Lesson: Nested For Loops
# Task: Use nested for loops to print all combinations of:
#   adj = ["red", "big", "tasty"]
#   fruits = ["apple", "banana", "cherry"]
# Print each adjective with each fruit (e.g., "red apple")

# TODO: Create the nested loop structure
"""
NESTED_FOR_EXPECTED = "red apple\nred banana\nred cherry\nbig apple\nbig banana\nbig cherry\ntasty apple\ntasty banana\ntasty cherry\n"

# --- LESSON 7b: LOOPS - NESTED WHILE LOOP ---
NESTED_WHILE_CODE = """
# Lesson: Nested While Loops
# Task: Use nested while loops to print rows and columns for a 3x3 grid.
# Each cell should be printed in the format: Row X, Col Y (separated by a space or newline).

# TODO: Implement nested while loops to output a 3x3 set of row/col labels
"""
# Expected output for a simple 3x3 nested while (one cell per line):
NESTED_WHILE_EXPECTED = (
    "Row 1, Col 1\nRow 1, Col 2\nRow 1, Col 3\n"
    "Row 2, Col 1\nRow 2, Col 2\nRow 2, Col 3\n"
    "Row 3, Col 1\nRow 3, Col 2\nRow 3, Col 3\n"
)

# --- LESSON 8: CONDITIONALS - SIMPLE IF ---
SIMPLE_IF_CODE = """
# Lesson: Simple Conditional Statements
# Task: Write an if-else statement to check if num > 0
# If true, print "The number is positive."
# If false, print "The number is not positive."
# Use num = 5

# TODO: Write the if-else statement
"""
SIMPLE_IF_EXPECTED = "The number is positive.\n"

# --- LESSON 9: CONDITIONALS - IF-ELIF-ELSE ---
GRADE_IF_CODE = """
# Lesson: Grading with If-Elif-Else
# Task: Write an if-elif-else statement to determine grade based on score:
#   90 or above = "Grade: A"
#   80 to 89 = "Grade: B"
#   70 to 79 = "Grade: C"
#   Below 70 = "Grade: F"
# Use score = 95

# TODO: Write the if-elif-else structure
"""
GRADE_IF_EXPECTED = "Grade: A\n"

# --- LESSON 10: FUNCTIONS - BASIC ---
FUNCTION_CODE = """
# Lesson: Basic Functions
# Task: Define a function called greet_person that takes a name parameter
# and prints "hello, {name}!!"
# Then call the function with "Alice" as the argument

# TODO: Define the function and call it
"""
FUNCTION_EXPECTED = "hello, Alice!!\n"

# --- LESSON 11: LISTS - BASIC ---
LIST_CODE = """
# Lesson: Lists
# Task: Create a list containing three car names: audi, ferrari, mclaren
# Then print the list

# TODO: Create and print the list
"""
LIST_EXPECTED = "['audi', 'ferrari', 'mclaren']\n"

# --- LESSON 12: LISTS - EDITING ---
LIST_EDIT_CODE = """
# Lesson: Editing Lists
# Task: Start with this list:
#   months = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]
# Then:
#   1. Change index 1 to "february"
#   2. Add "aug" to the end
#   3. Print the length of the modified list

# TODO: Perform the list operations and print the length
"""
LIST_EDIT_EXPECTED = "8\n"

# --- LESSON 13: OPERATORS - ARITHMETIC ---
OPERATORS_CODE = """
# Lesson: Arithmetic Operators
# Task: Create two variables a = 10 and b = 3
# Then print the results of:
#   Addition (a + b)
#   Subtraction (a - b)
#   Multiplication (a * b)
# Format: "Addition: 13" etc.

# TODO: Create variables and print arithmetic operations
"""
OPERATORS_EXPECTED = "Addition: 13\nSubtraction: 7\nMultiplication: 30\n"

# --- LESSON 14: TEMPERATURE CONVERSION ---
TEMP_CODE = """
# Lesson: Temperature Conversion
# Task: Convert Fahrenheit to Celsius using this formula:
#   C = ((F - 32) * 5) / 9
# Use F = 32 and print the result formatted as:
#   "{F} degrees Fahrenheit is {C} degrees Celsius."
# Round C to 2 decimal places

# TODO: Implement the temperature conversion
"""
TEMP_EXPECTED = "32 degrees Fahrenheit is 0.0 degrees Celsius.\n"

# Central Dictionary to hold all lesson data
LESSONS = {
    "Printing - Basic": {
        "code": PRINTING_BASIC_CODE,
        "expected": PRINTING_BASIC_EXPECTED
    },
    "Printing - Formatting": {
        "code": PRINTING_FORMAT_CODE,
        "expected": PRINTING_FORMAT_EXPECTED
    },
    "Variables - Concatenation": {
        "code": VAR_CONCAT_CODE,
        "expected": VAR_CONCAT_EXPECTED
    },
    "Variables - Assignment": {
        "code": VAR_ASSIGN_CODE,
        "expected": VAR_ASSIGN_EXPECTED
    },
    "Data Types - Tuple": {
        "code": TUPLE_CODE,
        "expected": TUPLE_EXPECTED
    },
    "Loops - For": {
        "code": FOR_LOOP_CODE,
        "expected": FOR_LOOP_EXPECTED
    },
    "Loops - While": {
        "code": WHILE_LOOP_CODE,
        "expected": WHILE_LOOP_EXPECTED
    },
    "Loops - Nested For": {
        "code": NESTED_FOR_CODE,
        "expected": NESTED_FOR_EXPECTED
    },
    "Loops - Nested While": {
        "code": NESTED_WHILE_CODE,
        "expected": NESTED_WHILE_EXPECTED
    },
    "Conditionals - Simple": {
        "code": SIMPLE_IF_CODE,
        "expected": SIMPLE_IF_EXPECTED
    },
    "Conditionals - Grade": {
        "code": GRADE_IF_CODE,
        "expected": GRADE_IF_EXPECTED
    },
    "Functions - Basic": {
        "code": FUNCTION_CODE,
        "expected": FUNCTION_EXPECTED
    },
    "Lists - Basic": {
        "code": LIST_CODE,
        "expected": LIST_EXPECTED
    },
    "Lists - Editing": {
        "code": LIST_EDIT_CODE,
        "expected": LIST_EDIT_EXPECTED
    },
    "Operators - Arithmetic": {
        "code": OPERATORS_CODE,
        "expected": OPERATORS_EXPECTED
    },
    "Temperature - Conversion": {
        "code": TEMP_CODE,
        "expected": TEMP_EXPECTED
    }
}
