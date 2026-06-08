from item import Item

class Electronic(Item):
    def __init__(self, id, name, price, quantity,  warranty)->None:
        super().__init__(id, name, price, quantity)
        self.warranty:int = warranty # in month
    
    def get_warranty(self)-> int:
        return self.warranty