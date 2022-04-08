from.item import Item

class Clothing(Item):
    def __init__(self, age = 0, category = "Clothing", condition = 0):
        #have to pass the arguments from the SubClass init to the init block of Base
        super().__init__(age, category = category, condition = condition)
        
    def __str__(self):
        return  "The finest clothing you could wear."

    #answer from class discussion: compare to mine and think about diff ??
    # def__init__(self,condition = 0)
    #     super().__init__(category="Clothing", condition= condition))
