import datetime

def add_expense():
    #logic will be no.of entries then loops ask for category then amount date and print
    number_of_entries = int(input("number of entries you want to add : \n"))
    with open ('expense.txt','a') as f:
        for i in range(number_of_entries):
            category = input("enter the category for expense : \n")
            amount = input("enter the amount of expense spent : \n")
             
            date = input("enter the date as DD-MM-YYYY or enter for todays date : \n")
            if date == "":
                date = datetime.datetime.now(tz=None).strftime("%d-%m-%Y")
            else:
                date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%d-%m-%Y")

            f.write(f"{category}|{amount}|{date}\n")
   
def show_expense():
    #most simple just open the file and read and print the line
    with open("expense.txt","r") as f:
        data = f.read()
        print(data)#shows all the expenses
          
def remove_expense():
    # so for remove expense i will read the file split the string using | then for i ,amount categor.. enumerate
    #   and put it in list starting from 1 then ask user to remove whichever it wants 
    # and then i will use index - 1 so that it will match what user sees and then
    #  re write evrything and store it in expense txt again
    with open("expense.txt","r") as f:
            lines = f.readlines()
            expenses = []

            for line in lines:
                expense = line.strip().split("|")
                expenses.append(line)

            for i ,expense in enumerate(expenses,start = 1):
                print(f"{i}.category : {expense[0]} , amount : {expense[1]} , date : {expense[2]}")

            choice = int(input("Enter the number of expense you want to remove: "))
            index = choice -1 

            expense.pop(index)

            with open("expense.txt", "w") as f:
                for expense in expenses:

                       line = "|".join(expense)

            # Write the expense back into the file
            f.write(line + "\n")

    print("Expense removed successfully!")



    #as simple as it sound just make new txt and then add the income
    #i think its better to make another list for this ?
def add_income():
        income = input("Enter your income: ")
        date = input("Enter the date as DD-MM-YYYY or press Enter for today's date: ")
        if date == "":
            date = datetime.datetime.now(tz=None).strftime("%d-%m-%Y")
        else:
            date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%d-%m-%Y")

        with open("income.txt", "a") as f:
            f.write(f"{income}|{date}\n")

        print(f"Income of {income} added successfully!")

        #somehow i have to subtract the income from expense of the correct time wth!!!!!!!??????




def monthly_expense():
    month = input("Enter month and year (MM-YYYY): ")

    total = 0

    with open("expense.txt", "r") as f:
        for line in f:
            category, amount, date = line.strip().split("|")

            expense_month = date[3:10]  # gets MM-YYYY from DD-MM-YYYY

            if expense_month == month:
                print(f"Category: {category}, Amount: {amount}, Date: {date}")
                total += float(amount)

    print(f"\nTotal expense for {month}: {total}")

    #here i have to somehow check the date of the each shit all that and show that


def check_profit_or_loss(income,expense):
    if income > expense:
        print(f"you the real chad \n you have {income - expense} left ")
    elif income == expense:
        print("earn more spend less")
    else:
        print(f"you fucked chad \n you broke bitch \n negative {expense - income} \n bwahahahah")

# def exit(): no need o f ths
#     print("Exited the program succefully")
    

while(True):
    print("\n===PERSONAL EXPENSE TRACKER===\n")
    print("1.add_expense")
    print("2.show_expense")
    print("3.remove_expense")
    print("4.add_income")
    print("5.monthly_expense")
    print("6.exit")

    try:
        user = int(input("Choose an option \n"))

        if user == 1:
            add_expense()
        elif user == 2:
            show_expense()
        elif user == 3:
            remove_expense()
        elif user == 4:
            add_income()
        elif user == 5:
            monthly_expense()
        elif user == 6:
            break
        else:
            print(" Value Exceeded from the current choices !!")

    except ValueError:
        print("Invalid Value Entered !!")

print("Thank you for using PERSONAL EXPENSE TRACKER \n Have a Nice Day !!")
