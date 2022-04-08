from swap_meet.item import Item

class Electronics (Item):
    def __init__(self,condition = 0):
        self.category = "Electronics"

        super().__init__(self.category,condition)


    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        if self.condition == 5:
            return "exccelent"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 3:
            return "good"
        elif self.condition == 2:
            return "okay"
        elif self.condition == 1:
            return "bad"
