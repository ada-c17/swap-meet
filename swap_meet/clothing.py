class Clothing:
    
    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
    # range 0 - 1 --> "Don't touch with bare hands"
    # range 1 - 2 --> "Is it worth it? Probably not."
    # range 2 - 3 --> "Meh, it's neutral."
    # range 3 - 4 --> "It's a good find."
    # range 4 - 5 --> "Top tier item! Must have."

        if (self.condition >= 0) and (self.condition <= 1):
            return "Don't touch with bare hands."
        elif (self.condition > 1) and (self.condition <= 2):
            return "Is it worth it? Probably not."
        elif (self.condition > 2) and (self.condition <= 3):
            return "Meh, it's neutral."
        elif (self.condition > 3) and (self.condition <= 4):
            return "It's a good find."
        elif (self.condition > 4) and (self.condition <= 5):
            return "Top tier item! Must have."
