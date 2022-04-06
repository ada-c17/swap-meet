class Item:
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition <= 1.0:
            return "You probably want a glove for this one..."
        elif self.condition > 1.0 and self.condition <= 2.0:
            return "That was a good catch from my neighbor's garbage bin."
        elif self.condition > 2.0 and self.condition <= 3.0:
            return "Nothing special, just a fair trade."
        elif self.condition > 3.0 and self.condition <= 4.0:
            return "Packaging is damaged, but works perfectly."
        else:
            return "Actually, I am not sure I want to swap this perfect thing."