
def add_books():
    return
def remove_books():
    return
def show_books():
    return
def status_book():
    return
def search_books():
    return
def borrow_books():
    return
def return_books():
    return
def exit():
    print("successfully loged out \n Have a good day")
    


print("Welcome Buddy !!")
print("===Library Management System===")
print("1.add_books")
print("2.show_books")
print("3.remove_books")
print("4.view_books")
print("5.search_books")
print("6.borrow_books")
print("7.return_books")
print("8.exit")

try:
    user = int(input("Choose an option \n"))

    if user == 1:
        add_books()
    elif user == 2:
        show_books()
    elif user == 3:
        remove_books()
    elif user == 4:
        show_books()
    elif user == 5:
        search_books()
    elif user == 6:
        borrow_books()
    elif user == 7:
            return_books()
    elif user == 8:
        exit()
    else:
        print(" Value Exceeded from the current choices !!")

except ValueError:
    print("Invalid Value Entered !!")

