from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, condition = None):
        super().__init__("Electronics",condition)
        
   
    
    def __str__(self):      
        return (f"A gadget full of buttons and secrets.")
    
