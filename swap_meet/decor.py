class Decor:
    def __init__(self, condition=0.0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return f"The quality of this item is {self.condition}."
