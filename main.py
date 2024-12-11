class Book:
    # init constructor method to initialize attributes
    def __init__(self, title, author, pages, genre, read = False, purchases = 0):
        self._title = title
        self._author = author
        self._pages = pages
        self._genre = genre
        self._read = read
        self._purchases = purchases

    # returning book instance's description
    def description(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}, Genre: {self._genre}"
    
    # setting read to True and displaying confirmation message
    def markAsRead(self):
        self._read = True
        print(f"{self._title} has been marked as read!")
        return self._read
    
class eBookReader:
    # init contructor method to initialize lists (data)
    def __init__(self):
        self._availableBooks = []
        self._purchasedBooks = []
        self._genres = []
        self._titlesBought = []

    # add a book to available books (already populated data) (breze added try/except let me know if any of this doesn't work and feel free to change anything if needed I kept the original version of this so if we need to go back to it we can)
    def addBook(self, book):
        try:
            if book not in self._availableBooks:
                self._availableBooks.append(book)
                print(f"{book._title} has been added to system.")
            else:
                print(f"{book._title} is already in the system.")
        except Exception as e:
            print(f"An error occurred while adding the book: {e}")

    # return pages in a book to load reading simulator (Jose)
    def getPages(self, title):
        try:
            for book in self._availableBooks:
                if book._title == title:
                    return int(book._pages)
        except Exception as e:
            print(f"An error occured getting the number of pages of {title}: {e}")

    # Update book method (Amedeo)
    def updateBook(self, title, newTitle=None, newAuthor=None, newPages=None, newGenre=None):
        for book in self._availableBooks:
            if book._title == title:
                if newTitle:
                    book._title = newTitle
                if newAuthor:
                    book._author = newAuthor
                if newPages:
                    book._pages = newPages
                if newGenre:
                    book._genre = newGenre
                print(f"{title} has been updated.")
                return
        print(f"{title} not found in available books.")

    # Delete book method (Amedeo)
    def deleteBook(self, title):
        for book in self._availableBooks:
            if book._title == title:
                self._availableBooks.remove(book)
                print(f"{title} has been removed from the system.")
                return
        print(f"{title} not found in available books.")

    # buying a book if not purchased, available, and exists (breze added try/except let me know if any of this doesn't work)
    def buyBook(self, bookName):
        try:
            for book in self._availableBooks:
                if book._title == bookName:
                    self._purchasedBooks.append(book)
                    if book._title + '\n' not in self._titlesBought:
                        self._titlesBought.append(book._title + '\n')
                        print(f"{book._title} has been successfully purchased!")
                    book._purchases += 1
                    return
            print(f"{bookName} is not available.")
        except Exception as e:
            print(f"An error occurred while buying the book: {e}")

    
    # displaying the description of books inside purchased books list (breze added try/except let me know if any of this doesn't work)
    def viewPurchasedBooks(self):
        try:
            if not self._purchasedBooks:
                print(f"There are no purchased books ... yet!")
            else:
                print(f"These are the purchased books: ")
                for book in self._purchasedBooks:
                    print('\t' + book.description())
        except Exception as e:
            print(f"An error occurred while viewing purchased books: {e}")

    # marking a book as read if there book is already purchased and not yet read (breze added try/except let me know if any of this doesn't work)
    def readPurchasedBook(self, bookName):
        try:
            if not self._purchasedBooks:
                print(f"There are no purchased books ... yet!")
            else:
                for book in self._purchasedBooks:
                    if book._title == bookName:
                        if book._read == False:
                            book.markAsRead()
                        else:
                            print(f"{book._title} has already been read.")
                        return
                print(f"{bookName} is not purchased.")
        except Exception as e:
            print(f"An error occurred while marking the book as read: {e}")

    # view which genres are available for purhcase in the system (breze added try/except let me know if any of this doesn't work)
    def availableGenres(self):
        try:
            if not self._availableBooks:
                print(f"There are no books available ... yet!")
            else:
                print(f"These are the available genres: ")
                for book in self._availableBooks:
                    if book._genre not in self._genres:
                        self._genres.append(book._genre)
                for genre in self._genres:
                    print('\t' + genre)
        except Exception as e:
            print(f"An error occurred while viewing available genres: {e}")

    # filtering method by genre with user input (breze added try/except and the recursive function let me know if any of this doesn't work)
    def filterByGenres(self):
        try:
            self.availableGenres()
            # filtering and user input
            print(f"Select a genre to filter. (Case sensitive)")
            userGenre = input(" >")
            if userGenre not in self._genres:
                print(f"{userGenre} is not available.")
            else:
                print(f"These are the available books with genre \"{userGenre}\"")
                self._filterByGenreRecursive(userGenre, 0)
        except Exception as e:
            print(f"An error occurred while filtering genres: {e}")
    
    def _filterByGenreRecursive(self, genre, index):
        try:
            if index < len(self._availableBooks):
                book = self._availableBooks[index]
                if book._genre == genre:
                    print('\t' + book.description())
                self._filterByGenreRecursive(genre, index + 1)
        except Exception as e:
            print(f"An error occurred during the recursive genre filter: {e}")

    # track book purchases (breze added try/except let me know if any of this doesn't work)
    def trackBookPurchases(self):
        try:
            if not self._purchasedBooks:
                print("There are no books purchased ... yet!")
            else:
                titles = []
                purchases = []
                for book in self._purchasedBooks:
                    if book._purchases not in purchases:
                        purchases.append(book._purchases)
                    if book._title not in titles:
                        titles.append(book._title)
                print("These are the books that have been purchased: ")
                for i in range(len(titles)):
                    print('\t' + f"{titles[i]} has been purchased {purchases[i]} time(s).")
        except Exception as e:
            print(f"An error occurred while tracking book purchases: {e}")

    # top 3 purchased books with recursion (breze added try/except and the recursive function let me know if any of this doesn't work)
    def topPurchasedBooks(self):
        try:
            if not self._purchasedBooks:
                print("There are no books purchased ... yet!")
            else:
                purchaseCount = []
                usedTitles = []
                for book in self._purchasedBooks:
                    if book._title not in usedTitles:
                        usedTitles.append(book._title)
                        purchaseCount.append(book._purchases)
                topPurchases = list(purchaseCount)
                topTitles = list(usedTitles)
                self._sortTopBooksRecursive(topPurchases, topTitles, 0)
                print("The top 3 most purchased books are: ")
                for i in range(3):
                    print(f"\t{(i + 1)}. {topTitles[i]}: {topPurchases[i]} buys.")
        except Exception as e:
            print(f"An error occurred while getting top purchased books: {e}")

    def _sortTopBooksRecursive(self, purchases, titles, index):
        try:
            if index < len(purchases) - 1:
                maxIndex = index
                for y in range(index + 1, len(purchases)):
                    if purchases[y] > purchases[maxIndex]:
                        maxIndex = y
                purchases[index], purchases[maxIndex] = purchases[maxIndex], purchases[index]
                titles[index], titles[maxIndex] = titles[maxIndex], titles[index]
                self._sortTopBooksRecursive(purchases, titles, index + 1)
        except Exception as e:
            print(f"An error occurred during the recursive sorting: {e}")

    # search for books by author with recursion (breze added try/except and the recursive function let me know if any of this doesn't work)
    def searchAuthor(self):
        try:
            print("Enter the author name to search for available books: (Case sensitive)")
            userAuthor = input(" >")
            self._searchAuthorRecursive(userAuthor, 0, 0)
        except Exception as e:
            print(f"An error occurred while searching for the author: {e}")
    
    def _searchAuthorRecursive(self, author, index, found):
        try:
            if index < len(self._availableBooks):
                book = self._availableBooks[index]
                if book._author == author:
                    print('\t' + f"{book._title} by {book._author} is available!")
                    found += 1
                self._searchAuthorRecursive(author, index + 1, found)
            elif found == 0:
                print(f"{author} does not have books available right now.")
        except Exception as e:
            print(f"An error occurred during the recursive author search: {e}")

    # search for books by title with recursion and binary search (breze added try/except and the recursive function let me know if any of this doesn't work)
    def searchByTitle(self):
        try:
            if not self._availableBooks:
                print("There are no available books ... yet!")
                return

            print("Enter the book's title to search for availability: (Case sensitive)")
            userTitle = input(" >")

            # Sort titles before performing binary search
            titles = [book._title for book in self._availableBooks]
            titles.sort()

            # Perform binary search recursively
            self._recursiveBinarySearch(titles, userTitle, 0, len(titles) - 1)
        except Exception as e:
            print(f"An error occurred while searching for the title: {e}")

    def _recursiveBinarySearch(self, userTitles, titles, min, max):
        try:
            if min <= max:
                mid = (min + max) // 2
                if userTitles[mid] == titles:
                    print(f"{titles} has been found and is available.")
                    return
                elif userTitles[mid] < titles:
                    self._recursiveBinarySearch(userTitles, titles, mid + 1, max)
                else:
                    self._recursiveBinarySearch(userTitles, titles, min, mid - 1)
            else:
                print(f"{titles} is not available.")
        except Exception as e:
            print(f"An error occurred during the binary search: {e}")

    # saving book purchase data to a file (breze added try/except let me know if any of this doesn't work)
    def saveToFile(self):
        try:
            with open('Resources/purchasedBooks.txt', 'w') as file:
                for book in self._purchasedBooks:
                    if book._title not in self._titlesBought:
                        file.write(f"{book._title}\n")
                        self._titlesBought.append(book._title)
            print("File has been successfully saved.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    # loading book purchase data from a file (breze added try/except let me know if any of this doesn't work)
    def loadFromFile(self):
        try:
            with open('Resources/purchasedBooks.txt', 'r') as file:
                loadedTitles = file.readlines()
                self._titlesBought = loadedTitles
            print("File has been successfully loaded.")
        except Exception as e:
            print(f"An error occurred while loading from file: {e}")

# Added Queue class to create new queues. (Jose)
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []
        return

    def enqueue(self, value):
        # Add new item to back of queue
        self.items.append(value)
        return
    
    def dequeue(self):
        # Remove and return first item of queue
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)
        
    def isEmpty(self):
        # Returns True if the queue is empty, False if not
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def first(self):
        # Return the first item of queue without removing
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]
        
    def last(self):
        # Return the last item of queue without removing
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
        
    def queueSize(self):
        return len(self.items)
    
    def queueItems(self):
        return self.items
    
# Added Stack class to create new stacks. (Jose)
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []
        return
    
    def getSize(self):
        # Return stack size
        return len(self.items)

    def isEmpty(self):
        # Return True if the stack is empty, otherwise False
        if len(self.items) == 0:
            return True
        else:
            return False
       
    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
        return

    def pop(self):
        # Remove and return the top item from the stack if it's not empty
        # If the stack is empty, return None
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
        
    def pushBookmark(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
        return

    def popBookmark(self):
        # Remove and return the top item from the stack if it's not empty
        # If the stack is empty, return None
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        # Return the top item without removing it if the stack is not empty
        # If the stack is empty, return None
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

#Q
#Added Node class
class Node():
    def __init__(self, value=None, next=None, previous=None):
        #Define node's properties: value, next; default
        self.value = value
        self.next = next
        self.previous = previous
        return

#Added LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    #Define add_to_front
    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    #Define add
    def add(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head
        else:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = new
            new.previous = traverse
            self.tail = new      
        return

    #Define print_list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

#Added BookList class
class BookList:
    def __init__(self):
        self.books = LinkedList()

    #Define add_book
    def add_book(self, title, author, pages, genre):
        new_book = Book(title, author, pages, genre)
        self.books.add(new_book)

    #Define display_books
    def display_books(self):
        temp = self.books.head
        while temp:
            print(f"{temp.data.title}, {temp.data.author}, {temp.data.pages}, {temp.data.genre}")
            temp = temp.next

def main():
    # print() # differentiate betweeen two mains

    # singular instance of eBookReader class
    userOne = eBookReader()

    # adding Book instances (books) to userOne's simulation
    userOne.addBook(Book("Mansfield Park", "Jane Austen", "488", "Novel"))
    userOne.addBook(Book("The Jungle Book", "Rudyard Kipling", "277", "Fiction"))
    userOne.addBook(Book("Little Women", "Louisa May Alcott", "449", "Novel"))
    userOne.addBook(Book("The Phantom of the Opera", "Gaston Leroux", "360", "Novel"))
    userOne.addBook(Book("Snow Crash", "Neil Stephenson", "559", "Fiction"))

    # simulating user purchases
    for i in range(6):
        userOne.buyBook("Mansfield Park")
    for i in range(1):
        userOne.buyBook("Little Women")
    for i in range(3):
        userOne.buyBook("The Phantom of the Opera")
    for i in range(4):
        userOne.buyBook("The Jungle Book")
    for i in range(10):
        userOne.buyBook("Snow Crash")

    # simulating user actions
    userOne.loadFromFile()
    userOne.availableGenres()
    userOne.trackBookPurchases()
    userOne.topPurchasedBooks()
    userOne.filterByGenres()
    userOne.searchAuthor()
    userOne.searchByTitle()
    userOne.saveToFile()
    # EX for Updating a book (Amedeo)
    userOne.updateBook("Mansfield Park", newTitle="Northanger Abbey", newAuthor="Jane Austen")
    # EX for Deleting a book (Amedeo)
    userOne.deleteBook("The Jungle Book")

    # (Jose)
    # Singular instance of reading list using a queue
    readingList = Queue()
    
    # simulating user actions (queue)
    '''user want to know if queue is empty'''
    readingList.isEmpty() # True
    '''user is adding books to his reading list'''
    readingList.enqueue("Snow Crash")
    readingList.enqueue("Little Women")
    readingList.enqueue("The Jungle Book")
    '''user wants to know how big his current reading list is'''
    readingList.queueSize() # 3
    '''user has read "Snow Crash" and wants to remove it from queue'''
    readingList.dequeue()
    '''user wasnt to know what was the last book he queued'''
    readingList.last() # The Jungle Book
    '''user want to add another book to queue'''
    readingList.enqueue("The Phantom of the Opera")
    '''user reads 2 books'''
    readingList.dequeue() # Little Women is gone
    readingList.dequeue() # The Jungle Book is gone
    '''user wants to know what books he has in his reading list'''
    readingList.queueItems() # ["The Phantom of the Opera"]

    # User reading book simulation (Snow Crash)
    snowCrashBook = Stack()
    
    '''User browsing pages forward'''
    for i in range(20):  # User skimmed 20 pages
        print(f"User flips to page {i}")
        snowCrashBook.push(i)
    '''User flipping pages backward to beginning'''
    while not snowCrashBook.isEmpty():
        currentPage = snowCrashBook.pop()
        print(f"User flips back to page {currentPage}")
    '''User reads 42 pages''' 
    for i in range(42):
        snowCrashBook.push(i)
    '''User goes back 3 pages'''
    for i in range(3):
        currentPage = snowCrashBook.pop()
        print(f"User flips back to page {currentPage}")
    '''User bookmarks 1 page behind'''
    bookmarkCurrentPage = snowCrashBook.pop()
    snowCrashBook.pushBookmark(bookmarkCurrentPage)
    '''User resumes to read from bookmark'''
    currentBookmark = snowCrashBook.popBookmark()
    '''User reads from bookmark to end of book'''
    endBook = userOne.getPages("Snow Crash")
    for i in range(currentBookmark, endBook + 1):
        print(f"User flips to page {i}")
        snowCrashBook.push(i)
    '''User ends book, empty pages loaded, mark as read'''
    while not snowCrashBook.isEmpty():
        snowCrashBook.pop()
    userOne.readPurchasedBook("Snow Crash")

    #Q
    #Create LinkedList
    bookList = BookList()

    #Add books to list
    bookList.head = Node("The Catcher in the Rye", "J. D. Salinger", "288", "Novel", (1))
    second = Node("Fahrenheit 451", "Ray Bradbury", "176", "Fiction", (2))

    #Link books
    bookList.head.next = second

if __name__ == "__main__":
    main()
