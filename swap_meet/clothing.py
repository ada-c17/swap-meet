class Clothing:
    def __init__(self, condition=0.0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        return f"The quality of this item is {self.condition}."
