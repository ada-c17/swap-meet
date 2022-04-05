class Item:
    def __init__(self, category = None):
        if not category:
            category = ""
        self.category = category
        