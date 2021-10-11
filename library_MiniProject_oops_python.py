from abc import ABC,abstractmethod

class Books(ABC):
    @abstractmethod
    def displayBooks(self):
         pass

    @abstractmethod
    def lendBook(self, user, book):
         pass

    @abstractmethod
    def addBook(self, book):
        pass

    @abstractmethod
    def returnBook(self, book):
        pass


class Library(Books):       #inheritance
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}  #blank dict to store books

    def displayBooks(self):
        print("We have following books in our library:")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})       #update function will update the dict
            print(f"Database has been updated. Book issued!")
        else:
            print(f"Book is already issued by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, book):
        self.lendDict.pop(book)

list1 = Library(['Python', 'Data structures', 'Life sciences', 'C++ Basics', 'Algorithms'], "library")

while(True):
        print(f"Welcome to the {list1.name}. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        choice = input()
        if choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            choice = int(choice)


        if choice == 1:
            list1.displayBooks()

        elif choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            list1.lendBook(user, book)

        elif choice == 3:
            book = input("Enter the name of the book you want to add: ")
            list1.addBook(book)

        elif choice == 4:
            book = input("Enter the name of the book you want to return: ")
            list1.returnBook(book)
            print(f"{book} book has been returned.")

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        choice1 = ""
        while(choice1!="c" and choice1!="q"):
            choice1 = input()
            if choice1 == "q":
                exit()

            elif choice1 == "c":
                continue