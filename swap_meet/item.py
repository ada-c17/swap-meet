class Item:
    def __init__(self, category = None, condition = 0):
        if not category:
            category = ""
        self.category  = category
        self.condition  = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 0 and self.condition < 1:
            return "Yuck. Qdoba level!"
        elif self.condition >= 1 and self.condition < 2:
            return "Oh, no. Chipotle level!"
        elif self.condition >= 2 and self.condition < 3:
            return "Ok. Chili's level!"
        elif self.condition >= 3 and self.condition < 4:
            return "Yum! Moe's level!"
        elif self.condition >= 4 and self.condition < 5:
            return "Yes! Don Arturo's level!"
        elif self.condition == 5:
            return "Yummmmmy. Nacho's level!"