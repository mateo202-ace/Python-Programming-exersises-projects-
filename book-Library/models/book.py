# this class stores book info and sees if it as been read or not and has an easy print string


class Book:
    def __init__(self, title, author, genre, status="To Be Read"):
        # Initializes a book object

        self.title = title
        self.author = author
        self.genre = (
            genre if isinstance(genre, list) else [genre]
        )  # Ensures genre is always a list
        self.status = status

    def marked_as_unread(self):
        # marks book as unread
        self.status = "Finished"

    def __str__(self):
        status = "Book has been read" if self.read else "Book has not been read"
        return f"{self.title} by {self.author} Its a:{self.genre} Status: [{status}]"
