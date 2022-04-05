class Item:
    def __init__(self, category = None):
        if not category:
            category = ""
        self.category = category
    


    def __str__(self):
        self.category = "Hello World!"
        return self.category
        