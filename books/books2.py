import csv
import os

FILENAME = "books.csv"

# ---------------- LOAD DATA ----------------
def load_books():
    books = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    return books

# ---------------- SAVE DATA ----------------
def save_books(books):
    with open(FILENAME, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["S.No", "Book Name", "Author", "Publisher", "Edition Year", "ISBN"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

# ---------------- ADD BOOK ----------------
def add_book(books):
    print("\nAdd New Book")
    book_name = input("Enter Book Name: ").strip()
    if not book_name:
        print("Book name cannot be empty.")
        return

    author = input("Enter Author: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    publisher = input("Enter Publisher (press Enter to skip): ").strip()
    edition = input("Enter Edition Year (press Enter to skip): ").strip()
    isbn = input("Enter ISBN (press Enter to skip): ").strip()

    serial = str(len(books) + 1)

    books.append({
        "S.No": serial,
        "Book Name": book_name,
        "Author": author,
        "Publisher": publisher,
        "Edition Year": edition,
        "ISBN": isbn
    })

    save_books(books)
    print("Book saved successfully.")

# ---------------- VIEW BOOKS ----------------
def view_books(books):
    if not books:
        print("No books available.")
        return

    print("\nAll Books:\n")
    for book in books:
        print("------------------------------")
        print("Serial Number:", book["S.No"])
        print("Book Name:", book["Book Name"])
        print("Author:", book["Author"])
        print("Publisher:", book["Publisher"])
        print("Edition Year:", book["Edition Year"])
        print("ISBN:", book["ISBN"])

# ---------------- SEARCH BOOK ----------------
def search_books(books):
    term = input("Enter Book Name or Author to search: ").lower().strip()

    found = False
    for book in books:
        if term in book["Book Name"].lower() or term in book["Author"].lower():
            print("------------------------------")
            print("Serial Number:", book["S.No"])
            print("Book Name:", book["Book Name"])
            print("Author:", book["Author"])
            print("Publisher:", book["Publisher"])
            print("Edition Year:", book["Edition Year"])
            print("ISBN:", book["ISBN"])
            found = True

    if not found:
        print("No matching book found.")

# ---------------- EDIT BOOK ----------------
def edit_book(books):
    serial = input("Enter Serial Number to edit: ").strip()

    for book in books:
        if book["S.No"] == serial:
            print("Press Enter to keep current value.")

            new_name = input(f"Book Name ({book['Book Name']}): ").strip()
            if new_name:
                book["Book Name"] = new_name

            new_author = input(f"Author ({book['Author']}): ").strip()
            if new_author:
                book["Author"] = new_author

            new_publisher = input(f"Publisher ({book['Publisher']}): ").strip()
            if new_publisher:
                book["Publisher"] = new_publisher

            new_edition = input(f"Edition Year ({book['Edition Year']}): ").strip()
            if new_edition:
                book["Edition Year"] = new_edition

            new_isbn = input(f"ISBN ({book['ISBN']}): ").strip()
            if new_isbn:
                book["ISBN"] = new_isbn

            save_books(books)
            print("Book updated successfully.")
            return

    print("Serial number not found.")

# ---------------- MAIN MENU ----------------
def main():
    books = load_books()

    while True:
        print("\nMain Menu")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Edit Book")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            edit_book(books)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
