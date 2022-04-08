QUALITY_DESCRIPTIONS = {
    0: "Probably best to scrap for parts", #for condition [0.0, 1)
    1: "Fixer-Upper", #for condition [1, 2)
    2: "Fine.", #for condition [2, 3)
    3: "Used, still has lots of life", #for condition [3,4)
    4: "Gently used; gave-up-on-this-hobby tier", #for condition [4,5)
    5: "Waited too long to return this; new in box" #for condition 5.0 only
}

class Item:
    '''
        An item at a swap meet.
        
        Attributes:
            category (str): item type
            condition (float): item quality (range 0-5; default 0.0)
    '''

    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        #truncate condition to int (for positive floats, equivalent to flooring)
        rating_bound = int(self.condition)
        return QUALITY_DESCRIPTIONS[rating_bound]