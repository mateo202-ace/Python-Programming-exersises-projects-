import tkinter as tk
from tkinter import simpledialog, messagebox
from models.library import Library
from models.book import Book


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Personal Library Manager")
        self.root.geometry("500x400")
        self.root.configure(bg="#808080")  # Light gray background

        self.library = Library("My Library")

        # Title Label
        title_label = tk.Label(
            root, text="📖 My Library", font=("Arial", 16, "bold"), bg="#f5f5f5"
        )
        title_label.pack(pady=10)

        # Book List Display
        self.book_listbox = tk.Listbox(root, width=50, height=20, font=("Comic Sans MS", 12))
        self.book_listbox.pack(pady=10)
        self.load_books()

        # Button Frame
        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=10)

        # Styled Buttons
        btn_style = {
            "font": ("Arial", 10, "bold"),
            "bg": "#007BFF",
            "fg": "white",
            "width": 15,
        }

        self.add_button = tk.Button(button_frame, text="➕ Add Book", command=self.add_book, **btn_style)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(button_frame, text="❌ Remove Book", command=self.remove_book, **btn_style)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.random_button = tk.Button(
            button_frame,
            text="🎲 Pick Random",
            command=self.pick_random_book,
            **btn_style,
        )
        self.random_button.grid(row=1, column=0, padx=5, pady=5)

        self.switch_library = tk.Button(button_frame, text="📚 Switch Librarys", command=self.switch_library, **btn_style)
        self.switch_library.grid(row=3, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(button_frame, text="🚪 Exit", command=root.quit, **btn_style)
        self.quit_button.grid(row=1, column=1, padx=5, pady=5)

    def load_books(self):
        """Load books into the listbox"""
        self.book_listbox.delete(0, tk.END)  # Clear list
        for book in self.library.books:
            self.book_listbox.insert(
                tk.END, f"{book.title} - {book.author} [{book.status}]"
            )

    def add_book(self):
        """Add a new book using input dialogs"""
        title = simpledialog.askstring("Input", "Enter book title:")
        author = simpledialog.askstring("Input", "Enter book author:")
        genre = simpledialog.askstring("Input", "Enter book genre (comma-separated):")

        if title and author and genre:
            new_book = Book(title, author, genre.split(", "))
            self.library.add_book(new_book)
            self.load_books()
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def remove_book(self):
        """Remove a selected book"""
        selected_index = self.book_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Select a book to remove!")
            return

        book_title = self.book_listbox.get(selected_index[0]).split(" - ")[0]
        if self.library.remove_book(book_title):
            self.load_books()
            messagebox.showinfo("Success", "Book removed!")
        else:
            messagebox.showerror("Error", "Book not found!")

    def pick_random_book(self):
        """Pick a random book to read"""
        book = self.library.pick_random_book()
        if isinstance(book, Book):
            messagebox.showinfo(
                "📖 Read This Book!", f"Try reading: {book.title} by {book.author}"
            )
        else:
            messagebox.showwarning(
                "No Books", "No books available in the 'To Be Read' list."
            )

    def switch_library(self):
        """Switch the current library to the new one by selecting a new CSV file"""
        new_csv_file = simpledialog.askstring(
            "Switch Library", "Enter the path to the new library CSV file:"
        )
        if new_csv_file:
            result = self.library.switch_lib(new_csv_file)
            self.load_books()
            messagebox.showinfo("Library Switch", result)
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid file path.")

        self.load_books()


# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
