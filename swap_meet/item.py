class Item:
    def __init__(self, category=None, condition = 0.0):
        if not category:
            category = ""
        self.condition = condition
        self.category = category

   
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        #if else 1-5
        if self.condition == 1.0:
            return "Horrid"
        elif self.condition == 2.0:
            return "Ugly"
        elif self.condition == 3.0:
            return "getting warmer"
        elif self.condition == 4.0:
            return "almost...doesnt count"
        elif self.condition ==  5.0:
            return "winner winner chicken dinner"            


            