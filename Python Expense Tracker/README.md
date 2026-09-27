# 💰 Personal Expense Tracker

A simple **command-line Personal Expense Tracker built with Python** for recording expenses and income, viewing financial records, and calculating monthly expenses.

This project was created to practice Python fundamentals including **functions, loops, file handling, string manipulation, date handling, exception handling, and basic data processing**.

> 🚧 Educational project — built as part of my Python learning journey.

---

## ✨ Features

### ➕ Add Expenses

Add one or multiple expenses by providing:

- Expense category
- Amount
- Date

The user can enter a custom date or press Enter to automatically use today's date.

Example:

```text
Food|250|26-09-2026
Transport|100|26-09-2026
Expenses are stored in:

expense.txt

📖 View Expenses
Displays all recorded expenses stored in expense.txt.

The application reads the file and displays the stored records in the terminal.

🗑️ Remove Expenses
The project includes functionality for selecting an expense from the stored records and removing it.

The current implementation is still being improved and will eventually provide more robust expense selection and deletion.

💵 Add Income
Allows the user to record income along with its date.

Income is stored separately in:

income.txt

Example:

25000|26-09-2026

📊 Monthly Expense Calculation
Users can enter a month and year in:

MM-YYYY

The program then searches the stored expenses and calculates the total spending for that month.

Example:

Enter month and year (MM-YYYY): 09-2026

Category: Food, Amount: 250, Date: 26-09-2026
Category: Transport, Amount: 100, Date: 25-09-2026

Total expense for 09-2026: 350

🖥️ Application Menu
The program uses a simple menu-driven interface:

===PERSONAL EXPENSE TRACKER===

1.add_expense
2.show_expense
3.remove_expense
4.add_income
5.monthly_expense
6.exit

Choose an option

The user selects an operation by entering the corresponding number.

🛠️ Technologies Used
Language
🐍 Python 3

Python Modules
import datetime

Concepts Practiced
Functions

Loops

Conditional statements

Lists

File handling

String manipulation

split()

strip()

lower()

datetime

Date formatting

Exception handling

try/except

User input

Basic data processing

📂 Project Structure
Personal Expense Tracker/
│
├── expense_tracker.py
├── expense.txt
├── income.txt
└── README.md

File names may vary depending on the current version of the project.

expense_tracker.py
Contains the main application logic and menu system.

expense.txt
Stores expense records.

The format used is:

category|amount|date

Example:

Food|250|26-09-2026
Transport|100|25-09-2026
Entertainment|500|20-09-2026

income.txt
Stores income records using:

income|date

Example:

25000|26-09-2026

💾 File Handling
This project uses plain text files to persist data between program executions.

Three main file operations are practiced:

open("expense.txt", "r")
open("expense.txt", "w")
open("expense.txt", "a")

Mode	Purpose
r	Read existing data
w	Rewrite file
a	Append new data

The project also uses the | character as a simple delimiter between fields.

For example:

Food|250|26-09-2026

can be separated using:

line.split("|")

📅 Date Handling
The project uses Python's datetime module to work with dates.

Users can either enter a date manually:

26-09-2026

or press Enter to automatically use the current date.

Dates are stored in:

DD-MM-YYYY

format.

The project also extracts the month and year from stored dates to calculate monthly expenses.

🧩 Program Structure
The application is divided into separate functions, with each function handling a specific operation.

Personal Expense Tracker
          │
          ├── add_expense()
          │
          ├── show_expense()
          │
          ├── remove_expense()
          │
          ├── add_income()
          │
          ├── monthly_expense()
          │
          └── check_profit_or_loss()

This helped me practice breaking a larger problem into smaller functions rather than putting all the logic inside one block.

⚠️ Input & Error Handling
The main menu uses try/except to handle invalid menu input.

try:
    user = int(input("Choose an option"))
except ValueError:
    print("Invalid Value Entered !!")

The application also validates dates using Python's datetime functionality.

🧠 What I Learned
This project helped me understand how basic Python concepts can be combined to create a useful command-line application.

Some of the main concepts I practiced include:

Writing and organizing functions

Reading and writing files

Working with structured text data

Processing strings

Working with dates

Handling user input

Using loops to process multiple records

Calculating values from stored data

Handling invalid input

Debugging program logic

One important lesson from this project was learning how to turn a real-world requirement into smaller programming problems.

For example:

"Track my expenses"
        ↓
Store expense data
        ↓
Add expenses
        ↓
Display expenses
        ↓
Remove expenses
        ↓
Filter by month
        ↓
Calculate totals

⚠️ Current Limitations
This is an early learning implementation and has several areas that can be improved:

Expense deletion logic needs refinement

Income and expenses are stored separately

Profit/loss calculation is not currently connected to the main menu

No category-based expense summaries

No monthly income calculation

No overall balance calculation

Duplicate/invalid records are possible

Data is stored in plain text files

No database is used

Limited input validation

No automated tests

All functionality is currently contained in one Python file

These limitations provide opportunities for future versions.

🚧 Future Improvements
💾 Better Data Storage
Move from text files to structured formats such as:

Text Files
    ↓
JSON
    ↓
SQLite
    ↓
SQL Database

📊 Financial Reports
Add:

Total income

Total expenses

Remaining balance

Monthly income

Monthly expenses

Profit/loss

Category-wise spending

Highest expense

📅 Better Date Filtering
Allow users to view:

Daily expenses

Weekly expenses

Monthly expenses

Yearly expenses

Custom date ranges

🏷️ Category Analysis
Provide summaries such as:

Food          ₹4,500
Transport     ₹2,000
Entertainment ₹1,500
Shopping      ₹3,000

🧪 Testing
Add tests for:

Adding expenses

Removing expenses

Adding income

Monthly calculations

Date validation

Invalid input

Edge cases

🖥️ User Interface
Possible future versions could include:

Tkinter GUI

Web interface

Charts and visualizations

Dashboard

▶️ How to Run
Navigate to the project directory:

cd "Python Expense Tracker"

Run the program:

python expense_tracker.py

If your Python file has a different name, replace expense_tracker.py with the appropriate filename.

🌱 Future Direction
This project is part of my Python Labs repository and represents an early step in learning how to build applications that work with real-world data.

The project can gradually evolve from:

Python Fundamentals
        ↓
File Handling
        ↓
Structured Data
        ↓
JSON
        ↓
Object-Oriented Design
        ↓
Databases
        ↓
Data Analysis
        ↓
Larger Applications

Build → Break → Debug → Understand → Improve