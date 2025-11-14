from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
#Challenge level 1 psuedo code:
# Print all books that have "available" = true with book id, author, and title. (loop through list using for loop?)
#-------   Old Code  --------
'''
def printBooks():
        for book in library_books:
            if book["available"]:
              print(book["id"]+"-", book["title"]+"-", book["author"])
'''


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
#Challenge level 2 psuedo code:
# get input from user about author and genre, print all books with that author or genre
# -------- Old Code -------
'''
def searchBooks():
    author = str.lower(input("what author are you looking for? "))
    genre = str.lower(input("What genre are you looking for? "))
    for book in library_books:
        if str.lower(book["author"]) == author or str.lower(book["genre"]) == genre:
            print(book["id"]+"-", book["title"]+"-", book["author"])
'''
            


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
# Challenge level 3 psuedo code:
# Create a function to checkout a book by ID - If the book is available, set the key to unavailable, set datetime to 2 weeks from today, 
# increment the checkouts counter, if the book is not available print message saying it is already checked out.
# -------- Old Code -------
'''
def checkout():
    bookCheck = input("Enter book ID: ")
    for book in library_books:
        if book["id"] == bookCheck:
            if book["available"]:
                book["available"] = False
                book["checkouts"] += 1
                book["due_date"] = datetime.today() + timedelta(weeks=2)
            else:
                print("That book is already checked out")
'''
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
# Challenge level 4 psuedo code:
# Get book ID from user, set its availability to true and clear the due_date
'''
def returnBook():
    bookId = input("Enter book ID: ")
    for book in library_books:
        if book["id"] == bookId:
            book["available"] = True
            book["due_date"] = None
'''
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
# Write another functions to list all overdue books (due_date before today + still checked out)
'''
def listOverdueBooks():
    for book in library_books:
        if book["available"] == False:
             if datetime.fromisoformat(book["due_date"]) < datetime.today():
                print(book["id"]+"-", book["title"]+"-", book["author"])
'''
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
#
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts    
b1 = Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, "None", 2)
b2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5)
b3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3)
b4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
b5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6)
b6 = Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8)
b7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
b8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3)
books = [b1, b2, b3, b4, b5, b6, b7, b8]


def viewBooks():
    for book in books:
        if book.available == True:
            print(book.id, "--", book.title, "--", book.author)


def searchBooks():
    bookFound = False
    author = input("what author are you looking for? ").lower()
    genre = input("What genre are you looking for? ").lower()
    for book in books:
        if book.author.lower() == author or book.genre.lower() == genre:
            print("\n", book.id, "--", book.title, "--", book.author)
            bookFound = True
    if bookFound == False:
        print("\nBook not found")


def checkout():
    bookCheck = input("Enter book ID: ")
    for book in books:
        if book.id == bookCheck:
            if book.available:
                book.available = False
                book.checkouts += 1
                book.due_date = datetime.today() + timedelta(weeks=2)
                print(f"\nSuccessfully checked out book, due date: {book.due_date}\n")
            else:
                print("\nThat book is already checked out\n")


def returnBook():
    bookReturned = False
    bookId = input("Enter book ID: ")
    for book in books:
        if book.id == bookId and book.available == False:
            book.available = True
            book.due_date = None
            bookReturned = True
    if bookReturned:
        print("\nBook successfully returned\n")
    else:
        print("\nError - Book already returned\n")


def listOverdueBooks():
    for book in books:
        if book.available == False:
             if datetime.fromisoformat(book.due_date) < datetime.today():
                 print("\n", book.id, "--", book.title, "--", book.author)
def library():
    while True:
        print("1. View\n2. Search\n3. Checkout\n4. Return\n5. Overdue Books\n6. Quit\n-----------------------")
        choice = int(input("<6 to quit>Select an option from 1 - 6: "))
        if choice == 1:
            print("Avalaible Books:")
            viewBooks()
            print("")
        if choice == 2:
            searchBooks()
            print("")
        if choice == 3:
            checkout()
        if choice == 4:
            returnBook()
        if choice == 5:
            listOverdueBooks()
        if choice == 6:
            break
library()






# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    pass