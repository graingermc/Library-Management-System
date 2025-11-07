

#===========================================
#               Book Class
#===========================================
class Book:

    # Constructs a new book object with its own Title, Author, and Availability status
    def __init__(self, title = "null", author = "null", availableStatus = True):
        self.__title = title
        self.__author = author
        self.__availableStatus = availableStatus

    # Turns availability status bool into a string that can be printed and written to library file
    def statusToString(self):
        if self.__availableStatus:
            return "[Available]"
        else:
            return "[Checked Out]"
        
    # Returns a string displaying Title, Author, and Availability status of book that can be printed and written to file
    def bookToString(self):
    
        return (f"{self.__title}, by {self.__author} {self.statusToString()}" )


#===========================================
#               Main Functions
#===========================================

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
        for book in bookList:
            file.writelines(book.bookToString(),"\n")
            file.flush()

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
    argAuthor = bookString[commaIndex+5:bracketIndex]

    match bookString[bracketIndex+1:-1]:
        case "Available":
            argAvailableStatus = True
        case "Checked Out":
            argAvailableStatus = False

    return argTitle, argAuthor, argAvailableStatus
    

#-----Gets Choice Of user-----
def Ask_For_Choice():
    newChoice = input("                    Enter Choice : ")
    return newChoice

#-----Register New Book-----
def Register_New_Book():
    print("")
    print("                        []-------------------[]")
    newTitle = input("                         Enter New Book Title: ")
    newAuthor = input("                         Enter New Book Author: ")
    print("                        []-------------------[]")
    newBook = Book(newTitle, newAuthor)
    bookList.append(newBook)
    print(f"                           [('{newTitle}', by {newAuthor}) added]")
    print("")

#-----Check Book In/Out-----
def Check_Book_In_Out():
    pass

#-----View All Books-----
def View_All_Books():
    for book in bookList:
        print(book.bookToString())







#=============================================
#                Main Program 
#=============================================


#List that stores all books after they're loaded from the file
bookList = Load_From_File()

print(bookList)

                                    # Main Menu
print("")
print("[]================================================================[]")
print("|                                                                  |")
print("|                    [Library Management System]                   |")
print("|                                                                  |")
print("[]================================================================[]")
print("")
print("                          ---OPTIONS---")
print("")
print("                    [A.] Register New Book")
print("                    [B.] Check Book In/Out")
print("                    [C.] View All Books")
print("                    [D.] Close Program")
print("")



isRunning = True

while isRunning:
    choice = Ask_For_Choice()

    match choice:
        case "A" | "a" | "Register" | "register":
            Register_New_Book()
        case "B" | "b" | "Check In" | "check in":
            Check_Book_In_Out()
        case "C" | "c":
            View_All_Books()
        case "D" | "d" | "Close Program" | "close program":
            print("")
            print("[]================================================================[]")
            print("|                           -Program Closed-                       |") 
            print("[]================================================================[]")
            print("")
            isRunning = False
        case _:
            print("")
            print(f"'{choice}' Was Not An Option")
            print("")










