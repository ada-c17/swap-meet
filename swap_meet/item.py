class Item:

    def __init__(self,category= None, condition = 0):
        if category is None:
            category = ""
        self.category = category
        if condition is 0:
            condition = 0
        self.condition = condition 

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition <= 2:
            return "Heavily used"
        elif self.condition <= 5 :
            return "Great condition"
            

        





