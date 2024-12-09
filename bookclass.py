class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Publisher",self.name)
 
class Book(publisher):
    def __init__(self,title,author):
        
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print("Title :",self.title)
        print("Author:",self.author)

class Python(Book):
    def __init__(self,price,pages,pubname,title,author):
        self.name=pubname
        self.title=title
        self.author=author
        
        self.price=price
        self.pages=pages
    def display(self):
        super().display()
        print("Price :",self.price)
        print("Pages :",self.pages)

pubname =str(input("Enter the Publisher name :"))
title =str(input("Enter the Title of the book :"))
author =str(input("Enter the Author name :"))
pages =int(input("Enter the number of pages:"))
price =int(input("Enter the Price of Book:"))

py = Python(price,pages,pubname,title,author)
print("Book Details:")
py.display()



    
    
        
    
        
