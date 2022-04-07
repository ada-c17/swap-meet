from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0, age = None):
        super().__init__(condition = condition, age = age, category = "Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return super().condition_description()

    def age_description(self):
        return super().age_description()
