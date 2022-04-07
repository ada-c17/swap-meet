from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category="", condition=0):
        super().__init__("Decor", condition)

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        CONDITIONS = {
            0: "This is broken",
            1: "Okay",
            2: "Need to get repairs",
            3: "I need this in my room",
            4: "Excellent, for decorate",
            5: "Flawless"
        }
        return CONDITIONS[self.condition] 