class Item:
    def __init__(self, age=0, condition=0, category=""):
        self.category = category
        self.condition = float(condition)
        self.age = float(age)
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        descriptions = {
            1.0: "Trash.",
            2.0: "Repairable",
            3.0: "Is it shiney?",
            4.0: "That's definitely shiney",
            5.0: "I know what I have!"
        }
        return descriptions[self.condition]