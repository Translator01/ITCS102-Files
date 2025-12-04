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

    # Create the LessonActivity instance with imported data
    activity = LessonActivity(
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
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
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
    print('--- Temperature Calculator ---')
    print('------------------------------')
    