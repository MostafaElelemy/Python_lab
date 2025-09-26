"""
main.py - Entry point
- Imports all task modules.
- Displays a menu and runs the selected task.
- Uses input validation and avoids code duplication via helpers.
NOTE: As required, if __name__ == "__main__" guard is used ONLY here.
"""
from utils import prompt_choice

import task1_math as t1
import task2_regex as t2
import task3_datetime as t3
import task4_products as t4
import task5_os_manager as t5
import task6_random_data as t6
import task7_log_check as t7

MENU = {
    "1": ("Math Automation", t1.run),
    "2": ("Regex Log Cleaner", t2.run),
    "3": ("Datetime Reminder Script", t3.run),
    "4": ("Product Data Transformer", t4.run),
    "5": ("OS File Manager", t5.run),
    "6": ("Random Data Generator", t6.run),
    "7": ('Decorators Task: "execution_log.txt" viewer', t7.run),
}

def show_menu():
    print("\n=== Task Menu ===")
    for key in sorted(MENU.keys(), key=int):
        print(f"{key}) {MENU[key][0]}")
    print("=================")

def main():
    show_menu()
    choice = prompt_choice("Select a task number: ", list(MENU.keys()))
    print(f"\nRunning: {MENU[choice][0]}\n")
    MENU[choice][1]()

if __name__ == "__main__":
    main()
