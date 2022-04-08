class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1:
            return "Belongs in the trash."
        elif self.condition <= 2:
            return "Oof...bad idea."
        elif self.condition <= 3:
            return "Is it really worth it?"
        elif self.condition <= 4:
            return "Heyyyy, this is pretty good~"
        elif self.condition <= 5:
            return "Brilliant, incredible, amazing, show stopping, spectacular item!"   
    