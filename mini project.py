'''First mini project '''
'''
end=" " prevent print statement to move to next line during every iteration
'''
'''
Q-:You have to create a library management System . This must be done by creating a class called library

The class library should have the following functions:
1)display book: It displays all the books in the library along with whether they a+re available or lent to someone
2)lend book: This will allow the user to issue a book from the library. If the requested book is lent to someone
             then print their name
3)add book: This fn is used to enter the name of the book to be added to the lib
4)return book : Allows the user to return a book

The Constructor of the class should take 2 arguments:
1) a list of all the book in the lib
2) the name of the lib

E.g:
HarryLibrary = Library(listofbooks, library_name)

You are to keep record of which book is issued to who via a dict as follows:
key - name of the book
value - name of the person issued to
dictionary (books-nameofperson)

create a main function and run an infinite while loop asking
users for their input"""'''
class Library:
    def __init__(self,lstbooks,libname):
        self.book=lstbooks
        self.name=libname
        self.lend_dict = {}
    def display(self):
        for book in self.book:
           if book in self.lend_dict:
             print(f'{book} is lend to {self.lend_dict[book]}')
           else:
               print(f'Available books : {book}')

        # print(f'Available books \n {self.book}')
    def customer_lend(self,user,value2):
        # value2 = input("Enter the name of book you want to lend ")
        if value2 not in self.book:
            print (f"sorry {user} book currently not available")
        elif value2 in self.lend_dict:
            print(f'sorry {value2} is issued to {self.lend_dict[value2]}')
        else:
            self.lend_dict[value2] = user
            print(f'{value2} is issued to {user}')


    def donate_book(self,user,value2):
        # value=input("enter the book name you want to donate")
        if value2 in self.book:
            print(f'{value2} is already available in library')
        else:
            self.book.append(value2)
            print(f"Thanks {user} for donating {value2} to this library")

        return self.book
    def return_book(self,user,value2):
        if value2 in self.lend_dict and self.lend_dict[value2] == user :
            del self.lend_dict[value2]
            print(f'{user} thanks for returning{value2}')

        elif  value2 not in self.lend_dict:
            print(f'This book is already present in library,')
        else:
            print(f"{user} it seems you haven't borrow this {value2},or not present in pur records")

pankaj = Library(['hindi', 'english', 'maths', 'science', 'geography'],'Pankaj_library')
while True:
    try:
     name_1 = input("Enter your name:- ")
     print(f"WELCOME TO THE {pankaj.name}")
     choice =int(input(f'choose one option from following :-\n'
                       f'1. see books present in library\n'
                       f'2. to Lend a book\n'
                       f'3. to donate a book\n'
                       f'4.to return a book\n'
                       f'5. exit :- \n'))
    except ValueError:
        print("choose from available option only ")
        continue
    if choice == 1:
        pankaj.display()
    elif choice == 2 :
        book_1=input("Enter the name of the book you want to lend :-")
        pankaj.customer_lend(name_1,book_1)
    elif choice == 3 :
        book_2 = input("Enter the name of book you want to donate :-")
        pankaj.donate_book(name_1,book_2)
    elif choice == 4:
        book_3 = input("Enter the name of book you want to return")
        pankaj.return_book(name_1,book_3)
    elif choice==5:
        print(f'Exiting from library ')
        break



































































































