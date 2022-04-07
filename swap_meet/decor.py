from swap_meet.item import Item
class Decor(Item):
    
    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."
    
    # def condition_description(self):
    #     # 0 - 1 --> "Don't touch with bare hands"
    #     # 1 - 2 --> "Is it worth it? Probably not."
    #     # 2 - 3 --> "Meh, it's neutral."
    #     # 3 - 4 --> "It's a good find."
    #     # 4 - 5 --> "Top tier item! Must have."

    #     if (self.condition >= 0) and (self.condition <= 1):
    #         return "Don't touch with bare hands."
    #     elif (self.condition > 1) and (self.condition <= 2):
    #         return "Is it worth it? Probably not."
    #     elif (self.condition > 2) and (self.condition <= 3):
    #         return "Meh, it's neutral."
    #     elif (self.condition > 3) and (self.condition <= 4):
    #         return "It's a good find."
    #     elif (self.condition > 4) and (self.condition <= 5):
    #         return "Top tier item! Must have."