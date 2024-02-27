class Book:
    def __init__(self, title, author):
        if not isinstance(title, str):
            self.title = ""
        else:
            self.title = str(title)
        
        if not isinstance(author, str):
            self.author = ""
        else:
            self.author = str(author)
        
    
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    
    
    def print_Book(self):
        try:
            title = self.title
        except:
            title = ""

        try:
            author = self.author
        except:
            author = ""

        
        
        result = "Título: {} \nAutor: {}".format(title, author)

    def serialize(self):
        return {
            'title': self.title,
            'author': self.author
        }