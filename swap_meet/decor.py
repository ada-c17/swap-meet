from swap_meet.item import Item
#wave 5: - `Decor`/child class of Item class. category attribute is Decor. the strigfy method returns "Something to decorate your space."
class Decor(Item):
   def __init__(self,category="Decor", condition= 0 ):
      super().__init__(category,condition)
   def __str__(self):
      return "Something to decorate your space."
  
    
    






