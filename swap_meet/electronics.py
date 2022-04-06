from swap_meet.item import Item



class Electronics(Item):

    category = "Electronics"

    def __init__(self, *args, **kwargs):
        super().__init__(category=Electronics.category, *args, **kwargs)     

    @staticmethod
    def __str__():
        return "A gadget full of buttons and secrets."
