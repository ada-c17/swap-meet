class Item:
    def __init__(self, category = "", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 <= self.condition < 1:
            return f"The condition of this item is {self.condition} out of 5, so it's not in good shape."
        if 1 <= self.condition < 2:
            return f"The condition of this item is {self.condition} out of 5, so it's likely heavily used."
        if 2 <= self.condition < 3:
            return f"The condition of this item is {self.condition} out of 5, so it's had some wear and tear."
        if 3 <= self.condition < 4:
            return f"The condition of this item is {self.condition} out of 5, so it should be decent."
        if 4 <= self.condition < 5:
            return f"The condition of this item is {self.condition} out of 5, so it's in great shape!"
        if self.condition == 5:
            return f"The condition of this item is {self.condition} out of 5, so it's in mint condition!"
