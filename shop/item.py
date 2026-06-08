class Item:
    def __init__(self, id, name, price, quantity)->None:
        self.id : int = id
        self.name: str = name
        self.price: int = price
        self.quantity: int = quantity

    def get_id(self)->int:
        return self.id
    
    def get_name(self)->str:
        return self.name
    
    def get_price(self)-> int:
        return self.price
    
    def get_quantity(self)-> int:
        return self.quantity
    

    # sorting the items
    def __lt__(self, other):
        if self.price < other.price:
            return False
        else:
            return True
        
    # handle duplicate
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        
        return self.id == other.id
