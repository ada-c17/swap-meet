class Item:
    def __init__(self, category=None, condition=0):
        if category:
            self.category=category
        else:
            self.category = ""
        
        self.condition=condition

    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        if self.condition < 1:
            return "This item might have some defects"
        elif 1 <= self.condition < 2:
            return "This item is in fair condition"
        elif 2 <= self.condition < 3:
            return "This item is in good condition"
        elif 3 <= self.condition < 4:
            return "This item is in very good condition"
        elif 4 <= self.condition <= 5:
            return "This item is in excellent condition"
        
