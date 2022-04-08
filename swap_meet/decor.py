from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "Decor", condition = condition)

    def __str__(self):
        string_item = "Something to decorate your space."
        return string_item

    def condition_description(self):
        return super().condition_description()