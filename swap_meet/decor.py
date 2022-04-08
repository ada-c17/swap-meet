from pyparsing import condition_as_parse_action
from swap_meet.item import Item
class Decor(Item):
    def __init__(self, condition = 0 ):
        super().__init__(category= "Decor", condition = condition)
    def __str__(self, category= "Decor"): 
        self.category = "Something to decorate your space."
        return self.category
  

