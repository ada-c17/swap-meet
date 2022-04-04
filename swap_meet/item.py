class Item:
    def __init__(self, category=None):
        if category:
            self.category = category
        else:
            self.category = ""