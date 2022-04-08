
class Item:
    def __init__(self,category = "", condition = None):      
        self.category = category
        self.condition = condition
        if condition is None:
           self.condition = 0
         

    def __str__(self):      
        return f"Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "Seen a better day"

        elif self.condition >= 1 and self.condition < 2:
            return  "Needs some love"

        elif self.condition >= 2 and self.condition < 3:
            return "Great bargin find"

        elif self.condition >= 3 and self.condition < 4:
            return "Good condition"

        elif self.condition >= 4 and self.condition < 5:
            return "Really good condition"

        else:
            return "Pristine condition"



        


        
        

        


book_1 = Item(category="books")
coat_1 = Item(category="clothing")
hat_1 = Item(category="clothing")