import os
import sys
import time
import platform
from time import sleep
import subprocess
from Lesson_Templates import *


class loader:
    def loading1():
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
            sys.stdout.flush()
    
    def __init__(self, items, prefix='Progress:', suffix='Done', length=50, decimals=1, fill='█'):
        # 1. Store the list of items to iterate over
        self.items = items
        # 2. Store the total number of items as an attribute
        self.total = len(items)
        
        # 3. Store the display parameters as attributes
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.decimals = decimals
        self.fill = fill
        
        # 4. Initialize the progress bar at 0%
        self._loadbar(0) 

    def _loadbar(self, iteration):
        # Ensure we don't divide by zero if the list is empty
        if self.total == 0:
            return

        percent_value = 100 * (iteration / float(self.total))
        percent = ('{0:.' + str(self.decimals) + 'f}').format(percent_value)
        
        # Calculate the number of characters to fill the bar
        filledLength = int(self.length * iteration // self.total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        
        # Print the progress bar
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end='\r')
        
        # Print a newline when done
        if iteration == self.total:
            print()

    def run_task(self):
        # Loop through the items
        for i, item in enumerate(self.items):
            # i is 0-indexed, so we use i + 1 for the current step count (1-indexed)
            current_iteration = i + 1
            
            # --- Perform your task here ---
            # Example: Simulate work by sleeping
            time.sleep(0.1) 
            
            # 5. Call the private progress bar method with the current step
            self._loadbar(current_iteration)
        
        print("Task finished.")

class file_opener:
    def __init__(self, lesson_name, template_code, expected_output):
        self.lesson_name = lesson_name
        self.template_code = template_code
        self.expected_output = expected_output
    
    def __init__(self, lesson_name, template_code, expected_output):
        self.lesson_name = lesson_name
        self.template_code = template_code
        self.expected_output = expected_output 
        self.filename = f"{self.lesson_name}_activity.py"

    def _create_file(self):
        """Internal method to create the .py file."""
        try:
            with open(self.filename, 'w') as file:
                file.write(self.template_code)
            print(f"✅ Activity file created: **{self.filename}**")
        except Exception as e:
            print(f"Error creating file: {e}")
            raise 

    def _open_file_in_editor(self):
        """Internal method to open the file based on the OS."""
        system = platform.system()
        
        try:
            if system == "Windows":
                os.startfile(self.filename)
            elif system == "Darwin": # macOS
                os.system(f"open {self.filename}")
            elif system == "Linux":
                os.system(f"xdg-open {self.filename}")
            else:
                print(f"Warning: Could not automatically open file on {system}")
                
            print("\n👉 Please make your changes in the opened file, save it.")

        except Exception as e:
            print(f"Error opening file: {e}")

    def _run_and_grade_code(self):
        """Runs the user's code and grades the output."""
        print(f"\n--- Grading Submission for {self.filename} ---")
        
        try:
            # Execute the user's code file safely
            result = subprocess.run(
                ['python', self.filename],
                capture_output=True, 
                text=True,           
                timeout=5            
            )
        except subprocess.TimeoutExpired:
            print("❌ FAILED: Execution timed out! Check for infinite loops.")
            return

        # Check for errors (like SyntaxError)
        if result.stderr:
            print("❌ FAILED: Code Error Detected.")
            print(f"Error Details:\n{result.stderr}")
            return

        # Compare outputs
        if result.stdout.strip() == self.expected_output.strip():
            print("PASS")
            print("✅ Excellent! Your output matches the solution.")
        else:
            print("❌ FAILED: Incorrect Output.")
            print(f"Expected:\n{repr(self.expected_output.strip())}")
            print(f"Your Code Produced:\n{repr(result.stdout.strip())}")

    def start_activity_flow(self):
        """The main execution sequence for a single lesson."""
        print(f"\n--- Starting Lesson: {self.lesson_name} ---")
        self._create_file()
        self._open_file_in_editor()
        
        # Pause until the user is ready to submit
        input("\n**PRESS ENTER** when you have finished saving the file to submit for grading...")
        
        self._run_and_grade_code()


# --- Main Program Execution ---

def load_lesson(lesson_key):
    """Loads lesson data and starts the activity flow."""
    lesson_data = LESSONS.get(lesson_key)
    
    if not lesson_data:
        print(f"Error: Lesson '{lesson_key}' not found in templates.")
        return

    # Create the file_opener instance with imported data
    activity = file_opener(
        lesson_name=lesson_key,
        template_code=lesson_data["code"],
        expected_output=lesson_data["expected"]
    )
    activity.start_activity_flow()

def Main_Menu():
    while True:
        print("\n--- Welcome to the Code Lesson Compiler ---")
        print('----------------------------------------------')
        print('Seleact a lesson to begin:')
        print("1. Printing")
        print("2. Variables")
        print("3. Loops")
        print("4. Conditionals")
        print("5. Functions")
        print('6. Lists')
        print('7. Others')
        print('0. Exit')
        print('----------------------------------------------')
        choice = input("Enter your choice: ")
        if choice == '1':
            submenu.printing_menu()
        elif choice == '2':
            submenu.variables_menu()
        elif choice == '3':
            submenu.loops_menu()
        elif choice == '4':
            submenu.conditionals_menu()
        elif choice == '5':
            submenu.functions_menu()
        elif choice == '6':
            submenu.lists_menu()
        elif choice == '7':
            pass
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# printing lessson examples
def basic_printing():
    print('--- Example of basic printing ---')
    print('---------------------------------')
    print("print('Hello World!')")
    print("print('Welcome to ITCS 102!')")
    print("print('Python is fun!')")
    print('Output:')
    print("Hello World!")
    print("Welcome to ITCS 102!")
    print("Python is fun!")
    print('---------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def string_formatting():
    print('--- Example of string formatting ---')
    print('------------------------------------------------------')
    print("name = 'Bob'")
    print("age = 25")
    print("info = f'My name is {name} and I am {age} years old.'")
    print("print(info)")
    print('Output:')
    name = 'Bob'
    age = 25
    info = f'My name is {name} and I am {age} years old.'
    print(info)
    print('------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

# Variable lesson examples
def string_concatenation_with_variables():
    print('--- Example of string concatenation with variables ---')
    print('------------------------------------------------------')
    print("first_name = 'Alice'")
    print("last_name = 'Smith'")
    print("full_name = first_name + ' ' + last_name")
    print("print(full_name)")
    print('Output:')
    first_name = 'Alice'
    last_name = 'Smith'
    full_name = first_name + ' ' + last_name
    print(full_name)
    print('------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def variable_assignment():
    print('------------- Example of variable assignment -------------')
    print('----------------------------------------------------------')
    print("# Assign the result of 7 + 3 to a variable named 'answer'")
    print("answer = 7 + 3")
    print("print(answer)")
    print('Output:')
    answer = 7 + 3
    print(answer)
    print('----------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def tuple():
    print('---------------- Example of tuple -----------------')
    print('---------------------------------------------------')
    print('fruits = ("apple", "orange", "grapes", "cherry")')
    print('print(fruits)')
    print('Output:')
    fruits = ("apple", "orange", "grapes", "cherry")
    print(fruits)
    print('---------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

#Loops Example
def for_loop():
    print("----------- Example of a For Loop -----------")
    print('---------------------------------------------')
    print('for i in range(5): # This will output 1  to 4')
    print("\tprint('i')")
    print('Output:')
    for i in range(5): # This will output 1 to 4
        print (i)
    print('---------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def while_loop():
    print('----------- Example of a While Loop -----------')
    print('-----------------------------------------------')
    print('clothes = True')
    print('while clothes == True:')
    print('\tisDirty = input("Is the clothes clean? (yes/no): ").lower()')
    print("\tif isDirty == 'no':")
    print('\t\tprint("Washing Continues")')
    print('\t\tcontinue')
    print('\telse:')
    print('\t\tprint("Your clothes is clean")')
    print('\t\tbreak')
    print('Output:')
    clothes = True

    while clothes == True:
        isDirty = input("Is the clothes clean? (yes/no): ").lower()
        if isDirty == 'no':
            print("Washing Continues")
            continue
        else:
            print("Your clothes is clean")
            break
    print('---------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def nested_for_loop():
    print('----------- Example of a Nested For Loop -----------')
    print('----------------------------------------------------')
    print('adj = ["red", "big", "tasty"]')
    print('fruits = ["apple", "banana", "cherry"]')
    print('for x in adj:')
    print('\tfor y in fruits:')
    print('\t\tprint(x, y)')
    print('Output:')
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
        for y in fruits:
            print(x, y)
    print('----------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def nested_while_loop():
    print('-------------- Example of a Nested While Loop ---------------')
    print('-------------------------------------------------------------')
    print('# Initialize the outer loop counter (rows)\
        \ni = 1\
        \n# Outer while loop (runs as long as i is less than or equal to 3)\
        \nwhile i <= 3:\
        \n\t# Initialize the inner loop counter (columns)\
        \n\tj = 1\
        \n\t# Inner while loop (runs as long as j is less than or equal to 3)\
        \n\twhile j <= 3:\
        \n\t# Print the current row and column number, formatted\
        \n\t\tprint("Row {i}, Col {j}", end=" | ")\
        \n\t# Increment the inner loop counter\
        \n\tj += 1\
        \n# After the inner loop finishes, print a new line for the next row\
        \n print("\n")\
        \n# Increment the outer loop counter\
        \ni += 1')
    print('Output:')
    # Initialize the outer loop counter (rows)
    i = 1
    # Outer while loop (runs as long as i is less than or equal to 3)
    while i <= 3:
        # Initialize the inner loop counter (columns)
        j = 1
        # Inner while loop (runs as long as j is less than or equal to 3)
        while j <= 3:
        # Print the current row and column number, formatted
            print(f"Row {i}, Col {j}", end=" | ")
        # Increment the inner loop counter
        j += 1
    # After the inner loop finishes, print a new line for the next row
    print("\n")
    # Increment the outer loop counter
    i += 1
    print('-------------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

#Conditional statement Examples
def simple_condi_statements():
    print('--- Example of simple conditional statements ---')
    print('------------------------------------------------')
    print('num = int(input("Enter a number: "))')
    print('if num > 0:')
    print('    print("The number is positive.")')
    print('else:')
    print('    print("The number is not positive.")')
    print('Output:')
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    else:
        print("The number is not positive.")
    print('------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def logical_condi_statements():
    print('--- Example of logical conditional statements ---')
    print('-------------------------------------------------')
    print("score = int(input('Enter your score here: '))")
    print('if score >= 90:')
    print("\tprint('Grade: A')")
    print('elif score >= 80:')
    print("\tprint('Grade B:')")
    print('elif score >= 70:')
    print("\tprint('Grade: C')")
    print('else:')
    print("\tprint('Grade: F')")
    print('Output:')
    score = int(input('Enter your score here: '))

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
    print('-------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def nested_condi_statement():
    print('--- Example of nested conditional statements ---')
    print('------------------------------------------------')
    print('age = int(input("Enter your age:"))')
    print("has_license = input('Do you have a license(Y/N)')")
    print('if age >= 18:')
    print("\tif has_license == 'Y'")
    print("\t\tprint('Eligible to drive')")
    print("\telse:")
    print("\t\tprint('Not eligible to drive')")
    print('else:')
    print("\tprint('Not old enough to drive')")
    print('Output')
    age = int(input('enter age:'))
    has_license = input('Do you have a license(Y/N)')
    if age >= 18:
        if has_license == 'Y':
            print("Eligible to drive")
        else:
            print("Not eligible to drive without a license")
    else:
        print("Not old enough to drive")
    print('------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

#Functions Example
def function_example():
    print('------ Def function Example ------')
    print('----------------------------------')
    print('def greet_person(name):')
    print('\tprint(f"hello,{name}!!")')
    print()
    print('name = input("Enter your name: ")')
    print('greet_person(name)')
    
    print('Output:')
    
    def greet_person(name):
        print(f'hello,{name}!!')
    
    name = input('Enter your name here: ')
    greet_person(name)
    print('------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

#List
def list_example():
    print('------------ List Example ------------')
    print('--------------------------------------')
    print('cars = ["audi","ferrari", "mclaren" ]')
    print('print(cars)')
    print()
    print('Output')
    cars = ["audi","ferrari", "mclaren" ]
    print(cars)
    print('---------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def editing_lists():
    print('----------------------- Editing list -----------------------')
    print('------------------------------------------------------------')
    print('months = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]')
    print('months[1] = "february" # changes the element at index 1 ')
    print('print(months)')
    print('months.append("aug") #adds elements to the end of the list')
    print('print(months)')
    print('months.pop() #removes the last element')
    print('print(months)')
    print('list = len(months) #determines how many items within the list')
    print('print("Length of list:", list) ')
    print('months.sort() # sorts the list from low to high')
    print('print("Sorted list:", months)')
    print()
    print('Output:')
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]
    print(months)

    months[1] = 'february'
    print(months)


    months.append("aug")
    print(months)


    months.pop()
    print(months)

    months.remove("mar")
    print(months)

    months.insert(4, "new")
    print(months)

    list = len(months)
    print("Length of list:", list)

    months.sort()
    print("Sorted list:", months)
    print('------------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

#arithmetic example
def operators_example():
    print('------------- Arithmetric Operators -------------')
    print('-------------------------------------------------')
    print('a = input("Put any number here: ")')
    print('b = input("Put any number here: ")')
    print()
    print('print(f"Addition: {a + b}")')
    print('print(f"Subtraction: {a - b}")')
    print('print(f"Multiplication: {a * b}")')
    print('print(f"Division: {a / b}")')
    print('print(f"Modulus: {a % b}")')
    print('print(f"Exponentiation: {a ** b}")')
    print()
    print('Output:')
    a = input("Put any number here: ") 
    b = input("Put any number here: ")
    print()
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Modulus: {a % b}")
    print(f"Exponentiation: {a ** b}")
    print('-------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def temperatures():
    print('------------------------------ Temperature ------------------------------')
    print('-------------------------------------------------------------------------')
    print('F = float(input("Enter Temperature in FARENHEIT: "))')
    print("C = ((F - 32)*5)/9")
    print("round(C,2)")
    print('print(f"{F} degrees in Farenheit converted to Celsius is {C}")')
    print('C = eval(input("Enter Temperature in CELSIUS: "))')
    print("F = (C * 9/5) + 32")
    print('print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")')
    print()
    print("Output:")
    F = float(input("Enter Temperature in FARENHEIT: "))
    C = ((F - 32) * 5) / 9
    round(C, 2)

    print(f"{F} degrees in Farenheit converted to Celsius is {C}")

    C = eval(input("Enter Temperature in CELSIUS: "))
    F = (C * 9 / 5) + 32

    print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")
    print('------------------------------------------------------------------------')
    clear = input('Press ENTER to return to the Main Menu...')

def temp_calc():
    print("--------- Simple Calculator ---------")
    print("-------------------------------------")
    print(" 1. Temperature Conversion")
    print(" 2. Arithmetic Operations")
    print("-------------------------------------")
    choice = input("Enter your choice: ")
    os.system("cls")

    if choice == "1":
        print("------- Temperature Conversion -------")
        print("--------------------------------------")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("--------------------------------------")
        temp_choice = input("Enter your choice: ")

        if temp_choice == "1":
            print('------------ Fahrenheit to Celsius Conversion ------------')
            print("----------------------------------------------------------")
            F = eval(input("Enter Temperature in Fahrenheit: "))
            C = ((F - 32) * 5) / 9
            print(f"{F} degrees Fahrenheit is {round(C, 2)} degrees Celsius.")
            print("----------------------------------------------------------")
            clear = input('Press ENTER to return to the Main Menu...')
            os.system("cls")

        elif temp_choice == "2":
            print('------------- Celsius to Fahrenheit Conversion -------------')
            print("------------------------------------------------------------")
            C = eval(input("Enter Temperature in Celsius: "))
            F = (C * 9 / 5) + 32
            print(f"{C} degrees Celsius is {round(F, 2)} degrees Fahrenheit.")
            print("------------------------------------------------------------")
            clear = input('Press ENTER to return to the Main Menu...')
            os.system("cls")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    elif choice == "2":
        print("------- Arithmetic Operations -------")
        print("-------------------------------------")
        print(" 1. Add")
        print(" 2. Subtract")
        print(" 3. Multiply")
        print(" 4. Divide")
        print("-------------------------------------")
        operation_choice = input("Enter your choice: ")

        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))

        if operation_choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            clear = input('Press ENTER to return to the Main Menu...')
            os.system("cls")

        elif operation_choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            clear = input('Press ENTER to return to the Main Menu...')
            os.system("cls")

        elif operation_choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            clear = input('Press ENTER to return to the Main Menu...')
            os.system("cls")

        elif operation_choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                clear = input('Press ENTER to return to the Main Menu...')
                os.system("cls")
            else:
                print("Error! Division by zero is not allowed.")
                clear = input('Press ENTER to return to the Main Menu...')
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
            clear = input('Press ENTER to return to the Main Menu...')
    else:
        print("Invalid input! Please enter 1 or 2.")
        clear = input('Press ENTER to return to the Main Menu...')

class submenu:
    def printing_menu():
        while True:
            print('--------------------------------- Printing Menu -----------------------------------')
            print('-----------------------------------------------------------------------------------')
            print()
            print(' In Python, print() is a built-in function used to display\
                    \noutput to the console (standard output device). \
                    \nIt is a fundamental tool for programmers to show text messages, \
                    \nvariable values or the results of operations during program execution or debugging.')
            print()
            print('------------------------------------------------------------------------------------')
            print('1. Basic Printing')
            print('2. String Formatting')
            print('3. Lesson Activity')
            print('0. Return to Main Menu')
            print('------------------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            os.system('cls')
            if choice == '1':
                basic_printing()
            elif choice == '2':
                string_formatting()
            elif choice == '3':
                # Let the user choose which printing lesson to load
                print('\nSelect a printing lesson activity:')
                print('1. Basic')
                print('2. Formatting')
                subchoice = input('Enter your choice: ')
                if subchoice == '1':
                    load_lesson("Printing - Basic")
                elif subchoice == '2':
                    load_lesson("Printing - Formatting")
                else:
                    print('Invalid printing lesson choice.')
            elif choice == '0':
                break
            else:
                print('Invalid choice. Please try again.')
    
    def variables_menu():
        print('------------------------------- Variables Menu -----------------------------------')
        print('----------------------------------------------------------------------------------')
        print()
        print(' Variables in Python are used to store data values. \
                \nThey act as containers for data that can be referenced and manipulated throughout a program. \
                \nVariables are created by assigning a value to a name using the equals sign (=). \
                \nThe value can be of various data types, such as integers, floats, strings, lists, etc.')
        print()
        print('----------------------------------------------------------------------------------')
        print('1. String Concatenation with Variables')
        print('2. Variable Assignment')
        print('3. Lesson Activity')
        print('0. Return to Main Menu')
        print('----------------------------------------------------------------------------------')
        choice = input('Enter your choice: ')
        os.system('cls')
        if choice == '1':
            string_concatenation_with_variables()
        elif choice == '2':
            variable_assignment()
        elif choice == '3':
            # Let the user choose which variable lesson to load
            print('\nSelect a variable lesson activity:')
            print('1. String Concatenation')
            print('2. Assignment')
            subchoice = input('Enter your choice: ')
            if subchoice == '1':
                load_lesson("Variables - String Concatenation")
            elif subchoice == '2':
                load_lesson("Variables - Assignment")
            else:
                print('Invalid variable lesson choice.')
        elif choice == '0':
            return
        else:
            print('Invalid choice. Please try again.')
    
    def loops_menu():
        print('-------------------------------- Loops Menu -----------------------------------')
        print('-------------------------------------------------------------------------------')
        print()
        print(' Loops in Python are used to execute a block of code repeatedly for a specified number of times or while a certain condition is met. \
                \nThey help automate repetitive tasks and iterate over sequences like lists, tuples, or strings. \
                \nThe two main types of loops in Python are for loops and while loops.')
        print()
        print('-------------------------------------------------------------------------------')
        print('1. For Loop')
        print('2. While Loop')
        print('3. Nested Loops')
        print('4. Lesson Activity')
        print('0. Return to Main Menu')
        print('-------------------------------------------------------------------------------')
        choice = input('Enter your choice: ')
        os.system('cls')
        if choice == '1':
            for_loop()
        elif choice == '2':
            while_loop()
        elif choice == '3':
            print('--- Nested Loops Menu ---')
            print('1. Nested For Loop')
            print('2. Nested While Loop')
            nested_loop_choice = input('Enter your choice: ')
            if nested_loop_choice == '1':
                nested_for_loop()
            elif nested_loop_choice == '2':
                nested_while_loop()
            else:
                print('Invalid nested loop choice.')
        elif choice == '4':
            # Let the user choose which loop lesson to load
            print('\nSelect a loop lesson activity:')
            print('1. For Loop')
            print('2. While Loop')
            print('3. Nested For Loop')
            print('4. Nested While Loop')
            print('0. Return to Loops Menu')
            subchoice = input('Enter your choice: ')
            if subchoice == '1':
                load_lesson("Loops - For Loop")
            elif subchoice == '2':
                load_lesson("Loops - While Loop")
            elif subchoice == '3':
                load_lesson("Loops - Nested For Loop")
            elif subchoice == '4':
                load_lesson("Loops - Nested While Loop")
            else:
                print('Invalid loop lesson choice.')
        elif choice == '0':
            return
        else:
            print('Invalid choice. Please try again.')
    
    def conditionals_menu():
        print('----------------------------- Conditionals Menu ------------------------------')
        print('-------------------------------------------------------------------------------')
        print()
        print(' Conditional statements in Python are used to perform different actions based on whether a certain condition is true or false. \
                \nThey allow for decision-making in code, enabling the program to execute specific blocks of code depending on the evaluation of conditions. \
                \nThe main conditional statements in Python are if, elif (else if), and else.')
        print()
        print('-------------------------------------------------------------------------------')
        print('1. Simple Conditional Statements')
        print('2. Logical Conditional Statements')
        print('3. Nested Conditional Statements')
        print('4. Lesson Activity')
        print('0. Return to Main Menu')
        print('-------------------------------------------------------------------------------')
        choice = input('Enter your choice: ')
        os.system('cls')
        if choice == '1':
            simple_condi_statements()
        elif choice == '2':
            logical_condi_statements()
        elif choice == '3':
            nested_condi_statement()
        elif choice == '4':
            # Let the user choose which conditional lesson to load
            print('\nSelect a conditional lesson activity:')
            print('1. Simple If-Else')
            print('2. If-Elif-Else')
            print('3. Nested If Statements')
            subchoice = input('Enter your choice: ')
            if subchoice == '1':
                load_lesson("Conditionals - Simple If")
            elif subchoice == '2':
                load_lesson("Conditionals - If-Elif-Else")
            elif subchoice == '3':
                load_lesson("Conditionals - Nested If")
            else:
                print('Invalid conditional lesson choice.')
        elif choice == '0':
            return
        else:
            print('Invalid choice. Please try again.')
    
    def functions_menu():
        print('----------------------------- Functions Menu ------------------------------')
        print('---------------------------------------------------------------------------')
        print()
        print(' Functions in Python are reusable blocks of code that perform a specific task. \
                \nThey help organize code, improve readability, and allow for code reuse. \
                \nFunctions are defined using the def keyword, followed by the function name and parentheses. \
                \nThey can take input parameters and return output values.')
        print()
        print('---------------------------------------------------------------------------')
        print('1. Function Example')
        print('2. Lesson Activity')
        print('0. Return to Main Menu')
        print('---------------------------------------------------------------------------')
        choice = input('Enter your choice: ')
        os.system('cls')
        if choice == '1':
            function_example()
        elif choice == '2':
            # Let the user choose which function lesson to load
            print('\nSelect a function lesson activity:')
            print('1. Basic Function')
            subchoice = input('Enter your choice: ')
            if subchoice == '1':
                load_lesson("Functions - Basic Function")
            else:
                print('Invalid function lesson choice.')
        elif choice == '0':
            return
        else:
            print('Invalid choice. Please try again.')
    def lists_menu():
        print('------------------------------- Lists Menu -------------------------------')
        print('-------------------------------------------------------------------------')
        print()
        print(' Lists in Python are ordered collections of items that can hold multiple values in a single variable. \
                \nThey are mutable, meaning their contents can be changed after creation. \
                \nLists can contain elements of different data types, including numbers, strings, and even other lists. \
                \nThey are defined using square brackets [].')
        print()
        print('-------------------------------------------------------------------------')
        print('1. List Example')
        print('2. Editing Lists')
        print('3. Lesson Activity')
        print('0. Return to Main Menu')
        print('-------------------------------------------------------------------------')
        choice = input('Enter your choice: ')
        os.system('cls')
        if choice == '1':
            list_example()
        elif choice == '2':
            editing_lists()
        elif choice == '3':
            # Let the user choose which list lesson to load
            print('\nSelect a list lesson activity:')
            print('1. Basic List')
            print('2. Editing Lists')
            subchoice = input('Enter your choice: ')
            if subchoice == '1':
                load_lesson("Lists - Basic")
            elif subchoice == '2':
                load_lesson("Lists - Editing")
            else:
                print('Invalid list lesson choice.')
        elif choice == '0':
            return
        else:
            print('Invalid choice. Please try again.')
        
Main_Menu()