"""
Task1
Створіть клас, який описує книгу. Він повинен містити інформацію про
автора, назву, рік видання та жанр. Створіть кілька різних книжок.
Визначте для нього методи _repr_ та _str_.
"""


class Book:
    """
    Book with info about it: author, title, year of publication, and genre.
    """

    def __init__(self, author: str, title: str, year: int, genre: str):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"{self.__class__}: {self.title}, {self.author}"

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, genre: {self.genre}"


# Create books
hamlet = Book('Shakespeare William', 'Hamlet', 2019, 'tragic')
mysterious_island = Book('Jules Verne', 'The Mysterious Island', 2017, 'adventure novel')
mohican = Book('James Fenimore Cooper', 'The Last of the Mohicans', 2019, 'historical romance')

# Print books
print(hamlet, "\n", hamlet.__repr__(), "\n")
print(mysterious_island, "\n", mysterious_island.__repr__(), "\n")
print(mohican, "\n", mohican.__repr__(), "\n")
