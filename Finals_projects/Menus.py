import os
import sys
import time
import platform
from time import sleep
import subprocess
import json
import hashlib
from Lesson_Templates import *
import textwrap

# --- Simple user system (stores users in users.json) ---
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')


def load_users():
    """Load users from disk.

    Returns a dictionary mapping username -> record. If the users file
    does not exist or cannot be read, returns an empty dict. This keeps
    runtime code simple by allowing callers to treat `users` as a
    dictionary even on first run.
    """
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception:
        return {}


def save_users(data):
    """Persist the `users` mapping to disk.

    Uses UTF-8 and pretty-prints JSON. Errors are printed but not
    raised to avoid crashing the interactive menu on a save failure.
    """
    try:
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving users: {e}")


def hash_password(password, salt=None):
    """Create a salted SHA-256 hash of `password`.

    If `salt` is None a new random salt is generated. The function
    returns a tuple `(salt, digest)` where `salt` is stored with the
    user and `digest` is compared during login.
    """
    if salt is None:
        salt = os.urandom(16).hex()
    digest = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()
    return salt, digest


# Global in-memory users and session
users = load_users()
current_user = None


def clear_screen():
    """Cross-platform console clear."""
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        # If clear fails for any reason, ignore to avoid crashing the menu
        pass


def safe_int_input(prompt):
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def safe_float_input(prompt):
    """Prompt until the user enters a valid float (or integer)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (e.g., 3.14).")


def create_user():
    global users
    """Interactive account creation.

    Prompts for username and password, performs simple validation,
    hashes the password using `hash_password` and saves the record to
    disk with `save_users`.
    """
    print('\n--- Create New User ---')
    username = input('Enter a username: ').strip()
    if not username:
        print('Username cannot be empty.')
        return
    if username in users:
        print('That username already exists.')
        return
    pwd = input('Enter password: ')
    pwd2 = input('Confirm password: ')
    if pwd != pwd2:
        print('Passwords do not match.')
        return
    salt, hashed = hash_password(pwd)
    users[username] = {'salt': salt, 'password': hashed, 'profile': {}}
    save_users(users)
    # Print only the created username (minimal confirmation)
    print(username)


def login_user():
    global current_user, users
    """Interactive login prompt.

    Prompts for username/password, re-computes the salted hash and
    compares to the stored value. On success sets `current_user`.
    """
    print('\n--- Login ---')
    username = input('Username: ').strip()
    if username not in users:
        print('User not found.')
        return
    pwd = input('Password: ')
    salt = users[username].get('salt')
    _, hashed = hash_password(pwd, salt)
    if hashed == users[username].get('password'):
        current_user = username
        print(f'Logged in as {username}')
    else:
        print('Incorrect password.')


def logout_user():
    global current_user
    """Log out the currently authenticated user (if any)."""
    if current_user:
        print(f'User {current_user} logged out.')
        current_user = None
    else:
        print('No user currently logged in.')



class loader:
    """Loader utilities.

    This class provides two related facilities used by the menus:
    1. `loading1()` a short ASCII frame animation used as a quick
       transition between menus. It uses only ASCII so it is safe on
       Windows consoles.
    2. An instance-based progress bar which accepts a list of `items`
       and exposes `run_task()` and `run_with_callback(callback)` to run
       work while updating the bar. Use the progress bar when you have
       real work to perform and want a percentage display.
    """
    @staticmethod
    def loading1():
        # Shorter default animation: 10 iterations, faster delay
        # Use ASCII-friendly frames to avoid console encoding errors on Windows
        animation = [
            "[>         ]",
            "[>>        ]",
            "[>>>       ]",
            "[>>>>      ]",
            "[>>>>>     ]",
            "[>>>>>>    ]",
            "[>>>>>>>   ]",
            "[>>>>>>>>  ]",
            "[>>>>>>>>> ]",
            "[>>>>>>>>>>]",
        ]

        iterations = 10
        delay = 0.06

        for i in range(iterations):
            time.sleep(delay)
            sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
            sys.stdout.flush()
        print()

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
        """Run a task across the stored items while updating the progress bar.

        If a callable is provided as the first argument, it will be called for
        each item as: callback(item, index). If no callback is provided, the
        method falls back to a simulated workload using time.sleep(0.1).

        Example usage:
            loader(items).run_task(my_callback)
            where my_callback(item, index) performs the real work.
        """
        def _default_work(_item, _idx):
            # simulate work when no callback is provided
            time.sleep(0.1)

        # allow passing a callable via attribute for backwards compatibility
        callback = getattr(self, 'work_callback', None)

        # If user passed a callback to this method at runtime, prefer it
        # (we support both setting self.work_callback or passing as arg later)
        if callable(callback):
            work_fn = callback
        else:
            work_fn = _default_work

        # Loop through the items and run the work function, updating the bar
        for i, item in enumerate(self.items):
            current_iteration = i + 1

            try:
                work_fn(item, i)
            except Exception as e:
                # don't crash the progress viewer; report and continue
                print(f"\nError while processing item {i}: {e}")

            # Update progress bar
            self._loadbar(current_iteration)

        print('Loading complete!')

    def run_with_callback(self, callback):
        """Run the progress bar while calling `callback(item, index)` for each item.

        This is a convenience wrapper that temporarily sets the internal
        `work_callback` attribute and calls `run_task()`.
        """
        if not callable(callback):
            raise TypeError('callback must be callable')

        # attach callback, run, then remove it
        self.work_callback = callback
        try:
            self.run_task()
        finally:
            delattr(self, 'work_callback')

class file_opener:
    """Manage the lifecycle of a lesson activity file.

    Responsibilities:
    - create a file from a lesson template (`_create_file`)
    - open it in the user's default editor (`_open_file_in_editor`)
    - wait for the user to save and submit, then run and grade the
      student's code (`_run_and_grade_code`).

    The public flow is `start_activity_flow()` which orchestrates the
    above steps and shows short loader animations before key steps.
    """

    def __init__(self, lesson_name, template_code, expected_output):
        # Basic activity metadata
        self.lesson_name = lesson_name
        self.template_code = template_code
        self.expected_output = expected_output
        self.filename = f"{self.lesson_name}_activity.py"

    def _create_file(self):
        """Internal method to create the .py file."""
        try:
            # write using UTF-8 to avoid platform encoding issues
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(self.template_code)
            print(f"Activity file created: {self.filename}")
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
            """Orchestrate creating, opening and grading a lesson activity.

            Sequence:
            1. Show a short loading animation for UI continuity.
            2. Write the lesson template to a file (`_create_file`).
            3. Open the file in the user's editor (`_open_file_in_editor`).
            4. Wait for the user to save/finish and press Enter.
            5. Show a short loading animation then run and grade the file
               by executing it in a subprocess and comparing stdout to the
               expected output.

            The method uses try/except guards around animations so the
            function still works when run in environments that cannot
            render the animation (for example during automated tests).
            """
            print(f"\n--- Starting Lesson: {self.lesson_name} ---")

            # Show a short frame animation before creating/opening the activity
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass

            # Create the activity file and open it in the user's editor
            self._create_file()
            self._open_file_in_editor()

            # Pause until the user is ready to submit
            input("\n**PRESS ENTER** when you have finished saving the file to submit for grading...")

            # Show a brief frame animation before grading the submission
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass

            # Run the student's file and compare stdout to the expected text
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
    # Main entry UI: shows a small animation then displays top-level menu
    # options. The menu prints the currently logged-in user and routes the
    # user to submenus (Printing, Variables, Loops, Conditionals, etc.).
    # Each submenu is responsible for its own further prompts and
    # navigation. Animations are wrapped in try/except to preserve
    # behavior under test or minimal shells.
    try:
        loader.loading1()
        clear_screen()
    except Exception:
        pass
    while True:
        # main loop
        print("\n--- Welcome to the Code Lesson Compiler ---")
        print('----------------------------------------------')
        print('Seleact a lesson to begin:')
        if current_user:
            print(f'Logged in: {current_user}')
        else:
            print('Logged in: None')
        print("1. Printing")
        print("2. Variables")
        print("3. Loops")
        print("4. Conditionals")
        print("5. Functions")
        print('6. Lists')
        print('7. Others')
        print('8. User')
        print('0. Exit')
        print('----------------------------------------------')
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.printing_menu()
        elif choice == '2':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.variables_menu()
        elif choice == '3':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.loops_menu()
        elif choice == '4':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.conditionals_menu()
        elif choice == '5':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.functions_menu()
        elif choice == '6':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.lists_menu()
        elif choice == '7':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.others_menu()
        elif choice == '8':
            try:
                loader.loading1()
                clear_screen()
            except Exception:
                pass
            submenu.user_menu()
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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

def tuple():
    print('---------------- Example of tuple -----------------')
    print('---------------------------------------------------')
    print('fruits = ("apple", "orange", "grapes", "cherry")')
    print('print(fruits)')
    print('Output:')
    fruits = ("apple", "orange", "grapes", "cherry")
    print(fruits)
    print('---------------------------------------------------')
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

def nested_while_loop():
    print('-------------- Example of a Nested While Loop ---------------')
    print('-------------------------------------------------------------')
    print(textwrap.dedent("""
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
"""))
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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

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
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

def temperatures():
    print('------------------------------ Temperature ------------------------------')
    print('-------------------------------------------------------------------------')
    print('F = float(input("Enter Temperature in FARENHEIT: "))')
    print("C = ((F - 32)*5)/9")
    print("round(C,2)")
    print('print(f"{F} degrees in Farenheit converted to Celsius is {C}")')
    print('C = float(input("Enter Temperature in CELSIUS: "))')
    print("F = (C * 9/5) + 32")
    print('print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")')
    print()
    print("Output:")
    F = float(input("Enter Temperature in FARENHEIT: "))
    C = ((F - 32) * 5) / 9
    round(C, 2)

    print(f"{F} degrees in Farenheit converted to Celsius is {C}")

    C = safe_float_input("Enter Temperature in CELSIUS: ")
    F = (C * 9 / 5) + 32

    print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")
    print('------------------------------------------------------------------------')
    clear = input('Press ENTER to return to the menu...')
    clear_screen()

def temp_calc():
    print("--------- Simple Calculator ---------")
    print("-------------------------------------")
    print(" 1. Temperature Conversion")
    print(" 2. Arithmetic Operations")
    print("-------------------------------------")
    choice = input("Enter your choice: ")
    clear_screen()

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
            F = safe_float_input("Enter Temperature in Fahrenheit: ")
            C = ((F - 32) * 5) / 9
            print(f"{F} degrees Fahrenheit is {round(C, 2)} degrees Celsius.")
            print("----------------------------------------------------------")
            clear = input('Press ENTER to return to the menu...')
            clear_screen()

        elif temp_choice == "2":
            print('------------- Celsius to Fahrenheit Conversion -------------')
            print("------------------------------------------------------------")
            C = safe_float_input("Enter Temperature in Celsius: ")
            F = (C * 9 / 5) + 32
            print(f"{C} degrees Celsius is {round(F, 2)} degrees Fahrenheit.")
            print("------------------------------------------------------------")
            clear = input('Press ENTER to return to the menu...')
            clear_screen()

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

        num1 = safe_float_input("Enter first number: ")
        num2 = safe_float_input("Enter second number: ")

        if operation_choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            clear = input('Press ENTER to return to the menu...')
            clear_screen()

        elif operation_choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            clear = input('Press ENTER to return to the menu...')
            clear_screen()

        elif operation_choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            clear = input('Press ENTER to return to the menu...')
            clear_screen()

        elif operation_choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                clear = input('Press ENTER to return to the menu...')
                clear_screen()
            else:
                print("Error! Division by zero is not allowed.")
                clear = input('Press ENTER to return to the menu...')
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
            clear = input('Press ENTER to return to the menu...')
    else:
        print("Invalid input! Please enter 1 or 2.")
        clear = input('Press ENTER to return to the menu...')

class submenu:
    def printing_menu():
        while True:
            print('--------------------------------- Printing Menu -----------------------------------')
            print('-----------------------------------------------------------------------------------')
            print()
            print(textwrap.dedent("""
                In Python, print() is a built-in function used to display
                output to the console (standard output device).
                It is a fundamental tool for programmers to show text messages,
                variable values or the results of operations during program execution or debugging.
                """))
            print()
            print('------------------------------------------------------------------------------------')
            print('1. Basic Printing')
            print('2. String Formatting')
            print('3. Lesson Activity')
            print('0. Return to Main Menu')
            print('------------------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                basic_printing()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
    
    def variables_menu():
        while True:
            print('------------------------------- Variables Menu -----------------------------------')
            print('----------------------------------------------------------------------------------')
            print()
            print(textwrap.dedent("""
            Variables in Python are used to store data values.
            They act as containers for data that can be referenced and manipulated throughout a program.
            Variables are created by assigning a value to a name using the equals sign (=).
            The value can be of various data types, such as integers, floats, strings, lists, etc.
            """))
            print()
            print('----------------------------------------------------------------------------------')
            print('1. String Concatenation with Variables')
            print('2. Variable Assignment')
            print('3. Lesson Activity')
            print('0. Return to Main Menu')
            print('----------------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                string_concatenation_with_variables()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
    
    def loops_menu():
        while True:
            print('-------------------------------- Loops Menu -----------------------------------')
            print('-------------------------------------------------------------------------------')
            print()
            print(textwrap.dedent("""
            Loops in Python are used to execute a block of code repeatedly for a specified number of times or while a certain condition is met.
            They help automate repetitive tasks and iterate over sequences like lists, tuples, or strings.
            The two main types of loops in Python are for loops and while loops.
            """))
            print()
            print('-------------------------------------------------------------------------------')
            print('1. For Loop')
            print('2. While Loop')
            print('3. Nested Loops')
            print('4. Lesson Activity')
            print('0. Return to Main Menu')
            print('-------------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                for_loop()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                while_loop()
            elif choice == '3':
                print('--- Nested Loops Menu ---')
                print('1. Nested For Loop')
                print('2. Nested While Loop')
                nested_loop_choice = input('Enter your choice: ')
                if nested_loop_choice == '1':
                    try:
                        loader.loading1()
                        clear_screen()
                    except Exception:
                        pass
                    nested_for_loop()
                elif nested_loop_choice == '2':
                    try:
                        loader.loading1()
                        clear_screen()
                    except Exception:
                        pass
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
        
    def conditionals_menu():
        while True:
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
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                simple_condi_statements()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                logical_condi_statements()
            elif choice == '3':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
    
    def functions_menu():
        while True:
            print('----------------------------- Functions Menu ------------------------------')
            print('---------------------------------------------------------------------------')
            print()
            print(' Functions in Python are reusable blocks of code that perform a specific task. \
                    \nThey help organize code, improve readability, and allow for code reuse. \
                    \nFunctions are defined using the def keyword, followed by the function name and parentheses. \
                    \nThey can take input parameters and break output values.')
            print()
            print('---------------------------------------------------------------------------')
            print('1. Function Example')
            print('2. Lesson Activity')
            print('0. Return to Main Menu')
            print('---------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
    def lists_menu():
        while True:
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
            print('3. Tuple Example')
            print('4. Lesson Activity')
            print('0. Return to Main Menu')
            print('-------------------------------------------------------------------------')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                list_example()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                editing_lists()
            elif choice == '3':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                tuple()
            elif choice == '4':
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
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')
    
    def others_menu():
        while True:
            print('------------------------------ Others Menu ------------------------------')
            print('-------------------------------------------------------------------------')
            print()
            print(' This section includes various other programming concepts and examples that do not fit into the previous categories. \
                    \nThese may include arithmetic operations, temperature conversions, and simple calculators. \
                    \nEach topic provides practical examples to help understand their implementation in Python.')
            print()
            print('-------------------------------------------------------------------------')
            print('1. Arithmetic Operators')
            print('2. Temperature Conversion')  
            print('3. Simple Calculator')
            print('0. Return to Main Menu')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                operators_example()
            elif choice == '2':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                temperatures()
            elif choice == '3':
                try:
                    loader.loading1()
                    clear_screen()
                except Exception:
                    pass
                temp_calc()
            elif choice == '0':
                break
            else:
                print('Invalid choice. Please try again.')

    def user_menu():
        # On entry, ask if the user already has an account. If not, walk them
        # through account creation first, then offer the full user menu.
        first_time = True
        while True:
            if first_time:
                first_time = False
                has = input('Do you already have an account? (y/n): ').strip().lower()
                clear_screen()
                if has in ('y', 'yes'):
                    login_user()
                elif has in ('n', 'no'):
                    create_user()
                    # Offer to login immediately after creating an account
                    want_login = input('Do you want to login now? (y/n): ').strip().lower()
                    clear_screen()
                    if want_login in ('y', 'yes'):
                        login_user()
                else:
                    print('Please answer y or n.')
                    continue

            print('------------------------------ User Menu ------------------------------')
            print('1. Create Account')
            print('2. Login')
            print('3. Logout')
            print('0. Return to Main Menu')
            choice = input('Enter your choice: ')
            clear_screen()
            if choice == '1':
                create_user()
            elif choice == '2':
                login_user()
            elif choice == '3':
                logout_user()
            elif choice == '0':
                clear_screen()
                break
            else:
                print('Invalid choice. Please try again.')



if __name__ == "__main__":
    # On first run require creating a user account before showing the menu.
    clear_screen()
    # If there are no users stored, force creation of at least one account.
    if not users:
        print('No user accounts found. Please create an account to continue.')
        while not users:
            create_user()
            # reload users from disk in case something changed
            users = load_users()
        clear_screen()

    # After ensuring an account exists, prompt to login.
    print('Please login to continue.')
    login_user()
    clear_screen()

    Main_Menu()