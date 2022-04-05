class Item:
    
    def __init__(self, category = ""):
        self.category = category

    #override str() for Item, returns "Hello World!" instead
    def __str__(self):
        return "Hello World!"
         


