    # wave 2
    # attributes: 
    #   category - an empty string

    # wave 3
    # stringify returns "Hello World!""

    # wave 5
    # add condition attribute
    # add instance method condition_description
class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            description = "Trash"
        elif self.condition == 1:
            description = "It Works"
        elif self.condition == 2:
            description = "Decent"
        elif self.condition == 3:
            description = "Good"
        elif self.condition == 4:
            description = "Like New"
        elif self.condition == 5:
            description = "New"
        return description