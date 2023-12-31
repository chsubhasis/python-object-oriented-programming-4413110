# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title):
        self.myTitle = title


# TODO: create instances of the class
book1 = Book("My book1")
book2 = Book("My book2")

# TODO: print the class and property
print(book1)
print(book1.myTitle)
print(book2)
print(book2.myTitle)
