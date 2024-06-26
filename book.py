class Book:
    def __init__(self, title, author, isbn, publication_date, genre, availability=True):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__availability = availability

    #getter for title
    def get_title(self):
        return self.__title

    #setter for title
    def set_title(self, title):
        self.__title = title

    #etter for author
    def get_author(self):
        return self.__author

    #setter for author
    def set_author(self, author):
        self.__author = author

    #getter for ISBN
    def get_isbn(self):
        return self.__isbn

    #getter for publication date
    def get_publication_date(self):
        return self.__publication_date

    #setter for publication date
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    #getter for genre
    def get_genre(self):
        return self.__genre

    #setter for genre
    def set_genre(self, genre):
        self.__genre = genre

    #getter for availability
    def get_availability(self):
        return self.__availability

    #setter for availability
    def set_availability(self, availability):
        self.__availability = availability