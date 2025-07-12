class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.author}, {self.year} год"
    
book = Book("Буратино", "Алексей Николаевич Толстой", 1936)
print(book)