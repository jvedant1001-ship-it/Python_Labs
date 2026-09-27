# 📚 Library Management System

A simple **command-line Library Management System built with Python**.

This project was created to practice Python fundamentals such as **functions, loops, conditional logic, file handling, string manipulation, exception handling, and basic data management**.

The application allows users to manage a collection of books through a menu-driven interface.

> 🚧 This is an educational project created while learning Python. It is not intended to represent a production-ready library management system.

---

## ✨ Features

The current application provides the following functionality:

### ➕ Add Books

Allows the user to add multiple books to the library.

The program asks how many books should be added and then accepts each book name individually.

Books are stored in:

```text
books.txt
📖 Show Books
Displays all books currently stored in the library.

The application reads the contents of books.txt and prints them to the terminal.

🗑️ Remove Books
Allows a user to remove a book by entering its exact name.

The program:

Reads the existing books

Searches for the requested book

Rewrites the file without the selected book

Reports whether the book was found

🔎 Search Books
Allows users to search for a book by name.

The search is case-insensitive and supports partial matches.

For example:

Search: harry

Harry Potter
Harry Potter and the Chamber of Secrets

📤 Borrow Books
The current implementation checks whether a requested book exists before attempting to record the borrowing action.

This feature is an early implementation and is planned for improvement as the project evolves.

📥 Return Books
A return operation is included in the program and demonstrates working with a separate file:

borrowed.txt

This part of the project is currently being improved and will eventually use a more structured approach for tracking borrowed books.

🚪 Exit
Allows the user to exit the application through the menu.

🖥️ Application Menu
When the program starts, it displays:

Welcome Buddy !!
===Library Management System===

1.add_books
2.show_books
3.remove_books
4.search_books
5.borrow_books
6.return_books
7.change_name_of_book
8.exit

Choose an option

The user selects an operation by entering the corresponding number.

🛠️ Technologies Used
Language
🐍 Python 3

Python Concepts
Functions

Loops

Conditional statements

Lists

File handling

String manipulation

strip()

lower()

Exception handling

try/except

User input

Basic program flow

Files Used
books.txt
borrowed.txt

The project uses simple text files instead of a database to practice Python file handling and persistent storage.

📂 Project Structure
Library Management System/
│
├── library.py
├── books.txt
├── borrowed.txt
└── README.md

File names may vary depending on the current version of the project.

library.py
Contains the main application logic and functions for managing books.

books.txt
Stores the books available in the library.

Example:

The Alchemist
Atomic Habits
Harry Potter
The Hobbit

borrowed.txt
Intended to store information related to borrowed books.

This functionality is currently being developed further.

🧩 Program Structure
The project is divided into separate functions, with each function responsible for a specific operation.

                    Library Management System
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
      Add Books           Show Books         Remove Books
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                Search              Borrow / Return

Some of the main functions are:

add_books()
remove_books()
show_books()
search_books()
borrow_books()
return_books()
exit_program()

This approach helped me practice breaking a larger program into smaller, reusable functions.

💾 File Handling
One of the main concepts practiced in this project is file handling.

Books are written to a text file using:

with open("books.txt", "a") as f:
    ...

Books can then be read using:

with open("books.txt", "r") as f:
    ...

The project also demonstrates rewriting files when removing data:

with open("books.txt", "w") as f:
    ...

The three modes used are:

Mode	Purpose
r	Read existing data
w	Rewrite/overwrite a file
a	Append new data

⚠️ Input Validation
The main menu uses exception handling to prevent invalid menu input from crashing the program.

try:
    user = int(input("Choose an option \n"))
except ValueError:
    print("Invalid Value Entered !!")

This allows the program to handle inputs such as:

abc
hello
3.5

without terminating unexpectedly.

🧠 Concepts Learned
This project helped me understand several important Python concepts.

Functions
Instead of putting everything into one large block of code, individual operations are separated into functions.

For example:

def add_books():
    ...

and:

def remove_books():
    ...

This makes the program easier to understand and modify.

File Handling
I learned how Python programs can store and retrieve information using files.

String Manipulation
The project uses methods such as:

strip()
lower()

to clean input and perform case-insensitive searches.

Loops
Loops are used to:

Add multiple books

Iterate through stored books

Search for matching books

Rewrite files while removing entries

Exception Handling
try/except is used to handle invalid user input.

🔄 Program Flow
The overall program follows a simple menu-driven loop:

Start
  │
  ▼
Display Menu
  │
  ▼
Get User Input
  │
  ▼
Validate Input
  │
  ├── Add Book
  ├── Show Books
  ├── Remove Book
  ├── Search Book
  ├── Borrow Book
  ├── Return Book
  ├── Change Book Name
  │
  ▼
Display Result
  │
  ▼
Return to Menu
  │
  ▼
Exit

▶️ How to Run
Make sure Python is installed on your system.

Navigate to the project directory:

cd "Library Management System"

Then run:

python library.py

If your Python file has a different name, replace library.py with the appropriate filename.

⚠️ Current Limitations
This project is still an early learning implementation.

Some areas that can be improved include:

Borrowed books are not properly separated from available books

Return functionality needs a more consistent borrowing system

change_name_of_book() is currently not implemented

Book records are stored as plain text

Duplicate books are possible

Book availability is not tracked using structured data

There is no user/account system

There is no admin authentication

The application does not use a database

Error handling can be expanded

The code is currently contained in a single Python file

These limitations provide opportunities for future improvements.

🚧 Future Improvements
Possible improvements for future versions include:

🧱 Object-Oriented Programming
Refactor the project using classes such as:

Library
   │
   ├── Book
   └── User

This would allow the project to practice concepts such as:

Classes

Objects

Encapsulation

Inheritance

Polymorphism

💾 Structured Data
Replace plain text files with:

JSON

SQLite

SQL databases

👤 User Management
Add:

User accounts

Login

User-specific borrowed books

Admin functionality

📚 Better Book Tracking
Track information such as:

Book
├── Title
├── Author
├── ID
├── Availability
└── Borrower

🔎 Improved Search
Add search by:

Book title

Author

Book ID

Category

🧪 Testing
Add automated tests for:

Adding books

Removing books

Searching

Borrowing

Returning

Invalid input

Edge cases

📚 What I Learned
The main purpose of this project was to understand how individual Python concepts can come together to create a working application.

Through this project, I practiced:

Breaking a problem into functions

Working with files

Managing program state

Processing user input

Handling invalid input

Searching through stored data

Updating persistent data

Debugging unexpected behavior

One of the biggest lessons was learning that getting a program to work is only the beginning.

As I learn more Python, I can revisit this project and improve its structure, data management, validation, and functionality.

🌱 Future Direction
This project is part of my broader Python Labs learning journey.

The next versions can gradually move from:

Text Files
    ↓
JSON
    ↓
Object-Oriented Design
    ↓
SQLite / SQL
    ↓
APIs
    ↓
Larger Applications

Each iteration will be an opportunity to apply concepts learned from later projects.

Build → Break → Debug → Understand → Improve