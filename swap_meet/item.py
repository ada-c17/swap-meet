class Item:
    def __init__(self,category = None, condition = 0.0):
        if not category:
            category= ""
        self.category = str(category)
        self.condition = condition

    def __str__(self):
        stringfied_item = "Hello World!"
        return str(stringfied_item)
    
    def condition_description(self):
        if self.condition == 1:
            result = str("Rating one *")
        elif self.condition == 2:
            result = str("Rating two **")
        elif self.condition == 3:
            result = str("Rating three ***")
        elif self.condition == 4:
            result = str("Rating four ****")
        elif self.condition ==5:
            result = str("Rating five *****")
        return result 
    
    
