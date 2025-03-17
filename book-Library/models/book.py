#this class stores book info and sees if it as been read or not and has an easy print string

class Book:
    def __init__(self, title: str, author: str, genre: str, year: int, read: bool = False):
        # Initializes a book object

        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.read = read

    def marked_as_unread(self):
        #marks book as unread
        self.read = False

    def marked_as_read(self):
        #marks book as read
        self.read = True

    def __str__(self):
        status = 'Book has been read' if self.read else 'Book has not been read'
        return f'{self.title} by {self.author} published in: {self.year}-{self.genre} [{status}]'