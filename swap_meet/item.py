class Item:
    def __init__(self, category = "", condition = 5):
        self.category = category
        self.condition = condition

    def __str__(self):
        return("Hello World!")

    def __repr__(self): #created repr dunder method just for funzies
        rep = f"Item({self.category}, {str(self.condition)})"
        return rep

    def condition_description(self):
        return f"The item's condition is {self.condition} out of 5."