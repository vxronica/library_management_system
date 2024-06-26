class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    #getter for name
    def get_name(self):
        return self.__name

    #setter for name
    def set_name(self, name):
        self.__name = name

    #getter for library id
    def get_library_id(self):
        return self.__library_id

    #setter for library id
    def set_library_id(self, library_id):
        self.__library_id = library_id

    #getter for borrowed books
    def get_borrowed_books(self):
        return self.__borrowed_books

    #borrow book
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    #return book
    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)