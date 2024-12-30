class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    # This method is used to define what should be returned when you call str() on an object or when you try to print the object.
    # When you print an object, Python uses the __str__ method to decide how to represent it as a string. Without this method, printing an object will just show some default, boring information about it.

    def __str__(self):
        pass

class Library():

    def __init__(self): 
        self.books = [] # here book variable is initialized as an empty list and it will store the book objects.

    def add_books(self, title, author):
        new_book = Book(title, author) # here we are creating a new Book object with the given title and author.
        self.books.append(new_book) # this new book object is added to the list of books in the library.
        # self.books[0] is a book object
        # print(self.books[0].title)
        print(f"Book \"{title}\" added to the library!")

    def display_books(self):
        if not self.books: 
            print("\nNo books in the library!")
        else:
            print("\nBook records:")
            for book in self.books: # here "book" variable is a "Book object"
                status = "Available" if book.is_available else "Borrowed"
                print(f"{book.title} by {book.author} [{status}]")
    
    def borrow_book(self, title):
        
        # Check if the book exists or not
        for book in self.books: 
            if book.title.lower() == title.lower():
                print("Book found!")
                
                if book.is_available:
                    print("Book borrowing success!")
                    book.is_available = False
                    return
                else:
                    print("but already taken by someone!")
                    return
        
        print("No book with this name")

    def return_book(self, title):

        # Check if the book exists or not
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book record found!")

                if not book.is_available:
                    print("Book returning process successful!")
                    book.is_available = True
                    return
        
        print("May be wrong library! No such book exists in our records.")

def main():
    library = Library()

    while True: # Infinite loop until user chooses to exit    

        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        match choice:
            case "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                library.add_books(title, author)
            case "2":
                library.display_books()
            case "3":
                title = input("Enter book title to borrow: ")
                library.borrow_book(title)
            case "4":
                title = input("Enter book title to return: ")
                library.return_book(title)
            case "5":
                print("\nThank you for visiting the library!")
                break
            case _:
                print("Invalid choice. Please try again.")

# Some code is only meant to run when the file is executed directly (like testing)
# It prevents code from running when the file is imported into another program.
if __name__ == "__main__":
    main()