# Book management operations

books = [
    {"id": 101, "title": "Python", "author": "John", "available": True},
    {"id": 102, "title": "Java", "author": "James", "available": True},
    {"id": 103, "title": "C++", "author": "David", "available": True}
]

def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter title: ")
    author = input("Enter author: ")

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })

    print("Book added.")

def search_book():
    title = input("Enter title: ").lower()

    for book in books:
        if book["title"].lower() == title:
            print(book)
            return

    print("Book not found.")

def issue_book():
    book_id = int(input("Enter book ID: "))

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued.")
            else:
                print("Book is not available.")
            return

    print("Book not found.")

def return_book():
    book_id = int(input("Enter book ID: "))

    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            print("Book returned.")
            return

    print("Book not found.")

def display_available():
    for book in books:
        if book["available"]:
            print(book)

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")\n