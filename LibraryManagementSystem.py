

#===========================================
#               Book Class
#===========================================
class Book:

    # Constructs a new book object with its own Title, Author, and Availability status
    def __init__(self, title = "null", author = "null", availableStatus = True):
        self.title = title
        self.author = author
        self.availableStatus = availableStatus

    # When a book is checked in or out, its Availability Status changes
    def checkInOut(self, bool):
        self.availableStatus = bool

    # Turns availability status bool into a string that can be printed and written to library file
    def statusToString(self):
        if self.availableStatus:
            return "[Available]"
        else:
            return "[Checked Out]"
    
    # Returns a string displaying Title, Author, and Availability status of book that can be printed and written to file
    def bookToString(self):
        return (f"{self.title}, by {self.author} {self.statusToString()}")




#=================================================
#               Functions                    
#=================================================


#*******[ File Loading and Saving ]*******[]

#-----Load From File-----
def Load_From_File():
    newList = []
    with open("library.txt", "r") as file:
        for line in file:
            bookLine = line.strip()
            newTitle, newAuthor, newAvailableStatus = StringToBook(bookLine)
            newBook = Book(newTitle, newAuthor, newAvailableStatus)
            newList.append(newBook)
    return newList

#-----Load To File-----
def Load_To_File():
    with open("library.txt", "w") as file:
        try:
            for book in bookList:
                file.write(book.bookToString() + "\n")
            print(f"{'~Library Saved Successfully~':^65}")
        except TypeError:
            print("ERROR: Books could not be saved to library")
            

#-----String to Book Args
def StringToBook(bookString):
#takes Title, Author, and Availability Status from string and turns it into book argument

    commaIndex = 0
    bracketIndex = 0

    for i in range(len(bookString)):
        if(bookString[i] == ","):
            commaIndex = i
        if(bookString[i] == "["):
            bracketIndex = i

    argTitle = bookString[0:commaIndex]
    argAuthor = bookString[commaIndex+5:bracketIndex-1]

    match bookString[bracketIndex+1:-1]:
        case "Available":
            argAvailableStatus = True
        case "Checked Out":
            argAvailableStatus = False

    return argTitle, argAuthor, argAvailableStatus
    
#----- Sort Book List-----
#uses selection sort method to sort books based on author's name
def SortBookList():

    for i in range(len(bookList)):
        lowestElementIndex = i
        for j in range(i, len(bookList)):
            if(bookList[j].author < bookList[lowestElementIndex].author ):
                lowestElementIndex = j

        bookList[i], bookList[lowestElementIndex] = bookList[lowestElementIndex], bookList[i]
    
#****************************************[]





#********[ Interaction Functions ]*******[]

#-----Ask for Choice-----
def Ask_For_Choice():
    newChoice = input(f"{' '*20}Enter Choice: ")
    print("")
    return newChoice

#-----Display Options-----
def Display_Options():
    print(f"{'---OPTIONS---':^65}")
    print("")
    print(f"{' ' * 20} [A.] Register New Book")
    print(f"{' ' * 20} [B.] Check Book In/Out")
    print(f"{' ' * 20} [C.] View All Books")
    print(f"{' ' * 20} [D.] Close Program")
    print("")

#-----Register New Book-----
def Register_New_Book():
    print(f"{'----Registering New Book----':^65}")
    newTitle = input(f"{' ' * 20}Title of Book: ")
    newAuthor = input(f"{' ' * 20}Author of Book: ")
    print(f"{'----------------------------':^65}")
    print("")

    newBook = Book(newTitle, newAuthor)

    bookFound = False

    for book in bookList:
        if (book.title, book.author) == (newTitle, newAuthor):
            print(f"{'That book is already registered to the library':^65}")
            bookFound = True
            break

    if bookFound == False:  
        bookList.append(newBook)

        print(f"{'[ Book Registered ]':^65}")
        print(f"{f'{newTitle}, by {newAuthor} has been registered to the library': ^65}")
        print("")
    
    SortBookList()

#-----Check Book In/Out-----
def Check_Book_In_Out():
    print(f"{'Checking in or out?':^65}") 
    print(f"{'--------------------':^65}")
    print(f"{'[1] In': ^65}")
    print(f"{'[2] Out': ^65}")
    print(f"{'[3] Neither': ^65}")
    print("")
    choice = Ask_For_Choice()

    choiceToString = {"1":"In", "In":"In", "in":"In", '2':"Out", "Out":"Out", "out":"Out"}
    choiceToBool = {"In":True, "Out":False}

    match choice:
        case "1" | "In" | "in" | "2" | "Out" | "out":
            print(f"{f'----Checking Book {choiceToString[choice]}----':^65}")
            bookTitle = input(f"{' ' * 20}Title of Book: ")
            bookAuthor = input(f"{' ' * 20}Author of Book: ")
            print(f"{'----------------------------':^65}")

            bookFound = False

            for book in bookList:
                if (book.title, book.author) == (bookTitle, bookAuthor):
                    bookFound = True

                    if(book.availableStatus != choiceToBool[choiceToString[choice]]):
                        book.checkInOut(choiceToBool[choiceToString[choice]])
                        print(f"{f'{bookTitle}, by {bookAuthor} has been successfully Checked {choiceToString[choice]}.':^65}")
                    else:
                        print(f"{f'That book has already been Checked {choiceToString[choice]}.':^65}")
                        print("")
                        Check_Book_In_Out()
                        break
                    print("")

                    break

            if bookFound == False:
                print(f"{f'{bookTitle}, by {bookAuthor} was not found in the library.':^65}")
                print("")
                Check_Book_In_Out()

        case "3" | "Neither" | "neither":
            pass
        case _:
            print(f"{f'{choice} is not an option':^65}")
            Check_Book_In_Out()
    
    print("")

#-----View All Books-----
def View_All_Books():
    print(f"{'------Library Contents------':^65}")
    for book in bookList:
        print(f"{book.bookToString():^65}")
    print("")

#-----Close Program-----
def Close_Program():
    print(f"    []{'[]     ':=>60}")
    print(f"    |{'-Program Closed-':^55}|")
    print(f"    []{'[]     ':=>60}")
    print("")
    isRunning = False

#****************************************[]





#==================================================
#                Main Program Begin
#==================================================


#List that stores all books after they're loaded from the file
bookList = Load_From_File()


#     ===== Program Header =====
print("")
print(f"[]{'=[]':=>65}")
print(f"| {'|':>65}")
print(f"|{'[Library Management System]':^65}|")
print(f"| {'|':>65}")
print(f"[]{'=[]':=>65}")
print("")


isRunning = True

while isRunning:
    Display_Options()

    choice = Ask_For_Choice()

    match choice:
        case "Options" | "options":
            Display_Options()
        case "A" | "a" | "Register" | "register":
            Register_New_Book()
        case "B" | "b" | "Check In" | "check in":
            Check_Book_In_Out()
        case "C" | "c":
            View_All_Books()
        case "D" | "d" | "Close Program" | "close program":
            Close_Program()
            break
        case _:
            print("")
            print(f"'{choice}' Was Not An Option")
            print("")


    print(f"{'What else would you like to do?':^65}")
    print(f"{'--------------------------------':^65}")
    print("")

#Write the final version of the book list to the library file before ending the program
Load_To_File()
print("")

#==================================================
#                  [Program End]
#==================================================