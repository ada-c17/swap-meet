class Item:
    def __init__(self, category = None):
        if category == None:
            self.category = ""
        else:
            self.category = category

    def __str__(self):
        self.category = "Hello World!" 
        return self.category
# item = Item("stringified_item")
# str(item)

    

