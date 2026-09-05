
def add_books():
    number_of_books = int(input("number of books you want to add : \n"))
    with open("books.txt",'a') as f:
        for i in range(number_of_books):
            add = input("write the name of book you want to add : \n")
            f.write(f"{add} \n")
    
def remove_books():
    book = input("Enter the book you want to remove : \n")
    with open("books.txt", "r") as f:
        a = f.readlines()
    with open("books.txt",'w') as f:
        found = False

        for line in a:
            if line.strip() == book:
                found = True
            else:
                f.write(line)

    if found:
        print("book removed")
    else:
        print("book not found")


def show_books():
    with open('books.txt','r') as f:
        data = f.read()
        print(data)

def status_book():
    book = input("Enter the book you want to check : \n")
    with open("books.txt",'r') as f:
        a = f.readlines()
    found = False
    for line in a:
        if line.strip() == book:
            found = True
    if found:
        print("book is available")
    else:
        print("book not found")

def search_books():
    book = input("Enter the book you want to search ")
    with open("books.txt",'r') as f:
        a = f.readlines()
        for line in a:
         line = line.strip()
         if book.lower() in line.lower():
            print("book found")
         else:
            print("no book found")
    
def borrow_books():
    book = input("Enter the book you want to borrow : \n")
    with open("books.txt", "r") as f:
        a = f.readlines()
    found = False

    for line in a:
        if line.strip() == book:
            found= True

    if found:
        with open("books.txt",'a') as f:
            f.write(f"{book} \n")

        print("book borrowed")
    else:
        print("book not found")


def return_books():
    book = input("Enter the book you want to return : \n")

    with open("books.txt", 'r') as f:
        a = f.readlines()
    found =False
    with open("borrowed.txt",'w') as f:
        for line in a:
            if line.strip() == book:
                found = True
            else:
                f.write(line)

    if found:
        print("book returned")
    else:
        print("book was not borrowed")


def change_name_of_book():
    return

def exit_program():
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
    print("4.search_books")
    print("5.borrow_books")
    print("6.return_books")
    print("7.change_name_of_book")
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
            search_books()
        elif user == 5:
            borrow_books()
        elif user == 6:
            return_books()
        elif user == 7:
            exit_program()
            break
       
        else:
            print(" Value Exceeded from the current choices !!")

    except ValueError:
        print("Invalid Value Entered !!")