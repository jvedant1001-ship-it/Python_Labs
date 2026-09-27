# 🏦 Banking Management System

A console-based **Banking Management System built with Python** to practice Object-Oriented Programming, file handling, data persistence, authentication, transaction management, and structured program design.

This project simulates basic banking operations such as creating accounts, logging in, depositing and withdrawing money, transferring funds, viewing transaction history, changing PINs, and calculating savings-account interest.

> 🚧 This is an educational project and is not intended for real-world banking or financial use.

---

## 📌 Features

### 👤 Account Management

- Create a new bank account
- Automatically generate account numbers
- Support for:
  - Savings Account
  - Current Account
- Store account holder information
- View account details

### 🔐 Authentication

- 4-digit PIN-based login
- PIN verification
- Change existing PIN
- Basic input validation

### 💰 Banking Operations

- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- Validate insufficient balance
- Enforce minimum balance requirements for Current Accounts

### 📊 Transaction History

Every successful transaction can be recorded with:

- Transaction type
- Amount
- Remaining/current balance
- Date and time

Example:

```text
TRANSACTION HISTORY
-----------------------------------------------------------------
2026-09-26 20:30:12 | Deposit              | ₹5000.00    | Balance: ₹15000.00
2026-09-26 20:35:41 | Withdrawal            | ₹2000.00    | Balance: ₹13000.00
💾 Persistent Data
Account information and transaction history are stored in:

bank_data.json

The application loads the saved data when it starts and updates the JSON file after changes.

🧱 Object-Oriented Design
One of the main goals of this project was to practice Object-Oriented Programming (OOP).

The project uses a base Account class with specialized account types.

                    Account
                   /       \
                  /         \
                 ▼           ▼
       SavingsAccount    CurrentAccount

Account
The base class contains common functionality such as:

Account information

PIN verification

Deposits

Withdrawals

Transaction history

PIN changes

Account details

JSON serialization

SavingsAccount
Extends Account and adds:

Interest rate

Interest calculation

CurrentAccount
Extends Account and adds:

Minimum balance requirement

Customized withdrawal behavior

Bank
Responsible for managing the collection of accounts and handling:

Account creation

Login

Account number generation

Money transfers

Saving data

Loading data

🧠 OOP Concepts Practiced
This project helped me practice several important Python OOP concepts:

Concept	Where It Is Used
Classes & Objects	Account, Bank, SavingsAccount, CurrentAccount
Inheritance	SavingsAccount and CurrentAccount inherit from Account
Method Overriding	CurrentAccount.withdraw()
Encapsulation	PIN stored using _pin
Polymorphism	Different account types provide specialized behavior
Constructors	__init__() methods
Instance Methods	Banking and account operations

🛠️ Technologies & Python Features
Language
🐍 Python 3

Python Modules
import json
import os
from datetime import datetime

Concepts Used
Object-Oriented Programming

Classes and objects

Inheritance

Method overriding

Encapsulation

Dictionaries

Lists

Functions

Loops

Conditional logic

Exception handling

File handling

JSON serialization

Date and time handling

Input validation

📂 Project Structure
Banking Project/
│
├── bank.py
├── bank_data.json
├── README.md
└── .gitignore

bank.py
Contains the complete banking application including:

Account classes

Bank management

Authentication

Transactions

Menu system

Data persistence

bank_data.json
Stores account information and transaction history so data persists between program executions.

README.md
Project documentation.

▶️ How to Run
1. Clone the repository
git clone <your-repository-url>

2. Navigate to the project
cd "Banking Project"

3. Run the program
python bank.py

On Windows, you can also use:

python bank.py

🖥️ Main Menu
When the program starts, you will see:

BANKING MANAGEMENT SYSTEM
1. Create Account
2. Login
3. Exit

Enter your choice:

After logging in, the account menu provides:

Welcome, User

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Transaction History
6. Account Details
7. Change PIN
8. Calculate Interest
9. Logout

💡 Example Workflow
A typical session can look like:

Create Account
      ↓
Generate Account Number
      ↓
Login with Account Number + PIN
      ↓
Check Balance
      ↓
Deposit / Withdraw
      ↓
Transfer Money
      ↓
View Transaction History
      ↓
Logout

Account information is saved to bank_data.json, allowing it to be loaded again the next time the program runs.

💾 Data Persistence
The project uses Python's built-in json module to store application data.

Example structure:

{
    "100001": {
        "account_number": "100001",
        "name": "Example User",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": [],
        "account_type": "Savings",
        "interest_rate": 4
    }
}

This allowed me to practice converting Python objects and data structures into persistent structured data.

⚠️ Validation & Error Handling
The application performs several validation checks, including:

Empty account holder names

Invalid PIN formats

Invalid numeric input

Negative deposit amounts

Negative withdrawal amounts

Insufficient account balance

Invalid account numbers

Invalid account types

Current Account minimum balance requirements

Attempting to transfer money to the same account

Missing or corrupted JSON data

Python exception handling is used to prevent invalid input from crashing the application.

🔐 Security Note
This project is designed for learning purposes.

PINs are currently stored in the JSON file in plain text. This is not appropriate for a real banking application.

A future version could improve this by implementing:

Password/PIN hashing

Better authentication

Database-based storage

User authorization

Secure session management

More robust input validation

Transaction integrity controls

The current implementation intentionally keeps the architecture simple so the focus remains on learning Python and OOP concepts.

🚧 Current Limitations
This is a console-based educational project, so it currently does not include:

Graphical user interface

Web interface

Database integration

Secure PIN hashing

Multi-user sessions

Automated testing

Real banking APIs

Transaction rollback mechanisms

Advanced financial calculations

These are possible directions for future versions.

🔮 Future Improvements
Some improvements I would like to explore:

🗄️ Database
Replace JSON storage with:

SQLite

SQL

Relational database design

🔐 Security
Hash PINs instead of storing them directly

Improve authentication

Add account lockout mechanisms

🧪 Testing
Unit tests

Integration tests

Edge-case testing

Automated test suites

🖥️ User Interface
Possible future versions could use:

Tkinter

Web-based interface

REST API + frontend

🏗️ Architecture
Further improvements could include:

Separating business logic from user interface

Multiple Python modules

Service classes

Better error handling

Logging

More structured project architecture

📚 What I Learned
This project helped me move from writing individual Python functions toward thinking about how multiple components work together.

Some of the main things I practiced were:

Designing classes around real-world concepts

Using inheritance to share common functionality

Overriding methods for specialized behavior

Managing relationships between objects

Persisting application data

Handling invalid user input

Designing program flow

Debugging unexpected behavior

Structuring a larger Python program

One of the biggest lessons from this project was that building an application involves more than making individual features work.

It requires thinking about:

Requirements
     ↓
Program Structure
     ↓
Data
     ↓
Business Logic
     ↓
Validation
     ↓
Persistence
     ↓
User Interaction

🎯 Learning Goals
This project was built as part of my ongoing journey to strengthen:

🐍 Python

🧱 Object-Oriented Programming

🧠 Problem Solving

💾 Data Persistence

🐞 Debugging

🏗️ Program Design

🧪 Testing

🔧 Code Improvement

It is one step in my broader goal of becoming stronger in software development and eventually moving toward AI/ML development.

