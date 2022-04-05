class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def condition_description(self, condition):
        self.condition = condition