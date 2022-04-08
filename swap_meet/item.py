class Item:
    def __init__(self, category = ""):
        self.category = category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return f"The quality of this item is {self.condition}."
