
def add_books():
    with open("books.txt",'a') as f:
        add = input("write the name of book you want to add")
        f.write(add)

    
def remove_books():
    return
def show_books():
    with open('books.txt','r') as f:
        data = f.read()
        print(data)
def status_book():
    return
def search_books():
    book = str(input("Enter the book you want to search "))
    with open("books.txt",'r') as f:
        a = f.readlines()
        if book == a:
            print("book found")
        else:
            print("no book found")
    
def borrow_books():
    return
def return_books():
    return
def exit():
    print("successfully loged out \n Have a good day")
    

while True:
    print("Welcome Buddy !!")
    print("===Library Management System===")
    # chose = input("press 1 if admin \n press 2 if user")
    # password = "admin@123"
    # if chose == 1:
    #     key = input("enter the password")
    #     if key == password:
    #         print("welcome admin")
    #     else:
    #         print("retry")

    # if chose == 2:
    #     print("Welcome user")
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

