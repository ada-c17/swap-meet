class Item:
    def __init__(self,category = None, condition = 0.0):
        if not category:
            category= ""
        self.category = str(category)
        self.condition = condition

    def __str__(self):
        stringfied_item = "Hello World!"
        Item = stringfied_item
        Item = str(Item)
        return str(stringfied_item)
    
    def condition_description(self):
        if self.condition == 1:
            result = str("Value one")
        elif self.condition == 2:
            result = str("Value two")
        elif self.condition == 3:
            result = str("Value three")
        elif self.condition == 4:
            result = str("Value four")
        elif self.condition ==5:
            result = str("Value five")
        return result 
    
    
