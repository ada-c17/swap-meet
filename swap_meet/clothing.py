from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "Clothing", condition = condition)

    def __str__(self):
        string_item = "The finest clothing you could wear."
        return string_item

    def condition_description(self):
        return super().condition_description()
