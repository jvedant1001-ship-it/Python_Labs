def add_expense():
    print("haki")

def show_expense():
    print("haki")
    
def remove_expense():
    print("haki")

def view_expense():
    print("haki")

def monthly_expense():
    print("haki")

def exit():
    print("Exited the program succefully")


print("\n===PERSONAL EXPENSE TRACKER===\n")
print("1.add_expense")
print("2.show_expense")
print("3.remove_expense")
print("4.view_expense")
print("5.monthly_expense")
print("6.view_expense")
print("7.exit")

try:
    user = int(input("Choose an option \n"))

    if user == 1:
        add_expense()
    elif user == 2:
        show_expense()
    elif user == 3:
        remove_expense()
    elif user == 4:
        view_expense()
    elif user == 5:
        monthly_expense()
    elif user == 6:
        view_expense()
    elif user == 7:
        exit()
    else:
        print(" Value Exceeded from the current choices !!")

except ValueError:
    print("Invalid Value Entered !!")


print("Thank you for using PERSONAL EXPENSE TRACKER \n Have a Nice Day !!")
