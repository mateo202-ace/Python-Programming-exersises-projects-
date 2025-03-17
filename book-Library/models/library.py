import csv
import random
from models.book import Book


class Library:
    def __init__(self, name, csv_file="data/book.csv"):

        # initializes a library, creates the name and the empty library
        self.name = name
        self.csv_file = csv_file
        self.books = self.load_books_from_csv()  # Auto loads books on startup

    def load_books(self):
        # loads books from a CSV file into the library

        books = []
        try:
            with open(self.csv_file, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        row["Book Name"].strip(),
                        row["Auther"].strip(),
                        row["Genre - Theme - Type"]
                        .strip()
                        .split(" - "),  # Convert Genre into a list
                        row["Status"].strip(),
                    )
                    books.append(book)
        except FileNotFoundError:
            print(
                print(
                    f"⚠️ Warning: {self.csv_file} not found. Starting with an empty library."
                )
            )
            return books

    def save_books_to_csv(self):
        # Saves the current books list to the CSV file
        with open(self.csv_file, "w", newline="", encoding="utf-8") as file:
            filednames = ["Book Name", "Author", "Genre - Theme - Type", "Status"]
            writer = csv.DictWriter(file, fieldnames=filednames)
            writer.writeheader
            for book in self.books:
                writer.writerow(
                    {
                        "Book Name:": book.title,
                        "Author": book.author,
                        "Genre - Theme - Type": " - ".join(book.genre),
                        "Status": book.status,
                    }
                )

    def add_book(self, book):
        # adds a book to the library
        self.books.append(book)
        self.save_books_to_csv()

    def remove_book(self, title):
        # loops through the Library Removes book by title

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books_to_csv()
                return True

        return False

    def pick_random_book(self):
        return random.choice(self.books) if self.books else "📖 No books available!"

    def list_books(self):
        # list books on readable format
        return (
            "\n".join(str(book) for book in self.books)
            if self.books
            else "No books in this library"
        )
