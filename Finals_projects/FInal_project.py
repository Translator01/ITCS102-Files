import time
import sys
import os
import platform

os.system('cls')

#loading animation credits: https://github.com/Amitgajare2/LoadingAnimation/blob/main/loading02.py
def animation():
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(50):
        time.sleep(0.2)
        sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
        sys.stdout.flush()
    os.system('cls')


    # --- Helper function from section 1 ---
def open_file_in_editor(filename):
    """Opens a file using the operating system's default program."""
    system = platform.system()
    
    # ... (insert the platform-specific code from section 1 here) ...
    if system == "Windows":
        os.startfile(filename)
        print(f"File **{filename}** opened on Windows.")
    elif system == "Darwin": # macOS
        os.system(f"open {filename}")
        print(f"File **{filename}** opened on macOS.")
    elif system == "Linux":
        os.system(f"xdg-open {filename}")
        print(f"File **{filename}** opened on Linux.")
    else:
        print(f"Warning: Could not automatically open file on unrecognized OS: {system}")


