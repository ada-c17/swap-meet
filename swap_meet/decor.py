class Decor:
    
    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
    # range 0 - 1.5 --> "Don't touch with bare hands"
    # range 1.5 - 2.5 --> "Is it worth it? Probably not."
    # range 2.5 - 3.5 --> "Meh, it's neutral."
    # range 3.5 - 4.5 --> "It's a goooood find."
    # range 4.5 - 5 --> "Top tier item! Must have."
        pass
