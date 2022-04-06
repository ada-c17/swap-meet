
class Item:
    def __init__(self, category = None, condition = 0):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition    

    # return string, when instance is assign
    def __repr__(self):
        return self.category

    # return string "Hello World!"
    def __str__(self):
        if not self.category:
            return "Hello World!"
        return self.category

    # def condition_description(self):