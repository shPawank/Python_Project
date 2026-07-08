# Exercise 6 - Library Management System in Python
# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and demonstrate how you can:
# Print all books
# Add a book
# Get the number of books using different methods
# Also, show that your program does not persist the books after the program is stopped.

class Library:
    def __init__(self):            #constructor to initialize the instance variables
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"Number of books: {self.no_of_books}")
        print("The books in the library are:")
        for book in self.books:
            print(book)


l1 = Library()
l1.add_book("Atomic Habits")
l1.add_book("The Power of Habit")
l1.add_book("Deep Work")
l1.add_book("The 7 Habits of Highly Effective People")
l1.showInfo()