from swap_meet.item import Item
class Decor(Item):
    '''
    A class to represent a decor instance with inheritance from the Item class

    ...

    ---Attributes---
    INHERITED
    category : str, optional
        empty string by default, otherwise a specific category represented by a string
    condition : int or float, optional
        zero by default, otherwise a number representing the condition of the item

    ---Methods---
    __str__():
        sets dunder str to a string
    '''
    def __init__(self, condition=0):
        '''
        Constructs all the necessary attributes for a decor object; inherits from Item

        ---Paramters---
        condition : int or float, optional
            zero by default, otherwise a number representing the condition of the item
        '''
        super().__init__("Decor", condition)

    def __str__(self):
        '''sets dunder str to a string'''
        return "Something to decorate your space."
