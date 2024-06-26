from book import Book
from user import User
from author import Author
from genre import Genre
import re

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []
    
    #displays main menu
    def display_main_menu(self):
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

    #displays book menu
    def display_book_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

    #displays user menu
    def display_user_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

    #displays author menu
    def display_author_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

    #displays genre menu
    def display_genre_menu(self):
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")

    #runs the program
    def run_program(self):
        while True:
            self.display_main_menu()
            choice = input("Please enter your choice (1-5): ")

            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                self.genre_operations()
            elif choice == "5":
                print("Exiting the Library Management System.")
                break
            else:
                print("Invalid option. Please try again.")

    #book operation options
    def book_operations(self):
        while True:
            self.display_book_menu()
            book_choice = input("Please select an option (1-6): ")

            if book_choice == "1":
                self.add_book()
            elif book_choice == "2":
                self.borrow_book()
            elif book_choice == "3":
                self.return_book()
            elif book_choice == "4":
                self.search_book()
            elif book_choice == "5":
                self.display_all_books()
            elif book_choice == "6":
                break
            else:
                print("Invalid option. Please try again and enter a number from 1-6.")
    #adds a book
    def add_book(self):
        try:
            title = input("Please enter the book title: ")
            if not title:
                raise ValueError("Title cannot be empty.")

            author_name = input("Please enter the author's name: ")
            if not author_name:
                raise ValueError("Author name cannot be empty.")

            isbn = input("Please enter the book ISBN: ")
            if not re.match(r"^(\d{10}|\d{13})$", isbn): #simplified to 10 or 13 digits, no dashes
                raise ValueError("Invalid ISBN format. Please enter a 10 or 13 digit ISBN without dashes")

            publication_date = input("Please enter the publication date (YYYY-MM-DD): ")
            if not publication_date:
                raise ValueError("Publication date cannot be empty.")
            genre_name = input("Please enter the genre name: ")
            if not genre_name:
                raise ValueError("Genre cannot be empty.")
            
            #finds or creates author
            author = None
            for existing_author in self.authors:
                if existing_author.get_name() == author_name:
                    author = existing_author
                    break
            if author is None:
                author_biography = input("Please enter the author's biography: ")
                author = Author(author_name, author_biography)
                self.authors.append(author)

            #finds/creates genere
            genre = None
            for existing_genre in self.genres:
                if existing_genre.get_name() == genre_name:
                    genre = existing_genre
                    break
            if genre is None:
                genre_description = input("Please enter the genre description: ")
                genre_category = input("Please enter the genre category: ")
                genre = Genre(genre_name, genre_description, genre_category)
                self.genres.append(genre)

            #creates and add books
            book = Book(title, author, isbn, publication_date, genre)
            self.books.append(book)
            print(f"Book '{title}' was added successfully!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    #function to borrow book
    def borrow_book(self):
        isbn = input("Please enter the ISBN of the book to borrow: ")
        user_id = input("Please enter your library ID: ")
        #find matching book by ISBN
        book = None
        for books in self.books:
            if books.get_isbn() == isbn:
                book = books
                break
        #fingding user by library id
        user = None
        for users in self.users:
            if users.get_library_id() == user_id:
                user = users
                break

        if book and user:
            if book.get_availability():
                book.set_availability(False)
                user.borrow_book(book.get_title())
                print(f"Book '{book.get_title()}' borrowed successfully!")
            else:
                print(f"Book '{book.get_title()}' is not available to borrow.")
        else:
            print("Invalid ISBN or User ID.")
    #function to return book
    def return_book(self):
        isbn = input("Please enter the ISBN of the book to return: ")
        user_id = input("Please enter your library ID: ")

        #finding a book by ISBN
        book = None
        for books in self.books:
            if books.get_isbn() == isbn:
                book = books
                break
        #finding user by library id
        user = None
        for users in self.users:
            if users.get_library_id() == user_id:
                user = users
                break
        if book and user:
            if not book.get_availability():
                book.set_availability(True)
                user.return_book(book.get_title())
                print(f"Book '{book.get_title()}' returned successfully!")
            else: 
                print(f"Book '{book.get_title()}' was not borrowed in the system.")
        else:
            print("Invalid ISBN or User ID.")
    #function to search for a book
    def search_book(self):
        isbn = input("Please enter the ISBN of the book to search: ")
        book = None
        for books in self.books():
            if books.get_isbn() == isbn:
                book = books
                break
        if book:
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author().get_name()}")
            print(f"ISBN: {book.get_isbn()}")
            print(f"Publication Date: {book.get_publication_date()}")
            print(f"Genre: {book.get_genre().get_name()}")
            print(f"Availability: {'Available' if book.get_availability() else 'Borrowed'}")
        else:
            print("Book not found.")
    #function to display all books
    def display_all_books(self):
        if not self.books:
            print("No books available to display.")
        else:
            for book in self.books:
                print(f"{book.get_title()} (ISBN: {book.get_isbn()})")
    #for user operations
    def user_operations(self):
        while True:
            self.display_user_menu()
            user_choice = input("Please select an option (1-4): ")

            if user_choice == '1':
                self.add_user()
            elif user_choice == '2':
                self.view_user_details()
            elif user_choice == '3':
                self.display_all_users()
            elif user_choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    #function to add user
    def add_user(self):
        name = input("Please enter the user's name: ")
        library_id = input("Please enter the library ID of the user: ")

        user = User(name, library_id)
        self.users.append(user)
        print(f"User '{name}' was added successfully!")

    #function to view user details
    def view_user_details(self):
        library_id = input("Please enter the library ID of the user: ")

        user = None
        for users in self.users():
            if users.get_library_id() == library_id:
                user = users
                break

        if user:
            print(f"Name: {user.get_name()}")
            print(f"Library ID: {user.get_library_id()}")
            print(f"Borrowed Books: {', '.join(user.get_borrowed_books())}")
        else:
            print("User not found. Please try again")
    #function to display all users
    def display_all_users(self):
        if not self.users:
            print("No users available.")
        else:
            for user in self.users:
                print(f"{user.get_name()} (Library ID: {user.get_library_id()})")
    #function for author operations menu
    def author_operations(self):
        while True:
            self.display_author_menu()
            author_choice = input("Please select an option (1-4): ")

            if author_choice == '1':
                self.add_author()
            elif author_choice == '2':
                self.view_author_details()
            elif author_choice == '3':
                self.display_all_authors()
            elif author_choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    #function to add author
    def add_author(self):
        name = input("Please enter the author's name: ")
        biography = input("Please enter the author's biography: ")

        author = Author(name, biography)
        self.authors.append(author)
        print(f"Author '{name}' was added successfully to the system!")
    #function to view author details
    def view_author_details(self):
        name = input("Please enter the author's name you would like to see: ")
        author = None
        for authors in self.authors:
            if authors.get_name() == name:
                author = authors
                break

        if author:
            print(f"Name: {author.get_name()}")
            print(f"Biography: {author.get_biography()}")
        else:
            print("Author not found.")
    #function to display all authors
    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        else:
            for author in self.authors:
                print(f"{author.get_name()}")
    #function for genre operations menu
    def genre_operations(self):
        while True:
            self.display_genre_menu()
            genre_choice = input("Please select an option (1-4): ")

            if genre_choice == '1':
                self.add_genre()
            elif genre_choice == '2':
                self.view_genre_details()
            elif genre_choice == '3':
                self.display_all_genres()
            elif genre_choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    #function to add genre
    def add_genre(self):
        name = input("Please enter the genre name: ")
        description = input("Please enter the description: ")
        category = input("Please enter the category: ")

        genre = Genre(name, description, category)
        self.genres.append(genre)
        print(f"Genre '{name}' was added successfully!")
    #function to view genre details
    def view_genre_details(self):
        name = input("Please enter the genre name: ")
        genre = None
        for genres in self.genres():
            if genres.get_name() == name:
                genre = genres
                break

        if genre:
            print(f"Name: {genre.get_name()}")
            print(f"Description: {genre.get_description()}")
            print(f"Category: {genre.get_category()}")
        else:
            print("Genre not found.")
    #function to display all genres
    def display_all_genres(self):
        if not self.genres:
            print("No genres available.")
        else:
            for genre in self.genres:
                print(f"{genre.get_name()}")