class Item:
    '''
    Class representing an item to be traded

    Methods:
        condition_description()

    Variables:
        category: category of an item
        condition: condition of an item from 0-5
    '''
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """returns a descrption based on quality of an item"""
        
        quality = {5: "The beauty of this item can only be expressed through tears of joy!",
                    4: "Crisp! Just like the day it left the factory floor!",
                    3: "Something is a little off but super well maintained... just like the vendor.",
                    2: "Time as taken its toll but not something you would have to hide when family visits.",
                    1: "... it's not great",
                    0: "\"If you stare into the abyss, the abyss stares back at you\" -Nietzsche-"
                    }
        
        return quality[self.condition]