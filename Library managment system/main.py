import tkinter as tk
from tkinter import messagebox

books = []

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if title == "" or author == "" or year == "":
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "status": "Available"
    }

    books.append(book)

    clear_entries()
    show_books()

def show_books():
    books_list.delete(0, tk.END)

    for index, book in enumerate(books, start=1):
        text = (
            f"{index}. {book['title']} | "
            f"{book['author']} | "
            f"{book['year']} | "
            f"{book['status']}"
        )

        books_list.insert(tk.END, text)

def select_book(event):
    selected = books_list.curselection()

    if not selected:
        return

    index = selected[0]
    book = books[index]

    title_entry.delete(0, tk.END)
    title_entry.insert(0, book["title"])

    author_entry.delete(0, tk.END)
    author_entry.insert(0, book["author"])

    year_entry.delete(0, tk.END)
    year_entry.insert(0, book["year"])

def search_book():
    search_title = title_entry.get().lower()

    books_list.delete(0, tk.END)

    for index, book in enumerate(books, start=1):
        if search_title in book["title"].lower():
            text = (
                f"{index}. {book['title']} | "
                f"{book['author']} | "
                f"{book['year']} | "
                f"{book['status']}"
            )

            books_list.insert(tk.END, text)

def borrow_book():
    selected = books_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a book first."
        )
        return

    index = selected[0]
    book = books[index]

    if book["status"] == "Available":
        book["status"] = "Borrowed"
        messagebox.showinfo(
            "Borrow",
            "Book borrowed successfully!"
        )
        show_books()

    else:
        messagebox.showwarning(
            "Borrow",
            "This book is already borrowed."
        )

def return_book():
    selected = books_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a book first."
        )
        return

    index = selected[0]
    book = books[index]

    if book["status"] == "Borrowed":
        book["status"] = "Available"
        messagebox.showinfo(
            "Return",
            "Book returned successfully!"
        )
        show_books()

    else:
        messagebox.showwarning(
            "Return",
            "This book was not borrowed."
        )

def delete_book():
    selected = books_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a book first."
        )
        return

    index = selected[0]

    books.pop(index)

    clear_entries()
    show_books()

    messagebox.showinfo(
        "Delete",
        "Book deleted successfully!"
    )


def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)


window = tk.Tk()

window.title("Library Management System")
window.geometry("800x600")


input_frame = tk.Frame(window)
input_frame.pack(pady=15)


# Title
tk.Label(
    input_frame,
    text="Book Title"
).grid(row=0, column=0, padx=5, pady=5)

title_entry = tk.Entry(
    input_frame,
    width=35
)
title_entry.grid(row=0, column=1, padx=5, pady=5)


# Author
tk.Label(
    input_frame,
    text="Author"
).grid(row=1, column=0, padx=5, pady=5)

author_entry = tk.Entry(
    input_frame,
    width=35
)
author_entry.grid(row=1, column=1, padx=5, pady=5)


# Year
tk.Label(
    input_frame,
    text="Year"
).grid(row=2, column=0, padx=5, pady=5)

year_entry = tk.Entry(
    input_frame,
    width=35
)
year_entry.grid(row=2, column=1, padx=5, pady=5)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)


add_button = tk.Button(
    button_frame,
    text="Add Book",
    width=15,
    command=add_book
)
add_button.grid(row=0, column=0, padx=5)


search_button = tk.Button(
    button_frame,
    text="Search",
    width=15,
    command=search_book
)
search_button.grid(row=0, column=1, padx=5)


borrow_button = tk.Button(
    button_frame,
    text="Borrow",
    width=15,
    command=borrow_book
)
borrow_button.grid(row=0, column=2, padx=5)


return_button = tk.Button(
    button_frame,
    text="Return",
    width=15,
    command=return_book
)
return_button.grid(row=0, column=3, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=15,
    command=delete_book
)
delete_button.grid(row=0, column=4, padx=5)

tk.Label(
    window,
    text="Books",
    font=("Arial", 14, "bold")
).pack(pady=5)

books_list = tk.Listbox(
    window,
    width=100,
    height=15
)
books_list.pack(pady=10)
# When user clicks a book
books_list.bind(
    "<<ListboxSelect>>",
    select_book
)

window.mainloop()


# #books = [] #ساخت لیست
#
# #while True: #اجرای مدوام برنامه
#    # print("\n===== Library Management System =====") #منو برنامه
#    # print("1. Add Book")
#     #print("2. Show Books")
#     print("3. Search Books")
#     print("4. Borrow book")
#     print("5. return book")
#     print("6. Delete book")
#     print("7. Exit")
#
#
#     choice = input("Choose an option: ") #گرفتن انتخاب
#
#     if choice == "1": #چون همیشه استرینگه
#         title = input("Enter the book title: ")
#         author = input("Enter the author name: ")
#         year = input("Enter the year: ")
#
#         book = { #اطلاعات یک کتاب در دیکشتری
#             "title": title,
#             "author": author,
#             "year" : year,
#             "status": "Available"
#         }
#
#         books.append(book) #اضافه کردن به لیست
#
#         print("Book added successfully!")
#
#     elif choice == "2":
#
#         if len(books) == 0: #بررسی اگر کتابی وجود دارد یا نه
#             print("No books found.")
#
#         else:
#             for index, book in enumerate(books, start=1):
#                 print(f"\n{index}. {book['title']}")
#                 print(f"   Author: {book['author']}")
#                 print(f"   Year: {book['year']}")
#                 print(f"   Status: {book['status']}")
#
#     elif choice == "3":
#         search_title = input("Enter the book title to search: ")
#
#         found = False #هنور کتابی نیست
#
#         for book in books:
#             if search_title.lower() == book["title"].lower(): #حروف کوچیک میشود
#                 print("\nBook found!")
#                 print(f"Title: {book['title']}")
#                 print(f"Author: {book['author']}")
#                 print(f"Year: {book['year']}")
#                 print(f"Status: {book['status']}")
#
#                 found = True #اگر کتاب پیدا شد
#
#         if not found : #کتاب نیست
#             print("Book not found.")
#
#     elif choice == "4":
#         borrow_title = input("Enter the book title to borrow: ")
#         found = False
#
#         for book in books:
#             if borrow_title.lower() == book["title"].lower():
#                 found = True
#
#                 if book["status"] == "Available":
#                     book["status"] = "Borrowed"
#                     print(f"\nBook borrowed successfully!")
#
#                 else:
#                     print("this book is already borrowed")
#
#         if not found :
#             print("Book not found.")
#
#
#     elif choice == "5":
#        return_title = input("Enter the book title to return: ")
#        found = False
#
#        for book in books:
#             if return_title.lower() == book["title"].lower():
#                 found = True
#
#                 if book["status"] == "Borrowed":
#                     book["status"] = "Available"
#                     print("Book returned successfully!")
#                 else:
#                     print("This book was not borrowed.")
#
#                 if not found:
#                  print("Book not found.")
#
#     elif choice == "6":
#         delete_title = input("Enter the book title to delete: ")
#
#         found = False
#
#         for book in books:
#             if delete_title.lower() == book["title"].lower():
#                 books.remove(book)
#                 found = True
#
#                 print("Book deleted successfully!")
#                 break
#
#         if not found:
#             print("Book not found.")
#
#     elif choice == "7": #خروج از برنامه
#         print("Goodbye!")
#         break
#
#     else:
#         print("Invalid option. Please try again.")