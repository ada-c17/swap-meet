from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "Electronics", condition = condition)

    def __str__(self):
        string_item = "A gadget full of buttons and secrets."
        return string_item
        
    def condition_description(self):
        return super().condition_description()