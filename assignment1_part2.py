class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title

    def display(self):
        print('{0}, written by {1}'.format(self.title, self.author))

a = Book('Of Mice and Men', 'John Steinbeck')
b = Book('To Kill a Mockingbird', 'Harper Lee')
a.display()
b.display()
