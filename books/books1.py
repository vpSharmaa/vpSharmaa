import pandas as pd

# Lists to store book details
serial_numbers = []
book_names = []
authors = []
publishers = []
editions = []
isbns = []

print("Enter book details")
print("Type 'stop' as book name when finished\n")

serial = 1

while True:
    book = input("Enter name of the book: ").strip()

    # Stop condition
    if book.lower() == "stop":
        break

    if book == "":
        print("❌ Book name cannot be empty\n")
        continue

    author = input("Enter Author's name: ").strip()
    if author == "":
        print("❌ Author name cannot be empty\n")
        continue

    publisher = input("Enter publication details: ").strip()

    edition = input("Enter Edition year: ").strip()
    if not edition.isdigit():
        print("❌ Edition year must be numeric\n")
        continue

    isbn = input("Enter ISBN / ISSN number: ").strip()
    if not isbn.isdigit():
        print("❌ ISBN must contain digits only\n")
        continue

    # Append validated data
    serial_numbers.append(serial)
    book_names.append(book)
    authors.append(author)
    publishers.append(publisher)
    editions.append(int(edition))
    isbns.append(isbn)

    serial += 1
    print("✅ Book added successfully\n")

# Create DataFrame
df = pd.DataFrame({
    "S.No": serial_numbers,
    "Book Name": book_names,
    "Author": authors,
    "Publisher": publishers,
    "Edition Year": editions,
    "ISBN / ISSN": isbns
})

# Sort alphabetically by Book Name
df = df.sort_values(by="Book Name")

# Save to Excel
df.to_excel("books.xlsx", index=False)

print("\n📘 Excel file created successfully")
print(df)

# ---------------- SEARCH FUNCTION ----------------
while True:
    print("\nSearch Options:")
    print("1. Search by Book Name")
    print("2. Search by Author")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        search_book = input("Enter book name to search: ").strip().lower()
        result = df[df["Book Name"].str.lower().str.contains(search_book)]
        print(result if not result.empty else "❌ Book not found")

    elif choice == "2":
        search_author = input("Enter author name to search: ").strip().lower()
        result = df[df["Author"].str.lower().str.contains(search_author)]
        print(result if not result.empty else "❌ Author not found")

    elif choice == "3":
        print("Exiting search...")
        break

    else:
        print("❌ Invalid choice")
