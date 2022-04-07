"""

- `Electronics`
  - Has an attribute `category` that is `"Electronics"`
  - Its stringify method returns `"A gadget full of buttons and secrets."`

"""

from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

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
