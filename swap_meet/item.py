class Item:
    def __init__(self, category = None, condition = 0 ):
        if not category:
            category = ""
        self.category = category
        self.condition = float(condition)
        
    def __str__(self):
        return f'Hello World!'

    def condition_description(self):
        if self.condition <= 5 and self.condition > 4:
            return "Perfect condition!"
        elif self.condition <= 4 and self.condition > 3:
            return "Still pretty good!"
        elif self.condition <= 3 and self.condition > 2:
            return "Not too bad but not great."
        elif self.condition <= 2 and self.condition > 1:
            return "Pretty well used."
        elif self.condition <= 1 and self.condition > 0:
            return "Heavily used, not good"
        else:
            return "Probably should be free"

            

