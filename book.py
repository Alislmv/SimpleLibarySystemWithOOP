class Book:
    def __init__(self, bookID, title, author, pageCount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.isAvailable = True
 
    def showInfo(self):
        print(f"""
 
ID: {self.bookID}
Title: {self.title}
Author: {self.author}
pageCount: {self.pageCount}
        """)
 
        if self.isAvailable:
            print("Status: Available.")
        else:
            print("Status: Borrowed.")


    def borrow(self):
        if self.isAvailable:
            self.isAvailable = False
            print(f"{self.title} borrowed.")

        else:
            print("This book is already in the libary.")


    def returnBook(self):
        if not self.isAvailable:
            self.isAvailable = True
            print(f"{self.title} returned")

        else:
            print("\nThis book is already in the libary")
 
book1 = Book(1, "Clean Code", "Robert Martin", 464)
book2 = Book(2, "Python Crash Course", "Eric Matthes", 560)
book3 = Book(3, "Atomis Habits", "James Clear", 320)
 
# for i in book1, book2, book3:
#     i.showInfo()