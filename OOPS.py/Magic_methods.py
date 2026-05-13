"""

Magic methods  : Dunder methods (Double underscore's) 
                 They allow developer's to define or customize the behaviour of object's.
                 Python has buit-in methods like __init__ , __str__ , __eq__ , __lt__ , __gt__ , __getitem__ , __contains__ , __add__ ....


"""

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return f"{self.num_pages < other.num_pages}"
    def __gt__(self, other):
        return f"{self.num_pages > other.num_pages}"
    
    def __getitem__(self,key):
        
        if key == 'title':
            return self.title 
        elif key == 'author':    
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else :
            return f"key '{key}' was not matched!"

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, item):
         return item in self.title or item in self.author 
                
    
    


book1 = Book("Atomic habits","P.P Peter park",234)
book2 = Book("Harry potter","S.P Spongebob",340)
book3 = Book("You can't hurt me","J.R Alice",187)

# print(book1)
# print(book2)
# print(book3)

# print(book1 == book2)

# print(book1  > book2)

# print(book3['title'])

# print(book1 + book2)

print("Atomic habits" in book1)





