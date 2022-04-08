from swap_meet.item import Item
#wave 5: - `Clothing`/child class of Item class. category attribute is clothing. the strigfy method returns "the finest closing you could wear."

class Clothing(Item):
    def __init__(self,category="Clothing",condition= 0):
        super().__init__ (category ,condition)
        
    
    def __str__(self):
      return "The finest clothing you could wear."
  
      

