class Item:
    def __init__(self, category= '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return f"condition is {self.condition} and it's very bad"
        elif self.condition >= 1 and self.condition<= 3:
            return f"condition is {self.condition} and it's moderate"
        elif self.condition > 3 and self.condition<=5:
            return f"condition is {self.condition} and it's very good"
