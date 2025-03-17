import random

class Library:
    def __init__(self, name: str):
        # initializes a library, creates the name and the empty library
        self.name = name
        self.books = []
    

    def add_book(self, book):
        # adds a book to the library
        self.books.append(book)
    
    def remove_book(self, title):
        # loops through the Library Removes book by title 

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove
                return True
            
        return False
    
    def list_books(self):
        # list books on readable format
        return '\n'.join(str(book) for book in self.books) if self.books else 'No books in this library'