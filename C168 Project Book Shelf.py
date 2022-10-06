class Book:
    def __init__(self, name, author, price, pub, pub2):
        self.aname = name
        self.Aauthor = author
        self.bprice = price
        self.bpub = pub
        self.bpub2 = pub2
    def add_book(self):
        print("Book Name: " + self.aname)
        print("Book Author: " + str(self.Aauthor))
        print("Book price: " + str(self.bprice))
        print("Book was published in: " + str(self.bpub))
        print("Book Added")
        print("This book was published " + str(self.bpub2))
        
b1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "$23 CAD", 1997, "25 years ago")
b1.add_book()

