class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return f"Title: {self.title}"

    def get_author(self) -> str:
        return f"Author: {self.author}"

pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
hamletas = Book("Hamletas", "Viljamas Šekspyras")
karas_ir_taika = Book("Karas ir taika", "Levas Tolstojus")

print(pride_and_prejudice.get_title())
print(karas_ir_taika.get_author())