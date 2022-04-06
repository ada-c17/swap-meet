class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition


    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        descriptions = {
            0: "You tell me?",
            1: "Do you really want this?",
            2: "This might be nice in the corner on a shelf somewhere.",
            3: "It's better than nothing!",
            4: "I used it but I didn't really use it",
            5: "Just as good as the store but it'll cost you less",
        }

        return descriptions[self.condition]