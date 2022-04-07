class Item:
    def __init__(self, category=None, condition=0):
        if category is None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1:
            return "Why are you even swapping this?"
        elif self.condition <= 2:
            return "You could do better."
        elif self.condition <= 3:
            return "Blisteringly mediocre."
        elif self.condition <= 4:
            return "I'll accept this. I guess."
        elif self.condition <= 5:
            return "Wow, this is amazing!"