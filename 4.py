# -*- coding: utf-8 -*-
"""21

@author: Dan
"""


#part a)
class Book(object):
    
    increment = 0
    
    def __init__(self,title,price):
        self.title = title
        self.price = price
        Book.increment += 1
        self.nextBookRef = 150 + Book.increment
        self.bookRef = self.nextBookRef
        
    #def init(self.title,self.price):
       
       #return f" the book title is: {self.title} and price book price is: {self.price}"
   
    def __str__(self):
        
        return f" the book title is: {self.title} and book price is: {self.price} with book reference: {self.bookRef}"
    
    def setPrice(self,newPrice):
        if newPrice > 0:
            self.price = newPrice
        else:
            print("price must be at least 1 and positive")
           
    def increasePrice(self,extraPrice):
         if extraPrice >= 0:
             self.price += extraPrice
         else:
             print("increase price must be at least 1 and positive")  
    
    def getNextBookRef(self):
         return f"{self.nextBookRef}"

if __name__ == '__main__':
    
    a =  Book("test",1.00)
    
    
    print(a)
    #print (a.init)
    a.setPrice(123456789)
    print(a.price) 
    a.increasePrice(2)   
    print(a.price)
    print(a.getNextBookRef())
    b =  Book("test2",100.00)
    print(b)


#part b)
    print("Part B from the assignment starts here")
    book1 = Book("Dog Days", 18.00)
    book2 = Book("Treasure Isaland",7.50)
    book3 = Book("Python for All", 45.00)
    
    bookGroup = []

    #append objects to the list
    bookGroup.append(book1)
    bookGroup.append(book2)
    bookGroup.append(book3)
    
   
    #print out list
    for i in bookGroup:
        print (i)
        
    print("the value of nextBookRef is: " + str(book3.nextBookRef))
    
    
#part c)
    print("Part C from the assignment starts here")
    
    """Write the code to search the bookGroup List for books whose price is greater than
    searchPrice above and display the title of each of those books."""

    searchPrice = float(input ("Enter your price: "))
    
    for i in bookGroup:
        
        if i.price > searchPrice:
            print("book title is: "+ str(i.title))
                            
                            
                            
                            
                            
                            