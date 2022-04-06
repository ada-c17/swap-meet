from .item import Item

class Electronics(Item):
    #keep condition as 0.0 to allow it to change
    def __init__(self, condition = 0.0):
        '''
        Constructs attributes for Electronics object from parent class, default values: category = "Electronics", condition =0.
        '''
        #"Electronics" gets set as keyword argument value in super__init_- -> which is a method CALL, set condition = condition to ensure attribute inherited 
        #and not reassigned above
        super().__init__(condition = condition, category = "Electronics")

    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "A gadget full of buttons and secrets."
