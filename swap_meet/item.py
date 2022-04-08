class Item:

    def __init__(self, category="", condition=0.0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition = int(self.condition)
        descriptions = {
            0: 'You should probably pass on this one...', 
            1: 'Poor', 
            2: 'Meh', 
            3: 'Good', 
            4: 'Great', 
            5: 'Brand spankin new'
        }
        return descriptions[condition]

