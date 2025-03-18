import tkinter as tk
from gui import LibraryApp

from models.book import Book
from models.library import Library

if __name__ == "__main__": 
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

