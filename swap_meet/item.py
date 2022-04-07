class Item:

    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition = self.condition
        while condition >= 0 and condition <= 5:
            if condition in range(0, 1):
                return "Yikes..."
            if condition in range(1, 2):
                return "Poor"
            if condition in range(2, 3):
                return "Mint"
            if condition in range(3, 4):
                return "Fine Enough"
            if condition in range(4, 5):
                return "Good"
            if condition == 5:
                return "Perfect!"

    def __repr__(self):
        return f"condition description={self.condition_description}"