"""
Simple Student Grade Management System
Author: [Your Name]
"""

import csv
import os

def add_student():
    """Add a new student to the database."""
    file_exists = os.path.isfile('final_grade.csv')
    
    with open('final_grade.csv', "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        if not file_exists:
            writer.writerow(["name", "grade"])
        
        name = input('Enter student name: ')
        grade = int(input('Enter grade: '))
        writer.writerow([name, grade])
        print(f"✅ {name} added!")

def show_all():
    """Display all students."""
    try:
        with open('final_grade.csv', "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if len(rows) <= 1:
                print("No students found!")
                return
            
            print("\n📚 Student List:")
            for i, row in enumerate(rows[1:], 1):
                print(f"{i}. {row[0]} - Grade: {row[1]}")
    except FileNotFoundError:
        print("No data found. Add some students first!")

def show_avg():
    """Calculate average grade."""
    try:
        with open('final_grade.csv', "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if len(rows) <= 1:
                print("No grades found!")
                return
            
            grades = [int(row[1]) for row in rows[1:] if len(row) >= 2]
            if grades:
                print(f"\n📊 Average grade: {sum(grades)/len(grades):.2f}")
    except FileNotFoundError:
        print("No data found!")

def main():
    """Main program loop."""
    while True:
        print("\n1. Add Student")
        print("2. Show All")
        print("3. Show Average")
        print("4. Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            show_avg()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()