from .item import Item

class Decor(Item):
    '''
    Class representing a Decor item to be traded
    Child of Item class

    Methods:
        condition_description() from Item class

    Variables:
        category: category of Decor default is Decor
        condition: condition of Decor from 0-5
    '''
    def __init__(self, category="Decor", condition=0):#unsure of if the redundant value sets are necessary
        super().__init__(category, condition)
        
    def __str__(self):
        return "Something to decorate your space."
