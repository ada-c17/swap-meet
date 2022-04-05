from swap_meet.item import Item
class Electronics(Item):

    category = "Electronics"

    def __init__(self, condition=0, age=None):
        super().__init__(Electronics.category, condition, age)     

    @staticmethod
    def __str__():
        return "A gadget full of buttons and secrets."
