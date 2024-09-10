class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_detals(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.author)

b = Book("My life", "Arbaz", 69)
(b.show_detals())