class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """Returns a description of item condition."""
        if self.condition == 5.0:
            return "This item is brand new and in perfect condition."    
        elif self.condition >= 4.0:
            return "This item is in great condition."
        elif self.condition >= 3.0:
            return "This item is in good condition."
        elif self.condition >= 2.0:
            return "This item is in OK condition."
        else:
            return "This item has seen better days."
    

