import os
os.system('cls')
def Main_Menu():
    while True:
        print('Select from the following options:')
        print('-------------------------------------')
        print('A - Variables & Print Output')
        print('B - Operators')
        print('C - If/Else Statements')
        print('D - Loops')
        print('E - Lists & Dictionaries')
        print('F - Functions')
        print('Q - Quit')
        print('-------------------------------------')
        choice = input('Enter your choice: ').upper()
        if choice == 'A':
            os.system('cls')
            sub_menu.printing_menu()
        elif choice == 'B':
            os.system('cls')
            sub_menu.operators_menu()
        elif choice == 'C':
            os.system('cls')
            sub_menu.if_else_statement_menu()
        elif choice == 'D':
            os.system('cls')
            sub_menu.loops_menu()
        elif choice == 'E':
            print('E - Lists & Dictionaries (Coming Soon)')
        elif choice == 'F':
            print('F - Functions (Coming Soon)')
        elif choice == 'Q':
            print('Thank you for using the menu. Goodbye!')
            break

# #submenus
class sub_menu():
    @staticmethod
    def printing_menu():
        while True:
            print('Select a lesson from the following options:')
            print('------------------------------------------------')
            print('1 - String concatenation & formatting and Basic printing')
            print('2 - Data Types')
            print(f"3 - Input, eval and int function")
            print('Q - Quit to Main Menu')
            choice = input('Enter your choice: ').upper()
            os.system('cls')

            # --- LESSON 1 LOGIC IS NOW NESTED ---
            if choice == '1':
                print('==================================================================')
                print('You selected String formatting and Basic printing lesson.')
                print('Select on of the following')
                print('1. Basic printing') 
                print('2. String Formatting using f-strings:')
                print('3. String concatenation using + operator and , in print() function')
                print('Q. Quit to previous menu')
                print('==================================================================')
                sub_choice = input('Enter your choice: ').upper() # sub_choice is defined here
                os.system('cls')

                if sub_choice == '1': # Corrected: 'if' for the first check
                    print('Have selected Basic printing.')
                    print('==================================================================')
                    print('In Python, Basic printing can be done using the print function \nExamples:')
                    print('print("Hello World")')
                    print('print("Ayoko na")')
                    print('print("miss ko na sya")')
                    print('OUTPUT:')
                    print("Hello World!")
                    print("Ayoko na")
                    print("miss ko na sya")
                    print('==================================================================')
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == '2':
                    
                    print('Have selected String Formatting using f-strings.')
                    print('==================================================================')
                    print('In Python, f-strings (formatted string literals) allow you to embed expressions inside string literals, using curly braces {}.' \
                    '\nThis provides a concise and readable way to include variable values and expressions directly within strings.' \
                    '\nTo create an f-string, prefix the string with the letter f or F.')
                    print('This is an example of f-string usage.')
                    print('input:')
                    print('name = input("Enter your name: ")')
                    print('age = int(input("Enter your age: "))')
                    print('print(f"Hello, {name}. You are {age} years old.")')
                    print('Final output:')
                    name = input("Enter your name: ")
                    age = int(input("Enter your age: "))
                    print(f"Hello, {name}. You are {age} years old.")
                    print('==================================================================')
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == '3':
                    print('Have selected String concatenation using + operator and , in print() function.')
                    print('==================================================================')
                    print('In Python, you can concatenate strings using the + operator or by using commas within the print() function.' \
                    '\nUsing + operator joins strings together without spaces, while using commas in print() adds spaces between the items automatically.')
                    print('This is an example of string concatenation.')
                    print('input:')
                    print('str1 = "Hello"')
                    print('str2 = "World"')
                    print('print(str1 + " " + str2)  # Using + operator')
                    print('print(str1, str2)        # Using , in print() function')
                    print('Final output:')
                    str1 = "Hello"
                    str2 = "World"
                    print(str1 + " " + str2)  # Using + operator
                    print(str1, str2)        # Using , in print() function
                    print('==================================================================')
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == 'Q':
                    # This will break out of the inner menu, returning to the main menu for Lesson 1, 2, 3 choice
                    break 
                else:
                    print('Invalid sub-choice. Please try again.')
                    print('==================================================================')
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
            # --- END OF LESSON 1 LOGIC ---

            elif choice == '2':
                print('You selected Data Types lesson. ')
                print('In python we have four main data types:')
                print('1. Integer (int): Represents whole numbers, both positive and negative, without decimal points.\n Example: 42, -7, 0')
                print('2. Floating Point (float): Represents real numbers that include decimal points.\n Example: 3.14, -0.001, 2.0')
                print('3. String (str): Represents sequences of characters enclosed in single or double quotes.\n Example: "Hello, World!", \'Python\'')
                print('4. Boolean (bool): Represents one of two values: True or False.\n Example: True, False')
                print('These data types are fundamental for storing and manipulating data in Python programs.')
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            
            elif choice == '3':
                print('You selected Input, eval and int function lesson.')
                print('You selected Input, eval and int function lesson.')
                print('1. input(): The input() function is used to take input from the user as a string.\n Example: name = input("Enter your name: ")')
                print('2. eval(): The eval() function evaluates a string expression and returns the result.\n Example: result = eval("3 + 5")  # result will be 8')
                print('3. int(): The int() function converts a value to an integer.\n Example: number = int("42")  # number will be 42')
                print('These functions are commonly used for user interaction and data type conversion in Python.')
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue    
            elif choice == 'Q':
                break
            else:
                print('Invalid choice. Please try again.')
                print('==================================================================')
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
    
    def operators_menu():
        while True:
            print('Operators menu selected.')
            print('====================================')
            print('Choose an operator to learn about:')
            print('1 - Arithmetic Operators')
            print('2 - Relational Operators')
            print('3 - Logical Operators')
            print('Q - Quit to Main Menu')
            choice = input('Enter your choice: ').upper()
            if choice == '1':
                print('You selected Arithmetic Operators.')
                print('Arithmetic operators are used to perform mathematical operations such as ' \
                '\naddition (+), subtraction (-), multiplication (*), division (/), ' \
                '\nmodulus (%), exponentiation (**), and floor division (//).')
                print('Examples:')
                print('a = input()')
                print('b = 3')  
                print('Addition: a + b =', 10 + 3)
                print('Subtraction: a - b =', 10 - 3)
                print('Multiplication: a * b =', 10 * 3)
                print('Division: a / b =', 10 / 3)
                print('Modulus: a % b =', 10 % 3)
                print('Exponentiation: a ** b =', 10 ** 3)
                print('Floor Division: a // b =', 10 // 3)
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '2':
                print('You selected Relational Operators.')
                print('Relational operators are used to compare two values. ' \
                '\nThey include equal to (==), not equal to (!=), greater than (>), ' \
                '\ngreater than or equal to (>=), less than (<), and less than or equal to (<=).')
                print('Examples:')
                print('a = 10')
                print('b = 3')
                print('Equal to: a == b ->', 10 == 3)
                print('Not equal to: a != b ->', 10 != 3)
                print('Greater than: a > b ->', 10 > 3)
                print('Greater than or equal to: a >= b ->', 10 >= 3)
                print('Less than: a < b ->', 10 < 3)
                print('Less than or equal to: a <= b ->', 10 <= 3)
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '3':
                print('You selected Logical Operators.')
                print('Logical operators are used to combine conditional statements. \nThey include and, or, and not.')
                print('Examples:')
                print('a = True')
                print('b = False')
                print('Logical AND: a and b ->', True and False)
                print('Logical OR: a or b ->', True or False)
                print('Logical NOT: not a ->', not True)
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == 'Q':
                break
            else: 
                print('Invalid choice. Please try again.')
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
    
    def if_else_statement_menu():
        while True:    
            print('If/Else Statements menu selected.')
            print('Select one of the following topics to learn about:')
            print('====================================')
            print('1 - If Statements')
            print('2 - If-Else Statements')
            print('3 - Elif Statements')
            print('Q - Quit to Main Menu')
            choice = input('Enter your choice: ').upper()
            if choice == '1':
                print('You selected If Statements.')
                print('An if statement is used to test a specific condition. ')
                print('If the condition evaluates to True, the block of code within the if statement is executed. ')
                print('Example:')
                print('num = int(input("Enter a number: "))')
                print('if num > 0:')
                print('    print("The number is positive.")')
                num = int(input("Enter a number: "))
                if num > 0:
                    print("The number is positive.")
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '2':
                print('You selected If-Else Statements.')
                print('An if-else statement is used to test a condition and provide an alternative block of code to execute if the condition is False. ')
                print('Example:')
                print('num = int(input("Enter a number: "))')
                print('if num % 2 == 0:')
                print('    print("The number is even.")')
                print('else:')
                print('    print("The number is odd.")')
                num = int(input("Enter a number: "))
                if num % 2 == 0:
                    print("The number is even.")
                else:
                    print("The number is odd.")
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '3':
                print('You selected Elif Statements.')
                print('An elif statement is used to check multiple conditions in sequence. ')
                print('If the first condition is False, the next condition is checked, and so on. ')
                print('Example:')
                print('num = int(input("Enter a number: "))')
                print('if num > 0:')
                print('    print("The number is positive.")')
                print('elif num == 0:')
                print('    print("The number is zero.")')
                print('else:')
                print('    print("The number is negative.")')
                num = int(input("Enter a number: "))
                if num > 0:
                    print("The number is positive.")
                elif num == 0:
                    print("The number is zero.")
                else:
                    print("The number is negative.")
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == 'Q':
                print('Returning to Main Menu...')
                os.system('cls')
                break
            else:
                print('Invalid choice. Please try again.')
                cls = input('Enter any key to continue...')
                os.system('cls')

    def loops_menu():
        while True:
            print('Loops menu selected.')
            print('====================================')
            print('Choose a loop type to learn about:')
            print('1 - For Loops')
            print('2 - For in Range Loops')
            print('3 - While Loops')
            print('4 - Nested Loops')
            print('Q - Quit to Main Menu')
            choice = input('Enter your choice: ').upper()
            if choice == '1':
                print('You Selected For loops.')
                print('For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. ')
                print('Example:')
                print('fruits = ["apple", "banana", "cherry"]')
                print('for fruit in fruits:')
                print('    print(fruit)')
                fruits = ["apple", "banana", "cherry"]
                for fruit in fruits:
                    print(fruit)
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '2':
                print('You Selected For in Range loops.')
                print('For in range loops are used to iterate over a sequence of numbers generated by the range() function.' \
                '\n The range() function can take one, two, or three arguments to define the start, stop, and step of the sequence.')
                print('Example:')
                print('for i in range(5):  # Iterates from 0 to 4')
                print('    print(i)')
                print('for i in range(2, 6):  # Iterates from 2 to 5')
                print('    print(i)')
                print('OUTPUT:')
                for i in range(5):  # Iterates from 0 to 4
                    print(i)
                for i in range(2, 6):  # Iterates from 2 to 5
                    print(i)
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '3':
                print('You Selected While loops.')
                print('While loops are used to repeatedly execute a block of code as long as a specified condition is True.'
                '\n and can only be terminated when the condition becomes False or a break statement is encountered.')
                print('Example:')
                print('count = 0')
                print('while count < 5:')
                print('    print(count)')
                count = 0
                while count < 5:
                    print(count)
                    count += 1
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == '4':
                print('You Selected Nested loops.')
                print('Nested loops are loops that exist within another loop. '
                '\nThe inner loop is executed completely for each iteration of the outer loop.')
                print('Example:')
                print('for i in range(3):')
                print('    for j in range(2):')
                print('        print(f"i: {i}, j: {j}")')
                for i in range(3):
                    for j in range(2):
                        print(f"i: {i}, j: {j}")
                cls = input('Enter any key to continue...')
                os.system('cls')
                continue
            elif choice == 'Q':
                break
            else:
                print('Invalid choice. Please try again.')
                cls = input('Enter any key to continue...')
                os.system('cls')

    def List_and_Dictionaries_menu():
        while True:
            print('You have Selected List and Dictionaries')
            print('==========================================')
            print('Select one of the choices below: ')
            print('1 - Lists')
            print('2 - Dictionaries')
            print('Q - Quit to Main Menu')
            choice = input('Enter your choice: ').upper()
            if choice == '1':
                print('You selected Lists.')
                print('====================================')
                print('pick one of the topics below to learn about:')
                print('1 - Creating a List')
                print('2 - Accessing List Elements')
                print('3 - Modifying a List')
                print('4 - list functions')
                print('Q - Quit to previous menu')
                sub_choice = input('Enter your choice: ').upper()
                if sub_choice == '1':
                    print('You selected Creating a List.')
                    print('In Python, a list is created by placing all the items (elements) inside square brackets [], separated by commas. ')
                    print('Example:')
                    print('my_list = [1, 2, 3, "apple", "banana"]')
                    my_list = [1, 2, 3, "apple", "banana"]
                    print('Created List:', my_list)
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == '2':
                    print('You selected Accessing List Elements.')
                    print('In Python, you can access list elements by their index using square brackets [].' \
                    '\n note that Python uses zero-based indexing, meaning the first element is at index 0.')
                    print('Example:')
                    print('my_list = [10, 20, 30, 40, 50]')
                    print('first_element = my_list[0]  # Accessing the first element')
                    my_list = [10, 20, 30, 40, 50]
                    first_element = my_list[0]  # Accessing the first element
                    print('First Element:', first_element)
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == '3':
                    print('You selected Modifying a List.')
                    print('In Python, you can modify list elements by accessing them via their index and assigning a new value.')
                    print('Example:')
                    print('my_list = [10,20,30]')
                    print('my_list[1] = 25  # Modifying the second element')
                    my_list = [10, 20, 30]
                    my_list[1] = 25  # Modifying the second element
                    print('Modified List:', my_list)
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == '4':
                    print('You selected list functions.')
                    print('In Python, lists come with several built-in functions that allow you to manipulate and interact with them.')
                    print('Some common list functions include:')
                    print('1. append(): Adds an element to the end of the list.')
                    print('2. remove(): Removes the first occurrence of a specified element from the list.')
                    print('3. pop(): Removes and returns the element at a specified index (default is the last element).')
                    print('4. sort(): Sorts the elements of the list in ascending order.')
                    print('5. reverse(): Reverses the order of the elements in the list.')
                    print('Example:')
                    print('my_list = [3, 1, 4]')
                    print('my_list.append(2)  # my_list is now [3, 1, 4, 2]')
                    print('my_list.remove(1)  # my_list is now [3, 4, 2]')
                    print('popped_element = my_list.pop()  # popped_element is 2, my_list is now [3, 4]')
                    print('my_list.sort()  # my_list is now [3, 4]')
                    print('my_list.reverse()  # my_list is now [4, 3]')
                    my_list = [3, 1, 4]
                    my_list.append(2)  # my_list is now [3, 1, 4, 2]
                    my_list.remove(1)  # my_list is now [3, 4, 2]
                    popped_element = my_list.pop()  # popped_element is 2, my_list is now [3, 4]
                    my_list.sort()  # my_list is now [3, 4]
                    my_list.reverse()  # my_list is now [4, 3]
                    print('Final List:', my_list)
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
                elif sub_choice == 'Q':
                    break
                else:
                    print('Invalid choice. Please try again.')
                    cls = input('Enter any key to continue...')
                    os.system('cls')
                    continue
            #elif choice == '2':
Main_Menu()
