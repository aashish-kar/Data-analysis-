# Abstraction
# The main idea of abstraction is showing what is needed


# abstractmethod
# It is a decorator
# there are 3 conditions for abstractmethod
# 1. The parent class should inherit from ABC (Abstract Base Class)
# import from abc
# 2. Parent class should have atleast one abstractmethod
# 3. The child class should inherit from Parent class

# Then, every child class that inherits from Parent class should have abstractmethod

# from abc import ABC, abstractmethod

# class Teacher(ABC):
#     name = "Teacher"
    
#     @abstractmethod
#     def work(self):
#         print("I am a teacher")
        
# class MathTeacher(Teacher):
#     name = "Math Teacher"
    
#     # def work(self):
#     #     print("I am a math teacher")
        
# class EngTeacher(Teacher):
#     name = "Eng Teacher"
    
#     # def work(self):
#     #     print("I am a english teacher")
        
# m1 = MathTeacher()
# e1 = EngTeacher()
# print(m1.name)
# print(e1.name)


# Magic Methods
# Magic methods are the special type of methods that executes automatically under certain condition
# and magic methods start sand ends with __
# You can find the magic methods for every methods
# Eg: __init__ , __str__ , __add__ , __sub__ etc

# __init__ => RUns automatically at the time of object creation

# __str__ => Runs automatically when an object is printed

# class Student:
    
#     def __init__(self, name, age, gender, value):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.value = value
        
#     def __str__(self):
#         return f"{self.name} object is printed with value {self.value}"
    
#     def __add__(self, other):
#         # return f"Addition = {self.value + other.value}"
#         return "Ujjwal Neupane"
        
# s1 = Student("Ujjwal",27,"Male", 5)
# print(s1)
        
# s2 = Student("Sita",26,"Female", 10)
# print(s2)

# # + > __add__
# # - => __sub__

# result = s1 + s2 # s1.__add__(s2)
# print(result)



# LMS 
# 2 classes => Book Ebook
# 4 methods, view books, add books, remove books, search book

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        
        def __str__(self):
            return "Physical Book"
        
class EBook(Book):
    def __init__(self, name, author, price, size):
        super().__init__(name, author, price)
        self.size = size
    
    def __str__(self):
            return "EBook"

class LMS:
    books = []
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    # def add_book(self, name, author, price):
    #     type = input("ENter your book type (p/o): ").lower()
    #     if type == 'p':
    #         name = Book(name, author, price)
    #     elif type == 'o':
    #         size = input("ENter the size: ")
    #         name = EBook(name, author, price, size)
            
        
            
            
            
            
        
    
    def __str__(self):
        return f"{self.name} library"

lms = []
while True:
    choice = input("Do you want to create or visit LMS or exit? (c/v/e) :  ").lower()
    if choice == 'c':
        lib_name = input("ENter name of library: ")
        lib_address = input("ENter address of library: ")
        lms_name = LMS(lib_name, lib_address)
        lms.append(lms_name)
    elif choice == 'v':
        name = input("Enter the name of library to view: ")
        visited = False
        for lib in lms:
            if name == lib.name:
                print(f"Visiting the {name} Library")
                visited = True
                while True:
                    choice_lib = input("ENter 1 to add book, 2 to view books, 3 to remove book, 4 to search book, 5 to exit: ")
                    if choice_lib == '1':
                        name = input("ENter book name: ")
                        author = input("ENter book author: ")
                        price = input("ENter book price: ")
                        type = input("ENter your book type (p/o): ").lower()
                        if type == 'p':
                            name = Book(name, author, price)
                        elif type == 'o':
                            size = input("ENter the size: ")
                            name = EBook(name, author, price, size)
                            
                        lms_name.books.append(name)
                        
                    elif choice_lib == '2':
                        for book in lms_name.books:
                            print(f"Name = {book.name}")
                            print(f"Author = {book.author}")
                            print(f"Price = {book.price}")
                            try:
                                if "EBook" in str(book):
                                    print(f"Size = {book.size}")
                            except:
                                print("No Books found")
                    # elif choice in ['3','4']:
                    elif choice_lib == '3' or choice_lib == '4':
                        book_name_search = input("Enter the book name:")
                        is_found = False
                        for book in lms_name.books:
                            if book.name == book_name_search:
                                is_found = True
                                if choice_lib == '3':
                                    lms_name.books.remove(book)
                                    print(f"{book_name_search} deleted successfully")
                                elif choice_lib == '4':
                                    index = lms_name.books.index(book)
                                    print(f"{book_name_search} found at index {index}")
                                    
                        if not is_found:
                            print("Book not found")
                        
                    elif choice_lib == '5':
                        break
        if not visited:
            print("Library Not found")
    elif choice == 'e':
        break
    else:
        print("Invalid Input")