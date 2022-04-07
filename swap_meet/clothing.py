from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category="", condition=0):
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        CONDITIONS = {
            0: "It has stains",
            1: "Okay",
            2: "Not my color",
            3: "This could work for date night",
            4: "I need this in my closet!",
            5: "Flawless"
        }
        return CONDITIONS[self.condition]