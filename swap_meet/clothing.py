from swap_meet.item import Item
class Clothing(Item):
    '''
    A class to represent a clothing instance with inheritance from the Item class

    ...
    
    ---Attributes---
    INHERITED
    category : str, optional
        empty string by default, otherwise a specific category represented by a string
    condition : int or float, optional
        zero by default, otherwise a number representing the condition of the item
    age : int or float, optional
        None by default, otherwise a number representing how old the item is in years

    ---Methods---
    __str__():
        sets dunder str to a string
    '''
    def __init__(self, condition=0, age=None):
        '''
        Constructs all the necessary attributes for a clothing object; inherits from Item

        ---Paramters---
        condition : int or float, optional
            zero by default, otherwise a number representing the condition of the item
        '''
        super().__init__("Clothing", condition, age)
        
    def __str__(self):
        '''sets dunder str to a string'''
        return "The finest clothing you could wear."
    