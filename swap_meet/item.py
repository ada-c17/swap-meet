class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        descriptions = {
            0: "Trash",
            1: "Salvageable",
            2: "A little busted",
            3: "Honestly fine",
            4: "It works",
            5: "Perfect"
        }
        return descriptions[self.condition]