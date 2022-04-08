from swap_meet.item import Item

class Clothing (Item):
    def __init__(self,condition = 0):
        self.category = "Clothing"

        super().__init__(self.category,condition)


    def __str__(self):
        return "The finest clothing you could wear."

    
    def condition_description(self):
        if self.condition == 5:
            return "exccelent"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 3:
            return "good"
        elif self.condition == 2:
            return "okay"
        elif self.condition == 1:
            return "bad"