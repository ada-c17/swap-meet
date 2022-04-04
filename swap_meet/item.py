class Item:
    
    # constructor for class Item
    def __init__(self, category = ""):
        self.category = category

    # method to stringify an Item
    def __str__(self):
        return "Hello World!"