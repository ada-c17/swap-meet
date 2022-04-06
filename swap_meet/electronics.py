from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0.0):
        super().__init__(category, condition)


    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return Item.condition_description(self)
        # return "Bought it last year, rarely used!"