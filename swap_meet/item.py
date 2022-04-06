class Item:
    def __init__(self, condition = 0, category = ""):
        self.condition = condition
        self.category = category


    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        """Returns strings describing the condition of item instance"""

        if self.condition <= 1:
            return "I mean I wouldn't touch this with a ten foot pole but, uh, you do you."
        elif self.condition <= 2:
            return "It's....tolerable. I suppose. If one must."
        elif self.condition <= 3:
            return "Decent."
        elif self.condition <= 4:
            return "Alright, NOW we're talking. Nothing's perfect, right?"
        elif self.condition <= 5:
            return "Excellent. Full marks. Drinks all around!"
        else:
            return "Oh my god BUY THIS NOW ITS CONDITION IS OUT OF THIS WORLD"

