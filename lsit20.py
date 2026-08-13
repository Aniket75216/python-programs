books = ["Python", "Java", "C++"]

books.append("PHP")

book = input("Enter book name: ")

if book in books:
    print("Book Found")

books.remove("Java")

print("Books:", books)
print("Total Books:", len(books))