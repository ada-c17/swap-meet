    # wave 2
    # attributes: 
    #   category - an empty string

    # wave 3
    # stringify returns "Hello World!""

    # wave 5
    # add condition attribute
class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"