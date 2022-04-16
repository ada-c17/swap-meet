"""

- `Clothing`
  - Has an attribute `category` that is `"Clothing"`
  - Its stringify method returns `"The finest clothing you could wear."`

"""
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "The finest clothing you could wear."
    
    # def condition_description(self):
    #     if 0 <= self.condition <= 1:
    #         return "Is okie"
    #     elif self.condition <= 2:
    #         return "Not tooo bad"
    #     elif self.condition <= 3:
    #         return "Could be worse"
    #     elif self.condition <= 4:
    #          return "Not great"
    #     elif self.condition <= 5:
    #         return "Bad, very bad"

    pass