
from item import Item

class Book(Item):
    def __init__(self, id, name, price, quantity, author)->None:
        super().__init__(id, name, price, quantity)
        self.author: str = author

    def get_author(self) -> str:
        return self.author
    
