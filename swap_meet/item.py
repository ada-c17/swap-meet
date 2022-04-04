class Item:
    def __init__(self,category="",condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        CONDITIONS = {0:"Trash filler",
                    1:"Fancy trash filler",
                    2:"Limited edition and limited lifespan",
                    3:"Like your average friend's worst item",
                    4:"Might be able to tell if you look close enough",
                    5:"Nobody can tell"}
        return CONDITIONS[self.condition]