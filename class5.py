# Book information

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

books = [
    Book(101, "Python Basics", "John", 450),
    Book(102, "Java Programming", "James", 550),
    Book(103, "Data Science", "David", 650)
]

for book in books:
    book.display()
