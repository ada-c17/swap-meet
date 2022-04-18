from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0):
        '''
        Constructor of an object of parent class. Its parameter condition has a default value of 0
        '''
        super().__init__(category = "Electronics", condition = condition)

    def __str__(self):
        '''
        Overrides its parent(Item)'s method and returns its own message
        '''
        return "A gadget full of buttons and secrets."

   