import pandas as pd

# Lists to store book details
book_names = []
authors = []
publishers = []
editions = []
isbns = []

print("Enter book details")
print("Type 'stop' as book name when you are done\n")

while True:
    book = input("Enter name of the book: ")

    # stop condition
    if book.lower() == "stop":
        break

    author = input("Enter Author's name: ")
    publisher = input("Enter publication details: ")
    edition = input("Enter Edition year: ")
    isbn = input("Enter ISBN No. or ISSN No.: ")

    # Append data to lists
    book_names.append(book)
    authors.append(author)
    publishers.append(publisher)
    editions.append(edition)
    isbns.append(isbn)

    print("Book added successfully\n")

# Create DataFrame
df = pd.DataFrame({
    "Book Name": book_names,
    "Author": authors,
    "Publisher": publishers,
    "Edition": editions,
    "ISBN / ISSN": isbns
})

# Save to Excel
df.to_excel("books.xlsx", index=False)

print("\nExcel file created successfully")
print(df)
