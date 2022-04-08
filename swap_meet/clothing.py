from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = None):
        super().__init__("Clothing", condition)
    
    def __str__(self):      
        return (f"The finest clothing you could wear.")