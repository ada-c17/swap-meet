
class Item:
    def __init__(self, category=None, condition=0 ):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        '''stringify (convert to a string) an instance of `Item` 
            using `str()`, and return `"Hello World!"`
        '''
        return "Hello World!"

    def condition_description(self):
        '''assigning a description to items based on the value,
            ranging from 0 being the worst and 5 being best
        '''
        if self.condition == 0:
            return "I have so many questions"
        if self.condition == 1:
            return "You're a good friend"
        if self.condition == 2:
            return "You have interesting standards"
        if self.condition == 3:
            return "Gently used"
        if self.condition == 4:
            return "Like new"
        if self.condition == 5:
            return "Brand new in box"
    
