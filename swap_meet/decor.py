from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0):
        '''
        Constructor of an object of parent class. Its parameter condition has a default value of 0
        '''
        super().__init__(category = "Decor", condition = condition)

    def __str__(self):
        '''
        Overrides its parent(Item)'s method and returns its own message
        '''
        return "Something to decorate your space."

  