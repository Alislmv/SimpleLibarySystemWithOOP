from book import *
from student import *
from libary import *


libary = Libary("Libary")

libary.addBook(book1)
libary.addBook(book2)
libary.addBook(book3)

libary.addStudent(student1)
libary.addStudent(student2)
libary.addStudent(student3)


while True:
    print("""
===== LIBARY MANAGEMENT SYSTEM =====

1. Show Books
2. Show Students
3. Borrow Book
4. Return Book
5. Search Book
6. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        libary.showBooks()

    elif choice == "2":
        libary.showStudents()

    elif choice == "3":
        studentID = int(input("Enter Student ID: "))
        bookID = int(input("Enter Book ID: "))
        libary.borrowBook(studentID, bookID)

    elif choice == "4":
        studentID = int(input("Enter Student ID: "))
        bookID = int(input("Enter Book ID: "))
        libary.returnBook(studentID, bookID)

    elif choice == "5":
        bookID = int(input("Enter Book ID: "))
        book = libary.searchBook(bookID)

        if book:
            book.showInfo()
        else:
            print("Book not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")