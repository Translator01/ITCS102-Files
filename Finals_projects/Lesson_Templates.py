# templates.py

# --- LESSON 1: VARIABLES ---
VAR_ACTIVITY_CODE = """
# Lesson: Variables and Assignment
# Task: Assign the result of 10 * 5 to the variable 'answer'.
# The expected output is 50.
answer = 0 # <-- Change this line!

print(answer) 
"""
VAR_EXPECTED_OUTPUT = "50\n"


# --- LESSON 2: LOOPS ---
LOOP_ACTIVITY_CODE = """
# Lesson: For Loops
# Task: Change the range to print numbers 1, 2, 3, 4.
for i in range(1, 5): 
    print(i)
"""
LOOP_EXPECTED_OUTPUT = "1\n2\n3\n4\n"

# Central Dictionary to hold all lesson data
LESSONS = {
    "Variables": {
        "code": VAR_ACTIVITY_CODE,
        "expected": VAR_EXPECTED_OUTPUT
    },
    "Loops": {
        "code": LOOP_ACTIVITY_CODE,
        "expected": LOOP_EXPECTED_OUTPUT
    }
}
