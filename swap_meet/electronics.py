from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, category="", condition=0):
        super().__init__("Electronics", condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

    
    def condition_description(self):
        CONDITIONS = {
            0: "You might want to buy battery to fix this",
            1: "Okay",
            2: "Need extra care",
            3: "Oh this work",
            4: "Perfect Deals",
            5: "Flawless"
        }
        return CONDITIONS[self.condition]
