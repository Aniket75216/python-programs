# 20. Library Management
books = {
    "Python": True,
    "Java": True,
    "C++": True
}

def add_book(book):
    books[book] = True

def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned")

def search_book(book):
    if book in books:
        print("Book found")
    else:
        print("Book not found")

def display_books():
    print("Available Books:")
    for book, available in books.items():
        if available:
            print(book)

add_book("Data Structures")
issue_book("Python")
search_book("Java")
return_book("Python")
display_books()

# 21. Electricity Bill with Fixed Charges, Tax and Discount
def calculate_bill(units):
    if units <= 100:
        energy = units * 5
    elif units <= 200:
        energy = 100 * 5 + (units - 100) * 7
    else:
        energy = 100 * 5 + 100 * 7 + (units - 200) * 10

    fixed = 100
    subtotal = energy + fixed
    tax = subtotal * 0.05

    if units < 100:
        discount = subtotal * 0.05
    else:
        discount = 0

    return subtotal + tax - discount

units = int(input("Enter units: "))
print("Final Bill =", calculate_bill(units))


