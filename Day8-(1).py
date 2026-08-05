from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self, person_id, name):
        self.__person_id = person_id
        self.__name = name

    def get_name(self):
        return self.__name

    def get_person_id(self):
        return self.__person_id

    @abstractmethod
    def borrow_book(self, library, book_id):
        pass

    @abstractmethod
    def return_book(self, library, book_id):
        pass



class Library:
    def __init__(self):
        self.books = {
            101: {"title": "Python Programming", "available": True},
            102: {"title": "Java Basics", "available": True},
            103: {"title": "Data Structures", "available": True},
            104: {"title": "Operating Systems", "available": True},
            105: {"title": "Computer Networks", "available": True},
        }

    def display_books(self):
        print("\n========== Library Books ==========")
        for book_id, details in self.books.items():
            status = "Available" if details["available"] else "Borrowed"
            print(f"{book_id} - {details['title']} - {status}")
        print()



class Student(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = []

    def borrow_book(self, library, book_id):

        if book_id not in library.books:
            print("Book ID does not exist.")
            return

        if library.books[book_id]["available"]:
            library.books[book_id]["available"] = False
            self.borrowed_books.append(book_id)
            print(f"{self.get_name()} borrowed '{library.books[book_id]['title']}'")
        else:
            print("Book is already borrowed.")

    def return_book(self, library, book_id):

        if book_id in self.borrowed_books:
            library.books[book_id]["available"] = True
            self.borrowed_books.remove(book_id)
            print(f"{self.get_name()} returned '{library.books[book_id]['title']}'")
        else:
            print("You have not borrowed this book.")



class Librarian(Person):

    def borrow_book(self, library, book_id):

        if book_id not in library.books:
            print("Book ID does not exist.")
            return

        if library.books[book_id]["available"]:
            library.books[book_id]["available"] = False
            print(f"Librarian issued '{library.books[book_id]['title']}'")
        else:
            print("Book is already borrowed.")

    def return_book(self, library, book_id):

        if book_id not in library.books:
            print("Book ID does not exist.")
            return

        library.books[book_id]["available"] = True
        print(f"Librarian received '{library.books[book_id]['title']}'")

library = Library()

student = Student("S101", "Bharathi")
librarian = Librarian("L001", "Admin")


while True:

    print("\n========== Library Management ==========")
    print("1. Display Books")
    print("2. Student Borrow Book")
    print("3. Student Return Book")
    print("4. Librarian Issue Book")
    print("5. Librarian Receive Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        library.display_books()
        book_id = int(input("Enter Book ID to borrow: "))
        student.borrow_book(library, book_id)

    elif choice == "3":
        if len(student.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            print("Borrowed Books:", student.borrowed_books)
            book_id = int(input("Enter Book ID to return: "))
            student.return_book(library, book_id)

    elif choice == "4":
        library.display_books()
        book_id = int(input("Enter Book ID to issue: "))
        librarian.borrow_book(library, book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID to receive: "))
        librarian.return_book(library, book_id)

    elif choice == "6":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")