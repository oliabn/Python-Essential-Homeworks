"""
Task2
Створіть клас, який описує відгук до книги. Додайте до класу книги
поле – список відгуків. Зробіть так, щоб при виведенні книги на екран
за допомогою функції print також виводилися відгуки до неї.
"""


class Book:
    """
    Book with info about it: author, title, year of publication, genre, review.
    """

    def __init__(self, author: str, title: str, year: int, genre: str):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.review_list = []

    def __repr__(self):
        return f"{self.__class__}: {self.title}, {self.author}"

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, review: {self.review_list}"

    def add_review(self, review: str):
        self.review_list.append(review)


# Create books
hamlet = Book('Shakespeare William', 'Hamlet', 2019, 'tragic')
mysterious_island = Book('Jules Verne', 'The Mysterious Island', 2017, 'adventure novel')
mohican = Book('James Fenimore Cooper', 'The Last of the Mohicans', 2019, 'historical romance')

# Add book review
hamlet.add_review("This is a classic")
hamlet.add_review("Interesting")
mysterious_island.add_review("The best adventure book ever")
mohican.add_review("My favorite, I recommend it to everyone")

# Print books wirth review
print(hamlet)
print(mysterious_island)
print(mohican)
