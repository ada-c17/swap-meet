class Electronics:
    def __init__(self, condition=0.0):
        self.category = "Electronics"
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return f"The quality of this item is {self.condition}."
